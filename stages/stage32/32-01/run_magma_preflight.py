#!/usr/bin/env python3
import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
UPSTREAM_URL = (
    "https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/"
    "51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
)
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def fetch_bytes(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "perfect-cuboid-stage32/1.0"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} from {url}")
        return resp.read()


upstream = fetch_bytes(UPSTREAM_URL)
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit(
        f"upstream blob mismatch: expected {UPSTREAM_BLOB}, got {actual_blob}"
    )

preflight = (ROOT / "preflight_after_upstream.m").read_text(encoding="utf-8")
code = (
    "SetColumns(0);\n"
    "quick := true;\n"
    + upstream.decode("utf-8")
    + "\n"
    + preflight
)

data = urllib.parse.urlencode({"input": code}).encode("utf-8")
req = urllib.request.Request(
    MAGMA_URL,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage32/1.0",
    },
    method="POST",
)
with urllib.request.urlopen(req, timeout=240) as resp:
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

completion = "STAGE32_PREFLIGHT_END" in stdout
runtime_error = any(
    marker in stdout
    for marker in ("Runtime error", "Internal error", "User error", "Assertion failed")
)
success = http_status == 200 and completion and not runtime_error
payload = {
    "protocol": "official-magma-xml-calculator",
    "endpoint": MAGMA_URL,
    "http_status": http_status,
    "response_headers": response_headers,
    "upstream_url": UPSTREAM_URL,
    "upstream_git_blob_sha1": actual_blob,
    "stdout": stdout,
    "raw_xml": raw,
    "completion_marker_seen": completion,
    "runtime_error_seen": runtime_error,
    "success": success,
}
(ROOT / "magma-preflight-response.json").write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
(ROOT / "magma-preflight-stdout.txt").write_text(stdout, encoding="utf-8")

print(
    json.dumps(
        {
            "success": success,
            "protocol": payload["protocol"],
            "http_status": http_status,
            "runtime_error_seen": runtime_error,
            "upstream_git_blob_sha1": actual_blob,
        },
        sort_keys=True,
    )
)
print(stdout)

if not success:
    raise SystemExit("Stage32 Magma preflight did not finish cleanly")
