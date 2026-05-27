<h1 align="center">Schengen Visa Guide</h1>

<p align="center">
  <strong>English</strong>
  &nbsp;·&nbsp;
  <a href="../README.md"><strong>简体中文</strong></a>
</p>

<p align="center">
  <a href="../CHANGELOG.md"><img src="https://img.shields.io/badge/version-v1.0.0-orange" alt="Version"></a>
  &nbsp;
  <a href="../LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
</p>

<p align="center">
An AI agent skill for Chinese passport holders — pure markdown, platform-agnostic.<br>
Turns a chaotic visa checklist into a session-persistent, step-by-step interactive wizard.<br>
Works with Claude Code, Codex, OpenClaw, and any agent that reads skill files.
</p>

---

## The problem

DIY Schengen visa isn't paperwork — it's information warfare.

**Too many guides, no complete picture.**

One Xiaohongshu post covers the checklist. A Zhihu answer explains the appointment. A Bilibili video warns about common mistakes. Each is useful. None is complete. You end up with 8 tabs open, cross-referencing — only to find that none of them actually match your specific situation.

**Wrong identity, wrong documents.**

A student needs enrollment certificates and notarized parent sponsorship. An employed person needs company letters, business licenses, and salary slips. A freelancer needs to explain irregular income without standard proof — and may need a notarized relationship certificate for a sponsor. Same visa, completely different document stacks. Most guides are written for the "average applicant" — and average fits nobody.

**Cross-session amnesia. Every new chat is day one.**

Document prep takes 1–2 weeks, not one evening. Monday you sort insurance, Wednesday you print bank statements, Friday you book the appointment. You close the chat window between sessions. When you open it again — the AI doesn't even remember you're applying for a visa. You re-explain your identity, your country, your progress. After the third time, you give up and start tracking it in your head. Then you miss item #7.

**Documents form a dependency chain. Wrong order means redoing work.**

The itinerary dictates hotel dates. Hotel bookings must match itinerary cities. The flight reservation must align with the entry country — which must also be the country with the most itinerary days. Book hotels before the itinerary? Redo. Fly into Paris but Italy has the most days in your plan? Redo. No guide tells you the correct order — because a static page is flat, and this process has dependencies.

**The real cost isn't rejection. It's not knowing why you were rejected.**

The visa officer won't give you a reason. You get your passport back, stare at the rejection stamp, and guess: was the bank balance too low? Was the itinerary too rushed? Did the cover letter sound AI-generated? Then you wait another 3 weeks and roll the dice again.

---

## What this does

This skill turns your AI agent into a personal visa handler:

🪪 **Identify yourself once** → checklist tailored to you (5 identity types: student, employed, retired, freelancer, unemployed)

🔁 **Cross-session memory** → close the window, come back tomorrow, the agent reads `progress.md` and picks up exactly where you stopped — zero repetition

📋 **One item at a time** → 17–18 documents, each with clear instructions: where to get it, what format, common pitfalls

🛡️ **Sensitive boundary baked in** → passport scans, bank statements, ID photos — reminded, never generated. Itineraries and cover letters — generated, never faked

🌍 **29 countries, one lookup table** → official visa center URLs for every Schengen state. France/Italy/Spain have full appointment walkthroughs

📞 **Prepped for the phone call** → itinerary logic catches Monday-closed museums, impossible same-day city hops, and country-day mismatches — so the visa officer's random question doesn't trip you

---

## How it differs from reading a 攻略

| 攻略 (Guides) | This |
|---|---|
| Static text, one-size-fits-all | Custom checklist by **your** identity |
| You track progress in your head | `progress.md` — checked off as you go, survives reboots |
| "Go to the visa center website" | Exact URLs + step-by-step appointment flow per country |
| Hope you don't forget item #8 | Final review re-checks **every** checkbox, even the ticked ones |
| AI generates generic cover letters | Cover letter template asks for **your** truth first, then polishes |

In one line: 攻略 tell you what to do. This makes sure you actually do it.

---

## Can't I just ask ChatGPT / DeepSeek?

You can. But a general chatbot:

- **Doesn't remember you across sessions** — every new chat is a fresh start. You re-explain your identity, your country, your progress.
- **Has no structured flow** — it'll happily skip from insurance to itinerary because you asked, leaving a gap you won't notice until the appointment desk.
- **Doesn't enforce the sensitive boundary** — it might casually ask you to upload your bank statement. This skill has a hard rule: remind only.
- **May hallucinate visa center URLs** — this skill has all 29 official URLs verified and hardcoded.

General-purpose AI can help. This is purpose-built for one outcome: **getting you to the visa center with every document in order.**

---

## Install

Pure markdown, zero dependencies. Drop it into your agent's skills directory — works with any agent that reads skill files.

**Claude Code:**
```bash
cd ~/.claude/skills
git clone https://github.com/WJL-666123/schengen-visa-guide.git schengen-visa-guide
```

**Codex:**
```bash
cd ~/.codex/skills
git clone https://github.com/WJL-666123/schengen-visa-guide.git schengen-visa-guide
```

**OpenClaw / other agents:**
```bash
# Drop it into whichever directory your agent reads skills from
git clone https://github.com/WJL-666123/schengen-visa-guide.git schengen-visa-guide
```

---

## First use

Open your agent and say:

```
办申根签
```

The skill activates, reads `progress.md` (creates it if first time), and starts at the step where you are. Five identity types supported from day one — just pick yours.

---

## Project structure

```
schengen-visa-guide/
├── SKILL.md                      # Main wizard — full interactive flow + state machine
├── references/
│   ├── checklist.md              # Detailed per-document instructions by identity
│   ├── country-notes.md          # All 29 Schengen state URLs + France/Italy/Spain walkthrough
│   ├── cover-letter.md           # Cover letter template + common doubt counter-strategies
│   └── itinerary.md              # Itinerary generation rules + opening-hours verification
└── docs/
    ├── design.md                 # Architecture & design rationale
    ├── plan.md                   # Implementation plan
    └── project-description.md    # Design philosophy
```

---

## How it works under the hood

Five mechanisms, zero code:

1. **Session gate** — every new session, the agent must read `progress.md` before responding. Dead instruction, no exceptions.
2. **Push-then-save** — user confirms item → write to `progress.md` → then reply. Save first, talk second.
3. **Country router** — user picks a country → look up official URL from `country-notes.md`. Table lookup, not LLM guesswork.
4. **Sensitive/non-sensitive split** — ID docs, academic records, financials = remind only. Itinerary, cover letter = can generate.
5. **Final reconciliation** — re-check every item, including ticked ones, because a tick and a document-in-hand are two different things.

---

## Limitations

- Chinese passport only (for now)
- Schengen short-stay tourist visa (Type C) only
- Non-Schengen countries are explicitly rejected

---

## License

MIT — commercial use, modification, closed-source integration all fine.

---

*攻略 is a noun. This is a verb.*
