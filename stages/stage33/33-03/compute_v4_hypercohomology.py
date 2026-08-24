#!/usr/bin/env python3
import hashlib
import io
import json
import os
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
REPO = "fizawa460-bit/perfect-cuboid-game"
STAGE32_ARTIFACT_ID = 9486641560
STAGE32_ARTIFACT_URL = f"https://api.github.com/repos/{REPO}/actions/artifacts/{STAGE32_ARTIFACT_ID}/zip"
STAGE32_ARTIFACT_SHA256 = "cae5c9b5aa00d9a730510c9f0e01ab609acef9d759fcc93f64708da123d6813d"
STAGE32_CORE_CANONICAL_SHA256 = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
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


class StripCrossHostAuthRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        newreq = super().redirect_request(req, fp, code, msg, headers, newurl)
        if newreq is not None and urllib.parse.urlsplit(req.full_url).netloc != urllib.parse.urlsplit(newurl).netloc:
            newreq.remove_header("Authorization")
        return newreq


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


def git_blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def download_stage32():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN required")
    req = urllib.request.Request(
        STAGE32_ARTIFACT_URL,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "perfect-cuboid-stage33/1.7",
        },
    )
    opener = urllib.request.build_opener(StripCrossHostAuthRedirect())
    with opener.open(req, timeout=60) as resp:
        raw = resp.read()
    if hashlib.sha256(raw).hexdigest() != STAGE32_ARTIFACT_SHA256:
        raise SystemExit("Stage32 artifact digest mismatch")
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        core = json.loads(zf.read("picard-core.json"))
    if core.get("canonical_sha256_without_this_field") != STAGE32_CORE_CANONICAL_SHA256:
        raise SystemExit("Stage32 Picard core canonical hash mismatch")
    if core.get("rank") != 64 or core.get("known_class_count") != 140:
        raise SystemExit("Stage32 Picard core shape mismatch")
    return core


core32 = download_stage32()
known = core32["known_classes"]
prim_inds = [int(x) for x in core32["basis_known_indices_1based"]]
boundary_inds = list(range(1, 25)) + list(range(93, 141))
M = [known[j - 1] for j in boundary_inds]
if len(M) != 72 or any(len(row) != 64 for row in M):
    raise SystemExit("bad Stage32 boundary-to-primitive-Picard matrix")

req = urllib.request.Request(UPSTREAM_URL, headers={"User-Agent": "perfect-cuboid-stage33/1.7"})
resp, upstream_attempt = urlopen_retry(req, 60, "upstream fetch")
with resp:
    upstream = resp.read()
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit("upstream blob mismatch")
text = upstream.decode("utf-8")
i0 = text.index(SKIP_START)
i1 = text.index(SKIP_END, i0)
i2 = text.index(STOP_MARKER, i1)
source_core = text[:i0] + "\n// Stage33-03 skips unused degree-8 curves.\n" + text[i1:i2]

