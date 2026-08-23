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
    req = urllib.request.Request(url, headers={"User-Agent": "perfect-cuboid-stage32/1.2"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        if resp.status != 200:
            raise RuntimeError(f"HTTP {resp.status} from {url}")
        return resp.read()


upstream = fetch_bytes(UPSTREAM_URL)
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit(f"upstream blob mismatch: expected {UPSTREAM_BLOB}, got {actual_blob}")
text = upstream.decode("utf-8")
for marker in (SKIP_START, SKIP_END, END_MARKER):
    if text.count(marker) != 1:
        raise SystemExit(f"pinned upstream marker is not unique: {marker}")

# Execute only code that is load-bearing for the Stage32 numerical lattice:
# surface/nodes/known low-genus curves, exact 140x140 intersection pairing,
# Picard quotient/basis and hyperplane class.  The unrelated genus-3 curve
# construction and the later Aut/Galois/Brauer/K3 blocks are source-locked but
# intentionally not executed inside the online calculator's ~60s gateway.
head = text.split(SKIP_START, 1)[0]
pairing_and_pic = text.split(SKIP_END, 1)[1].split(END_MARKER, 1)[0]
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
        "User-Agent": "perfect-cuboid-stage32/1.2",
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
