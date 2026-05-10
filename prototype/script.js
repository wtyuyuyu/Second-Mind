const systems = {
  research: {
    label: "研究系统",
    status: "研究优先",
    headline: "把论文、方向、实验与判断编译成真正可推进的研究操作流。",
    summary:
      "研究系统不是论文仓库，而是方向选择器。它从 Zotero 和 Obsidian 吸入高价值材料，经由评分、概念抽取、方向归并与实验行动，形成可复盘的科研记忆。",
    modules: [
      {
        name: "方向地图",
        text: "维护长期研究方向、优先级与被推迟方向。",
      },
      {
        name: "论文输入层",
        text: "只处理星标、高亮、关键批注，不做低信号囤积。",
      },
      {
        name: "实验行动板",
        text: "把阅读结果压缩成下一步实验、概念验证或讨论任务。",
      },
      {
        name: "周复盘",
        text: "检查方向置信度、实验卡点和证据是否失效。",
      },
    ],
    workflow: ["Zotero 高亮", "评分", "概念/方向页", "实验动作", "复盘"],
    reviewQuestion:
      "哪一个研究方向正在消耗注意力，却没有持续提高方向清晰度？",
    nextAction:
      "把当前最强的一个方向拆成“关键机制、关键证据、关键实验”三栏。",
    impacts: [
      {
        system: "投资",
        text: "研究方向会提前暴露潜在产业化链条，例如水下机器人、传感器、材料平台。",
      },
      {
        system: "生活",
        text: "研究系统直接决定精力分配与专注节奏，方向过多会侵蚀执行质量。",
      },
    ],
    watchList: [
      "本周新增高价值论文是否真正改变了方向判断。",
      "实验动作是否能被压缩到 1-2 个最关键步骤。",
      "方向页是否开始重复堆积、没有新证据进入。",
    ],
  },
  ai: {
    label: "AI 系统",
    status: "操作层",
    headline: "把工具、自动化、模型与记忆层连接成可控的执行基础设施。",
    summary:
      "AI 系统负责维护 Codex、技能、自动化、API 使用和 Memory Vault 健康。它的目标不是炫技，而是降低摩擦、提高可重复执行能力，并保护整个 Second Mind 的结构稳定性。",
    modules: [
      {
        name: "工具编排",
        text: "管理 Codex、Hermes、Obsidian、Zotero 与本地脚本的角色边界。",
      },
      {
        name: "技能与插件",
        text: "优先复用开源 skill、插件与工作流，减少重复造轮子。",
      },
      {
        name: "记忆健康",
        text: "检查重复摘要、过期规则、无效待办与结构漂移。",
      },
      {
        name: "自动化策略",
        text: "只自动化高频、低歧义、可验证的流程。",
      },
    ],
    workflow: ["请求进入", "技能匹配", "执行", "写入记忆", "质量复查"],
    reviewQuestion:
      "当前自动化是在节省认知成本，还是只是在制造新的维护债务？",
    nextAction:
      "把当前已安装的 skill、插件和脚本按“高频/低频、稳定/脆弱”做一次清单。",
    impacts: [
      {
        system: "研究",
        text: "更好的工具编排会降低论文清洗和研究摘要的进入成本。",
      },
      {
        system: "投资",
        text: "AI 系统可以为算力、电力、机器人链条搭建观察与提醒工作流。",
      },
    ],
    watchList: [
      "哪些技能经常被触发，说明已经形成稳定工作流。",
      "哪些工具需要权限或人为确认，不能贸然自动化。",
      "Memory Vault 中是否出现重复摘要与偏离源事实的结论。",
    ],
  },
  life: {
    label: "生活系统",
    status: "节奏维护",
    headline: "把计划、精力、关系与长期生活设计纳入一个能复盘的节奏系统。",
    summary:
      "生活系统的作用不是记录心情，而是维护执行寿命。它关注每日计划、完成情况、心理支撑、关系维护和长期节奏设计，让研究与投资系统不至于在高压下失真。",
    modules: [
      {
        name: "日计划",
        text: "每日只保留少数真正重要的动作，避免任务表膨胀。",
      },
      {
        name: "能量复盘",
        text: "观察什么活动耗能、什么活动回能，建立个人节奏。",
      },
      {
        name: "关系与表达",
        text: "维护亲密关系、沟通风格和长期协作质量。",
      },
      {
        name: "长期规划",
        text: "把今天的行为和三个月、一年后的生活设计连接起来。",
      },
    ],
    workflow: ["今日计划", "执行记录", "能量观察", "周反思", "节奏修正"],
    reviewQuestion:
      "哪些看似重要的任务实际上只是占据注意力，并没有改善长期生活质量？",
    nextAction:
      "为本周建立一页生活复盘页，只记录耗能、回能、关系摩擦和修正动作。",
    impacts: [
      {
        system: "研究",
        text: "稳定的作息与注意力管理会直接提高研究判断质量与实验推进速度。",
      },
      {
        system: "投资",
        text: "情绪波动和现金流压力会改变风险容忍度，必须被显式记录。",
      },
    ],
    watchList: [
      "高压时期是否出现计划过载与复盘缺失。",
      "关系摩擦是否开始影响研究与投资判断。",
      "身体状态和情绪状态是否已经改变风险偏好。",
    ],
  },
  invest: {
    label: "投资系统",
    status: "教学模式",
    headline: "以国内可投资资产为主线，用国际前沿做技术锚点，建立可学习的投资框架。",
    summary:
      "投资系统当前优先围绕国内的算力、能源电力、数据中心，以及具身智能链条展开。国际前沿更多作为比较标尺，不直接替代国内观察池。它不仅输出观察结论，也负责教学：告诉用户该看哪些数据、这些数据说明什么、什么信号容易被误读。",
    modules: [
      {
        name: "国内算力主线",
        text: "先跟踪中国市场里真正可投资的芯片、服务器、光模块、IDC 与电力资产。",
      },
      {
        name: "国内能源电力",
        text: "观察中国市场里算力扩张背后的电力约束、装机、储能与机房基础设施。",
      },
      {
        name: "具身智能",
        text: "把机器人收窄成具身智能，重点看整机平台、灵巧手、关节/减速器，以及触觉传感与控制。",
      },
      {
        name: "国际比较与教学",
        text: "用 Tesla、Figure、Apptronik 等前沿路线做对照，同时解释数据怎么看、为什么看。",
      },
    ],
    workflow: ["主题筛选", "数据读取", "链条理解", "风险检查", "复盘"],
    reviewQuestion:
      "当前看涨逻辑究竟来自盈利改善，还是只是市场情绪和估值扩张？",
    nextAction:
      "先把优必选、越疆、兆威机电、他山科技放进国内对照表，再用 Tesla / Figure / Apptronik 做技术锚点比较。",
    impacts: [
      {
        system: "研究",
        text: "研究方向会为投资系统提供产业化信号与技术周期前瞻。",
      },
      {
        system: "生活",
        text: "投资系统必须和现金流、风险承受能力、情绪状态一起看，而不是孤立下注。",
      },
    ],
    watchList: [
      "优必选看具身智能收入占比、毛利率、亏损收窄和量产交付；越疆看平台升级是否真的落到收入与研发投入；兆威机电看灵巧手与微型驱动；他山科技看触觉传感是否定义下一代灵巧手能力。",
      "电力和数据中心约束是否开始成为算力扩张瓶颈。",
      "具身智能主题是否已经从热词阶段进入订单、交付和场景验证阶段。",
    ],
  },
  startup: {
    label: "创业系统",
    status: "产品探索",
    headline: "把科研机制、真实水下任务、客户需求和产品护城河压成一条能落地的创业主线。",
    summary:
      "创业系统不负责泛泛商业想象，而是专门管理产品入口、客户场景、系统对标、机械爪集成、护城河和验证路线。它承接研究系统里最有产品潜力的方向，也和投资系统共享产业映射与公司对标。",
    modules: [
      {
        name: "需求场景",
        text: "优先收敛低可见度、高压、沉积物扰动环境下的真实抓取与接触任务。",
      },
      {
        name: "产品路线",
        text: "从传感器走到三指机械爪末端模块，再决定是否扩展到完整操作平台。",
      },
      {
        name: "对标基线",
        text: "同时看顶级水下操作产品、现成六维力/力矩传感器和触觉公司路线。",
      },
      {
        name: "护城河",
        text: "围绕高压稳定性、离散事件输出、封装、漂移控制和系统接口形成壁垒。",
      },
    ],
    workflow: ["科学问题", "任务场景", "最小 demo", "机械集成", "客户验证"],
    reviewQuestion:
      "当前讨论的是一个真实反复出现的水下操作痛点，还是只是把新传感器强行找应用？",
    nextAction:
      "把三指机械爪第一代的目标物、输出信号、客户接口和深度等级拆成一页产品约束表。",
    impacts: [
      {
        system: "研究",
        text: "创业系统会反向约束研究系统：哪些机制必须解释，哪些性能必须优先证明。",
      },
      {
        system: "投资",
        text: "创业系统会告诉投资系统哪些公司是直接竞合对标，哪些只是技术参照。",
      },
    ],
    watchList: [
      "三指是否真的是水下抓取最优折中，而不是暂时最顺手的方案。",
      "第一代输出信号是原始 spike、接触事件，还是已经能给出软硬和滑移判断。",
      "当前护城河到底更偏机制、算法、封装，还是机械集成接口。",
    ],
  },
};

