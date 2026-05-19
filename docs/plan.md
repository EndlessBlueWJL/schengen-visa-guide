# Schengen Visa Skill — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an interactive Schengen visa wizard skill for Chinese-passport university students, covering 5-step process from country selection to visa collection.

**Architecture:** One main SKILL.md as the interactive wizard + 4 reference files (checklist, cover-letter, itinerary, country-notes). Progress tracked via `progress.md` written to user's project root.

**Tech Stack:** Markdown-only skill files. No code, no scripts, no dependencies.

---

## File Structure

```
schengen-visa-skill/
├── SKILL.md                  # Main wizard — create
├── references/
│   ├── checklist.md          # 15-item student checklist — create
│   ├── cover-letter.md       # Cover letter templates — create
│   ├── itinerary.md          # Itinerary guide — create
│   └── country-notes.md      # Country comparison — create
└── docs/
    ├── design.md             # Already exists
    └── plan.md               # This file
```

---

### Task 1: Create references/checklist.md

**Files:**
- Create: `d:/schengen-visa-skill/references/checklist.md`

- [ ] **Step 1: Write the checklist reference file**

```markdown
# 申根签证材料清单 — 在校学生版

> 共 15 项。每完成一项告诉我就好，我来勾掉。

## 证件类（4 项）

| # | 材料 | 说明 |
|---|------|------|
| 1 | 护照原件 + 所有面复印件 | 不需要复印空白页。原件递签当天带过去 |
| 2 | 身份证原件 + 复印件 | 正反面复印在同一面 |
| 3 | 户口本整本复印件 | 从封面到最后一页全部复印 |
| 4 | 两寸白底证件照 | 签证中心现场拍 35 块也行，自己带的话要近期 |

## 学生身份类（3 项）

| # | 材料 | 说明 |
|---|------|------|
| 5 | 中英文在读证明 | 学校教务处开具，需老师签字 + 学校公章 |
| 6 | 学生证原件 + 复印件 | 原件递签当天带过去 |
| 7 | 学信网中英文学籍证明 | 学信网（chsi.com.cn）在线申请，下载中英文版 |

## 资金类（1 项 + 备用方案）

| # | 材料 | 说明 |
|---|------|------|
| 8 | 最近三个月银行流水 | 余额至少 3 万以上。**父母出资**：另需父母流水 + 父母在职证明，若不在同一户口本还需亲属关系公证。**个人出资**：解释信里说明资金来源 |

## 旅行保障（1 项）

| # | 材料 | 说明 |
|---|------|------|
| 9 | 旅行保险 | 京东/支付宝搜"申根保险"购买。彩色打印前两页，保险日期必须完整覆盖行程。出签前别退，出签后可免费退 |

## 行程与机酒（3 项）

| # | 材料 | 说明 |
|---|------|------|
| 10 | 行程单 | 见 references/itinerary.md。可用「行程助手」app 或让我直接生成。申请国天数写最长，一天 3-4 景点，别太赶 |
| 11 | 机票预订单 | trip.com（携程海外版）预订，不用付款就能打印。出入境城市要呼应行程单 |
| 12 | 酒店预订单 | 携程选"免费取消"或"先用后付"，下单后下载确认单。酒店城市和日期必须跟行程单一致 |

## 灵魂材料（1 项）

| # | 材料 | 说明 |
|---|------|------|
| 13 | 解释信 | 见 references/cover-letter.md。解释资金疑点 + 强调回国约束力。英文写，可让我代笔 |

## 预约凭证（2 项）

| # | 材料 | 说明 |
|---|------|------|
| 14 | 签证申请表 | 在申请国签证官网上填写后生成的 PDF，打印出来 |
| 15 | 签证中心预约单 | 在 TLScontact/VFS/BLS 预约后生成的确认单，打印出来 |

---

### 材料准备顺序

1. 先做行程单（10）
2. 再订酒店（12）→ 日期和城市跟行程单对齐
3. 最后订机票（11）→ 出入境城市和日期呼应行程单
4. 三者都指向申请国，签证官才看不出破绽
```

- [ ] **Step 2: Verify file created correctly**

```bash
wc -l d:/schengen-visa-skill/references/checklist.md
# Should show ~65+ lines
```

---

### Task 2: Create references/country-notes.md

**Files:**
- Create: `d:/schengen-visa-skill/references/country-notes.md`

- [ ] **Step 1: Write the country notes reference file**

