#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ART = ROOT / "stages/stage32-ex3/scratch/ex3-04d-upstairs-h4-prym-rosati-fourier-gate.json"
TOWER = ROOT / "stages/stage32-ex3/ex3-00-o210-typed-cover-tower.json"
REPAIR = ROOT / "stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair.json"
REPAIR_NOTE = ROOT / "stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md"
CHAR = ROOT / "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-rational-character-algebra-integral-index-boundary.json"
WLOCK = ROOT / "stages/stage32/residual-32-01-production/post1505-o210-q4-x8-v4-torsor-plane-weierstrass-lock.json"


def csha_without_field(value: dict) -> str:
    v = dict(value)
    claimed = v.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert got == claimed
    return claimed


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


art = json.loads(ART.read_text())
tower = json.loads(TOWER.read_text())
repair = json.loads(REPAIR.read_text())
char = json.loads(CHAR.read_text())
wlock = json.loads(WLOCK.read_text())
note = REPAIR_NOTE.read_text()

assert art["status"] == "SCRATCH_PROVISIONAL_DIAGNOSTIC_NOT_RETAINED"
assert blob_sha1(TOWER) == art["source_locks"]["typed_cover_tower"]["blob_sha1"]
assert csha_without_field(tower) == art["source_locks"]["typed_cover_tower"]["canonical_sha256"]
assert csha_without_field(repair) == art["source_locks"]["audited_rosati_repair_arithmetic"]["canonical_sha256"]
assert csha_without_field(char) == art["source_locks"]["rational_H_character_algebra"]["canonical_sha256"]
assert csha_without_field(wlock) == art["source_locks"]["retained_H_character_names_and_pairs"]["canonical_sha256"]
assert blob_sha1(REPAIR_NOTE) == art["source_locks"]["rosati_trace_formula"]["blob_sha1"]
assert "sigma(Gamma)=2*d1*d2-Gamma^2" in note
assert "rational Rosati trace pairing" in note

# EX3-00 locks the actual degree-4 etale product cover and the two upstairs projection degrees.
p_to_x = [m for m in tower["tower_maps"] if m["map"] == "P->X"]
assert len(p_to_x) == 1 and p_to_x[0]["degree"] == 4 and p_to_x[0]["ramification_total"] == 0
assert tower["degree_adapter"]["n_pair_D_to_X8"] == [105, 81]

# Use only post1500 retained exact arithmetic, not its superseded exclusion decision.
r = repair["retained_exact_inputs"]
assert r["projection_degrees"] == [105, 81]
assert r["pair_map_generic_degree"] == 1 and r["pair_map_birational"] is True
assert r["D_square"] == 3874
assert [r["D_square"], r["deck_cross"]["u"], r["deck_cross"]["v"], r["deck_cross"]["uv"]] == [3874,3892,4020,4020]
assert repair["corrected_rosati_arithmetic"]["sigma"] == 1204
assert repair["corrected_rosati_arithmetic"]["Q"] == 602

# Beauville H-character rational decomposition: 2-dimensional trivial holomorphic block and three 1-dimensional nontrivial blocks, Q(i)^3.
ra = char["rational_character_adapter"]
assert ra["nontrivial_character_count"] == 3
assert ra["nontrivial_character_holomorphic_dimension_each"] == 1
assert ra["nontrivial_character_rational_endomorphism_algebra_each"] == "Q(i)"

# Retained F2 character names and their canonical Weierstrass-pair labels.
cp = wlock["character_pushouts"]
assert cp["H_basis"] == ["u", "v"]
assert cp["characters"]["chi_u"]["values"] == {"u":1,"v":0,"uv":1}
assert cp["characters"]["chi_v"]["values"] == {"u":0,"v":1,"uv":1}
assert cp["characters"]["chi_uv"]["values"] == {"u":1,"v":1,"uv":0}
assert cp["characters"]["chi_u"]["canonical_pair"] == "Z3"
assert cp["characters"]["chi_v"]["canonical_pair"] == "Z2"
assert cp["characters"]["chi_uv"]["canonical_pair"] == "Z1"

