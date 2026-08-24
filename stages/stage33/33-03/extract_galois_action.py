#!/usr/bin/env python3
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
            print(f"{label} transient failure {attempt}/{len(RETRY_DELAYS)}: {exc}")
    raise last


def fetch_bytes(url: str, timeout: int = 60):
    req = urllib.request.Request(url, headers={"User-Agent": "perfect-cuboid-stage33/1.4"})
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
    raise SystemExit(f"pinned upstream marker missing/out of order: {exc}")

# Reuse exactly the same Picard construction as audited Stage33-02, omitting
# only unused degree-8 curves.  The first pilot printed two full 64x64 integer
# matrices and hit the online XML output wall.  This revision keeps those
# matrices inside Magma, proves the needed identities there, and exports only:
#   * the two 72-component boundary permutations;
#   * exact Picard traces for cc, ct, and cc*ct;
#   * compact mod-2 row supports for later 2-primary quotient work.
core = (
    text[:i_skip_start]
    + "\n// Stage33-03 skips unused degree-8 curve construction.\n"
    + text[i_skip_end:i_stop]
)

extra = r'''
// Stage33-03 exact V4 Galois action, source-identical to the pinned upstream.
actperm := func<g, perm | qPic(Big![e[perm[j]] : j in [1..#e]])
                         where e := Eltseq(g @@ qPic)>;

ccL := hom<L -> L | -i>;
ccPL := hom<R -> R | ccL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actcc := func<C | Curve(Pr6, [ccPL(e) : e in DefiningEquations(C)])>;
permcc := [Position(C1s, actcc(C)) : C in C1s]
            cat [#C1s+Position(C2s, actcc(C)) : C in C2s]
            cat [#C1s+#C2s+Position(C3s, actcc(C)) : C in C3s]
            cat [#Cs+Position(pts, Pr6![ccL(a) : a in Eltseq(pt)]) : pt in pts];
ccPic := Matrix(Integers(), [Eltseq(actperm(Pic.j, permcc)) : j in [1..64]]);

ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permct := [Position(C1s, actct(C)) : C in C1s]
            cat [#C1s+Position(C2s, actct(C)) : C in C2s]
            cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
            cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];
ctPic := Matrix(Integers(), [Eltseq(actperm(Pic.j, permct)) : j in [1..64]]);

I64 := IdentityMatrix(Integers(),64);
assert ccPic*ccPic eq I64;
assert ctPic*ctPic eq I64;
assert ccPic*ctPic eq ctPic*ccPic;

side_inds := [1..24];
exc_inds := [#Cs + j : j in [1..48]];
boundary_inds := side_inds cat exc_inds;
assert #boundary_inds eq 72;
bpermcc := [Position(boundary_inds, permcc[j]) : j in boundary_inds];
bpermct := [Position(boundary_inds, permct[j]) : j in boundary_inds];
assert 0 notin bpermcc;
assert 0 notin bpermct;

boundary_gens := [qPic(Big.j) : j in boundary_inds];
for j in [1..72] do
  assert actperm(boundary_gens[j], permcc) eq boundary_gens[bpermcc[j]];
  assert actperm(boundary_gens[j], permct) eq boundary_gens[bpermct[j]];
end for;

printf "STAGE33_03_GALOIS_BEGIN\n";
printf "BOUNDARY_PERM_CC=%o\n", bpermcc;
printf "BOUNDARY_PERM_CT=%o\n", bpermct;
printf "PIC_TRACE_ID=64\n";
printf "PIC_TRACE_CC=%o\n", Trace(ccPic);
printf "PIC_TRACE_CT=%o\n", Trace(ctPic);
printf "PIC_TRACE_CCT=%o\n", Trace(ccPic*ctPic);
printf "BOUNDARY_EQUIVARIANCE_INTERNAL=true\n";
for j in [1..64] do
  printf "CCPIC_MOD2_SUPPORT_%o=%o\n", j,
    [k : k in [1..64] | IsOdd(ccPic[j,k])];
end for;
for j in [1..64] do
  printf "CTPIC_MOD2_SUPPORT_%o=%o\n", j,
    [k : k in [1..64] | IsOdd(ctPic[j,k])];
end for;
printf "STAGE33_03_GALOIS_END\n";
'''

