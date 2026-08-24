#!/usr/bin/env python3
import collections
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
STOP_MARKER = "// See Definition 6 for C1s, C2s, C3s."
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"
RETRY_DELAYS = (0, 5, 15, 30)

BASE_POINTS = {
    1: (0, 0, 1),
    2: (0, 1, 0),
    3: (1, 0, 0),
    4: (0, 1, -1),
    5: (1, 0, -1),
    6: (1, -1, 0),
    7: (1, -1, -1),
    8: (1, -1, 1),
    9: (1, 1, -1),
}
BASE_POINT_NAMES = {
    1: "P_X_Y_XY",
    2: "P_X_Z_XZ",
    3: "P_Y_Z_YZ",
    4: "P_X_YZ_S",
    5: "P_Y_XZ_S",
    6: "P_Z_XY_S",
    7: "P_XY_XZ",
    8: "P_XY_YZ",
    9: "P_XZ_YZ",
}
SIDE_TO_BASE_LINE = {**{i: "Lx" for i in range(1, 9)}, **{i: "Ly" for i in range(9, 17)}, **{i: "Lz" for i in range(17, 25)}}


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


req = urllib.request.Request(UPSTREAM_URL, headers={"User-Agent": "perfect-cuboid-stage33/1.4"})
resp, upstream_attempt = urlopen_retry(req, 60, "upstream fetch")
with resp:
    upstream = resp.read()
actual_blob = git_blob_sha(upstream)
if actual_blob != UPSTREAM_BLOB:
    raise SystemExit("upstream blob mismatch")
text = upstream.decode("utf-8")
i_stop = text.index(STOP_MARKER)
core = text[:i_stop]

