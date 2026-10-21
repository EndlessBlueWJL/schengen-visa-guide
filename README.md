<p align="center">
  <img src="docs/banner.svg" alt="Schengen Visa Guide" width="720">
</p>

<p align="center">
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/version-v1.1.0-003399?style=flat-square" alt="v1.1.0"></a>
  &nbsp;
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"></a>
  &nbsp;
  <a href="https://gitee.com/jinglong-wang/schengen-visa-guide"><img src="https://img.shields.io/badge/Gitee-%E9%95%9C%E5%83%8F-C71D23?style=flat-square&amp;logo=gitee&amp;logoColor=white" alt="Gitee 镜像"></a>
</p>

<p align="center">
  <a href="docs/README_EN.md"><strong>English</strong></a>
  &nbsp;·&nbsp;
  <strong>简体中文</strong>
</p>

<p align="center">
面向中国护照持有者的 AI Agent 技能——不挑平台。<br>
把一条死攻略变成一个能跨会话连续工作的交互式签证向导。<br>
关了窗口、明天再打开——它记得你办到哪了。<br>
<em>攻略是名词。这个——是动词。</em>
</p>

---

## 为什么需要这个 skill

通用 AI 和静态攻略都帮得上忙，但各有硬伤：

- **攻略不按身份写**——一篇死文章所有人看同一篇，学生和退休看的材料清单一样
- **AI 跨会话即失忆**——没法精确记住你的准备过程，每次打开可能要重新解释一遍
- **AI 没有固定流程**——你问保险它讲保险，你问行程它讲行程，中间漏了什么它不会主动提醒
- **AI 没有敏感信息边界**——可能随口让你上传银行流水
- **签证中心 URL 可能瞎编**——AI 一本正经给你个假网址
- **材料互相依赖，顺序错了准备过程变繁杂**

这个 skill 是只为一个目标设计的：**让你带着齐全的材料走进签证中心。**

---

## 这个 skill 做什么

把你的 AI Agent 变成私人签证管家：

🪪 **自报身份** → 自动匹配材料清单（学生 17 项、在职 18 项、退休 17 项、自由职业 17 项、无业 17 项、未成年人 17 项）

🔁 **跨会话记忆** → 关窗口、明天再开，Agent 先读 `progress.md`，从上次断点继续——不用复述一个字

📋 **逐项推进** → 17-18 份材料，每项讲清楚：去哪办、什么格式、容易踩什么坑

💰 **预算测算** → 按天数算出该准备多少资金证明（实操拟合：≤15 天 ¥2,000/天，>15 天递增），不用再信"余额 3 万"的民间传说

🛡️ **敏感边界** → 护照、银行流水、户口本——只提醒怎么办，绝不接触。
                  行程单、解释信——可以直接生成；用户主动上传的中文学籍报告——可生成英文译件

🌍 **29 国直链** → 全部申根国官方签证中心网址，法意西三国含详细预约步骤，含领区判定与录指纹提醒

📞 **防电调翻车** → 行程单逻辑自动检查周一闭馆、同天跨城、天数不匹配——签证官随机提问也问不倒

---

## 学信网证明：两个选项

