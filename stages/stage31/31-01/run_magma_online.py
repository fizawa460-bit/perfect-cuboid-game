#!/usr/bin/env python3
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
CODE = (ROOT / "magma_quartic_certificate.m").read_text(encoding="utf-8")
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"

data = urllib.parse.urlencode({"input": "SetColumns(0);\n" + CODE}).encode("utf-8")
req = urllib.request.Request(
    URL,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": REFERER,
        "User-Agent": "perfect-cuboid-stage31/1.0",
    },
    method="POST",
)
with urllib.request.urlopen(req, timeout=150) as resp:
    raw_bytes = resp.read()
    http_status = resp.status
    response_headers = dict(resp.headers.items())

raw = raw_bytes.decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines)
if stdout and not stdout.endswith("\n"):
    stdout += "\n"

completion = "STAGE31_MAGMA_QUARTIC_CERTIFICATE_END" in stdout
runtime_error = any(marker in stdout for marker in ("Runtime error", "Internal error", "User error", "Assertion failed"))
success = http_status == 200 and completion and not runtime_error
payload = {
    "protocol": "official-magma-xml-calculator",
    "endpoint": URL,
    "http_status": http_status,
    "response_headers": response_headers,
    "stdout": stdout,
    "raw_xml": raw,
    "completion_marker_seen": completion,
    "runtime_error_seen": runtime_error,
    "success": success,
}
(ROOT / "magma-response.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
(ROOT / "magma-stdout.txt").write_text(stdout, encoding="utf-8")

print(json.dumps({
    "success": success,
    "protocol": payload["protocol"],
    "http_status": http_status,
    "runtime_error_seen": runtime_error,
}, sort_keys=True))
print(stdout)

if not success:
    raise SystemExit("Magma certificate did not finish cleanly")
