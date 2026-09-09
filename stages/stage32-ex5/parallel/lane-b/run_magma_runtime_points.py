#!/usr/bin/env python3
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
CODE = (ROOT / "export_stoll_runtime_points.m").read_text(encoding="utf-8")
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"

data = urllib.parse.urlencode({"input": CODE}).encode("utf-8")
req = urllib.request.Request(
    URL,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": REFERER,
        "User-Agent": "perfect-cuboid-stage32ex5-b/1.0",
    },
    method="POST",
)
with urllib.request.urlopen(req, timeout=240) as resp:
    raw = resp.read().decode("utf-8", errors="replace")
    http_status = resp.status

root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines)
node_lines = [line for line in lines if line.startswith("NODE|")]
completion = "STAGE32EX5_B_RUNTIME_POINTS_END" in stdout
runtime_error = any(marker in stdout for marker in (
    "Runtime error", "Internal error", "User error", "Assertion failed"
))
success = (
    http_status == 200
    and completion
    and not runtime_error
    and len(node_lines) == 48
    and "COUNT|48" in stdout
    and "UNIQUE|48" in stdout
)
print(json.dumps({
    "http_status": http_status,
    "node_lines": len(node_lines),
    "runtime_error_seen": runtime_error,
    "completion_marker_seen": completion,
    "success": success,
}, sort_keys=True))
print(stdout)
if not success:
    raise SystemExit("Stage32EX5-B Magma runtime-point export did not finish cleanly")
