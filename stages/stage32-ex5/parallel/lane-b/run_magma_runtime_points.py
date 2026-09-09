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
        lines.append("".join(line.itertext()).strip())
stdout = "\n".join(lines)
records = []
for line in lines:
    if not line.startswith("NODE|"):
        continue
    tag, idx, payload = line.split("|", 2)
    records.append((int(idx), payload))
indices = [idx for idx, _ in records]
payloads = [payload for _, payload in records]
completion = "STAGE32EX5_B_RUNTIME_POINTS_END" in stdout
runtime_error = any(marker in stdout for marker in (
    "Runtime error", "Internal error", "User error", "Assertion failed"
))
index_ok = indices == list(range(48))
unique_ok = len(set(payloads)) == 48
coordinate_arity_ok = all(len(payload.split(",")) == 7 for payload in payloads)
success = (
    http_status == 200
    and completion
    and not runtime_error
    and len(records) == 48
    and index_ok
    and unique_ok
    and coordinate_arity_ok
    and "COUNT|48" in stdout
)
print(json.dumps({
    "http_status": http_status,
    "node_records": len(records),
    "indices_0_through_47": index_ok,
    "unique_normalized_points": unique_ok,
    "coordinate_arity_7": coordinate_arity_ok,
    "runtime_error_seen": runtime_error,
    "completion_marker_seen": completion,
    "success": success,
}, sort_keys=True))
for idx, payload in records:
    print(f"NODE|{idx}|{payload}")
print("COUNT|48")
print("UNIQUE|48" if unique_ok else f"UNIQUE|{len(set(payloads))}")
print("STAGE32EX5_B_RUNTIME_POINTS_END")
if not success:
    raise SystemExit("Stage32EX5-B Magma runtime-point export did not finish cleanly")
