#!/usr/bin/env python3
"""Diagnose the exact V4-compatible A2_02 component transition selector for V91C1D."""
from __future__ import annotations
import hashlib, itertools, json, runpy
from pathlib import Path

HERE = Path(__file__).resolve().parent
S33 = HERE.parent
V91C1A = HERE / "e3-v91c1a-a2-02-literal-boundary-seed-localization.json"
V91C1C = HERE / "e3-v91c1c-a2-02-strict-transform-prime-refinement.json"
SCALAR = HERE / "boundary-function-scalar-descent-certificate.json"
E_VERIFY = S33 / "33-11e" / "verify_stage33_11e_prime_galois_transport.py"
LOCKS = {
    V91C1A: "7f81ce5da7a4880cf0ffa048ab335fe2db9a643158d26144f45d0de22604b403",
    V91C1C: "ac46916c7e46d3f5b6ac67125b4622d4e4aaa028509879d45811f0e4ec8f28f6",
    SCALAR: "e7d0d003c71271822e51b626acf21575e0c490035bdf3ef802feb3d7c767e36b",
}


def csha(o): return hashlib.sha256(json.dumps(o, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
def load(path):
    o=json.loads(path.read_text(encoding="utf-8")); b=dict(o); h=b.pop("canonical_sha256")
    assert h==LOCKS[path]==csha(b), path; return o

def valid_maps(components, candidates):
    out=[]
    for perm in itertools.permutations(components):
        m=dict(zip(components, perm))
        if any(m[s] not in candidates[s] for s in components): continue
        if any(m[m[s]] != s for s in components): continue
        out.append(m)
    return out

def key(m, components): return tuple(m[s] for s in components)
def commute(a,b,components): return all(a[b[s]] == b[a[s]] for s in components)

v1a=load(V91C1A); v1c=load(V91C1C); scalar=load(SCALAR)
components=list(v1a["literal_package_record"]["component_ids_in_source_order"])
assert components==["EXC_003","EXC_004","EXC_011","EXC_012","SIDE_002","SIDE_004","SIDE_006","SIDE_008"]
assert v1c["exact_consequence"]["prime_level_cc_ct_transport_complete"] is True
srow=next(r for r in scalar["generator_records"] if r["source_direction"]=="A2_02")
assert srow["component_count"]==8 and srow["action_scalar_record_count"]==16
assert srow["action_scalar_records_sha256"]=="96ffaf2a0918193f8bd2fbb422a20a26557aa1747b57f8704b47d49251bd1c46"
assert srow["all_candidate_scalar_ratios_one"] is True
assert scalar["exact_conclusion"]["all_package_divisor_vectors_match_audited_stage33_11e"] is True

ens=runpy.run_path(str(E_VERIFY)); ecert=ens["build_certificate"]()
assert ecert["canonical_sha256"]=="1f76cec8b74a5d5122e3d83057472bfdf9447ed0817474a8b3405078b770c426"
erec=next(r for r in ecert["generator_records"] if r["source_direction"]=="A2_02")
assert erec["component_count"]==8 and erec["exact_consequence"]=="ZERO_EXACT_PRIME_LEVEL_CC_CT"
for g in ("cc","ct"):
    assert erec["prime_level_galois_differences"][g]=={"status":"ZERO_EXACT_PRIME_LEVEL","nonzero_prime_coefficients":0}

candidates={g:{c:set() for c in components} for g in ("cc","ct")}
for row in erec["action_checks"]:
    g=row["action"]; src=row["source_component"]
    if g in candidates and src in candidates[g]:
        candidates[g][src].update(row["matching_target_components"])
for g in candidates:
    assert all(candidates[g][c] for c in components)

valid={g:valid_maps(components,candidates[g]) for g in ("cc","ct")}
assert valid["cc"] and valid["ct"]
pairs=[]
for cc in valid["cc"]:
    for ct in valid["ct"]:
        if commute(cc,ct,components): pairs.append((cc,ct))
assert pairs
pairs.sort(key=lambda z:(key(z[0],components),key(z[1],components)))
cc,ct=pairs[0]
assert all(cc[cc[c]]==c and ct[ct[c]]==c and cc[ct[c]]==ct[cc[c]] for c in components)
out={
    "success":True,
    "marker":"V91C1D_A2_02_V4_TRANSITION_SELECTOR_PASS",
    "components":components,
    "prime_level_candidate_targets":{g:{c:sorted(candidates[g][c]) for c in components} for g in ("cc","ct")},
    "valid_cc_involution_count":len(valid["cc"]),
    "valid_ct_involution_count":len(valid["ct"]),
    "commuting_v4_pair_count":len(pairs),
    "canonical_cc_map":cc,
    "canonical_ct_map":ct,
    "all_selected_function_scalar_units_one":True,
    "prime_level_package_difference_cc":"ZERO_EXACT_PRIME_LEVEL",
    "prime_level_package_difference_ct":"ZERO_EXACT_PRIME_LEVEL",
}
print(json.dumps(out,sort_keys=True))
