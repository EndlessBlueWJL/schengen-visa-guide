---
name: schengen-visa-guide
description: Use EXCLUSIVELY when user mentions Schengen visa (申根签/申根签证/办申根签) or wants to apply for a tourist visa to Schengen countries (France, Italy, Spain, Germany, Switzerland, etc.). Covers ALL Chinese mainland passport holders — student, employed, retired, freelancer, or unemployed. This skill ONLY covers Schengen short-stay tourist visas.
---

# Schengen Visa Guide

## GATE

Every session starts here. Before any output:

1. Read progress.md.
2. Check `current_step`.
3. Jump to that step below. Execute the SAY template.

**Do not say hello. Do not ask what the user needs. Read progress.md first.**

If progress.md doesn't exist → create it (template at bottom of this file), then go to Step 1.

---

## MAIN FLOW (FIXED — DO NOT BRANCH)

```
Step 1: 询问身份
Step 2: 给出材料清单 + 流程图
Step 3: 询问申请国家
Step 4: 给出预约方法
Step 5: 逐项准备资料
Step 6: 最终核对
```

**Never skip steps. Never reorder. Never branch off this main line unless the user explicitly asks for something else.**

---

## Step 1: 询问身份

**current_step = identity**

**SAY (COPY EXACTLY):**
```
你目前的身份是？

在校学生 / 在职 / 退休 / 自由职业 / 无业
```

**Must NOT output anything else.**

**After user answers:** Write 身份 to progress.md. Set current_step = checklist. Go to Step 2.

---

## Step 2: 给出材料清单 + 流程图

**current_step = checklist**

Pick the template matching the user's identity. Show checklist first, then process flow. Do NOT ask any questions yet.

### 在校学生

**SAY (COPY EXACTLY):**
```
材料清单（共 17 项）：

【证件类】
□ 1. 护照原件 + 所有面复印件 ×2 份（有效期≥离开申根区后3个月，≥2空白页）
□ 2. 旧护照复印件（如有）
□ 3. 身份证原件 + 复印件
□ 4. 户口本整本复印件（封面到最后一页）
□ 5. 两寸白底证件照

【学生身份】
□ 6. 中英文在读证明（签字+公章）
□ 7. 学生证原件 + 复印件
□ 8. 学信网中英文学籍证明

【旅行保障】
□ 9. 旅行保险（保额≥3万欧元，覆盖全程，彩打前两页）

【资金类】
□ 10. 近3-6个月银行流水（余额≥3万）
□ 11. 房产证/车产复印件（有就提供，加分项）

【行程与机酒】
□ 12. 行程单（申请国天数最长）
□ 13. 机票预订单（trip.com 不付款）
□ 14. 酒店预订单（携程免费取消）

【灵魂材料】
□ 15. 解释信（资金来源 + 回国约束力 + 旅行目的）

【预约凭证】
□ 16. 签证申请表
□ 17. 签证中心预约单

---

流程图：

选申请国 → 网上预约 → 准备证件 → 学生材料 → 买保险 → 打流水 → 做行程单 → 订机票 → 订酒店 → 写解释信 → 递签 → 等出签
```

### 在职

**SAY (COPY EXACTLY):**
```
材料清单（共 18 项）：

【证件类】
□ 1. 护照原件 + 所有面复印件 ×2 份（有效期≥离开申根区后3个月，≥2空白页）
□ 2. 旧护照复印件（如有）
□ 3. 身份证原件 + 复印件
□ 4. 户口本整本复印件（封面到最后一页）
□ 5. 两寸白底证件照

【在职身份】
□ 6. 在职证明（公司抬头纸，法人签字+公章，体现姓名/职务/薪资/入职年限/准假日期）
□ 7. 营业执照副本复印件（加盖公章）
□ 8. 近6个月工资流水

【旅行保障】
□ 9. 旅行保险（保额≥3万欧元，覆盖全程，彩打前两页）

【资金类】
□ 10. 近3-6个月银行流水（余额≥3万）
□ 11. 房产证/车产复印件（有就提供，加分项）

【行程与机酒】
□ 12. 行程单（申请国天数最长）
□ 13. 机票预订单（trip.com 不付款）
□ 14. 酒店预订单（携程免费取消）

【已婚附加】（已婚者准备，未婚跳过）
□ 15. 结婚证复印件 + 英文翻译件

【灵魂材料】
□ 16. 解释信（资金来源 + 回国约束力 + 旅行目的）

【预约凭证】
□ 17. 签证申请表
□ 18. 签证中心预约单

---

流程图：

选申请国 → 网上预约 → 准备证件 → 公司开证明 → 买保险 → 打流水 → 做行程单 → 订机票 → 订酒店 → 结婚证（如有）→ 写解释信 → 递签 → 等出签
```

