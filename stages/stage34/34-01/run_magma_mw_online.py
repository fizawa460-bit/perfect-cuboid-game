#!/usr/bin/env python3
import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
CODE = (ROOT / "magma_mw_full_group_certificate.m").read_text(encoding="utf-8")
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"
FIBERS = ["20/21", "80/39", "24/7", "84/13", "48/55", "20/99", "60/11"]
MAX_TOTAL_RAW = 1048576


def run_one(label: str) -> dict:
    program = f'SetColumns(0);\ntarget := "{label}";\n' + CODE
    data = urllib.parse.urlencode({"input": program}).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html, application/xml, application/xhtml+xml",
            "Referer": REFERER,
            "User-Agent": "perfect-cuboid-stage34/1.1",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            raw_bytes = resp.read()
            http_status = resp.status
            response_headers = dict(resp.headers.items())
    except urllib.error.HTTPError as exc:
        return {
            "fiber": label,
            "success": False,
            "http_status": exc.code,
            "error": f"HTTPError: {exc.reason}",
            "raw_bytes": 0,
            "stdout": "",
            "raw_xml": "",
        }

    raw = raw_bytes.decode("utf-8", errors="replace")
    root = ET.fromstring(raw)
    lines = []
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):
            lines.append("".join(line.itertext()))
    stdout = "\n".join(lines)
    if stdout and not stdout.endswith("\n"):
        stdout += "\n"

    completion = "STAGE34_01_MAGMA_MW_SATURATION_END" in stdout
    runtime_error = any(marker in stdout for marker in (
        "Runtime error", "Internal error", "User error", "Assertion failed"
    ))
    return {
        "fiber": label,
        "success": http_status == 200 and completion and not runtime_error,
        "http_status": http_status,
        "response_headers": response_headers,
        "stdout": stdout,
        "raw_xml": raw,
        "raw_bytes": len(raw_bytes),
        "completion_marker_seen": completion,
        "runtime_error_seen": runtime_error,
    }


results = []
for fiber in FIBERS:
    result = run_one(fiber)
    results.append(result)
    print(json.dumps({
        "fiber": fiber,
        "success": result["success"],
        "http_status": result.get("http_status"),
        "raw_bytes": result.get("raw_bytes", 0),
    }, sort_keys=True))
    if result.get("stdout"):
        print(result["stdout"])

raw_total = sum(int(r.get("raw_bytes", 0)) for r in results)
all_success = all(bool(r.get("success")) for r in results)
payload = {
    "protocol": "official-magma-xml-calculator",
    "endpoint": URL,
    "request_mode": "one independent request per fiber",
    "fibers": FIBERS,
    "results": results,
    "raw_total_bytes": raw_total,
    "success": all_success,
}
(ROOT / "mw-magma-response.json").write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
stdout_all = "".join(
    f"===== FIBER {r['fiber']} =====\n{r.get('stdout', '')}" for r in results
)
(ROOT / "mw-magma-stdout.txt").write_text(stdout_all, encoding="utf-8")

if raw_total > MAX_TOTAL_RAW:
    raise SystemExit("Combined Magma responses exceeded the 1 MiB preflight cap")
if not all_success:
    failed = [r["fiber"] for r in results if not r.get("success")]
    raise SystemExit("Magma saturation certificate failed for: " + ", ".join(failed))
print("STAGE34_01_MW_SATURATION_ALL_FIBERS_PASS")
