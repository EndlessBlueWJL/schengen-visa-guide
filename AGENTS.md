# Repository rules

- This skill is a reusable tool. Never add a new user's reports, photographs,
  QR codes, verification codes, filled JSON/YAML, extracted text, progress or
  generated outputs to this repository, tests, documentation or Git history.
- Runtime material must remain outside all Git repositories. Tests use synthetic
  records only; realistic private verification belongs in an external directory.
- The only approved report images are the two reviewed fictional examples in
  `assets/chsi/`. Their hashes are fixed in `scripts/approved_chsi_assets.py`.
- Preserve the exact original author template in `vendor/chsi-translator/data/`.
  It is an existing upstream reference, not a new-user-data exemption. Never
  replace it with a user's report or broaden the checksum allowlist for runtime data.
- Keep processing local. Do not log private field values, report links or image
  contents, and do not add automatic uploads or remote translation services.
- Preserve the upstream license and attribution for vendored translation code.
- Run `python scripts/check_public_files.py --worktree` before review;
  `--staged` before commits. Pre-push checks reachable history. These checks do
  not replace human review and cannot prove arbitrary source code is non-private.
- Do not push automatically. Respect the user's authorization for publication.