### 退休

**SAY (COPY EXACTLY):**
```
材料清单（共 17 项）：

【证件类】
□ 1. 护照原件 + 所有面复印件 ×2 份（有效期≥离开申根区后3个月，≥2空白页）
□ 2. 旧护照复印件（如有）
□ 3. 身份证原件 + 复印件
□ 4. 户口本整本复印件（封面到最后一页）
□ 5. 两寸白底证件照

【退休身份】
□ 6. 退休证原件 + 复印件
□ 7. 退休金流水（近3-6个月）

【旅行保障】
□ 8. 旅行保险（保额≥3万欧元，覆盖全程，彩打前两页）

【资金类】
□ 9. 近3-6个月银行流水（余额≥3万）
□ 10. 房产证/车产复印件（有就提供，加分项）

【行程与机酒】
□ 11. 行程单（申请国天数最长）
□ 12. 机票预订单（trip.com 不付款）
□ 13. 酒店预订单（携程免费取消）

【已婚附加】（已婚者准备，未婚跳过）
□ 14. 结婚证复印件 + 英文翻译件

【灵魂材料】
□ 15. 解释信（资金来源 + 回国约束力 + 旅行目的）

【预约凭证】
□ 16. 签证申请表
□ 17. 签证中心预约单

---

流程图：

选申请国 → 网上预约 → 准备证件 → 退休材料 → 买保险 → 打流水 → 做行程单 → 订机票 → 订酒店 → 结婚证（如有）→ 写解释信 → 递签 → 等出签
```

### 自由职业

**SAY (COPY EXACTLY):**
```
材料清单（共 17 项）：

【证件类】
□ 1. 护照原件 + 所有面复印件 ×2 份（有效期≥离开申根区后3个月，≥2空白页）
□ 2. 旧护照复印件（如有）
□ 3. 身份证原件 + 复印件
□ 4. 户口本整本复印件（封面到最后一页）
□ 5. 两寸白底证件照

【身份材料】
□ 6. 收入来源说明（解释信里详细说明，附 freelancer 合同/稿费记录/投资收益证明等）
□ 7. 出资人材料（如有人出资：出资人银行流水 + 出资人身份证复印件 + 亲属关系公证。无人出资则跳过）

【旅行保障】
□ 8. 旅行保险（保额≥3万欧元，覆盖全程，彩打前两页）

【资金类】
□ 9. 近3-6个月银行流水（余额≥3万）
□ 10. 房产证/车产复印件（有就提供，加分项）

【行程与机酒】
□ 11. 行程单（申请国天数最长）
□ 12. 机票预订单（trip.com 不付款）
□ 13. 酒店预订单（携程免费取消）

【已婚附加】（已婚者准备，未婚跳过）
□ 14. 结婚证复印件 + 英文翻译件

【灵魂材料】
□ 15. 解释信（资金来源 + 回国约束力 + 旅行目的）

【预约凭证】
□ 16. 签证申请表
□ 17. 签证中心预约单

---

流程图：

选申请国 → 网上预约 → 准备证件 → 收入/出资人材料 → 买保险 → 打流水 → 做行程单 → 订机票 → 订酒店 → 结婚证（如有）→ 写解释信 → 递签 → 等出签
```

### 无业