# Pull the X-level four intersections to P=ZxZ through the degree-4 etale quotient.
xints = [3874,3892,4020,4020]
pints = [4*x for x in xints]
assert pints == art["etale_pullback_intersections"]["P_level_intersections_order_1_u_v_uv"] == [15496,15568,16080,16080]

d1,d2 = 105,81
twice = 2*d1*d2
assert twice == 17010 == art["upstairs_correspondence"]["twice_degree_product"]
L = [twice-x for x in pints]
assert L == [1514,1442,930,930] == art["upstairs_correspondence"]["trace_values_L_h_order_1_u_v_uv"]

# Convert retained F2-valued characters to +/-1 characters by sign=(-1)^chi.
chars = {
    "trivial": [1,1,1,1],
    "chi_u": [1,-1,1,-1],
    "chi_v": [1,1,-1,-1],
    "chi_uv": [1,-1,-1,1],
}
traces = {name: sum(a*b for a,b in zip(row,L))//4 for name,row in chars.items()}
assert traces == {"trivial":1204,"chi_u":18,"chi_v":274,"chi_uv":18}
assert traces == art["H_character_fourier_inversion"]["block_rational_rosati_traces"]
assert traces["trivial"] == repair["corrected_rosati_arithmetic"]["sigma"]
assert sum(traces[k] for k in ("chi_u","chi_v","chi_uv")) == 310

# Each nontrivial block is elliptic with CM field Q(i); rational Rosati trace is twice its endomorphism degree/norm.
degrees = {k: traces[k]//2 for k in ("chi_u","chi_v","chi_uv")}
assert degrees == {"chi_u":9,"chi_v":137,"chi_uv":9}
forced = art["elliptic_prym_consequence"]["forced_degrees_by_retained_character"]
assert forced["chi_u"] == {"degree":9,"canonical_pair":"Z3={0,infinity}"}
assert forced["chi_v"] == {"degree":137,"canonical_pair":"Z2={+i,-i}"}
assert forced["chi_uv"] == {"degree":9,"canonical_pair":"Z1={+1,-1}"}
assert sorted(degrees.values()) == sorted(art["elliptic_prym_consequence"]["forced_degrees_multiset"])

# Enumerate a maximal-order Z[i] candidate superset. Any smaller CM order can only remove elements.
def gaussian_of_norm(n: int):
    lim = int(n**0.5) + 1
    return sorted((a,b) for a,b in product(range(-lim,lim+1), repeat=2) if a*a+b*b == n)

g137 = gaussian_of_norm(137)
g9 = gaussian_of_norm(9)
assert len(g137) == 8
assert len(g9) == 4
assert len(g137)*len(g9)*len(g9) == 128
sup = art["elliptic_prym_consequence"]["maximal_order_candidate_superset"]
assert sup["norm_137_count"] == len(g137)
assert sup["norm_9_count"] == len(g9)
assert sup["ordered_scalar_triple_superset_count"] == 128

# Credit firewalls.
assert art["relation_to_prior_stage32"]["numerical_274_18_18_already_encoded_by_X_deck_cross_fourier"] is True
assert art["diagnostic_verdict"]["norm_level_population_empty"] is False
assert art["diagnostic_verdict"]["O210_excluded"] is False
assert art["diagnostic_verdict"]["Q602_excluded"] is False
assert all(v is False for v in art["firewalls"].values())

print("PASS EX3-04d scratch upstairs H4 Prym/Rosati Fourier gate")
print("P intersections [15496,15568,16080,16080]")
print("retained-character Fourier traces: trivial=1204, chi_u=18, chi_v=274, chi_uv=18")
print("elliptic Prym degrees: chi_u/Z3=9, chi_v/Z2=137, chi_uv/Z1=9; maximal-order scalar superset 128")
