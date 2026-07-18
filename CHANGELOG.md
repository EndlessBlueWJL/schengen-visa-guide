# Changelog

## v1.1.0 (2026-07-18)

A major content + structure overhaul. The flow is more accurate, more complete, and easier to maintain.

### Added
- **New identity type: minors (under 18)** — birth certificate + parental consent, both notarized with Hague Apostille; in-person submission and fingerprint rules for minors
- **Budget estimate** — a two-tier formula fitted to real agency / visa-center practice: `¥2,000 × days` (≤15d) and `¥30,000 + ¥4,000 × (days − 15)` (>15d), replacing the folklore flat "¥30k balance", with full disclaimers
- **Fingerprinting (VIS)** — added to the flow, appointment step, and submission-day reminders (59-month validity, under-12 exempt)
- **Timing & fees** — processing time (~15 days, up to 45), visa fee (€90 / €45 / free), service fee
- **Consular-district (领区) determination** — how to tell which district you belong to
- **Passport "issued within 10 years"** hard rule — was missing, a real rejection reason
- **Hague Apostille** notes — China joined the Apostille Convention on 2023-11-07
- Info-currency disclaimer across all files (as of 2025-07)

### Changed
- **90/180 rule** clarified (was "max 90 days")
- **Romania** updated — fully joined Schengen in 2025; stale e-visa claim removed
- Baltic states (Estonia/Latvia/Lithuania) split into three real links
- Germany caveat: some consulates require paid flight tickets
- Cover letter template: removed markdown symbols from the letter body
- GATE softened — single-question asks answered directly without launching the full flow

### Refactored
- **SKILL.md slimmed from 725 → 332 lines** — Step 2/Step 4 verbatim content moved to `references/`, eliminating duplication
- `SAY (COPY EXACTLY)` / "Must NOT output anything else" anti-pattern removed — replaced with "must include all points, natural phrasing allowed"
- `progress.md` path now platform-adaptive (Claude Code / Codex / fallback) instead of hardcoded to `~/.claude`
- PDF/Excel/Word generation now degrades gracefully when libraries are missing

## v1.0.0 (2026-05-27)

- Initial public release
- Support 5 identity types: student, employed, retired, freelancer, unemployed
- Cover all 29 Schengen states with verified visa center URLs
- France, Italy, Spain with full appointment walkthroughs
- Cross-session progress tracking via progress.md
- Itinerary generation with opening-hours verification
- Cover letter template with common doubt counter-strategies
- Bilingual README (Chinese + English)
