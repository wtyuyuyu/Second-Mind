from __future__ import annotations

from datetime import datetime, timezone, date
from email.utils import parsedate_to_datetime
from pathlib import Path
import html
import json
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


RUNTIME_ROOT = Path("/Users/wtyuyuyu/Library/Application Support/SecondMindSite")
OUTPUT_PATHS = [
    RUNTIME_ROOT / "latest_focus.json",
    Path("/Users/wtyuyuyu/Documents/Second-Mind/prototype/latest_focus.json"),
]
USER_AGENT = "SecondMindLatestFocus/1.0"
RSS_BASE = "https://news.google.com/rss/search"

TRACKS = [
    {
        "system": "研究",
        "kind": "高等级论文",
        "query": '("tactile sensing" OR "tactile perception" OR "haptic" OR "underwater adhesive" OR "hydrogel") (site:nature.com OR site:science.org)',
        "preferred_domains": ["nature.com", "science.org"],
        "preferred_terms": [
            "nature communications",
            "science advances",
            "science robotics",
            "nature sensors",
            "nature",
            "science",
            "tactile",
            "haptic",
            "hydrogel",
            "underwater adhesive",
        ],
        "summary_template": "当前领域的缺口，是很多工作只报触觉性能，却没有说清稳定感知真正卡在器件、界面还是系统层。它解决的问题，是把这个模糊判断推进成可拆分、可验证的科学问题。它采用的方案，是把感知链路分层后逐段验证各层级怎样共同决定结果。",
        "relation_template": "只有当它在稳定触觉感知、界面机制或水下工况约束上提供可迁移思路，才和当前主线直接相关。",
        "importance": "如果它改写了稳定感知的关键瓶颈，后续选题、实验优先级和论文故事都要跟着调整。",
    },
    {
        "system": "投资",
        "kind": "国内触觉公司",
        "query": '("tactile sensing" OR "visuotactile" OR "dexterous hand" OR "robot touch") (PaXini OR BrainCo OR "Apex Sensing" OR "他山科技" OR "flexible sensor")',
        "preferred_domains": ["prnewswire.com", "ehangzhou.gov.cn", "apexsensing.com"],
        "preferred_terms": [
            "tactile",
            "touch",
            "visuotactile",
            "dexterous hand",
            "full-palm",
            "fingertip",
            "flexible sensor",
            "electronic skin",
            "brainco",
            "paxini",
            "apex",
        ],
        "summary_template": "当前行业的缺口，是很多触觉公司能讲概念和样机，却没有清楚说明自己到底卖器件、模组还是平台。它解决的问题，是把产品边界和交付形态说得更明确。它采用的方案，是把硬件、数据、接口和集成能力打包成一条更完整的产品路线。",
        "relation_template": "核心比较维度是稳定性、模态、集成位置和量产路径，不是整机热度。",
        "importance": "如果国内公司把触觉做成交付产品，他山科技的产业位置和可交易映射都要重估。",
    },
    {
        "system": "投资",
        "kind": "国际触觉对标",
        "query": '("tactile sensing" OR "robotic hand" OR "dexterous hand") (Melexis OR XELA OR OYMotion OR PSYONIC)',
        "preferred_domains": ["melexis.com", "xelarobotics.com", "psyonic.io", "prnewswire.com"],
        "preferred_terms": [
            "tactile",
            "touch",
            "fingertip",
            "3d force",
            "robotic hand",
            "dexterous hand",
            "xela",
            "melexis",
            "oymotion",
            "psyonic",
        ],
        "summary_template": "当前国际路线的缺口，是不少触觉方案有能力演示，但还没有收敛成标准模块和工程部署。它解决的问题，是把触觉从实验室能力推进到更接近可集成部件的形态。它采用的方案，是同时收敛模块封装、接口定义和系统集成边界。",
        "relation_template": "国际条目主要用来对标国内触觉链条离标准模块和工程交付还有多远。",
        "importance": "它能给他山科技和国内公司一个更清晰的产业坐标，区分概念和标准件。",
    },
]

FALLBACK_ITEMS = [
    {
        "system": "研究",
        "title": "Tactile perception through fluid–solid interaction",
        "summary": "当前触觉研究的缺口，是很多工作强调材料或结构创新，却没有说清稳定感知究竟先卡在器件、界面还是系统链路。它解决的问题，是把流固耦合、压力传递、外置读出和算法解码这些环节放到同一条链里分析稳定信号怎么形成。它采用的方案，是用整套系统级验证而不是单器件对比，去拆开各层级对感知结果的贡献。",
        "relation": "",
        "importance": "",
        "source": "Nature Communications",
        "publishedAt": "2026-04-29",
        "url": "https://www.nature.com/articles/s41467-026-72497-3",
        "kind": "高等级论文",
    },
    {
        "system": "投资",
        "title": "BrainCo releases Revo 3 dexterous hand",
        "summary": "当前触觉赛道的缺口，是很多公司能演示灵巧手，却没有把触觉能力清楚收敛成可复用、可交付的末端方案。它解决的问题，是把全掌触觉、指尖视触融合和高频控制压到同一只手上，给出更完整的产品边界。它采用的方案，是把多种触觉相关能力和末端操作能力一起打包成可展示、可复用的系统样机。",
        "relation": "",
        "importance": "",
        "source": "eHangzhou",
        "publishedAt": "2026-04-09",
        "url": "https://www.ehangzhou.gov.cn/2026-04/09/c_297195.htm",
        "kind": "国内触觉公司",
    },
    {
        "system": "投资",
        "title": "Melexis and OYMotion elevate tactile sensing for next-generation robotic hands",
        "summary": "当前国际触觉路线的缺口，是不少方案有感知能力，但还没有收敛成标准化、可集成的机器人指尖模块。它解决的问题，是把触觉从实验室能力推进到更接近工程部署的部件形态。它采用的方案，是同时推进模块封装、接口定义、接触稳定性和系统集成边界。",
        "relation": "",
        "importance": "",
        "source": "Melexis",
        "publishedAt": "2026-04-21",
        "url": "https://www.melexis.com/en/news/2026/21apr2026-melexis-and-oymotion-elevate-tactile-sensing-for-next-generation-robotic-hands",
        "kind": "国际触觉对标",
    },
]


