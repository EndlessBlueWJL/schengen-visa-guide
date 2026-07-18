# 解释信指南

> ⚠️ **信息时效**：本指南信息截至 2025-07。

> 解释信是唯一能跟签证官「对话」的机会。必须说清楚三件事：**资金来源**、**回国约束力**、**旅行目的**。把材料的疑点全部解释干净，强调你一定会回国。

## 输出格式

解释信生成后，同时提供两种格式：
1. **聊天界面直接显示**——方便预览和讨论修改
2. **Word 可编辑版本**——用户下载后可以自行补充修改（用 python-docx 生成 .docx；若环境无该库，退化为 .txt 或 .md，让用户自行粘贴进 Word）

## 写解释信前必须提醒用户

向用户说明（须包含以下要点，可用自然语气）：

- 解释信最重要的是真实，模板只是骨架，得是用户自己的真实情况。
- 建议用户先告诉三件事：
  1. 钱的真实来源——工资？积蓄？家人给的？如有大额转账，真实原因是什么（平时钱放支付宝、理财赎回、家人临时转的等），照实说，签证官见得多了，撒谎一眼看穿。
  2. 国内有什么拴着——工作（公司、职位、年限）、房子（在哪、有无贷款）、家人（父母/配偶/孩子在干嘛）。
  3. 去欧洲的真实目的——纯旅游？看朋友？度蜜月？看演唱会？
- 这些写清楚再润色成英文，套模板一眼假反而坏事。

## 解释信模板（通用结构）

用英文写。**这是一封要打印的正式信件，正文里不要出现 markdown 符号（##、-、* 等）**，用普通段落和换行。结构如下：

```
[Your Name]
[Passport Number]
[Date]

To the Visa Officer,

Subject: Cover Letter for Schengen Visa Application

Dear Visa Officer,

I am [Name], a [year]-year student at [University Name], majoring in [Major].

Travel Purpose
I plan to visit [countries] from [start date] to [end date] (total [X] days).
This is my first trip to Europe, and I have always wanted to experience
European culture and history.

Itinerary Summary
- [Country 1]: [X days] - visit [key cities], [brief highlights]
- [Country 2]: [X days] - visit [key cities], [brief highlights]
- [Country 3]: [X days] - visit [key cities], [brief highlights]

My main destination is [application country] where I will spend the most
time ([X days]).

Financial Support
[选择一种，改下面的段落]

A) 个人出资版：
My travel expenses are covered by my personal savings. [解释资金来源，
如：I transferred 40,000 RMB to my bank account before applying because
I normally keep my money in Alipay for daily use.]

B) 父母/配偶出资版：
My travel expenses are sponsored by my [father/mother/spouse] [names]. Please find
their bank statements and employment certificates attached.

C) 自由职业版：
My income comes from [freelance work/investment returns/etc.]. [附上相关证明]

Strong Ties to China
[根据你的身份选择对应段落]

学生版：
- I am currently enrolled at [University] and my courses resume on [date].
- I have [X years] remaining until graduation.
- My family, including my parents, live in China.

在职版：
- I have been working at [Company] as [Position] for [X years].
- My annual salary is [amount], and I have been approved leave from [date] to [date].
- I have a stable career and property in China.

退休版：
- I am retired from [Company/Institution] with a stable pension.
- My children and family live in China.
- I have property and assets in China.

自由职业/无业版：
- My [spouse/parents/family] live in China.
- I have property and financial ties in China.
- [具体说明你的回国约束力]

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
| 临时大额转账 | "钱平时放在支付宝/微信，申请签证才转到银行卡"。⚠️ 能免则免——别为了凑余额临时转账，触发此疑点反而麻烦 |
| 行程特别长（30+ 天） | "年假/退休后时间充裕，第一次去欧洲想多看看" |
| 余额按预算公式估算刚够 | 如实说明资金构成（积蓄/工资结余/家人资助），强调往返机票和住宿已预订、实际花费可控 |
| 银行卡流水少 | "日常消费主要用微信/支付宝" |
| 白本护照 | "虽然第一次出国，但我准备了详细行程，证明我是去旅游" |
| 自由职业收入不稳定 | "附上近一年的收入流水/合同，证明有稳定收入来源" |

## 涉外公证书的认证（出资人/未成年人相关）

中国自 2023-11-07 起加入海牙公约（Apostille）。亲属关系公证、出生医学证明公证、父母同意出行委托书公证等涉外公证书，办**「公证 + 海牙认证（Apostille）」**即可，无需再办旧式的双认证。具体以当地公证处和外办要求为准。

## 身份加分项（强调在解释信里）

学生：
- 在读学生 = 天然回国约束力
- 提到学业进度和毕业计划
- 提到家人在国内

在职：
- 稳定工作 = 强回国约束力
- 提到职位、薪资、工作年限
- 提到有年假获批

退休：
- 退休金稳定
- 子女在国内
- 有房产等资产

通用：
- 提到家人在国内
- 提到有房产/资产
- 语气真诚，不要像套模板
