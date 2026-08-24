#!/usr/bin/env python3
import hashlib
import json
import pathlib
import time
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
STOP_MARKER = "// The automorphism group (see Proposition 4)"
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"
RETRY_DELAYS = (0, 5, 15, 30)


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def urlopen_retry(req, timeout, label):
    last = None
    for attempt, delay in enumerate(RETRY_DELAYS, start=1):
        if delay:
            time.sleep(delay)
        try:
            return urllib.request.urlopen(req, timeout=timeout), attempt
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            print(f"{label} transient network failure attempt {attempt}/{len(RETRY_DELAYS)}: {exc}")
    raise last


def fetch_bytes(url: str, timeout: int = 60) -> tuple[bytes, int]:
    req = urllib.request.Request(url, headers={"User-Agent": "perfect-cuboid-stage33/1.2"})
    resp, attempt = urlopen_retry(req, timeout, "upstream fetch")
    with resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} from {url}")
        return resp.read(), attempt


upstream, upstream_attempt = fetch_bytes(UPSTREAM_URL)
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit(f"upstream blob mismatch: expected {UPSTREAM_BLOB}, got {actual_blob}")
text = upstream.decode("utf-8")
try:
    i_skip_start = text.index(SKIP_START)
    i_skip_end = text.index(SKIP_END, i_skip_start)
    i_stop = text.index(STOP_MARKER, i_skip_end)
except ValueError as exc:
    raise SystemExit(f"pinned upstream marker missing or out of order: {exc}")

# BR0A needs the exact intersection/Picard lattice but not the later Aut/Galois
# layer. Keep the Stage33-02 request below the online calculator's bounded wall;
# Galois matrices are a Stage33-03 responsibility.
core = (
    text[:i_skip_start]
    + "\n// Stage33 skips unused degree-8 curve construction.\n"
    + text[i_skip_end:i_stop]
)
extra = (ROOT / "materialize_after_upstream.m").read_text(encoding="utf-8")
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra

payload_path = ROOT / "magma-request-summary.json"
payload_path.write_text(json.dumps({
    "upstream_url": UPSTREAM_URL,
    "upstream_git_blob_sha1": actual_blob,
    "upstream_fetch_attempt": upstream_attempt,
    "skip_unused_degree8": [i_skip_start, i_skip_end],
    "stop_before": STOP_MARKER,
    "stage33_03_galois_layer_intentionally_excluded": True,
    "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    "network_retry_delays_seconds": RETRY_DELAYS,
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")

data = urllib.parse.urlencode({"input": code}).encode("utf-8")
req = urllib.request.Request(
    MAGMA_URL,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage33/1.2",
    },
    method="POST",
)
try:
    resp, magma_attempt = urlopen_retry(req, 120, "Magma calculator")
    with resp:
        raw_bytes = resp.read()
        http_status = resp.status
except urllib.error.HTTPError as exc:
    diagnostic = exc.read().decode("utf-8", errors="replace")
    (ROOT / "magma-http-error.txt").write_text(
        f"HTTP {exc.code} {exc.reason}\n{diagnostic}\n", encoding="utf-8"
    )
    raise
except (urllib.error.URLError, TimeoutError) as exc:
    (ROOT / "magma-network-error.txt").write_text(
        f"all {len(RETRY_DELAYS)} attempts failed\n{exc!r}\n", encoding="utf-8"
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
    "magma_request_attempt": magma_attempt,
    "upstream_git_blob_sha1": actual_blob,
    "completion_marker_seen": completion,
    "runtime_error_seen": runtime_error,
    "success": success,
    "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(stdout)
if not success:
    raise SystemExit("Stage33-02 Magma materialization did not finish cleanly")