def _rss_url(query: str) -> str:
    encoded = urllib.parse.quote(query)
    return f"{RSS_BASE}?q={encoded}&hl=en-US&gl=US&ceid=US:en"


def _strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", html.unescape(text or "")).strip()


def _parse_date(raw: str) -> str:
    if not raw:
        return datetime.now().date().isoformat()
    try:
        parsed = parsedate_to_datetime(raw)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone().date().isoformat()
    except Exception:
        return datetime.now().date().isoformat()


def _parse_source_and_title(raw_title: str) -> tuple[str, str]:
    title = (raw_title or "").strip()
    if " - " in title:
        headline, source = title.rsplit(" - ", 1)
        return source.strip(), headline.strip()
    return "", title


def _domain(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    return parsed.netloc.lower()


def _trim_sentence(text: str, limit: int = 88) -> str:
    cleaned = re.sub(r"\s+", " ", text or "").strip(" -:：,，.;；。")
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[:limit].rstrip(" ,，.;；。") + "…"


def _compact_description(headline: str, description: str, source: str) -> str:
    text = _strip_html(description)
    for fragment in (headline, source):
        if fragment:
            text = text.replace(fragment, " ")
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\s+", " ", text).strip(" -:：,，.;；。")
    return _trim_sentence(text)


def _freshness_score(raw_date: str) -> int:
    try:
        published = date.fromisoformat(_parse_date(raw_date))
        age_days = (datetime.now().date() - published).days
    except Exception:
        return 0

    if age_days <= 7:
        return 30
    if age_days <= 30:
        return 20
    if age_days <= 120:
        return 10
    return 0


def _item_score(track: dict, headline: str, description: str, source: str, link: str, pub_date: str) -> int:
    haystack = " ".join([headline.lower(), description.lower(), source.lower(), link.lower()])
    score = _freshness_score(pub_date)

    for domain in track.get("preferred_domains", []):
        if domain in _domain(link):
            score += 40

    for term in track.get("preferred_terms", []):
        if term.lower() in haystack:
            score += 8

    return score


def _fetch_first_item(track: dict) -> dict | None:
    request = urllib.request.Request(_rss_url(track["query"]), headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=12) as response:
        payload = response.read()

    root = ET.fromstring(payload)
    channel = root.find("channel")
    if channel is None:
        return None

    best_item = None
    best_score = -1

    for item in channel.findall("item"):
        raw_title = item.findtext("title", default="")
        link = item.findtext("link", default="").strip()
        pub_date = item.findtext("pubDate", default="")
        description = _strip_html(item.findtext("description", default=""))
        source, headline = _parse_source_and_title(raw_title)
        if not headline or not link:
            continue

        score = _item_score(track, headline, description, source, link, pub_date)
        if score < best_score:
            continue

        best_item = {
            "system": track["system"],
            "title": headline,
            "summary": track["summary_template"].format(headline=headline),
            "relation": track["relation_template"],
            "importance": track["importance"],
            "source": source or "Google News",
            "publishedAt": _parse_date(pub_date),
            "url": link,
            "kind": track["kind"],
        }
        if description:
            compact = _compact_description(headline, description, source)
            if compact:
                best_item["summary"] = compact
        best_score = score
    return best_item


def _load_existing() -> list[dict]:
    for path in OUTPUT_PATHS:
        try:
            if path.exists():
                return json.loads(path.read_text(encoding="utf-8"))
        except (PermissionError, OSError, json.JSONDecodeError):
            continue
    return []


def _merge_with_fallback(items: list[dict]) -> list[dict]:
    result = items[:]
    seen_urls = {item["url"] for item in result}
    existing = _load_existing()

    for pool in (existing, FALLBACK_ITEMS):
        for item in pool:
            if len(result) >= 3:
                break
            if item["url"] in seen_urls:
                continue
            result.append(item)
            seen_urls.add(item["url"])
        if len(result) >= 3:
            break
    return result[:3]


def _write_outputs(items: list[dict]) -> None:
    payload = json.dumps(items, ensure_ascii=False, indent=2) + "\n"
    for path in OUTPUT_PATHS:
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(payload, encoding="utf-8")
        except PermissionError:
            continue


def main() -> int:
    items = []
    for track in TRACKS:
        try:
            item = _fetch_first_item(track)
        except Exception:
            item = None
        if item:
            items.append(item)

    items = _merge_with_fallback(items)
    if len(items) < 3:
        return 1

    _write_outputs(items)
    print(f"updated {len(items)} focus items at {datetime.now().isoformat(timespec='seconds')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
