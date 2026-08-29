#!/usr/bin/env python3
"""Extract the pinned Stoll ptsK index and qPicK coordinate for J2 infinity.

This is a deliberately small MAIN leaf.  It replays only the K_c setup through
construction of PicK from the source-locked Testa--Stoll Magma file.  It does
not run a Smith computation, does not select a Brauer coordinate, and does not
claim Stage33-12/33-07 closure.
"""
from __future__ import annotations

import ast
import hashlib
import json
import pathlib
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
UPSTREAM_URL = (
    "https://raw.githubusercontent.com/MichaelStollBayreuth/Verification/"
    "51233ed5ef2bf228fac9416c66db9adc0ebcaadd/Cuboids/cuboids.magma"
)
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"
START = "// Now repeat this for the K3 quotient obtained by forgetting c. See Section 6."
END = "// The hyperplane section"
RETRY_DELAYS = (0, 5, 15, 30)


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def urlopen_retry(req: urllib.request.Request, timeout: int, label: str):
    last = None
    for attempt, delay in enumerate(RETRY_DELAYS, 1):
        if delay:
            time.sleep(delay)
        try:
            return urllib.request.urlopen(req, timeout=timeout), attempt
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
            print(f"{label} transient failure {attempt}/{len(RETRY_DELAYS)}: {exc}")
    raise last


req = urllib.request.Request(UPSTREAM_URL, headers={"User-Agent": "perfect-cuboid-stage33/2.7"})
resp, upstream_attempt = urlopen_retry(req, 60, "upstream fetch")
with resp:
    upstream = resp.read()
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit(f"upstream blob mismatch {actual_blob}")
text = upstream.decode("utf-8")
i0 = text.index(START)
i1 = text.index(END, i0)
kcore = text[i0:i1]

# The K_c block only needs the pinned coefficient field from the earlier setup.
preamble = r'''
SetColumns(0);
quick := true;
L<i,s> := ext<Rationals() | Polynomial([1,0,1]), Polynomial([-2,0,1])>;
'''
extra = r'''
target := Pr5![1,0,0,0,-1,-1];
idx := Position(ptsK, target);
assert idx ne 0;
exc := #CsK + idx;
qv := Eltseq(qPicK(BigK.exc));
printf "STAGE33_12_J2_INFINITY_KC_BEGIN\n";
printf "NODE_COUNT=%o\n", #ptsK;
printf "CURVE_COUNT=%o\n", #CsK;
printf "TARGET_INDEX=%o\n", idx;
printf "BIGK_EXCEPTIONAL_INDEX=%o\n", exc;
printf "QPICK_COORD=%o\n", qv;
printf "STAGE33_12_J2_INFINITY_KC_END\n";
'''
code = preamble + "\n" + kcore + "\n" + extra
submitted_sha = hashlib.sha256(code.encode()).hexdigest()
payload = urllib.parse.urlencode({"input": code}).encode()
req = urllib.request.Request(
    MAGMA_URL,
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage33/2.7",
    },
    method="POST",
)
resp, magma_attempt = urlopen_retry(req, 240, "Stage33-12 J2 infinity Kc extractor")
with resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines: list[str] = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
if "STAGE33_12_J2_INFINITY_KC_END" not in stdout or any(
    x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")
):
    print(stdout)
    raise SystemExit("J2 infinity Kc exceptional extraction failed")


def scalar(name: str) -> int:
    m = re.search(rf"^{name}=([^\n]+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    return int(m.group(1).strip())


def seq(name: str):
    m = re.search(rf"^{name}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    return ast.literal_eval(m.group(1).replace(" ", ""))

idx = scalar("TARGET_INDEX")
node_count = scalar("NODE_COUNT")
curve_count = scalar("CURVE_COUNT")
qv = seq("QPICK_COORD")
assert node_count == 12
assert 1 <= idx <= node_count
assert len(qv) == 20

cert = {
    "schema": "STAGE33_12_J2_INFINITY_KC_EXCEPTIONAL_ORDER_V1",
    "source_lock": {
        "upstream_url": UPSTREAM_URL,
        "upstream_git_blob_sha1": actual_blob,
        "submitted_code_sha256": submitted_sha,
        "upstream_fetch_attempt": upstream_attempt,
        "magma_request_attempt": magma_attempt,
    },
    "target": {
        "stoll_projective_coordinates": [1, 0, 0, 0, -1, -1],
        "matches_result_md_P_inf_K": True,
    },
    "pinned_order": {
        "ptsK_count": node_count,
        "ptsK_index_1_based": idx,
        "CsK_count": curve_count,
        "BigK_exceptional_index_1_based": scalar("BIGK_EXCEPTIONAL_INDEX"),
        "qPicK_coordinate": qv,
    },
    "firewall": {
        "j2_branch_jacobian_to_discriminant_kummer_glue_materialized": False,
        "j2_kc_discriminant_coordinate_materialized": False,
        "stage33_12_closed": False,
        "stage33_07_closed": False,
        "theorem_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
    "next_exact_leaf": "COMBINE_CSK22_RESOLVED_BRANCH_AND_EJ2_WITH_PINNED_EXCEPTIONAL_CLASS_TO_MATERIALIZE_BRANCH_JACOBIAN_2TORSION_TO_KC_PICARD_DISCRIMINANT_KUMMER_GLUE",
}
raw_cert = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw_cert).hexdigest()
out = HERE / "j2-infinity-kc-exceptional-order.json"
out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "target_index": idx,
    "bigk_exceptional_index": cert["pinned_order"]["BigK_exceptional_index_1_based"],
    "qPicK_coordinate": qv,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