```markdown
# 申根签申请国对比

> 核心原则：行程单配合申请国。申请国天数写最长，出入境尽量走申请国。

## 三国推荐

| | 法国 | 意大利 | 西班牙 |
|---|---|---|---|
| **签证中心** | TLScontact | VFS Global | BLS |
| **领区限制** | 不分领区，全国任意城市可递 | 分领区 | 分领区 |
| **出签风格** | 偏紧，给的天数基本=行程单天数 | 通过率不错 | 有时会比行程多给几天 |
| **适合人群** | 不在北上广的、想就近递签的 | 行程主要在意国的 | 想多蹭几天的 |

## 其他国家

用户选了法/意/西之外的国家时：

1. 自行搜索该国的申根签证中心（TLScontact / VFS Global / BLS / 其他）
2. 确认是否有领区限制
3. 提醒：行程单里该国天数写最长

## 通用提醒

- 申根签是短期旅游签（C 签），最多停留 90 天
- 有申根签后可在申根区 29 国自由通行
- 第一次申请建议走法/意/西，通过率最高
- 不管真实计划怎么玩，材料上行程单、酒店、机票三者必须自洽
```

- [ ] **Step 2: Verify file created correctly**

```bash
wc -l d:/schengen-visa-skill/references/country-notes.md
```

---

### Task 3: Create references/cover-letter.md

**Files:**
- Create: `d:/schengen-visa-skill/references/cover-letter.md`

- [ ] **Step 1: Write the cover letter reference file**

```markdown
# 解释信指南

> 解释信是唯一能跟签证官「对话」的机会。把材料的疑点全部解释干净，强调你一定会回国。

## 学生解释信模板

用英文写，结构如下：

```
[Your Name]
[Passport Number]
[Date]

To the Visa Officer,

Subject: Cover Letter for Schengen Visa Application

Dear Visa Officer,

I am [Name], a [year]-year student at [University Name], majoring in [Major].

## Travel Purpose
I plan to visit [countries] from [start date] to [end date] (total [X] days).
This is my first trip to Europe, and I have always wanted to experience
European culture and history.

## Itinerary Summary
- [Country 1]: [X days] - visit [key cities], [brief highlights]
- [Country 2]: [X days] - visit [key cities], [brief highlights]
- [Country 3]: [X days] - visit [key cities], [brief highlights]

My main destination is [application country] where I will spend the most
time ([X days]).

## Financial Support
[选择一种，改下面的段落]

A) 个人出资版：
My travel expenses are covered by my personal savings. [解释资金来源，
如：I transferred 40,000 RMB to my bank account before applying because
I normally keep my money in Alipay for daily use.]

B) 父母出资版：
My travel expenses are sponsored by my parents [names]. Please find
their bank statements and employment certificates attached.

## Strong Ties to China
I have strong reasons to return to China after my trip:
- I am currently enrolled at [University] and my courses resume on [date].
- I have [X years] remaining until graduation.
- My family, including my parents, live in China.
- My career plan is to work in China after graduation in [field].

I assure you that I will return to China before my visa expires and
comply with all Schengen regulations.

Sincerely,
[Name]
[Phone]
[Email]
```

## 常见疑点 + 应对策略

| 疑点 | 如何解释 |
|------|---------|
| 临时大额转账 | "钱平时放在支付宝/微信，申请签证才转到银行卡" |
| 行程特别长（30+ 天） | "放寒假/暑假，有的是时间。第一次去欧洲想多看看" |
| 余额刚够 3 万 | "往返机票只要三千多，住青旅一晚一百多，够用" |
| 银行卡流水少 | "学生日常消费主要用微信/支付宝" |
| 白本护照 | "虽然第一次出国，但我准备了详细行程，证明我是去旅游" |

## 学生身份加分项（强调在解释信里）

- 在读学生 = 天然回国约束力
- 提到学业进度和毕业计划
- 提到家人在国内
- 提到未来的国内职业规划
- 语气真诚，不要像套模板
```

- [ ] **Step 2: Verify file created correctly**

```bash
wc -l d:/schengen-visa-skill/references/cover-letter.md
```

---

### Task 4: Create references/itinerary.md

**Files:**
- Create: `d:/schengen-visa-skill/references/itinerary.md`

- [ ] **Step 1: Write the itinerary reference file**