const todayActions = [
  {
    system: "研究",
    action: "把本人论文里的“早期时序处理”压成 3 条可迁移原则，挂到深海泰勒流触觉方向页。",
  },
  {
    system: "AI 系统",
    action: "清点当前已安装 skill / 插件 / 脚本，区分必须保留与可淘汰项。",
  },
  {
    system: "生活",
    action: "建立本周生活复盘页，只跟踪耗能、回能、关系摩擦和节奏修正。",
  },
  {
    system: "投资",
    action: "先做一张国内具身智能对照表：优必选、越疆、兆威机电、他山科技，对照 Tesla、Figure、Apptronik。",
  },
  {
    system: "创业",
    action: "把第一代水下三指机械爪的目标物、输出信号和最小集成接口压成一页产品约束表。",
  },
];

const systemOrder = ["research", "ai", "life", "invest", "startup"];
let activeSystem = "research";
let syncState = {
  generatedAt: "",
  source: "",
  metrics: {
    paperCount: 0,
    directionCount: 0,
    investCount: 0,
    toolCount: 5,
    systemCount: 5,
  },
  research: {
    papers: [],
    directions: [],
  },
  invest: {
    cards: [],
  },
  startup: {
    items: [],
  },
  focus: [],
};

const briefList = document.querySelector("#briefList");
const actionGrid = document.querySelector("#actionGrid");
const impactList = document.querySelector("#impactList");
const modulesGrid = document.querySelector("#modulesGrid");
const workflowRail = document.querySelector("#workflowRail");
const watchList = document.querySelector("#watchList");
const detailTitle = document.querySelector("#detailTitle");
const detailLabel = document.querySelector("#detailLabel");
const detailHeadline = document.querySelector("#detailHeadline");
const detailSummary = document.querySelector("#detailSummary");
const detailStatus = document.querySelector("#detailStatus");
const reviewQuestion = document.querySelector("#reviewQuestion");
const nextAction = document.querySelector("#nextAction");
const focusReviewButton = document.querySelector("#focusReviewButton");
const focusSetupButton = document.querySelector("#focusSetupButton");
const toolsPanel = document.querySelector("#toolsPanel");
const syncPanel = document.querySelector("#syncPanel");
const sidebarNoteLink = document.querySelector("#sidebarNoteLink");
const sidebarNoteTitle = document.querySelector("#sidebarNoteTitle");
const sidebarNoteBody = document.querySelector("#sidebarNoteBody");
const sidebarNoteAction = document.querySelector("#sidebarNoteAction");
const syncTimestamp = document.querySelector("#syncTimestamp");
const researchSyncList = document.querySelector("#researchSyncList");
const investSyncList = document.querySelector("#investSyncList");
const paperCount = document.querySelector("#paperCount");
const investCount = document.querySelector("#investCount");
const toolCount = document.querySelector("#toolCount");
const systemCount = document.querySelector("#systemCount");

