# Third-party translation engine

The guide retains its MIT license. Files under `vendor/chsi-translator/` are
derived from [muxiymmm/Online-Verification-Report-Translator20260714](https://github.com/muxiymmm/Online-Verification-Report-Translator20260714)
and the user's [fork](https://github.com/EndlessBlueWJL/Online-Verification-Report-Translator20260714).
They retain the original Apache-2.0 license in `vendor/chsi-translator/LICENSE`.

Upstream base: `7cc3e94b9e28197d8dd85dccf93a4f105b4d4a5e`.
This integration includes the locally reviewed changes dated 2026-10-20:
external private configuration, local confirmed-English fields, removal of
hidden sample text/photo/QR objects from newly generated PDFs, and an expiry
display calculated from the renewal date's calendar anniversary. The existing
template and font files are copied without modification. The original author's
filled sample configuration is not needed by this integration and is not copied.

The entry point `scripts/translate_chsi.py` extracts a supported Chinese report
and invokes that engine. Its fields, source images and outputs remain outside
the repository. Approved PNG examples use fictional data and contain neither
the user's photograph nor their verification code or QR code.

Runtime dependencies keep their respective licenses; in particular PyMuPDF is
distributed under AGPL/commercial terms. The guide's MIT license does not relicense
third-party code, assets, or dependencies. This tool is not affiliated with CHSI
and does not issue official English reports.
