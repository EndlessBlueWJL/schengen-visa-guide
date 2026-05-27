# Schengen Visa Guide — Claude Code Skill

一个给 Claude Code 用的申根签证助手技能。面向中国护照持有者，覆盖全部 29 个申根国的短期旅游签证（C 签），支持学生、在职、退休、自由职业、无业五种身份。

## 它做什么

这个 skill 把一条死攻略变成一个**能跨会话连续工作的交互式向导**：

- **断点续办**：每次新会话自动读取进度文件，从上次停下的地方继续，不用复述
- **按身份出清单**：根据你的身份给出定制化材料清单（学生 17 项、在职 18 项等）
- **逐项准备**：按依赖顺序逐项引导，完成一项勾一项
- **敏感边界**：证件照、银行流水、户口本只提醒怎么办，绝不接触；行程单和解释信可以直接生成
- **29 国直链**：内置全部申根国官方签证中心网址，法国/意大利/西班牙有详细预约流程

## 安装

### 方式一：克隆到全局 skills 目录

```bash
cd ~/.claude/skills
git clone https://github.com/<your-username>/schengen-visa-skill.git schengen-visa-guide
```

### 方式二：克隆到某个项目的 skills 目录

```bash
cd your-project/.claude/skills
git clone https://github.com/<your-username>/schengen-visa-skill.git schengen-visa-guide
```

### 方式三：直接下载

下载 ZIP 解压到 `~/.claude/skills/schengen-visa-guide/` 即可。

## 使用

在 Claude Code 中说：

```
办申根签
```

skill 会自动激活，从询问身份开始一步步引导你完成全部材料准备。

## 项目结构

```
schengen-visa-guide/
├── SKILL.md                      # 主控文件，完整交互流程和状态管理
├── references/
│   ├── checklist.md              # 材料清单详细说明
│   ├── country-notes.md          # 29 国签证中心网址 + 三国对比
│   ├── cover-letter.md           # 解释信模板与写作指南
│   └── itinerary.md              # 行程单生成规则
└── docs/
    ├── design.md                 # 设计文档
    ├── plan.md                   # 实现计划
    └── project-description.md    # 项目说明（设计理念）
```

## 工作原理

核心是五个机制：

1. **会话启动门**：每次新会话模型必须先读 progress 文件，再回复用户
2. **逐项推送 + 即时落盘**：用户确认一项 → 先写文件勾掉 → 再回复，先存再回
3. **申请国自适应路由**：选国后从 country-notes 查直链和流程，查表不推理
4. **敏感与非敏感边界**：证件/学籍/资金只提醒，行程单/解释信可生成
5. **最终确认**：全部勾完后再逐项复核，因为勾选和材料真正就位之间可能有差距

纯 markdown，零依赖，不需要数据库。

## 限制

- 仅中国护照
- 仅申根短期旅游签（C 签）
- 非申根国家会主动拒绝

## License

MIT