const folderMeta = {
  research: {
    title: "研究文件夹",
    body: "打开 10-Research，对论文源卡、方向页和实验动作做本地整理。",
    action: "打开研究文件夹",
  },
  ai: {
    title: "AI 系统文件夹",
    body: "打开 20-AI，查看工具、自动化、Memory Vault 和工作流相关页面。",
    action: "打开 AI 系统文件夹",
  },
  life: {
    title: "生活文件夹",
    body: "打开 30-Life，维护计划、能量复盘、关系与生活节奏记录。",
    action: "打开生活文件夹",
  },
  invest: {
    title: "投资文件夹",
    body: "打开 40-Invest，继续维护公司观察卡、链条对照表和复盘记录。",
    action: "打开投资文件夹",
  },
  startup: {
    title: "创业文件夹",
    body: "打开 50-Startup，继续维护产品路线、客户场景、对标基线和护城河判断。",
    action: "打开创业文件夹",
  },
};

function formatSyncTime(raw, source) {
  if (!raw) {
    return "尚未同步";
  }

  const time = new Date(raw);
  if (Number.isNaN(time.getTime())) {
    return "同步时间不可用";
  }

  const origin =
    source === "live-vault"
      ? "live vault"
      : source === "obsidian-local-rest-api"
        ? "Local REST API"
        : "最近快照";
  return `${origin}：${time.toLocaleString("zh-CN", {
    hour12: false,
  })}`;
}