**SAY (COPY EXACTLY):**
```
材料清单（共 17 项）：

【证件类】
□ 1. 护照原件 + 所有面复印件 ×2 份（有效期≥离开申根区后3个月，≥2空白页）
□ 2. 旧护照复印件（如有）
□ 3. 身份证原件 + 复印件
□ 4. 户口本整本复印件（封面到最后一页）
□ 5. 两寸白底证件照

【身份材料】
□ 6. 收入来源说明（解释信里详细说明）
□ 7. 出资人材料（如有人出资：出资人银行流水 + 出资人身份证复印件 + 亲属关系公证。不在同一户口本需亲属关系公证。无人出资则跳过）

【旅行保障】
□ 8. 旅行保险（保额≥3万欧元，覆盖全程，彩打前两页）

【资金类】
□ 9. 近3-6个月银行流水（余额≥3万）
□ 10. 房产证/车产复印件（有就提供，加分项）

【行程与机酒】
□ 11. 行程单（申请国天数最长）
□ 12. 机票预订单（trip.com 不付款）
□ 13. 酒店预订单（携程免费取消）

【已婚附加】（已婚者准备，未婚跳过）
□ 14. 结婚证复印件 + 英文翻译件

【灵魂材料】
□ 15. 解释信（资金来源 + 回国约束力 + 旅行目的）

【预约凭证】
□ 16. 签证申请表
□ 17. 签证中心预约单

---

流程图：

选申请国 → 网上预约 → 准备证件 → 收入/出资人材料 → 买保险 → 打流水 → 做行程单 → 订机票 → 订酒店 → 结婚证（如有）→ 写解释信 → 递签 → 等出签
```

**After showing checklist + flow:** Write checklist to progress.md. Set current_step = country. Go to Step 3.

---

## Step 3: 询问申请国家

**current_step = country**

**SAY (COPY EXACTLY):**
```
你想申请哪个申根国家？首次申请推荐这三个：

1. 法国 — 不分领区，全国任意城市都能递签，不用回老家。通过 TLScontact 预约，流程清晰。
2. 意大利 — 通过率不错，对学生和自由职业比较友好。
3. 西班牙 — 有时给的停留天数会比行程单写的多几天，比较大方。
```

**Must NOT ask anything else. No dates, no passport, no marriage.**

**After user answers:** Write 目标国家 to progress.md. Set current_step = appointment. Go to Step 4.

---

## Step 4: 给出预约方法

**current_step = appointment**

Look up the country and output the matching template.

| Country | System | URL |
|---|---|---|
| France | TLScontact | ① https://france-visas.gouv.fr/zh → ② https://visas-fr.tlscontact.cn |
| Italy | VFS Global | https://visa.vfsglobal.com/chn/zh/ita |
| Spain | BLS | https://web.blscn.cn |
| Germany | VFS Global | https://visa.vfsglobal.com/chn/zh/deu |
| Switzerland | VFS Global | https://visa.vfsglobal.com/chn/zh/che |
| Netherlands | VFS Global | https://visa.vfsglobal.com/chn/zh/nld |
| Other | See references/country-notes.md | — |

### France

**SAY (COPY EXACTLY):**
```
法国签证分两步：

第 1 步：先去 France-Visas 填表
网址：https://france-visas.gouv.fr/zh
填完会给你一个 FV 编号，截图保存。

第 2 步：拿着 FV 编号去 TLScontact 约时间
网址：https://visas-fr.tlscontact.cn

法国不分领区，全国任意城市都可以递签。

提醒：行程单里法国的天数要写最长，出入境机票最好也是法国，酒店跟行程单的日期城市要对上。

预约好了就说"约好了"，我们开始准备材料。
```

### Italy

**SAY (COPY EXACTLY):**
```
意大利通过 VFS Global 预约：
网址：https://visa.vfsglobal.com/chn/zh/ita

流程：
1. 填完申请表 → 获取申请码，截图保存
2. 系统会发邮件给你，里面有派发的账号和密码
3. 等待审核通过
4. 审核通过后会再发邮件通知缴费
5. 用派发的账号密码登录缴费

提醒：行程单里意大利的天数要写最长，出入境机票最好也是意大利，酒店跟行程单的日期城市要对上。

预约好了就说"约好了"，我们开始准备材料。
```

