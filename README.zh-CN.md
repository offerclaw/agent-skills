# OfferClaw Agent Skills

面向硕士留学申请场景的 AI 文书技能集合，覆盖 简历、推荐信、个人陈述等写作任务。

这是 [OfferClaw](https://offerclaw.pro) 对外发布的 graduate admissions writing agent skills 仓库。

[English README](./README.md)

## 已包含技能

### admissions-cv-writing

用于撰写或改写研究生申请 CV / Resume，并支持导出为 PDF。

**适用场景：**

- “帮我写申请硕士/博士的 CV”
- “把我的经历整理成英文学术简历”
- “按目标项目定制我的 graduate school resume”
- “把 CV 导出成 PDF”

**能力特点：**

- 按项目方向定制 CV 内容
- 支持学术、科研、实习经历编排
- 支持 Markdown 转 PDF
- 支持论文、项目、奖项信息组织

### recommendation-letter-writing

用于根据学生背景和推荐人语气撰写研究生申请推荐信。

**适用场景：**

- “帮我写一封推荐信”
- “为学生起草留学申请推荐信”
- “按目标项目重写推荐信”

**能力特点：**

- 匹配推荐人语气和身份
- 按项目方向调整强调重点
- 突出学生的研究、成绩与潜力
- 整合学术与实践背景材料

## 为什么是 OfferClaw

- 开源、可查看、可修改的专业留学 skill，经过申请季实战验证并拿到录取结果。
- 可以直接安装使用，也可以 Fork 后接入你自己的 agent 或 workflow
- 让 prompt、审核逻辑和写作标准沉淀为你自己的资产，而不是藏在外部平台

## 面向顾问、工作室与机构

如果你不是只想安装一个 skill，而是希望把这套能力接入自己的工作流，OfferClaw 也提供面向从业者的部署支持，包含全链路的AI agnt和自动化工作流集成，解锁更多的AI能力和差异化配置，把 AI 能力无缝嵌进你已经在用的工具和服务流程里。

## 安装

### 通过 GitHub / skills CLI 安装

安装整个仓库：

```bash
npx skills add offerclaw/agent-skills
```

安装单个技能：

```bash
npx skills add offerclaw/agent-skills --skill admissions-cv-writing
npx skills add offerclaw/agent-skills --skill recommendation-letter-writing
```

查看可安装技能列表：

```bash
npx skills add offerclaw/agent-skills --list
```

### 通过 ClawHub 安装

先安装 ClawHub CLI：

```bash
npm i -g clawhub
```

然后通过已发布的 skill slug 安装：

```bash
clawhub install admissions-cv-writing
clawhub install recommendation-letter-writing
```

ClawHub 会把已发布 skill 安装到你的 OpenClaw workspace。这个仓库仍然作为 GitHub 安装、Fork 和手动定制时的源仓库。

## 仓库结构

每个 skill 都位于 `skills/` 下的独立目录中：

```text
skills/<skill-name>/
├── SKILL.md          # 必需：skill 定义
├── references/       # 参考资料、模板、示例
├── scripts/          # 辅助脚本
└── assets/           # 静态资源
```

其中 `SKILL.md` 是唯一必需文件，其余目录按需提供。

## 了解更多

- 官网：[offerclaw.pro](https://offerclaw.pro)

## License

MIT