function buildBriefs() {
  return syncState.focus || [];
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function briefSentence(item, key, fallback) {
  const value = item?.[key];
  if (typeof value === "string" && value.trim()) {
    return escapeHtml(value.trim());
  }
  return escapeHtml(fallback);
}

function renderBriefs() {
  briefList.innerHTML = buildBriefs()
    .map(
      (item, index) => `
        <article class="brief-item">
          <span class="brief-rank">0${index + 1}</span>
          <div>
            <strong>${item.title}</strong>
            <div class="brief-copy">
              <p><span class="brief-system">${item.system}</span>${briefSentence(item, "summary", `${item.title} 还没有被压成可读的三句分析。`)}</p>
            </div>
            <div class="brief-meta-row">
              <span class="brief-meta">${item.kind} · ${item.publishedAt}</span>
              <a class="brief-link" href="${item.url}" target="_blank" rel="noreferrer">查看来源</a>
            </div>
          </div>
        </article>
      `,
    )
    .join("") || `
      <article class="brief-item">
        <span class="brief-rank">--</span>
        <div>
          <strong>还没有外部动态</strong>
          <div class="brief-copy">
            <p><span class="brief-system">AI 系统</span>当前还没有可展示的外部动态三句分析。</p>
          </div>
        </div>
      </article>
    `;
}

function renderActions() {
  actionGrid.innerHTML = todayActions
    .map(
      (item) => `
        <article class="action-item">
          <span>${item.system}</span>
          <strong>${item.action}</strong>
        </article>
      `,
    )
    .join("");
}

function renderMetrics() {
  paperCount.textContent = String(syncState.metrics.paperCount);
  investCount.textContent = String(syncState.metrics.investCount);
  toolCount.textContent = String(syncState.metrics.toolCount);
  systemCount.textContent = String(syncState.metrics.systemCount);
}

function renderSyncPanel() {
  syncTimestamp.textContent = formatSyncTime(syncState.generatedAt, syncState.source);

  researchSyncList.innerHTML = syncState.research.papers.length
    ? syncState.research.papers
        .slice(0, 5)
        .map(
          (item) => `
            <li>
              <strong>${item.name}</strong>
              <span>${item.modified ? item.modified.replace("T", " ") : "通过 Local REST API 同步"}</span>
            </li>
          `,
        )
        .join("")
    : `<li><strong>还没有论文卡</strong><span>当前网站未从 live vault 读到研究论文源卡。</span></li>`;

  investSyncList.innerHTML = syncState.invest.cards.length
    ? syncState.invest.cards
        .slice(0, 6)
        .map(
          (item) => `
            <li>
              <strong>${item.name}</strong>
              <span>${item.modified ? item.modified.replace("T", " ") : "通过 Local REST API 同步"}</span>
            </li>
          `,
        )
        .join("")
    : `<li><strong>还没有投资卡</strong><span>当前网站未从 live vault 读到公司或主题观察卡。</span></li>`;
}

function syncNavState() {
  document.querySelectorAll(".nav-item").forEach((button) => {
    button.classList.toggle("active", button.dataset.system === activeSystem);
  });
}

function renderDetails() {
  const system = systems[activeSystem];
  detailLabel.textContent = system.label;
  detailTitle.textContent = `${system.label}详情`;
  detailHeadline.textContent = system.headline;
  detailSummary.textContent = system.summary;
  detailStatus.textContent = system.status;
  reviewQuestion.textContent = system.reviewQuestion;
  nextAction.textContent = system.nextAction;

  modulesGrid.innerHTML = system.modules
    .map(
      (module) => `
        <article class="module-card">
          <strong>${module.name}</strong>
          <p>${module.text}</p>
        </article>
      `,
    )
    .join("");

  workflowRail.innerHTML = system.workflow
    .map(
      (step, index) => `
        <div class="workflow-step">
          <span>0${index + 1}</span>
          <strong>${step}</strong>
        </div>
      `,
    )
    .join("");

  impactList.innerHTML = system.impacts
    .map(
      (impact) => `
        <div class="impact-item">
          <span class="impact-letter">${impact.system.slice(0, 1)}</span>
          <div>
            <strong>${impact.system}</strong>
            <p>${impact.text}</p>
          </div>
        </div>
      `,
    )
    .join("");

  watchList.innerHTML = system.watchList
    .map((item) => `<li>${item}</li>`)
    .join("");

  toolsPanel.hidden = activeSystem !== "research";
  focusSetupButton.hidden = activeSystem !== "research";
  syncPanel.hidden = activeSystem !== "ai";

  const folder = folderMeta[activeSystem];
  sidebarNoteLink.href = `/open-folder?system=${activeSystem}`;
  sidebarNoteLink.title = folder.action;
  sidebarNoteTitle.textContent = folder.title;
  sidebarNoteBody.textContent = folder.body;
  sidebarNoteAction.textContent = folder.action;
}

function render() {
  syncNavState();
  renderMetrics();
  renderSyncPanel();
  renderBriefs();
  renderDetails();
}

async function loadVaultState() {
  try {
    const response = await fetch("/api/status", { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    syncState = await response.json();
    render();
  } catch (error) {
    syncTimestamp.textContent = `同步失败：${error.message}`;
  }
}

document.querySelectorAll(".nav-item").forEach((button) => {
  button.addEventListener("click", () => {
    activeSystem = button.dataset.system;
    render();
  });
});

focusReviewButton.addEventListener("click", () => {
  document.querySelector(".questions-row").scrollIntoView({
    behavior: "smooth",
    block: "start",
  });
});

focusSetupButton.addEventListener("click", () => {
  document.querySelector("#toolsPanel").scrollIntoView({
    behavior: "smooth",
    block: "start",
  });
});

renderActions();
render();
loadVaultState();
window.setInterval(loadVaultState, 30000);