### Spain

**SAY (COPY EXACTLY):**
```
西班牙通过 BLS 预约：
网址：https://web.blscn.cn

填表 + 预约都在这个网站完成。

提醒：行程单里西班牙的天数要写最长，出入境机票最好也是西班牙，酒店跟行程单的日期城市要对上。西班牙有时会比行程多给几天。

预约好了就说"约好了"，我们开始准备材料。
```

### Other countries

**SAY (fill {country} and {url}, COPY EXACTLY otherwise):**
```
{country} 通过 {system} 预约：
网址：{url}

提醒：行程单里 {country} 的天数要写最长，出入境机票最好也是 {country}，酒店跟行程单的日期城市要对上。

预约好了就说"约好了"，我们开始准备材料。
```

**After user confirms appointment done:** Set current_step = documents. Go to Step 5.

---

## Step 5: 逐项准备资料

**current_step = documents**

Guide through categories in this fixed order. One category at a time. After user confirms one category → check off items in progress.md → report progress → move to next.

**Fixed order:**

| # | Category | Action |
|---|---|---|
| 1 | 证件类 | Remind only |
| 2 | 身份材料 | Remind only (pick template matching identity) |
| 3 | 旅行保险 | Remind + recommend 京东/支付宝 |
| 4 | 资金类 | Remind only |
| 5 | 行程与机酒 | 行程单(can generate) → 机票(trip.com) → 酒店(携程) |
| 6 | 解释信 + 已婚附加 + 预约凭证 | 解释信(can generate), 已婚(如有则提醒), 预约凭证(打印) |

---

### Category 1: 证件类

**SAY (COPY EXACTLY):**
```
先从证件开始：

1. 护照原件 + 所有面复印件 ×2 份 — 有效期要超过离开申根区后 3 个月，至少 2 页空白签证页。
2. 旧护照复印件 — 有的话复印个人信息页+签证页+出入境盖章页。没有就跳过。
3. 身份证原件 + 复印件 — 正反面复印在同一面。
4. 户口本整本复印件 — 从封面到最后一页全部复印。
5. 两寸白底证件照 — 签证中心现场拍也行，自己带的话要近期的。

准备好了就说"证件好了"。
```

---

### Category 2: 身份材料

Pick the one matching the user's identity.

**在校学生 (COPY EXACTLY):**
```
学生身份材料：

6. 中英文在读证明 — 学校教务处开具，老师签字 + 学校公章。
7. 学生证原件 + 复印件 — 原件递签当天带过去。
8. 学信网中英文学籍证明 — 学信网（www.chsi.com.cn）在线申请下载。

准备好了就说"学生材料好了"。
```

**在职 (COPY EXACTLY):**
```
在职身份材料：

6. 在职证明 — 公司抬头纸，体现姓名/职务/薪资/入职年限/准假日期，法人或人事签字 + 公章。
7. 营业执照副本复印件 — 加盖公司公章。
8. 近 6 个月工资流水 — 银行打印。

准备好了就说"在职材料好了"。
```

**退休 (COPY EXACTLY):**
```
退休身份材料：

6. 退休证原件 + 复印件。
7. 退休金流水 — 近 3-6 个月。

准备好了就说"退休材料好了"。
```

**自由职业 (COPY EXACTLY):**
```
身份材料：

6. 收入来源说明 — 解释信里详细说明收入来源，附 freelancer 合同/稿费记录等。
7. 出资人材料 — 有人出资才需要：出资人银行流水 + 身份证复印件 + 亲属关系公证。没人出资跳过。

准备好了就说"身份材料好了"。
```

**无业 (COPY EXACTLY):**
```
身份材料：

6. 收入来源说明 — 解释信里详细说明。
7. 出资人材料 — 有人出资才需要：出资人银行流水 + 身份证复印件 + 亲属关系公证（不在同一户口本需要）。没人出资跳过。

准备好了就说"身份材料好了"。
```

