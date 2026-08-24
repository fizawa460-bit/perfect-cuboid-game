#!/usr/bin/env python3
import hashlib
import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
UPSTREAM_URL = (
    "https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/"
    "51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
)
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
SKIP_START = "// Genus 3 hyperelliptic curves of degree 8"
SKIP_END = "// Set up the intersection pairing"
AUT_GROUP_START = "// Set up the automorphism group in its representation on the Picard group."
CC_START = "// Set up complex conjugation."
STOP_MARKER = "// Automorphisms + Galois on Pic/2*Pic"
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def fetch_bytes(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "perfect-cuboid-stage33/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} from {url}")
        return resp.read()


upstream = fetch_bytes(UPSTREAM_URL)
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit(f"upstream blob mismatch: expected {UPSTREAM_BLOB}, got {actual_blob}")
text = upstream.decode("utf-8")
try:
    i_skip_start = text.index(SKIP_START)
    i_skip_end = text.index(SKIP_END, i_skip_start)
    i_aut = text.index(AUT_GROUP_START, i_skip_end)
    i_cc = text.index(CC_START, i_aut)
    i_stop = text.index(STOP_MARKER, i_cc)
except ValueError as exc:
    raise SystemExit(f"pinned upstream marker missing or out of order: {exc}")

# Retain all exact curve/intersection/Picard construction, skip the unused degree-8
# curve construction, skip the expensive Aut(S) group-order block, but retain the
# explicit curve permutations and both Q(i,sqrt2)/Q Galois matrices.
core = (
    text[:i_skip_start]
    + "\n// Stage33 skips unused degree-8 curve construction.\n"
    + text[i_skip_end:i_aut]
    + "\n// Stage33 skips unused Aut(S) group construction.\n"
    + text[i_cc:i_stop]
)
extra = (ROOT / "materialize_after_upstream.m").read_text(encoding="utf-8")
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra

payload_path = ROOT / "magma-request-summary.json"
payload_path.write_text(json.dumps({
    "upstream_url": UPSTREAM_URL,
    "upstream_git_blob_sha1": actual_blob,
    "skip_unused_degree8": [i_skip_start, i_skip_end],
    "skip_unused_aut_group": [i_aut, i_cc],
    "stop_before": STOP_MARKER,
    "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")

data = urllib.parse.urlencode({"input": code}).encode("utf-8")
req = urllib.request.Request(
    MAGMA_URL,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage33/1.0",
    },
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw_bytes = resp.read()
        http_status = resp.status
except urllib.error.HTTPError as exc:
    diagnostic = exc.read().decode("utf-8", errors="replace")
    (ROOT / "magma-http-error.txt").write_text(
        f"HTTP {exc.code} {exc.reason}\n{diagnostic}\n", encoding="utf-8"
    )
    raise

raw = raw_bytes.decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines)
if stdout and not stdout.endswith("\n"):
    stdout += "\n"

completion = "STAGE33_02_END" in stdout
runtime_error = any(x in stdout for x in (
    "Runtime error", "Internal error", "User error", "Assertion failed"
))
success = http_status == 200 and completion and not runtime_error
(ROOT / "magma-response.xml").write_text(raw, encoding="utf-8")
(ROOT / "magma-stdout.txt").write_text(stdout, encoding="utf-8")
(ROOT / "magma-response.json").write_text(json.dumps({
    "protocol": "official-magma-xml-calculator",
    "endpoint": MAGMA_URL,
    "http_status": http_status,
    "upstream_git_blob_sha1": actual_blob,
    "completion_marker_seen": completion,
    "runtime_error_seen": runtime_error,
    "success": success,
    "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(stdout)
if not success:
    raise SystemExit("Stage33-02 Magma materialization did not finish cleanly")
