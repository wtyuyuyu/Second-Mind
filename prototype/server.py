from datetime import datetime
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import subprocess
import urllib.parse
import urllib.request
import ssl


ROOT = Path(__file__).resolve().parent
SNAPSHOT_PATH = ROOT / "vault_snapshot.json"
REST_CONFIG_PATH = ROOT / "obsidian_local_rest_api.json"
LATEST_FOCUS_PATHS = [
    Path("/Users/wtyuyuyu/Documents/Second-Mind/prototype/latest_focus.json"),
    ROOT / "latest_focus.json",
]
VAULT_PATH = Path("/Users/wtyuyuyu/Library/Mobile Documents/iCloud~md~obsidian/Documents")
SYSTEM_PATHS = {
    "research": VAULT_PATH / "10-Research",
    "ai": VAULT_PATH / "20-AI",
    "life": VAULT_PATH / "30-Life",
    "invest": VAULT_PATH / "40-Invest",
    "startup": VAULT_PATH / "50-Startup",
}
TOOLS_COUNT = 5
SYSTEMS_COUNT = 5
REST_RESEARCH_PATH = "10-Research"
REST_INVEST_PATH = "40-Invest"


def _load_latest_focus():
    for path in LATEST_FOCUS_PATHS:
        try:
            if path.exists():
                return json.loads(path.read_text(encoding="utf-8"))
        except (PermissionError, OSError, json.JSONDecodeError):
            continue
    return []


def _note_payload(path: Path):
    stat = path.stat()
    return {
        "name": path.stem,
        "filename": path.name,
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
        "mtime": stat.st_mtime,
    }


def _rest_note_payload(name: str):
    return {
        "name": name.removesuffix(".md"),
        "filename": name,
        "modified": "",
        "mtime": 0,
    }


def _list_markdown(folder: Path):
    if not folder.exists():
        return []
    return sorted((path for path in folder.glob("*.md") if path.is_file()), key=lambda item: item.stat().st_mtime, reverse=True)


def _load_rest_config():
    if not REST_CONFIG_PATH.exists():
        return None
    return json.loads(REST_CONFIG_PATH.read_text(encoding="utf-8"))


def _rest_get_json(base_url: str, api_key: str, path: str):
    url = f"{base_url.rstrip('/')}/{path.lstrip('/')}"
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
    )
    context = ssl._create_unverified_context()
    with urllib.request.urlopen(request, context=context, timeout=5) as response:
        return json.loads(response.read().decode("utf-8"))


def _rest_status():
    config = _load_rest_config()
    if not config:
        return None

    base_url = config["baseUrl"]
    api_key = config["apiKey"]

    research_listing = _rest_get_json(base_url, api_key, f"vault/{REST_RESEARCH_PATH}/")
    invest_listing = _rest_get_json(base_url, api_key, f"vault/{REST_INVEST_PATH}/")

    research_files = research_listing.get("files", [])
    invest_files = invest_listing.get("files", [])

    research_papers = [
        _rest_note_payload(name)
        for name in research_files
        if name not in {"研究系统.md", "研究系统使用说明.md"} and not name.startswith("方向卡：")
    ]
    research_directions = [
        _rest_note_payload(name) for name in research_files if name.startswith("方向卡：")
    ]
    invest_cards = [
        _rest_note_payload(name)
        for name in invest_files
        if name not in {"投资系统.md", "国内主线与国际前沿对照：具身智能.md"}
    ]

    return {
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "source": "obsidian-local-rest-api",
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
        "focus": _load_latest_focus(),
    }


def _vault_status():
    try:
        rest_payload = _rest_status()
        if rest_payload:
            return rest_payload
    except Exception:
        pass

    research_folder = SYSTEM_PATHS["research"]
    invest_folder = SYSTEM_PATHS["invest"]

    research_notes = _list_markdown(research_folder)
    invest_notes = _list_markdown(invest_folder)

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

    payload = {
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "source": "live-vault",
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
        "focus": _load_latest_focus(),
    }

    if (
        payload["metrics"]["paperCount"] == 0
        and payload["metrics"]["directionCount"] == 0
        and payload["metrics"]["investCount"] == 0
        and SNAPSHOT_PATH.exists()
    ):
        snapshot = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
        snapshot["source"] = snapshot.get("source", "snapshot")
        snapshot["fallbackUsed"] = True
        return snapshot

    return payload


class SecondMindHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def _send_json(self, payload):
        encoded = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == "/api/status":
            self._send_json(_vault_status())
            return

        if parsed.path == "/open-vault":
            subprocess.Popen(["open", str(VAULT_PATH)])
            self.send_response(HTTPStatus.SEE_OTHER)
            self.send_header("Location", "/?opened=vault")
            self.end_headers()
            return

        if parsed.path == "/open-folder":
            system = params.get("system", ["research"])[0]
            target = SYSTEM_PATHS.get(system, VAULT_PATH)
            subprocess.Popen(["open", str(target)])
            self.send_response(HTTPStatus.SEE_OTHER)
            self.send_header("Location", f"/?opened={system}")
            self.end_headers()
            return

        super().do_GET()


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 4173), SecondMindHandler)
    print("Second Mind prototype server running on http://127.0.0.1:4173")
    server.serve_forever()
