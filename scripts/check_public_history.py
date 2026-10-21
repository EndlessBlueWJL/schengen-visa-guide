"""Block publishing reachable historical blobs that fail the public-file rules."""
import argparse
from pathlib import Path
import subprocess
import sys
from check_public_files import inspect_file

ROOT=Path(__file__).resolve().parents[1]


def check_revision(revision,root=ROOT):
    result=subprocess.run(["git","rev-list","--objects",revision],cwd=root,
                          check=True,stdout=subprocess.PIPE)
    failures=0
    for line in result.stdout.splitlines():
        object_id,separator,name=line.partition(b" ")
        if not separator:
            continue
        kind=subprocess.run(["git","cat-file","-t",object_id.decode("ascii")],cwd=root,
                            check=True,stdout=subprocess.PIPE).stdout.strip()
        if kind != b"blob":
            continue
        content=subprocess.run(["git","cat-file","blob",object_id.decode("ascii")],cwd=root,
                               check=True,stdout=subprocess.PIPE).stdout
        try:
            inspect_file(name.decode("utf-8"),content)
        except Exception:
            failures+=1
    return failures


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--revision")
    mode.add_argument("--pre-push",action="store_true")
    args=parser.parse_args(argv)
    if args.pre_push:
        revisions=[]
        for line in sys.stdin:
            parts=line.split()
            if len(parts)!=4:
                print("BLOCKED: invalid pre-push input.",file=sys.stderr)
                return 1
            local_sha=parts[1]
            if set(local_sha)!={"0"}:
                revisions.append(local_sha)
    else:
        revisions=[args.revision]
    try:
        failures=sum(check_revision(value) for value in set(revisions))
    except Exception:
        print("BLOCKED: history inspection could not complete.",file=sys.stderr)
        return 1
    if failures:
        print("BLOCKED: reachable Git history contains files rejected by the public-file rules. Clean current files do not erase old commits.",file=sys.stderr)
        return 1
    print("PASS: reachable history checked.")
    return 0


if __name__=="__main__":
    raise SystemExit(main())
