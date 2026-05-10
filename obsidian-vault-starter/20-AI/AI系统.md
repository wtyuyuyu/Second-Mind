---
type: system
system: ai
status: stabilizing
updated: 2026-05-05
---

# AI系统

## 系统使命

管理工具、自动化、模型使用、记忆层和工作流，把 AI 从“偶尔用一下”变成稳定生产力基础设施。

## 当前主线

- Codex 工作流固化
- Memory Vault 健康度维护
- Obsidian / Zotero 接入

## 运行流程

```text
需求 -> 工具选择 -> 工作流执行 -> 结果记录 -> 复用沉淀 -> 权限与边界复盘
```

## 当前关注

- [ ] 明确哪些任务值得开 subagent
- [ ] 把高频回答结构沉淀为长期规则
- [ ] 为 Obsidian 预留安全自动化边界

## 工作流页

```dataview
TABLE workflow_stage, reuse_level, updated
FROM "20-AI"
WHERE type = "ai-workflow"
SORT updated DESC
```

## 复盘问题

哪些 AI 自动化真的节省了判断成本，哪些只是制造了更复杂的流程？
