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
END_MARKER = "// The automorphism group (see Proposition 4)"
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def fetch_bytes(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "perfect-cuboid-stage32/1.3"})
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
    i_skip_end = text.index(SKIP_END, i_skip_start + len(SKIP_START))
    i_end = text.index(END_MARKER, i_skip_end + len(SKIP_END))
except ValueError as exc:
    raise SystemExit(f"pinned upstream marker missing or out of order: {exc}")

# Execute only code load-bearing for the Stage32 numerical lattice.  We skip
# the unrelated genus-3 constructions and stop before Aut/Galois/Brauer/K3.
head = text[:i_skip_start]
pairing_and_pic = text[i_skip_end + len(SKIP_END):i_end]
core = head + "\n// Stage32 resumes at the frozen intersection-pairing block.\n" + pairing_and_pic

hperp_setup = r'''
// Exact reconstruction of the frozen upstream H^perp setup.
Hperp := Kernel(Transpose(Matrix([HinPic])*pmPic));
pospmHperp := -BasisMatrix(Hperp)*pmPic*Transpose(BasisMatrix(Hperp));
LHp := LatticeWithGram(pospmHperp);
HperpMod := RSpace(Integers(), 63);
HperptoPic := hom<HperpMod -> Pic | Basis(Hperp)>;
'''
preflight = (ROOT / "preflight_after_upstream.m").read_text(encoding="utf-8")
code = "SetColumns(0);\nquick := true;\n" + core + hperp_setup + "\n" + preflight

data = urllib.parse.urlencode({"input": code}).encode("utf-8")
req = urllib.request.Request(
    MAGMA_URL,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage32/1.3",
    },
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=75) as resp:
        raw_bytes = resp.read()
        http_status = resp.status
        response_headers = dict(resp.headers.items())
except urllib.error.HTTPError as exc:
    diagnostic = exc.read().decode("utf-8", errors="replace")
    (ROOT / "magma-preflight-http-error.txt").write_text(
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
    "executed_core": {
        "skip_start_offset": i_skip_start,
        "resume_offset": i_skip_end + len(SKIP_END),
        "stop_offset": i_end,
        "skipped_between": [SKIP_START, SKIP_END],
        "stopped_before": END_MARKER,
    },
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

print(json.dumps({
    "success": success,
    "protocol": payload["protocol"],
    "http_status": http_status,
    "runtime_error_seen": runtime_error,
    "upstream_git_blob_sha1": actual_blob,
    "stopped_before": END_MARKER,
}, sort_keys=True))
print(stdout)
if not success:
    raise SystemExit("Stage32 Magma preflight did not finish cleanly")
