"""Reject runtime documents and changed reference assets without logging values."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import sys

from approved_chsi_assets import APPROVED_SHA256

ROOT = Path(__file__).resolve().parents[1]
PRIVATE_DIRS = {".data", "private", "personal", "runtime", "input", "inputs", "output", "outputs", "reports", "user-data"}
PRIVATE_FILES = {"progress.md", "extracted.json", "translation.json", "render-configuration.yaml", "configuration.yaml"}
DOCUMENT_EXTS = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tif", ".tiff", ".webp", ".docx", ".xlsx", ".csv", ".tsv", ".json", ".zip", ".7z"}


def inspect_file(name, data):
    if name in APPROVED_SHA256:
        if hashlib.sha256(data).hexdigest() != APPROVED_SHA256[name]:
            raise ValueError("Reviewed asset changed")
        return
    path = Path(name)
    if path.name.lower() in PRIVATE_FILES or any(part.lower() in PRIVATE_DIRS for part in path.parts):
        raise ValueError("Runtime content")
    if path.suffix.lower() in DOCUMENT_EXTS or b"\x00" in data:
        raise ValueError("Unapproved document or binary")
    if path.suffix.lower() in {".yaml", ".yml"} and not name.startswith(".github/workflows/"):
        raise ValueError("Unapproved configuration")
    data.decode("utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--staged", action="store_true")
    group.add_argument("--worktree", action="store_true")
    args = parser.parse_args(argv)
    result = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, check=True, stdout=subprocess.PIPE)
    files = {name.decode("utf-8") for name in result.stdout.split(b"\0") if name}
    if args.worktree:
        extra = subprocess.run(["git", "ls-files", "--others", "--exclude-standard", "-z"], cwd=ROOT, check=True, stdout=subprocess.PIPE)
        files.update(name.decode("utf-8") for name in extra.stdout.split(b"\0") if name)
    failed = checked = 0
    for name in sorted(files):
        if args.staged:
            blob = subprocess.run(["git", "show", ":" + name], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if blob.returncode:
                failed += 1
                continue
            data = blob.stdout
        else:
            path = ROOT / name
            if not path.exists():
                continue
            data = path.read_bytes()
        checked += 1
        try:
            inspect_file(name, data)
        except Exception:
            failed += 1
    if failed:
        print(f"BLOCKED: {failed} public candidate(s) failed privacy checks; no private names or values printed.", file=sys.stderr)
        return 1
    print(f"PASS: {checked} public candidate files checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
