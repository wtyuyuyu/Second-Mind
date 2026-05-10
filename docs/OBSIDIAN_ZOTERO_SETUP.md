# Second Mind 的 Obsidian / Zotero 最小接入方案

## 目标

这套配置不是为了把插件装满，而是为了先让 Second Mind 的研究系统能够跑通：

```text
Zotero 高价值输入 -> Obsidian 本地 Markdown 记忆 -> Codex 编译与复盘
```

## 最小必装

### Zotero

1. `Better BibTeX`
   - 作用：生成稳定的 citation key，作为 Zotero 与 Obsidian 之间的锚点。
   - 依据：Better BibTeX 官方说明其核心能力是管理 bibliographic data、导出和 citation keys，并说明 Zotero 8 已采用原生 citation key 字段。

### Obsidian

1. `Zotero Integration`
   - 作用：把 citations、bibliography、notes、PDF annotations 直接导入 Obsidian。
   - 依据：插件 README 明确写明它支持导入 citations、bibliographies、notes 和 PDF annotations，并且 **requires Better BibTeX for Zotero**。

2. `Dataview`
   - 作用：把 Markdown 文件当成可查询数据库，用于四系统列表、看板、聚合表。
   - 依据：项目 README 明确描述为 “A data index and query language over Markdown files”。

3. `Tasks`
   - 作用：统一行动项与复盘项，把不同系统的任务聚合到一起。
   - 依据：项目 README 明确说明它能跨整个 vault 跟踪任务、查询任务，并在任何视图中更新源文件。

4. `Templater`
   - 作用：把研究页、投资页、复盘页、系统页做成可重复模板。
   - 依据：项目 README 明确说明它支持变量、函数以及模板语言。

## 第二阶段再装

1. `Local REST API`
   - 作用：让 Codex 后续通过本地 API 读写 Obsidian，而不只是改磁盘文件。
   - 适合时机：当用户已经稳定使用四系统结构，开始需要自动化读写与脚本调用时。

## 安装顺序

1. 先在 Zotero 安装 `Better BibTeX`
2. 重启 Zotero
3. 在 Zotero 里确认 citation key 可见
4. 在 Obsidian 启用 Community Plugins
5. 依次安装：
   - `Zotero Integration`
   - `Dataview`
   - `Tasks`
   - `Templater`
6. 最后再考虑 `Local REST API`

## Zotero 需要额外确认的设置

`Zotero Integration` 的 README 额外提醒了两点：

1. 需要安装 `Better BibTeX`
2. 需要在 Zotero 里设置 `Quick Copy style`

如果没有设置 quick copy，创建 citation 或 bibliography 时容易报错。

## 每个插件在 Second Mind 里的角色

| 工具 | 角色 | 对应系统 |
| --- | --- | --- |
| Better BibTeX | 引文锚点与导出稳定层 | 研究 / AI |
| Zotero Integration | 文献与批注进入 Obsidian 的桥 | 研究 |
| Dataview | 本地 Markdown 查询层 | 四系统 |
| Tasks | 行动与复盘任务层 | 四系统 |
| Templater | 结构化页面生成层 | 四系统 |
| Local REST API | 自动化接口层 | AI |

## 不要一开始就做的事

- 不要一开始装太多 Obsidian 插件。
- 不要先追求全自动同步。
- 不要先做复杂图谱。
- 不要让 Zotero 和 Obsidian 双向自动覆盖彼此内容。

Second Mind 当前最重要的是：**把高价值输入稳定地转成结构化 Markdown 页面**。

## 建议的第一批模板

装完插件后，最先做四类模板：

1. `research-paper-source`
2. `research-direction`
3. `invest-company-watch`
4. `weekly-review`

## 置信度

- `Better BibTeX + Zotero Integration` 是当前最关键组合：**高**
  逻辑依据：官方 README 直接写出依赖关系。
- `Dataview + Tasks + Templater` 作为 Second Mind 的最小 Obsidian 结构层：**高**
  逻辑依据：它们分别覆盖查询、任务、模板，是四系统最基础的三块能力。
- `Local REST API` 立即安装的必要性：**中**
  逻辑依据：它对自动化价值高，但不是当前闭环验证的前置条件。

## 用户可能不知道自己不知道的点

### Unknown Unknowns

1. Zotero 与 Obsidian 的真正难点不是“能不能连上”，而是**导入后的结构是否稳定**。如果模板设计得差，后续 Dataview 和 Tasks 会变得很混乱。
2. `Templater` 很强，但它也允许执行脚本。能力越强，结构漂移和安全边界问题越容易出现，因此模板必须从少到多增长。
3. `Local REST API` 很适合自动化，但一旦接入，就意味着权限管理、写入边界和误操作风险都要进入 AI 系统的治理范围。