初始材料清单列出学信网证明及[中文版申请入口：学信档案](https://my.chsi.com.cn/)。登录后在“在线验证报告”中申请《教育部学籍在线验证报告》中文版并下载 PDF。逐项准备到这份材料时，Agent 才在聊天中展示下面的文字选项 1、2，再展示中英文虚构示例图；用户回复编号或直接说明选择，不使用弹窗或选择题工具。用户提前主动咨询办理方式时可直接说明；已上传并要求翻译时直接处理，不重复询问。

1. **上传中文版，由 skill 生成英文 PDF 译件和预览**。随包自带本地翻译引擎，真实资料保存在仓库外，不调用额外在线翻译服务。工具译件是否接受以申请国使领馆或签证中心要求为准。
2. **在学信网申请官方英文报告**。当前价目表为 **30 元**，以官网支付页面为准；无需向 skill 上传材料。

以下是已审阅的虚构示例，姓名、学校、日期等均为虚构，照片为简笔画，验证码与二维码均不可验证。英文图展示本工具输出。

| 中文报告示例 | 本工具英文译件示例 |
|---|---|
| ![中文虚构示例](assets/chsi/chsi-student-record-zh.png) | ![英文虚构示例](assets/chsi/chsi-student-record-en.png) |

该功能需要 Python；首次使用安装 `requirements-chsi.txt`。目前支持单页、可提取文字且版式匹配的《教育部学籍在线验证报告》，不将扫描件或其他学历/学位报告套入模板。详见 [使用流程、费用来源和隐私边界](references/chsi-translation.md)。

---

## 跟刷攻略有什么区别

| 刷攻略 | 这个 skill |
|---|---|
| 一篇死文章，所有人看同一篇 | 根据**你的身份**出定制清单 |
| 自己脑子记办到哪了 | `progress.md` 逐项勾选，跨会话不丢失 |
| "去签证中心官网预约" | 精确到每个国家的 URL + 分步骤预约流程 |
| 忘了第 8 项只能怪自己 | 最终核对**逐项重查**，勾过的也再确认一遍 |
| AI 生成千篇一律的解释信 | 先问你的真实情况，再润色成英文——签证官看不出模板味 |

一句话：攻略告诉你该干什么。这个 skill 引领你干且确保你**真的干了**。

---

## 安装

**Claude Code：**
```bash
cd ~/.claude/skills
git clone https://github.com/EndlessBlueWJL/schengen-visa-guide.git schengen-visa-guide
```

**Codex：**
```bash
cd ~/.codex/skills
git clone https://github.com/EndlessBlueWJL/schengen-visa-guide.git schengen-visa-guide
```

**OpenClaw / 其他 Agent：**
```bash
# 放到对应 Agent 读取 skills 的目录即可
git clone https://github.com/EndlessBlueWJL/schengen-visa-guide.git schengen-visa-guide
```

> 🇨🇳 **国内镜像**：本仓库同步在 Gitee —— [gitee.com/jinglong-wang/schengen-visa-guide](https://gitee.com/jinglong-wang/schengen-visa-guide)。国内克隆更快，把上面命令里的 GitHub 地址换成 `https://gitee.com/jinglong-wang/schengen-visa-guide.git` 即可。

> 💡 **更新？** 在 skill 目录里 `git pull` 即可。项目持续迭代中，更多国家预约流程持续补充。

---

## 上手

在 Agent 里说：

```
办申根签
```

skill 自动激活，读取 `progress.md`（第一次会自动创建），从你的进度位置开始。六种身份开箱即用。

---

## 项目结构

```
schengen-visa-guide/
├── SKILL.md                      # 主控文件，完整交互流程 + 状态机
├── references/
│   ├── checklist.md              # 按身份分类的材料详细说明 + 预算公式 + 时间费用
│   ├── country-notes.md          # 29 国签证中心网址 + 法意西预约流程 + 领区 + 录指纹
│   ├── cover-letter.md           # 解释信模板 + 常见疑点应对策略
│   ├── itinerary.md              # 行程单生成规则 + 景点营业时间验证
│   └── chsi-translation.md        # 学信网两个选项、示例和本地翻译流程
├── scripts/translate_chsi.py      # 提取中文报告、调用翻译引擎、生成预览
├── assets/chsi/                  # 仅两张虚构示例图
├── vendor/chsi-translator/       # 原项目引擎、字体、参考模板及 Apache-2.0 许可证
├── requirements-chsi.txt         # 可选翻译功能依赖
├── docs/
│   ├── design.md                 # 首版历史设计（当前流程以 SKILL.md 为准）
│   ├── plan.md                   # 首版历史实现计划
│   ├── project-description.md    # 设计理念
│   └── README_EN.md              # 英文 README
├── CHANGELOG.md                  # 版本变更记录
└── LICENSE
```

---

## 底层原理

1. **会话启动门**——每次新会话，办签流程必先读 `progress.md` 再开口（单点咨询除外）。硬指令。
2. **先存再回**——用户说"好了" → 先写文件勾掉 → 再回复。落盘优先于输出。
3. **申请国路由**——用户选国家 → 查 `country-notes.md` 获取官方直链。查表不推理，杜绝幻觉。
4. **材料处理边界**——证件、资金只提醒。行程单、解释信可生成；用户选择上传中文学籍报告后，可在私有目录生成英文译件。
5. **最终对账**——全部勾完再逐项复核，因为勾选和材料真正到手上是两回事。

---

## 注意事项

- **行程单**：也可以用「行程助手」App 自己动手创建。自己做一遍，每天去哪、住哪、怎么走心里有数。如果让 AI 生成，务必仔细看过并记住行程内容——电调时签证官会随机问行程、机票、酒店细节，答不上来直接拒签
- **解释信**：AI 写完之后请务必本人逐句核实。解释信是判断能否下签的关键材料，信息不实后果严重
- **信息时效**：签证政策、费率、网址及各国每日参考金额会调整，本 skill 信息截至 2025-07，**所有材料要求最终以申请国使领馆官网为准**

---

## 限制

- 目前仅支持中国护照
- 仅申根短期旅游签（C 签）
- 非申根国家会主动拒绝

---

## License

主体 skill 使用 MIT。内置翻译引擎保留 Apache-2.0 许可证，运行时依赖另遵从各自许可证，见 [第三方说明](THIRD_PARTY_NOTICES.md)。