```markdown
# 行程单指南

> 行程单是送签文件，不是真实的旅游计划。它的唯一目的是让签证官相信「这人是来旅游的，会按时回去」。

## 两个选项

### 选项 A：用「行程助手」app 自己做

1. 下载「行程助手」app
2. 选择要去的国家和城市，添加天数
3. 自动导出 Excel 格式的行程单
4. 简单修改格式即可
5. 做好后可以发给我帮你检查——是否合理、是否跟申请国匹配

### 选项 B：让我直接生成

告诉我：
- 申请哪个国家
- 想去哪些城市
- 总共多少天
- 预计出发日期

我生成一份送签标准的行程单表格，你拿去跟酒店和机票对一下就完事。

## 送签行程单规则

- **一天 3-4 个景点**，最多 5 个，不要特种兵
- **申请国天数写最长**——比如申法国，法国的天数要比其他国家都多
- **出入境城市最好在申请国**——申法国就巴黎进巴黎出
- **检查景点营业时间**——周一闭馆的别写周一
- **城市间移动合理**——巴黎到罗马没问题，但同一天跳三个国家就离谱
- **交通方式写清楚**——火车、飞机、步行
- **住哪一栏要跟酒店预订单一致**
- **格式**：日期 | 城市 | 当天安排 | 交通 | 住宿

## 最终格式（送签标准）

| 日期 | 城市 | 行程安排 | 交通方式 | 住宿 |
|------|------|---------|---------|------|
| 7/1 | Paris | Arrive at CDG, check in, visit Eiffel Tower (booked), Seine river walk | Flight CA123 | Hotel Ibis Paris |
| 7/2 | Paris | Louvre Museum (9:00-18:00, closed Tue), Tuileries Garden, Place de la Concorde | Metro | Hotel Ibis Paris |
| ... | ... | ... | ... | ... |

## 检查清单

生成或收到行程单后，确认以下：
- [ ] 申请国天数是否最长？
- [ ] 出入境是否在申请国？
- [ ] 每天景点是否 ≤4 个？
- [ ] 景点营业时间是否合理？
- [ ] 城市间移动方式是否写清楚？
- [ ] 酒店名是否跟预订单一致？
- [ ] 日期范围是否覆盖全程？
```

- [ ] **Step 2: Verify file created correctly**

```bash
wc -l d:/schengen-visa-skill/references/itinerary.md
```

---

### Task 5: Create SKILL.md

**Files:**
- Create: `d:/schengen-visa-skill/SKILL.md`

- [ ] **Step 1: Write the main SKILL.md**

```markdown
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

- Every time user says an item is done, immediately edit `progress.md` to check it off.
- After each update, report: "还有 X 项未完成。下一步建议：[next most urgent item]."
- Prioritize items with dependencies (e.g., remind them to get the enrollment certificate early since it needs a teacher's signature).

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
```

- [ ] **Step 2: Verify file structure is complete**

```bash
find d:/schengen-visa-skill -type f | sort
```
```

---

### Task 6: Final verification

**Files:**
- Verify: all files in `d:/schengen-visa-skill/`

- [ ] **Step 1: Verify all files exist and are non-empty**

```bash
for f in \
  "d:/schengen-visa-skill/SKILL.md" \
  "d:/schengen-visa-skill/references/checklist.md" \
  "d:/schengen-visa-skill/references/country-notes.md" \
  "d:/schengen-visa-skill/references/cover-letter.md" \
  "d:/schengen-visa-skill/references/itinerary.md"; do
  echo "=== $f ==="
  wc -l "$f"
done
```

Expected: All files exist with >0 lines.

- [ ] **Step 2: Cross-check with design doc**

Verify coverage against `docs/design.md`:
- [ ] 5-step flow all in SKILL.md
- [ ] 15 items all in checklist.md
- [ ] Country comparison in country-notes.md
- [ ] Cover letter template + doubt strategies in cover-letter.md
- [ ] Itinerary guide in itinerary.md
- [ ] Progress tracking mechanism in SKILL.md
- [ ] Final confirmation checklist in SKILL.md
- [ ] Sensitive material handling (remind-only) in SKILL.md
- [ ] Hotel booking division of labor in SKILL.md
- [ ] Material preparation order (itinerary → hotel → flight) in checklist.md

- [ ] **Step 3: Verify frontmatter format**

Check SKILL.md has valid YAML frontmatter with `name` and `description` fields. Description starts with "Use when..." and does not summarize the skill's workflow.
```

---

