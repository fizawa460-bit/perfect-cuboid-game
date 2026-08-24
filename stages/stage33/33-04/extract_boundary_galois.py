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


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def urlopen_retry(req, timeout, label):
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


req = urllib.request.Request(UPSTREAM_URL, headers={"User-Agent": "perfect-cuboid-stage33/1.4"})
resp, upstream_attempt = urlopen_retry(req, 60, "upstream fetch")
with resp:
    upstream = resp.read()
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit(f"upstream blob mismatch {actual_blob}")
text = upstream.decode("utf-8")
i_skip_start = text.index(SKIP_START)
i_skip_end = text.index(SKIP_END, i_skip_start)
i_stop = text.index(STOP_MARKER, i_skip_end)
core = text[:i_skip_start] + "\n// Stage33-04 skips unused degree-8 curves.\n" + text[i_skip_end:i_stop]

extra = r'''
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
ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permct := [Position(C1s, actct(C)) : C in C1s]
            cat [#C1s+Position(C2s, actct(C)) : C in C2s]
            cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
            cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];
side_inds := [1..24];
exc_inds := [#Cs+j : j in [1..48]];
boundary_inds := side_inds cat exc_inds;
bpermcc := [Position(boundary_inds, permcc[j]) : j in boundary_inds];
bpermct := [Position(boundary_inds, permct[j]) : j in boundary_inds];
assert 0 notin bpermcc;
assert 0 notin bpermct;
printf "STAGE33_04_GALOIS_BEGIN\n";
printf "BOUNDARY_PERM_CC=%o\n", bpermcc;
printf "BOUNDARY_PERM_CT=%o\n", bpermct;
printf "STAGE33_04_GALOIS_END\n";
'''
code = "SetColumns(0);\nquick := true;\n" + core + "\n" + extra
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
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "boundary-galois-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_04_GALOIS_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "Assertion failed")):
    print(stdout)
    raise SystemExit("boundary Galois extraction failed")


def seq(name):
    m = re.search(rf"^{name}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    return ast.literal_eval(m.group(1).replace(" ", ""))

cc = seq("BOUNDARY_PERM_CC")
ct = seq("BOUNDARY_PERM_CT")
if sorted(cc) != list(range(1, 73)) or sorted(ct) != list(range(1, 73)):
    raise SystemExit("invalid boundary permutation")
out = {
    "schema": "STAGE33_04_BOUNDARY_GALOIS_SOURCE_LOCK_V1",
    "upstream_git_blob_sha1": actual_blob,
    "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    "upstream_fetch_attempt": upstream_attempt,
    "magma_request_attempt": magma_attempt,
    "boundary_perm_cc_1based": cc,
    "boundary_perm_ct_1based": ct,
}
canonical = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
out["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "boundary-galois.json").write_text(json.dumps(out, indent=2, sort_keys=True)+"\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "cc_fixed_components": sum(j == x for j, x in enumerate(cc, 1)),
    "ct_fixed_components": sum(j == x for j, x in enumerate(ct, 1)),
    "canonical_sha256": out["canonical_sha256"],
}, indent=2, sort_keys=True))