---

### Category 3: 旅行保险

**SAY (COPY EXACTLY):**
```
旅行保险：

京东或支付宝搜"申根保险"。
要求：保额至少 3 万欧元，覆盖整个申根区，保险日期完整覆盖行程。
出签前别退保，出签后可退。
买了之后彩色打印前两页。

买好了就说"保险好了"。
```

---

### Category 4: 资金类

**SAY (COPY EXACTLY):**
```
资金证明：

10. 近 3-6 个月银行流水 — 银行打印，余额至少 3 万以上。别临时大额转账。
11. 房产证/车辆登记证复印件 — 有就提供，加分项。只交复印件。没有就跳过。

准备好了就说"资金好了"。
```

---

### Category 5: 行程与机酒

Three sub-steps in order.

**5a: 行程单 (COPY EXACTLY):**
```
行程单：

我可以帮你生成，会直接显示在聊天里，再给你一份 Excel 可编辑版本下载。

但在那之前强烈建议你先用「行程助手」app 自己做一遍——你自己动手排过，才会对每天去哪、住哪、怎么走有印象。递签后可能会接到电话核实（电调），签证官随机问你行程细节，答不上来直接拒签。

要我给你生成的话，告诉我：想去哪些城市、出发日期、总共几天。
```

**When generating itinerary:**
1. Show the itinerary table directly in chat.
2. Provide an Excel/CSV downloadable file.
3. **Attraction order must be logical and 顺路** — same-day attractions in the same area, no criss-crossing the city. Plan a relaxed route: morning one spot, lunch, afternoon one spot, evening stroll. Two attractions per half-day max.
4. **Pacing must be relaxed** — 2-3 attractions per day, max 4. Leave time for meals, rest, and transit between spots. Cross-city travel days: only one light activity after arrival. This is a visa document, not a real trip. Make it look like a normal person's vacation.
5. Verify every attraction's real opening hours. Do NOT place an attraction on a day it is closed (e.g. Monday closures, public holidays). Check seasonal hours based on travel month.
6. Mark hotel and transportation columns as "（待填）" — user fills these in themselves.
5. After output, MUST say (COPY EXACTLY):
```
行程单生成了。三件事：

1. 酒店和交通栏标了"待填"——你订完酒店和机票后自己填进去，酒店是你自己在携程挑的，我填不了。

2. 你一定要仔细看一遍这个行程单，记住每天去哪。电调会随机问，答不上来就麻烦了。所以还是推荐用「行程助手」app 自己动手做一遍加深印象。

3. 景点开放时间我标注了，但建议出发前再去官网确认一次防止临时变动。
```

After user confirms done → check off item → move to 5b.

**5b: 机票预订单 (COPY EXACTLY):**
```
机票去 trip.com（携程海外版）。

不用付款！走到支付页面就停，截图或下载预订确认单。
出入境城市呼应行程单 — 申哪个国家最好从那个国家出入境。
```

After user confirms done → check off item → move to 5c.

**5c: 酒店预订单 (COPY EXACTLY):**
```
酒店去携程。

筛选"免费取消"或"先用后付"，下单后下载确认单。
酒店城市和日期必须跟行程单一模一样。

要列出每个城市需要什么日期的酒店吗？
```

After user confirms done → check off item → move to Category 6.

---

### Category 6: 解释信 + 已婚附加 + 预约凭证

**6a: 解释信 (COPY EXACTLY):**
```
最后是解释信。我可以帮你写，会直接显示在聊天里，再给你一份 Word 可编辑版本。

但写之前先说清楚：解释信最重要的是真实，模板只是骨架。建议你先告诉我：

1. 钱的真实来源——工资？积蓄？家人给的？如果有大额转账，真实原因是什么（比如平时钱放支付宝、理财赎回、家人临时转的），照实说，签证官见得多了，撒谎一眼看穿。

2. 国内有什么拴着你——什么公司什么职位干了多久？有没有房子在哪？家人在干嘛？

3. 去欧洲的真实目的——纯旅游？看朋友？度蜜月？

这些写清楚了我再帮你润色成英文，不然套模板一眼假反而坏事。

准备好了就说，我来写。
```

