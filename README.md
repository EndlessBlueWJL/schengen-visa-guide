<h1 align="center">Schengen Visa Guide</h1>

<p align="center">
  <a href="docs/README_EN.md"><strong>English</strong></a>
  &nbsp;·&nbsp;
  <strong>简体中文</strong>
</p>

<p align="center">
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-v1.0.0-orange" alt="Version"></a>
  &nbsp;
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
</p>

<p align="center">
面向中国护照持有者的 AI Agent 技能——纯 markdown，不挑平台。<br>
把一条死攻略变成一个能跨会话连续工作的交互式签证向导。<br>
关了窗口、明天再打开——它记得你办到哪了。
</p>

---

## 痛点

- 攻略很多，没有一篇按你的身份写
- AI 没法精确的记住你的准备过程，他只是模糊的知晓，每次打开可能需要重新解释一遍
- 部分材料互相依赖，顺序错了准备过程变得繁杂

---

## 这个 skill 做什么

把你的 AI Agent 变成私人签证管家：

🪪 **自报身份** → 自动匹配材料清单（学生 17 项、在职 18 项、退休 17 项、自由职业 17 项、无业 17 项）

🔁 **跨会话记忆** → 关窗口、明天再开，Agent 先读 `progress.md`，从上次断点继续——不用复述一个字

📋 **逐项推进** → 17-18 份材料，每项讲清楚：去哪办、什么格式、容易踩什么坑

🛡️ **敏感边界** → 护照、银行流水、户口本——只提醒怎么办，绝不接触。行程单、解释信——可以直接生成

🌍 **29 国直链** → 全部申根国官方签证中心网址，法意西三国含详细预约步骤

📞 **防电调翻车** → 行程单逻辑自动检查周一闭馆、同天跨城、天数不匹配——签证官随机提问也问不倒

---

## 跟刷攻略有什么区别

| 刷攻略 | 这个 skill |
|---|---|
| 一篇死文章，全国人看同一篇 | 根据**你的身份**出定制清单 |
| 自己脑子记办到哪了 | `progress.md` 逐项勾选，跨会话不丢失 |
| "去签证中心官网预约" | 精确到每个国家的 URL + 分步骤预约流程 |
| 忘了第 8 项只能怪自己 | 最终核对**逐项重查**，勾过的也再确认一遍 |
| AI 生成千篇一律的解释信 | 先问你的真实情况，再润色成英文——签证官看不出模板味 |

一句话：攻略告诉你该干什么。这个 skill 确保你**真的干了**。

---

## 为什么不用 ChatGPT / DeepSeek？

通用聊天助手能做到一部分，但它：

- **跨会话即失忆**——每次新对话都是从头来，你得重新说身份、国家、进度
- **没有固定流程**——你问保险它讲保险，你问行程它讲行程，中间漏了什么它不会主动提醒
- **没有敏感信息边界**——可能随口让你上传银行流水。这个 skill 有硬约束：只提醒，不接触
- **签证中心 URL 可能瞎编**——这个 skill 的 29 国官方网址全部人工核实，写死在 reference 里

通用 AI 能帮忙。这个是只为一个目标设计的：**让你带着齐全的材料走进签证中心。**

---

## 安装

纯 markdown，零依赖。放到 Agent 的 skills 目录即用。

**Claude Code：**
```bash
cd ~/.claude/skills
git clone https://github.com/WJL-666123/schengen-visa-guide.git schengen-visa-guide
```

**Codex：**
```bash
cd ~/.codex/skills
git clone https://github.com/WJL-666123/schengen-visa-guide.git schengen-visa-guide
```

**OpenClaw / 其他 Agent：**
```bash
# 放到对应 Agent 读取 skills 的目录即可
git clone https://github.com/WJL-666123/schengen-visa-guide.git schengen-visa-guide
```

> 💡 **更新？** 在 skill 目录里 `git pull` 即可。项目持续迭代中，更多身份和国家流程正在补充。

---

## 上手

在 Agent 里说：

```
办申根签
```

skill 自动激活，读取 `progress.md`（第一次会自动创建），从你的进度位置开始。五种身份开箱即用。

---

## 项目结构

```
schengen-visa-guide/
├── SKILL.md                      # 主控文件，完整交互流程 + 状态机
├── references/
│   ├── checklist.md              # 按身份分类的材料详细说明
│   ├── country-notes.md          # 29 国签证中心网址 + 法意西预约流程
│   ├── cover-letter.md           # 解释信模板 + 常见疑点应对策略
│   └── itinerary.md              # 行程单生成规则 + 景点营业时间验证
└── docs/
    ├── design.md                 # 架构与设计思路
    ├── plan.md                   # 实现计划
    └── project-description.md    # 设计理念
```

---

## 底层原理

五个机制，零行代码：

1. **会话启动门**——每次新会话，Agent 必须先读 `progress.md` 再开口。硬指令，无例外。
2. **先存再回**——用户说"好了" → 先写文件勾掉 → 再回复。落盘优先于输出。
3. **申请国路由**——用户选国家 → 查 `country-notes.md` 获取官方直链。查表不推理，杜绝幻觉。
4. **敏感/非敏感分界**——证件、学籍、资金 = 只提醒。行程单、解释信 = 可生成。
5. **最终对账**——全部勾完再逐项复核，因为勾选和材料真正到手上是两回事。

---

## 限制

- 目前仅支持中国护照
- 仅申根短期旅游签（C 签）
- 非申根国家会主动拒绝

---

## License

MIT — 商用、修改、闭源集成均可。

---

*攻略是名词。这个——是动词。*