code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra
summary = {
    "upstream_url": UPSTREAM_URL,
    "upstream_git_blob_sha1": actual_blob,
    "upstream_fetch_attempt": upstream_attempt,
    "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    "skip_unused_degree8": [i_skip_start, i_skip_end],
    "stop_before": STOP_MARKER,
    "export_mode": "boundary_permutations_picard_traces_and_mod2_supports",
    "supersedes_full_integer_matrix_xml_export": True,
}
(ROOT / "galois-request-summary.json").write_text(
    json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)

payload = urllib.parse.urlencode({"input": code}).encode()
req = urllib.request.Request(
    MAGMA_URL,
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage33/1.4",
    },
    method="POST",
)
resp, magma_attempt = urlopen_retry(req, 150, "Magma calculator")
with resp:
    raw_bytes = resp.read()
    http_status = resp.status
raw = raw_bytes.decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines)
if stdout and not stdout.endswith("\n"):
    stdout += "\n"
(ROOT / "galois-magma-response.xml").write_text(raw, encoding="utf-8")
(ROOT / "galois-magma-stdout.txt").write_text(stdout, encoding="utf-8")

if "STAGE33_03_GALOIS_BEGIN" not in stdout or "STAGE33_03_GALOIS_END" not in stdout:
    print(stdout)
    raise SystemExit("missing Stage33-03 completion markers")
if any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed")):
    print(stdout)
    raise SystemExit("Magma reported an exact-execution error")


def scalar(name):
    m = re.search(rf"^{re.escape(name)}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    return m.group(1).strip()


def seq(name):
    return ast.literal_eval(scalar(name).replace(" ", ""))


def numbered_support(prefix):
    found = {}
    for m in re.finditer(rf"^{re.escape(prefix)}_(\d+)=(.+)$", stdout, re.M):
        found[int(m.group(1))] = ast.literal_eval(m.group(2).strip().replace(" ", ""))
    if set(found) != set(range(1, 65)):
        raise SystemExit(f"incomplete {prefix} rows: {len(found)}")
    rows = []
    for irow in range(1, 65):
        support = found[irow]
        if any(k < 1 or k > 64 for k in support) or len(set(support)) != len(support):
            raise SystemExit(f"bad mod2 support row {prefix}_{irow}")
        row = [0] * 64
        for k in support:
            row[k - 1] = 1
        rows.append(row)
    return rows

bperm_cc = seq("BOUNDARY_PERM_CC")
bperm_ct = seq("BOUNDARY_PERM_CT")
if sorted(bperm_cc) != list(range(1, 73)) or sorted(bperm_ct) != list(range(1, 73)):
    raise SystemExit("boundary Galois action is not a permutation")
cc_pic_mod2 = numbered_support("CCPIC_MOD2_SUPPORT")
ct_pic_mod2 = numbered_support("CTPIC_MOD2_SUPPORT")
pic_traces = {
    "id": int(scalar("PIC_TRACE_ID")),
    "cc": int(scalar("PIC_TRACE_CC")),
    "ct": int(scalar("PIC_TRACE_CT")),
    "cct": int(scalar("PIC_TRACE_CCT")),
}
if scalar("BOUNDARY_EQUIVARIANCE_INTERNAL").lower() != "true":
    raise SystemExit("Magma internal boundary equivariance assertion absent")

out = {
    "schema": "STAGE33_03_RAW_V4_ACTION_COMPRESSED_V2",
    "source_lock": {
        "upstream_git_blob_sha1": actual_blob,
        "submitted_code_sha256": summary["submitted_code_sha256"],
        "magma_endpoint": MAGMA_URL,
        "magma_request_attempt": magma_attempt,
        "http_status": http_status,
    },
    "boundary_perm_cc_1based": bperm_cc,
    "boundary_perm_ct_1based": bperm_ct,
    "picard_character_traces": pic_traces,
    "picard_cc_matrix_mod2": cc_pic_mod2,
    "picard_ct_matrix_mod2": ct_pic_mod2,
    "boundary_equivariance_checked_inside_magma": True,
    "full_integer_picard_matrices_materialized_inside_magma_not_exported": True,
}
canonical = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
out["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "galois-action-raw.json").write_text(
    json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({
    "success": True,
    "boundary_count": len(bperm_cc),
    "picard_traces": pic_traces,
    "canonical_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