**After user provides info and confirms:** Generate cover letter in chat + provide Word download. Check off item → move to 6b.

**6b: 已婚附加**

Only if the checklist has this item. If user is unmarried and the item is marked "未婚跳过", skip this.

**SAY (COPY EXACTLY):**
```
清单上有结婚证这一项。已婚的话：结婚证复印件 + 英文翻译件，网上有模板。未婚的话说"跳过"。
```

After user confirms → check off or skip → move to 6c.

**6c: 预约凭证 (COPY EXACTLY):**
```
最后两项：

17. 签证申请表 — 签证中心网站填完表生成的 PDF，打印。
18. 签证中心预约单 — 预约成功后的确认单，打印。

都打印好了就说"预约凭证好了"。
```

After user confirms → check off items → set current_step = review → go to Step 6.

---

## Step 6: 最终核对

**current_step = review**

**SAY (COPY EXACTLY):**
```
最后逐项核对：

1. 护照有效期超过离开申根区后 3 个月？≥2 空白页？
2. 旧护照复印了？（没有跳过）
3. 身份证、户口本（整本封面到最后一页）都复印好了？
4. 身份证明材料准备齐了？签字+公章都有？
5. 保险日期覆盖全程？保额≥3 万欧元？彩打前两页？
6. 银行流水最近 3-6 个月的？余额够？没有临时大额转账？
7. 行程单里申请国天数最长？
8. 机票预订单出入境城市呼应行程单？姓名跟护照一致？
9. 酒店预订单日期城市跟行程单一致？姓名跟护照一致？
10. 解释信讲清楚了资金来源+回国约束力+旅行目的？
11. 已婚的话：结婚证+英文翻译件准备好了？
12. 签证申请表和预约单都打印了？
13. 所有文件没有订书钉或回形针？按顺序叠好了？

全部确认好了就说"全部好了"。
```

**After user confirms all:** Set current_step = done. Go to done.

---

## Done

**current_step = done**

**SAY (COPY EXACTLY):**
```
全部就绪，可以去递签了。

当天提醒：
- 准时到签证中心
- 文件不要用订书钉或回形针，按顺序叠好
- 可能会电话核实，照实回答

出签后旅行保险可以退掉。

祝顺利出签！
```

---

## PROGRESS FILE

### Rules

1. Edit progress.md BEFORE replying to user.
2. Update current_step on every step transition.
3. Check off items immediately when user confirms.

### New User Template

```markdown
# Schengen Visa Progress

current_step: identity
身份：待确认
目标国家：待确认
```

After Step 2, insert the full checklist matching the user's identity.

---

## REFERENCE FILES

| Need | Read |
|---|---|
| Country links and details | `references/country-notes.md` |
| Detailed item instructions | `references/checklist.md` |
| Cover letter template | `references/cover-letter.md` |
| Itinerary guide | `references/itinerary.md` |

---

## HARD CONSTRAINTS

1. Chinese only for all user-facing output.
2. One step/category at a time. Never dump multiple.
3. Edit progress.md BEFORE replying.
4. Always read progress.md at session start.
5. Sensitive materials = remind only. Never generate or ask to see.
6. Non-sensitive (itinerary, cover letter) = can generate.
7. Non-Schengen country = say "这不是申根国家，这个 skill 覆盖不了。"
8. No staples or clips on documents.
9. Application country must have most days in itinerary.
10. Use SAY templates exactly. Do not paraphrase.
11. The flow is fixed: Step 1 → Step 2 → Step 3 → Step 4 → Step 5 → Step 6. Never branch off unless user explicitly asks.
12. Never ask about marriage, age, income, or other personal details. The checklist already covers conditional items with "如有/已婚者准备，XX跳过".
