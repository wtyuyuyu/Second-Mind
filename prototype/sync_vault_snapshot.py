from datetime import datetime
from pathlib import Path
import json


RUNTIME_ROOT = Path("/Users/wtyuyuyu/Library/Application Support/SecondMindSite")
SNAPSHOT_PATH = RUNTIME_ROOT / "vault_snapshot.json"
VAULT_PATH = Path("/Users/wtyuyuyu/Library/Mobile Documents/iCloud~md~obsidian/Documents")
RESEARCH_PATH = VAULT_PATH / "10-Research"
INVEST_PATH = VAULT_PATH / "40-Invest"
TOOLS_COUNT = 5
SYSTEMS_COUNT = 4


def _note_payload(path: Path):
    stat = path.stat()
    return {
        "name": path.stem,
        "filename": path.name,
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
        "mtime": stat.st_mtime,
    }


def _list_markdown(folder: Path):
    if not folder.exists():
        return []
    return sorted((path for path in folder.glob("*.md") if path.is_file()), key=lambda item: item.stat().st_mtime, reverse=True)


def build_snapshot():
    research_notes = _list_markdown(RESEARCH_PATH)
    invest_notes = _list_markdown(INVEST_PATH)

    research_papers = [
        _note_payload(path)
        for path in research_notes
        if path.stem not in {"研究系统", "研究系统使用说明"} and not path.stem.startswith("方向卡：")
    ]
    research_directions = [
        _note_payload(path) for path in research_notes if path.stem.startswith("方向卡：")
    ]
    invest_cards = [
        _note_payload(path)
        for path in invest_notes
        if path.stem not in {"投资系统", "国内主线与国际前沿对照：具身智能"}
    ]

    return {
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "source": "snapshot",
        "metrics": {
            "paperCount": len(research_papers),
            "directionCount": len(research_directions),
            "investCount": len(invest_cards),
            "toolCount": TOOLS_COUNT,
            "systemCount": SYSTEMS_COUNT,
        },
        "research": {
            "papers": research_papers,
            "directions": research_directions,
        },
        "invest": {
            "cards": invest_cards,
        },
    }


if __name__ == "__main__":
    RUNTIME_ROOT.mkdir(parents=True, exist_ok=True)
    SNAPSHOT_PATH.write_text(json.dumps(build_snapshot(), ensure_ascii=False, indent=2), encoding="utf-8")
    print(SNAPSHOT_PATH)