# The exact endpoint map is [a1:a2:a3:...] -> [a1^2:a2^2:a3^2].
# Classify every one of the 48 singular points against the nine audited
# seven-line intersection points without printing field elements.
pt_literal = "[" + ",".join("<%d,%d,%d>" % BASE_POINTS[j] for j in range(1, 10)) + "]"
extra = f'''
basepts := {pt_literal};
function SameProj(v,w)
  if forall{{x : x in v | x eq 0}} or forall{{x : x in w | x eq 0}} then
    return false;
  end if;
  return forall{{<r,s> : r,s in [1..3] | v[r]*w[s] eq v[s]*w[r]}};
end function;
ids := [];
for pt in pts do
  v := [pt[1]^2,pt[2]^2,pt[3]^2];
  matches := [j : j in [1..9] | SameProj(v,[L!basepts[j][k] : k in [1..3]])];
  assert #matches eq 1;
  Append(~ids,matches[1]);
end for;
printf "STAGE33_04_BASEMAP_BEGIN\\n";
printf "EXCEPTIONAL_BASE_POINT_IDS=%o\\n", ids;
printf "STAGE33_04_BASEMAP_END\\n";
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
resp, magma_attempt = urlopen_retry(req, 180, "Magma calculator")
with resp:
    raw = resp.read().decode("utf-8", errors="replace")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + "\n"
(ROOT / "sign-cover-boundary-map-magma-stdout.txt").write_text(stdout, encoding="utf-8")
if "STAGE33_04_BASEMAP_END" not in stdout or any(x in stdout for x in ("Runtime error", "Internal error", "Assertion failed", "User error")):
    print(stdout)
    raise SystemExit("sign-cover exceptional-point classification failed")

m = re.search(r"^EXCEPTIONAL_BASE_POINT_IDS=\[(.*)\]$", stdout, re.M)
if not m:
    raise SystemExit("missing exceptional base-point ids")
exc_ids = [int(x.strip()) for x in m.group(1).split(",") if x.strip()]
if len(exc_ids) != 48 or any(j not in BASE_POINTS for j in exc_ids):
    raise SystemExit("bad exceptional base-point classification")

skeleton = json.loads((ROOT / "boundary-residue-skeleton.json").read_text(encoding="utf-8"))
if skeleton["component_count"] != 72 or skeleton["codim2_crossing_count"] != 144:
    raise SystemExit("unexpected Stage33-04 skeleton")

# Map each endpoint boundary edge to the corresponding base incidence edge.
edge_preimages = collections.Counter()
for edge in skeleton["codim2_crossings"]:
    side_vertex = int(edge["side_vertex"])
    exc_vertex = int(edge["exceptional_vertex"])
    if not (1 <= side_vertex <= 24 and 25 <= exc_vertex <= 72):
        raise SystemExit("bad endpoint edge")
    line = SIDE_TO_BASE_LINE[side_vertex]
    point_id = exc_ids[exc_vertex - 25]
    x, y, z = BASE_POINTS[point_id]
    incidence_ok = {"Lx": x == 0, "Ly": y == 0, "Lz": z == 0}[line]
    if not incidence_ok:
        raise SystemExit(f"endpoint edge maps to non-incidence: {line}, P{point_id}")
    edge_preimages[(line, point_id)] += 1

# The physical side boundary only lies above x=0,y=0,z=0.  Record the exact
# base subgraph touched by the 72-component boundary and its cycle rank.
touched_points = sorted({j for _, j in edge_preimages})
touched_lines = sorted({line for line, _ in edge_preimages})
base_edges = sorted(edge_preimages)
V = len(touched_points) + len(touched_lines)
E = len(base_edges)
# The touched graph is connected iff all its vertices lie in one union-find component.
vertices = [("L", x) for x in touched_lines] + [("P", x) for x in touched_points]
idx = {v: i for i, v in enumerate(vertices)}
parent = list(range(len(vertices)))

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a,b):
    a,b=find(a),find(b)
    if a != b:
        parent[b]=a
for line,pid in base_edges:
    union(idx[("L",line)], idx[("P",pid)])
components = len({find(i) for i in range(len(vertices))})
cycle_rank = E - V + components

# Build mod-2 edge pullback C^1(base)->C^1(endpoint), and compute the rank
# induced on H^1 of graphs by quotienting coboundaries.  Since graph H^1 is the
# dual of H_1 over F2, this is the exact combinatorial Ford-incidence pullback
# rank before ramification/symbol-residue conditions.
endpoint_edges = skeleton["codim2_crossings"]
base_edge_index = {e:i for i,e in enumerate(base_edges)}
P = [[0]*len(endpoint_edges) for _ in base_edges]
for k, edge in enumerate(endpoint_edges):
    sv = int(edge["side_vertex"])
    ev = int(edge["exceptional_vertex"])
    key = (SIDE_TO_BASE_LINE[sv], exc_ids[ev-25])
    P[base_edge_index[key]][k] ^= 1

# GF(2) linear algebra helpers.
def rref(rows):
    A=[row[:] for row in rows]
    if not A:
        return A,[]
    m,n=len(A),len(A[0]); piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        for i in range(m):
            if i!=r and A[i][c]: A[i]=[x^y for x,y in zip(A[i],A[r])]
        piv.append(c); r+=1
        if r==m: break
    return A,piv

def rank(rows):
    return len(rref(rows)[1]) if rows else 0

# Coboundary row spaces are generated by vertex incidences in edge coordinates.
def coboundary_rows(lines, points, edges):
    out=[]
    for line in lines:
        out.append([1 if e[0]==line else 0 for e in edges])
    for pid in points:
        out.append([1 if e[1]==pid else 0 for e in edges])
    return out

base_B = coboundary_rows(touched_lines,touched_points,base_edges)
end_lines=[f"S{i}" for i in range(1,25)]
end_points=[f"E{i}" for i in range(1,49)]
end_edge_pairs=[(f"S{int(e['side_vertex'])}",f"E{int(e['exceptional_vertex'])-24}") for e in endpoint_edges]
end_B=[]
for v in end_lines+end_points:
    end_B.append([1 if v in e else 0 for e in end_edge_pairs])

# Image in endpoint H^1: span(pullback rows + endpoint coboundaries) modulo endpoint coboundaries.
pull_rows=P
induced_h1_rank = rank(end_B + pull_rows) - rank(end_B)
base_h1_dim = len(base_edges) - rank(base_B)
endpoint_h1_dim = len(endpoint_edges) - rank(end_B)
if base_h1_dim != cycle_rank or endpoint_h1_dim != skeleton["dual_graph_cycle_rank"]:
    raise SystemExit("graph cohomology dimension regression")

counts = collections.Counter(exc_ids)
cert = {
    "schema": "STAGE33_04_SIGN_COVER_BOUNDARY_BASEMAP_V1",
    "source_lock": {
        "upstream_git_blob_sha1": actual_blob,
        "submitted_code_sha256": hashlib.sha256(code.encode()).hexdigest(),
        "endpoint_map": "[a1:a2:a3:b1:b2:b3:c] -> [a1^2:a2^2:a3^2]",
        "sign_cover_degree": 64,
    },
    "exceptional_base_point_id_1based": exc_ids,
    "exceptional_fiber_histogram": {BASE_POINT_NAMES[j]: counts.get(j,0) for j in range(1,10)},
    "side_family_base_line": {"SIDE_A1_001..008":"Lx","SIDE_A2_001..008":"Ly","SIDE_A3_001..008":"Lz"},
    "touched_base_lines": touched_lines,
    "touched_base_point_ids": touched_points,
    "touched_base_point_names": [BASE_POINT_NAMES[j] for j in touched_points],
    "base_incidence_edge_preimage_multiplicity": {f"{line}--{BASE_POINT_NAMES[pid]}": mult for (line,pid),mult in sorted(edge_preimages.items())},
    "touched_base_graph": {"vertices":V,"edges":E,"components":components,"cycle_rank":cycle_rank},
    "endpoint_boundary_graph_h1_f2_dimension": endpoint_h1_dim,
    "touched_base_graph_h1_f2_dimension": base_h1_dim,
    "combinatorial_incidence_pullback_h1_f2_rank": induced_h1_rank,
    "ford_full_seven_line_h1_dimension": 9,
    "ford_full_pullback_complete": False,
    "ramification_symbol_residue_conditions_applied": False,
    "exceptional_residue_accounting_started": True,
    "multiquadratic_pullback_accounted": False,
    "physical_open_unramified_kernel_complete": False,
    "br0g_discharged": False,
    "next_exact_leaf": "L33-04-FORD9-TO-ENDPOINT72-RAMIFIED-RESIDUE-PULLBACK",
    "theorem_credit": False,
    "endpoint_credit": False,
}
canonical=json.dumps(cert,sort_keys=True,separators=(",",":")).encode()
cert["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
(ROOT / "sign-cover-boundary-map.json").write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps({
    "success":True,
    "exceptional_fiber_histogram":cert["exceptional_fiber_histogram"],
    "touched_base_graph":cert["touched_base_graph"],
    "combinatorial_incidence_pullback_h1_f2_rank":induced_h1_rank,
    "next_exact_leaf":cert["next_exact_leaf"],
    "certificate_sha256":cert["canonical_sha256"],
},indent=2,sort_keys=True))