prim_literal = "[" + ",".join(map(str, prim_inds)) + "]"
m_literal = "[" + ",".join(str(int(x)) for row in M for x in row) + "]"
extra = f'''
Z := Integers();
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
ccPic := Matrix(Z, [Eltseq(actperm(Pic.j, permcc)) : j in [1..64]]);
ctL := hom<L -> L | hom<GroundField(L) -> L | -s>, i>;
ctPL := hom<R -> R | ctL*Bang(L,R), [R.j : j in [1..7]]>
          where R := CoordinateRing(Pr6);
actct := func<C | Curve(Pr6, [ctPL(e) : e in DefiningEquations(C)])>;
permct := [Position(C1s, actct(C)) : C in C1s]
            cat [#C1s+Position(C2s, actct(C)) : C in C2s]
            cat [#C1s+#C2s+Position(C3s, actct(C)) : C in C3s]
            cat [#Cs+Position(pts, Pr6![ctL(a) : a in Eltseq(pt)]) : pt in pts];
ctPic := Matrix(Z, [Eltseq(actperm(Pic.j, permct)) : j in [1..64]]);

prim_inds := {prim_literal};
A := Matrix(Z, [Eltseq(qPic(Big.j)) : j in prim_inds]);
assert Abs(Determinant(A)) eq 1;
AinvQ := ChangeRing(A,Rationals())^-1;
Ainv := Matrix(Z,64,64,[Z!x : x in Eltseq(AinvQ)]);
Ccc := A*ccPic*Ainv;
Cct := A*ctPic*Ainv;
assert Ccc*Ccc eq IdentityMatrix(Z,64);
assert Cct*Cct eq IdentityMatrix(Z,64);
assert Ccc*Cct eq Cct*Ccc;

boundary_inds := [1..24] cat [93..140];
bpermcc := [Position(boundary_inds, permcc[j]) : j in boundary_inds];
bpermct := [Position(boundary_inds, permct[j]) : j in boundary_inds];
assert 0 notin bpermcc and 0 notin bpermct;
Pcc := ZeroMatrix(Z,72,72);
Pct := ZeroMatrix(Z,72,72);
for j in [1..72] do
  Pcc[j,bpermcc[j]] := 1;
  Pct[j,bpermct[j]] := 1;
end for;
assert Pcc*Pcc eq IdentityMatrix(Z,72);
assert Pct*Pct eq IdentityMatrix(Z,72);
assert Pcc*Pct eq Pct*Pcc;

Mstage := Matrix(Z,72,64,{m_literal});
assert Pcc*Mstage eq Mstage*Ccc;
assert Pct*Mstage eq Mstage*Cct;

procedure AddBlock(~D, B, r0, c0, sgn)
  for ii in [1..Nrows(B)] do
    for jj in [1..Ncols(B)] do
      if B[ii,jj] ne 0 then
        D[r0+ii-1,c0+jj-1] +:= sgn*B[ii,jj];
      end if;
    end for;
  end for;
end procedure;

function ResOp(G,n)
  I := IdentityMatrix(Z,Nrows(G));
  if IsOdd(n) then
    return G-I;
  else
    return G+I;
  end if;
end function;

function GroupCob(Ga,Gb,r)
  m := Nrows(Ga);
  D := ZeroMatrix(Z,(r+1)*m,(r+2)*m);
  for p in [0..r] do
    q := r-p;
    // Tensor-product resolution of C2 x C2, target components ordered by p.
    AddBlock(~D,ResOp(Gb,q+1),p*m+1,p*m+1,IsEven(p) select 1 else -1);
    AddBlock(~D,ResOp(Ga,p+1),p*m+1,(p+1)*m+1,1);
  end for;
  return D;
end function;

function TotalDiff(n)
  divrows := (n+1)*72;
  picrows := n eq 0 select 0 else n*64;
  divcols := (n+2)*72;
  piccols := (n+1)*64;
  D := ZeroMatrix(Z,divrows+picrows,divcols+piccols);
  GD := GroupCob(Pcc,Pct,n);
  AddBlock(~D,GD,1,1,1);
  // Internal divisor-to-Picard differential; sign is (-1)^(group degree).
  isgn := IsEven(n) select 1 else -1;
  for p in [0..n] do
    AddBlock(~D,Mstage,p*72+1,divcols+p*64+1,isgn);
  end for;
  if n ge 1 then
    GP := GroupCob(Ccc,Cct,n-1);
    AddBlock(~D,GP,divrows+1,divcols+1,1);
  end if;
  return D;
end function;

D0 := TotalDiff(0);
D1 := TotalDiff(1);
D2 := TotalDiff(2);
assert D0*D1 eq ZeroMatrix(Z,Nrows(D0),Ncols(D1));
assert D1*D2 eq ZeroMatrix(Z,Nrows(D1),Ncols(D2));

// H^2 = ker(D2)/im(D1).  SmithForm(Transpose(D2)) gives a saturated
// integral kernel basis through the right unimodular transform.
S2, _, V2 := SmithForm(Transpose(D2));
r2 := Rank(D2);
n2 := Nrows(D2);
kdim := n2-r2;
V2inv := V2^-1;
Coords := D1*Transpose(V2inv);
for rr in [1..Nrows(Coords)] do
  for cc in [1..r2] do
    assert Coords[rr,cc] eq 0;
  end for;
end for;
Brel := Submatrix(Coords,1,r2+1,Nrows(Coords),kdim);
SB := SmithForm(Brel);
rr := Rank(Brel);
diag := [Abs(Z!SB[j,j]) : j in [1..rr]];
tors := [d : d in diag | d ne 1];
free := kdim-rr;
assert forall{{d : d in tors | d in [2,4]}};

printf "STAGE33_03_V4_HYPER_BEGIN\\n";
printf "T0_RANK=%o\\n", Nrows(D0);
printf "T1_RANK=%o\\n", Nrows(D1);
printf "T2_RANK=%o\\n", Nrows(D2);
printf "T3_RANK=%o\\n", Ncols(D2);
printf "D1_RANK=%o\\n", Rank(D1);
printf "D2_RANK=%o\\n", r2;
printf "KERNEL_D2_RANK=%o\\n", kdim;
printf "RELATION_RANK=%o\\n", rr;
printf "H2_FREE_RANK=%o\\n", free;
printf "H2_TORSION=%o\\n", tors;
printf "STAGE33_03_V4_HYPER_END\\n";
'''
code = "SetColumns(0);\nquick := true;\n" + source_core + "\n" + extra
summary = {
    "schema": "STAGE33_03_V4_HYPERCOHOMOLOGY_REQUEST_V1",
    "upstream_git_blob_sha1": actual_blob,
    "stage32_artifact_id": STAGE32_ARTIFACT_ID,
    "stage32_artifact_sha256": STAGE32_ARTIFACT_SHA256,
    "stage32_core_canonical_sha256": STAGE32_CORE_CANONICAL_SHA256,
    "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
    "resolution": "tensor product of the standard 2-periodic C2 resolutions for V4=C2xC2",
    "totalization": "UPic=[Div_D degree 0 -> Pic degree 1], internal sign (-1)^group_degree",
}
(ROOT / "v4-hyper-request-summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")

