# .handoff — Doubao ↔ ChatGPT 协作交接区

这个文件夹是两个 AI 之间的沟通渠道。**用户（Li Lu）是唯一的调度者**，两个 AI 通过这里的文件和 git diff 协作，不直接对话。

## 角色分工

| | ChatGPT（架构师） | Doubao（施工方） |
|---|---|---|
| 职责 | 出方案、写内容大纲、审代码、把关技术准确性 | 按方案写 HTML/CSS/JS、推到 GitHub、浏览器测试 |
| 开工前 | 写 SPEC 到 `pending/` | 读 SPEC |
| 完工后 | 读 git diff 审代码，写反馈 | 写完成报告到 `done/` |

## 工作流（用户只说三句话）

1. **用户对 ChatGPT 说**："读 `PROJECT_CONTEXT.md` 和 `SPEC_TEMPLATE.md`，在 `pending/` 写一个新方案。"
2. **用户对 Doubao 说**："读 `pending/` 最新方案，按它做，完成后写报告到 `done/`。"
3. **用户对 ChatGPT 说**："审 `done/` 最新报告和 git diff，有问题写反馈到 `pending/`。"

## 文件夹状态机

```
pending/        ChatGPT 写的新方案在这
    ↓ (Doubao 开始干活)
in-progress/    Doubao 正在做
    ↓ (Doubao 做完 push)
done/           附完成报告，等 ChatGPT 审
    ↓ (ChatGPT 审完)
通过 → 留在 done/ 归档
有问题 → ChatGPT 在 pending/ 写 review-反馈.md
```

## 文件命名规则

- 方案：`YYYY-MM-DD-简短标题.md`，例如 `2026-09-24-threading-calculator.md`
- 反馈：`review-YYYY-MM-DD-标题.md`
