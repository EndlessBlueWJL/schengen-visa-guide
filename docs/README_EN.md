<h1 align="center">Schengen Visa Guide</h1>

<p align="center"><em>A guide is a noun. This is a verb.</em></p>

<p align="center">
  <strong>English</strong>
  &nbsp;·&nbsp;
  <a href="../README.md"><strong>简体中文</strong></a>
</p>

<p align="center">
  <a href="../CHANGELOG.md"><img src="https://img.shields.io/badge/version-v1.1.0-orange" alt="Version"></a>
  &nbsp;
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
</p>

<p align="center">
An AI agent skill for Chinese passport holders — platform-agnostic.<br>
Turns a dead guide into a session-persistent, step-by-step interactive wizard.<br>
Close the window, open it tomorrow — it remembers where you left off.
</p>

---

## Why this skill

General-purpose AI and static guides both help, but each has hard limits:

- **Guides aren't written for your identity** — one static article for everyone; a student and a retiree see the same checklist
- **AI has cross-session amnesia** — it can't precisely remember your progress; every session may require re-explaining
- **AI has no structured flow** — ask about insurance, it talks insurance; it won't proactively flag what you missed
- **AI has no sensitive boundary** — might casually ask you to upload your bank statement
- **Visa center URLs may be hallucinations** — AI confidently hands you a fake link
- **Documents are interdependent** — wrong order turns prep into chaos

This skill is purpose-built for one outcome: **getting you to the visa center with every document in order.**

---

## What this does

This skill turns your AI agent into a personal visa handler:

🪪 **Identify yourself once** → checklist tailored to you (6 identity types: student, employed, retired, freelancer, unemployed, minor)

🔁 **Cross-session memory** → close the window, come back tomorrow, the agent reads `progress.md` and picks up exactly where you stopped — zero repetition

📋 **One item at a time** → 17–18 documents, each with clear instructions: where to get it, what format, common pitfalls

💰 **Budget estimate** → computes how much proof of funds to show, by days (fitted to real practice: ¥2,000/day ≤15d, scaling up beyond) — no more folklore about a flat "¥30k balance"

🛡️ **Sensitive boundary baked in** → passport scans, bank statements, ID photos — reminded, never touched.
                                        Itineraries and cover letters — generated, never faked

🌍 **29 countries, one lookup table** → official visa center URLs for every Schengen state. France/Italy/Spain have full appointment walkthroughs, plus consular-district rules and fingerprint reminders

📞 **Prepped for the phone call** → itinerary logic catches Monday-closed museums, impossible same-day city hops, and country-day mismatches — so the visa officer's random question doesn't trip you

---

## How it differs from reading a 攻略

| 攻略 (Guides) | This |
|---|---|
| Static text, same for everyone | Custom checklist by **your** identity |
| You track progress in your head | `progress.md` — checked off as you go, survives reboots |
| "Go to the visa center website" | Exact URLs + step-by-step appointment flow per country |
| Hope you don't forget item #8 | Final review re-checks **every** checkbox, even the ticked ones |
| AI generates generic cover letters | Cover letter template asks for **your** truth first, then polishes |

In one line: 攻略 tell you what to do. This skill guides you through and makes sure you actually do it.

---

## Install

**Claude Code:**
```bash
cd ~/.claude/skills
git clone https://github.com/EndlessBlueWJL/schengen-visa-guide.git schengen-visa-guide
```

**Codex:**
```bash
cd ~/.codex/skills
git clone https://github.com/EndlessBlueWJL/schengen-visa-guide.git schengen-visa-guide
```

**OpenClaw / other agents:**
```bash
# Drop it into whichever directory your agent reads skills from
git clone https://github.com/EndlessBlueWJL/schengen-visa-guide.git schengen-visa-guide
```

> 💡 **Updating?** `git pull` inside the skill directory. This project is under active development — more country appointment flows are being added.

---

## First use

Open your agent and say:

```
办申根签
```

The skill activates, reads `progress.md` (creates it if first time), and starts at the step where you are. Six identity types supported from day one — just pick yours.

---

## Project structure

```
schengen-visa-guide/
├── SKILL.md                      # Main wizard — full interactive flow + state machine
├── references/
│   ├── checklist.md              # Detailed per-document instructions by identity + budget + fees
│   ├── country-notes.md          # All 29 Schengen state URLs + walkthroughs + districts + fingerprints
│   ├── cover-letter.md           # Cover letter template + common doubt counter-strategies
│   └── itinerary.md              # Itinerary generation rules + opening-hours verification
├── docs/
│   ├── design.md                 # Architecture & design rationale
│   ├── plan.md                   # Implementation plan
│   ├── project-description.md    # Design philosophy
│   └── README_EN.md              # English README
├── CHANGELOG.md                  # Version history
└── LICENSE
```

---

## How it works under the hood

1. **Session gate** — every new session, the visa flow must read `progress.md` before responding (single-question asks excepted). Dead instruction.
2. **Push-then-save** — user confirms item → write to `progress.md` → then reply. Save first, talk second.
3. **Country router** — user picks a country → look up official URL from `country-notes.md`. Table lookup, not LLM guesswork.
4. **Sensitive/non-sensitive split** — ID docs, academic records, financials = remind only. Itinerary, cover letter = can generate.
5. **Final reconciliation** — re-check every item, including ticked ones, because a tick and a document-in-hand are two different things.

---

## Important notes

- **Itinerary**: You can also use the Trip Planner (行程助手) app to build it yourself. Creating it by hand means you know where you're going each day — essential when the visa officer calls and quizzes you on your itinerary, flights, and hotels. If AI generates it, memorize the details. A wrong answer on the phone = rejection
- **Cover letter**: After AI drafts it, review every sentence personally. The cover letter is a deciding factor for approval — inaccurate information will cost you the visa
- **Info currency**: Visa policies, fees, URLs, and per-country daily reference amounts change. This skill's info is current as of 2025-07; **always verify requirements against the official consulate website**

---

## Limitations

- Chinese passport only (for now)
- Schengen short-stay tourist visa (Type C) only
- Non-Schengen countries are explicitly rejected

---

## License

MIT — commercial use, modification, closed-source integration all fine.