payload = urllib.parse.urlencode({"input": code}).encode()
req = urllib.request.Request(
    MAGMA_URL,
    data=payload,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage33/1.7",
    },
    method="POST",
)
resp, magma_attempt = urlopen_retry(req, 300, "Magma calculator")
with resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "v4-hyper-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_03_V4_HYPER_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "Assertion failed", "User error")):
    print(stdout)
    raise SystemExit("finite V4 UPic hypercohomology computation failed")


def scalar(name):
    import re
    m = re.search(rf"^{name}=(.+)$", stdout, re.M)
    if not m:
        raise SystemExit(f"missing {name}")
    return m.group(1).strip()


def magma_int_list(s):
    s = s.strip()
    if s == "[]":
        return []
    return [int(x.strip()) for x in s[1:-1].split(",") if x.strip()]

cert = {
    "schema": "STAGE33_03_FINITE_V4_UPIC_H2_V1",
    "source_locks": summary,
    "magma_request_attempt": magma_attempt,
    "cochain_ranks": {
        "total_0": int(scalar("T0_RANK")),
        "total_1": int(scalar("T1_RANK")),
        "total_2": int(scalar("T2_RANK")),
        "total_3": int(scalar("T3_RANK")),
    },
    "differential_ranks": {"d1": int(scalar("D1_RANK")), "d2": int(scalar("D2_RANK"))},
    "kernel_d2_rank": int(scalar("KERNEL_D2_RANK")),
    "relation_rank_inside_kernel": int(scalar("RELATION_RANK")),
    "finite_v4_h2_free_rank": int(scalar("H2_FREE_RANK")),
    "finite_v4_h2_torsion_invariants": magma_int_list(scalar("H2_TORSION")),
    "extension_data_included": True,
    "transgression_not_assumed_separately": True,
    "finite_v4_hypercohomology_complete": True,
    "absolute_two_primary_completion": False,
    "br0b_all_primary_classes_accounted": False,
    "next_exact_leaf": "L33-03-ABSOLUTE-TWO-PRIMARY-INFLATION-RESTRICTION",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
(ROOT / "finite-v4-hypercohomology.json").write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "finite_v4_h2_free_rank": cert["finite_v4_h2_free_rank"],
    "finite_v4_h2_torsion_invariants": cert["finite_v4_h2_torsion_invariants"],
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
