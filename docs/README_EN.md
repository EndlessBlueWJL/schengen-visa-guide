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
Turns a dead guide into a session-persistent, step-by-step interactive wizard.<br>
Close the window, open it tomorrow — it remembers where you left off.
</p>

---

## The problem

- Too many guides, none written for your identity
- AI can't precisely remember your progress — it has a vague sense at best. Every session may require re-explaining
- Some documents are interdependent — wrong order turns prep into chaos

---

## What this does

This skill turns your AI agent into a personal visa handler:

🪪 **Identify yourself once** → checklist tailored to you (5 identity types: student, employed, retired, freelancer, unemployed)

🔁 **Cross-session memory** → close the window, come back tomorrow, the agent reads `progress.md` and picks up exactly where you stopped — zero repetition

📋 **One item at a time** → 17–18 documents, each with clear instructions: where to get it, what format, common pitfalls

🛡️ **Sensitive boundary baked in** → passport scans, bank statements, ID photos — reminded, never generated.
                                        Itineraries and cover letters — generated, never faked

🌍 **29 countries, one lookup table** → official visa center URLs for every Schengen state. France/Italy/Spain have full appointment walkthroughs

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

## Can't I just ask ChatGPT / DeepSeek?

General-purpose AI can help, but it:

- **Cross-session amnesia** — AI can't precisely remember your progress. It has a vague sense at best. Every session may require re-explaining
- **No structured flow** — ask about insurance, it talks insurance. Ask about itinerary, it talks itinerary. It won't proactively flag what you missed
- **No sensitive boundary** — might casually ask you to upload your bank statement. This skill has a hard rule: remind only
- **Visa center URLs may be hallucinations** — this skill has all 29 official URLs verified and hardcoded

General AI can help. This is purpose-built for one outcome: **getting you to the visa center with every document in order.**

---

## Install

Pure markdown, zero dependencies. Drop it into your agent's skills directory.

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

> 💡 **Updating?** `git pull` inside the skill directory. This project is under active development — more identity types and country flows are being added.

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

1. **Session gate** — every new session, the agent must read `progress.md` before responding. Dead instruction, no exceptions.
2. **Push-then-save** — user confirms item → write to `progress.md` → then reply. Save first, talk second.
3. **Country router** — user picks a country → look up official URL from `country-notes.md`. Table lookup, not LLM guesswork.
4. **Sensitive/non-sensitive split** — ID docs, academic records, financials = remind only. Itinerary, cover letter = can generate.
5. **Final reconciliation** — re-check every item, including ticked ones, because a tick and a document-in-hand are two different things.

---

## Important notes

- **Itinerary**: Use the Trip Planner (行程助手) app to build it yourself. Creating it by hand means you know where you're going each day — essential when the visa officer calls and quizzes you on your itinerary, flights, and hotels. If AI generates it, memorize the details. A wrong answer on the phone = rejection
- **Cover letter**: After AI drafts it, review every sentence personally. The cover letter is a deciding factor for approval — inaccurate information will cost you the visa

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
