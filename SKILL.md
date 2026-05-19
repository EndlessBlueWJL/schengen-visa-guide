---
name: schengen-visa-guide
description: Use when user mentions Schengen visa, 申根签, 申根签证, European travel visa application, wants to apply for a visa to Europe, needs help with visa document checklist, cover letter, or itinerary for visa purposes.
---

# Schengen Visa Guide

Interactive Schengen visa wizard for Chinese-passport holders. Guides through the full DIY process — from choosing where to apply to submitting documents. Currently supports students; other profiles will be added later.

## Overview

This skill turns Claude into a step-by-step visa application guide. It maintains a progress file (`progress.md`) in the user's project directory and tracks which of the 15 required documents are done.

## Core Principles

- **The goal is getting the visa, not planning a real trip.** All advice optimizes for approval.
- **Sensitive materials (passport, ID, financials, academic records): only remind, never generate.** User says "done" → mark complete. Do not ask for or process their content.
- **Non-sensitive materials (itinerary, cover letter): can help generate or review.**
- **One question at a time.** Don't dump a huge checklist at once.
- **After every interaction, update `progress.md` and report what's still missing.**

## Session Start (MANDATORY — do this FIRST, before ANY response)

The very first thing you do in every new conversation — before saying "你好", before asking what they need, before anything — is:

1. Read `progress.md` in the project directory.
2. If it exists: tell the user "上次你办到了 X/Y 项，我们继续。下一步是 Z。" and resume from where they left off.
3. If it doesn't exist: they're new, create `progress.md` and start from Step 1.

**Do not skip this.** Every new window is a fresh start for Claude. The user should never have to re-tell you what they've already done.

## Flow

### Step 1: Country Selection

First, confirm the user is a university student. (This version only supports students.)

Then present 3 recommended countries as equal options:

1. **France** — TLScontact, no consular district limits (apply in any Chinese city), fast processing, but tends to give exactly the days you request
2. **Italy** — VFS Global, decent approval rate
3. **Spain** — BLS, sometimes gives more days than requested

If the user picks another country, that's fine — adapt. Look up the correct visa center for that country.

**After selection, warn the user:**
"申 [country] 的话，行程单里 [country] 的天数要写最长，出入境机票最好也是 [country]，酒店订单跟行程单的日期城市要对上。材料上别穿帮。"

### Step 2: Online Appointment

Look up the correct visa center for the chosen country (TLScontact / VFS Global / BLS / other). Guide the user:

1. Fill in the visa application form on the country's official visa website → generates an application number. **Screenshot it.**
2. Register on the visa center website (TLS/VFS/BLS) → link the application number → book an appointment.
3. Print both the application form and the appointment confirmation.

These become checklist items #14 and #15.

### Step 3: Document Preparation (15 items)

Use the checklist from `references/checklist.md`. Guide the user category by category:

**Sensitive categories (remind only, don't generate):**
- ID documents (items 1-4): Tell them what's needed and the format
- Student documents (items 5-7): Tell them where to get each one
- Financial documents (item 8): Explain the two paths (self-funded vs parent-sponsored); warn about the notarized relationship certificate if sponsored by parents and not in the same hukou

**Non-sensitive categories (can help generate/review):**
- Insurance (item 9): Recommend JD.com or Alipay, remind to print first 2 pages in color
- Itinerary (item 10): See `references/itinerary.md` — recommend 行程助手 app first, offer to generate directly
- Flight reservation (item 11): Direct to trip.com, no payment needed
- Hotel reservation (item 12): Direct to Ctrip, filter by "free cancellation." Claude can list what hotels are needed by date/city, but the user must book them. Claude can review the confirmations.
- Cover letter (item 13): See `references/cover-letter.md` — offer to draft it

**Appointment documents (items 14-15):** Already printed in Step 2.

**Important ordering:** Itinerary (10) → Hotels (12) → Flights (11). They must align: same dates, same cities, all pointing to the application country.

### Step 4: Appointment Day

When all items are done and user says they're ready:

Remind:
- Arrive on time at the visa center
- **Do NOT staple or clip any documents together.** Just stack them in order.
- You may get a phone verification call: answer truthfully, don't panic
- If asked about funds: explain calmly (the cover letter already covers this)

### Step 5: Wait for Result

- Mail delivery: about 1 week (Shanghai consular district is fast)
- Pickup: watch for notification
- Budget 2 weeks buffer
- After visa approval: cancel the travel insurance if you want (it's refundable)

## Progress Tracking

### Creating progress.md

On first interaction, create `progress.md` in the user's working directory with all 15 items as unchecked:

```markdown
# Schengen Visa Progress

## 证件类
- [ ] 1. 护照原件 + 所有面复印件
- [ ] 2. 身份证原件 + 复印件
- [ ] 3. 户口本整本复印件
- [ ] 4. 两寸白底证件照

## 学生身份类
- [ ] 5. 中英文在读证明（签字+公章）
- [ ] 6. 学生证原件 + 复印件
- [ ] 7. 学信网中英文学籍证明

## 资金类
- [ ] 8. 近三个月银行流水（余额≥3万）

## 旅行保障
- [ ] 9. 旅行保险（覆盖全程，彩打前两页）

## 行程与机酒
- [ ] 10. 行程单
- [ ] 11. 机票预订单（trip.com）
- [ ] 12. 酒店预订单（携程免费取消）

## 灵魂材料
- [ ] 13. 解释信

## 预约凭证
- [ ] 14. 签证申请表
- [ ] 15. 签证中心预约单
```

### Updating progress

**Every time the user says an item is done, you have TWO actions before replying:**

1. **First**: Edit `progress.md` and check off that item.
2. **Then**: Reply to the user confirming it's done, report remaining count, suggest next step.

This means the edit is the priority. User says "好了" → you immediately write the checkbox, then you speak. Never reply and then save — that's backwards. The save is the action; the reply is the summary.

### Final confirmation

When user says "准备好了" or "全部完成了", do a final review:

Go through every item — including ones already checked off:
1. All 15 items checked?
2. ID/student/financial documents confirmed obtained? (re-confirm even if previously checked)
3. Insurance dates fully cover the trip?
4. Bank statements are from the last 3 months?
5. Enrollment certificate has signature and school stamp?
6. Flight/hotel reservation names match passport?
7. Itinerary country days match the application country?
8. No staples or clips on any document?
9. Documents stacked in correct order?

All pass → "可以去递签了，祝顺利出签。"

## Reference Files

Read these as needed during the relevant step — don't load all at once:

- `references/checklist.md` — Full 15-item checklist with detailed instructions
- `references/country-notes.md` — France/Italy/Spain comparison + other countries
- `references/cover-letter.md` — Cover letter template + common doubt strategies
- `references/itinerary.md` — Itinerary guide (行程助手 app + direct generation)
