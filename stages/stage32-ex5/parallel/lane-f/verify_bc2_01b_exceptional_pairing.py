#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import itertools
import json
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[4]
LANE_DIR = Path(__file__).resolve().parent
RESULT = LANE_DIR / "bc2-01b-exceptional-pairing-canonical.json"
PRODUCTION = ROOT / "stages/stage32/residual-32-01-production"
RETAINED = ROOT / "stages/stage33/33-07/picard_base_rows_retained.py"
MARKING = ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py"

if str(PRODUCTION) not in sys.path:
    sys.path.insert(0, str(PRODUCTION))

from hperp_integral_adapter import HperpIntegralPairingAdapter, RETAINED_BASIS_KNOWN_LABELS_1BASED  # noqa: E402

I = sp.I
SQRT2 = sp.sqrt(2)
SIGNS = (1, -1)
EXPECTED_SELECTED_NORMAL_LABELS = [1,33,12,16,7,90,87,92,51,40,77,44,20,55,19,56,73,79,75,24,26,52,18,11,3,6]


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    value = mod.load()
    if not isinstance(value, dict):
        raise ValueError(f"{path} load() did not return dict")
    return value


def magma_sign_tuples(n: int):
    # Magma repeated iteration uses the first range as the innermost loop.
    for rev in itertools.product(SIGNS, repeat=n):
        yield tuple(reversed(rev))


def make_curves():
    curves = []
    add = curves.append
    for e1,e2,e3 in magma_sign_tuples(3): add(("C1_A1",(e1,e2,e3),lambda p,e1=e1,e2=e2,e3=e3:[p[0],p[1]+e1*p[5],p[2]+e2*p[4],p[3]+e3*p[6]]))
    for e1,e2,e3 in magma_sign_tuples(3): add(("C1_A2",(e1,e2,e3),lambda p,e1=e1,e2=e2,e3=e3:[p[1],p[2]+e1*p[3],p[0]+e2*p[5],p[4]+e3*p[6]]))
    for e1,e2,e3 in magma_sign_tuples(3): add(("C1_A3",(e1,e2,e3),lambda p,e1=e1,e2=e2,e3=e3:[p[2],p[0]+e1*p[4],p[1]+e2*p[3],p[5]+e3*p[6]]))
    for e3,e2,e1 in magma_sign_tuples(3): add(("C1_C",(e3,e2,e1),lambda p,e1=e1,e2=e2,e3=e3:[p[6],I*p[0]+e1*p[3],I*p[1]+e2*p[4],I*p[2]+e3*p[5]]))
    for e1,e2 in magma_sign_tuples(2): add(("C2_B1",(e1,e2),lambda p,e1=e1,e2=e2:[p[3],I*p[1]+e1*p[2],p[0]+e2*p[6]]))
    for e1,e2 in magma_sign_tuples(2): add(("C2_B2",(e1,e2),lambda p,e1=e1,e2=e2:[p[4],I*p[2]+e1*p[0],p[1]+e2*p[6]]))
    for e1,e2 in magma_sign_tuples(2): add(("C2_B3",(e1,e2),lambda p,e1=e1,e2=e2:[p[5],I*p[0]+e1*p[1],p[2]+e2*p[6]]))
    for e1,e2,e3 in magma_sign_tuples(3): add(("C3_A12",(e1,e2,e3),lambda p,e1=e1,e2=e2,e3=e3:[p[0]+e1*p[1],SQRT2*p[0]+e2*p[5],p[3]+e3*p[4]]))
    for e1,e2,e3 in magma_sign_tuples(3): add(("C3_A23",(e1,e2,e3),lambda p,e1=e1,e2=e2,e3=e3:[p[1]+e1*p[2],SQRT2*p[1]+e2*p[3],p[4]+e3*p[5]]))
    for e1,e2,e3 in magma_sign_tuples(3): add(("C3_A31",(e1,e2,e3),lambda p,e1=e1,e2=e2,e3=e3:[p[2]+e1*p[0],SQRT2*p[2]+e2*p[4],p[5]+e3*p[3]]))
    for e3,e2,e1 in magma_sign_tuples(3): add(("C3_I1",(e3,e2,e1),lambda p,e1=e1,e2=e2,e3=e3:[I*p[0]+e1*p[6],I*p[4]+e2*p[5],I*SQRT2*p[0]+e3*p[3]]))
    for e3,e2,e1 in magma_sign_tuples(3): add(("C3_I2",(e3,e2,e1),lambda p,e1=e1,e2=e2,e3=e3:[I*p[1]+e1*p[6],I*p[5]+e2*p[3],I*SQRT2*p[1]+e3*p[4]]))
    for e3,e2,e1 in magma_sign_tuples(3): add(("C3_I3",(e3,e2,e1),lambda p,e1=e1,e2=e2,e3=e3:[I*p[2]+e1*p[6],I*p[3]+e2*p[4],I*SQRT2*p[2]+e3*p[5]]))
    if len(curves) != 92: raise ValueError(f"curve count regression: {len(curves)}")
    return curves


def source_nodes():
    out=[]
    for a,b,c in itertools.product((-1,1),repeat=3): out.append((f"AXIS_X1:a={a},b={b},c={c}",(1,0,0,0,a,b,c)))
    for a,b,c in itertools.product((-1,1),repeat=3): out.append((f"AXIS_X2:a={a},b={b},c={c}",(0,1,0,a,0,b,c)))
    for a,b,c in itertools.product((-1,1),repeat=3): out.append((f"AXIS_X3:a={a},b={b},c={c}",(0,0,1,a,b,0,c)))
    for s,a,b in itertools.product((-1,1),repeat=3): out.append((f"Y1_Z_ZERO:s={s},a={a},b={b}",(0,1,s*I,0,a*I,b,0)))
    for s,a,b in itertools.product((-1,1),repeat=3): out.append((f"Y2_Z_ZERO:s={s},a={a},b={b}",(1,0,s*I,a*I,0,b,0)))
    for s,a,b in itertools.product((-1,1),repeat=3): out.append((f"Y3_Z_ZERO:s={s},a={a},b={b}",(1,s*I,0,a*I,b,0,0)))
    if len(out)!=48 or len({tuple(p) for _,p in out})!=48: raise ValueError("source-node count/distinctness regression")
    return out


def contains(curve, point) -> int:
    return int(all(sp.simplify(v)==0 for v in curve[2](point)))


def signature(curves, point, labels):
    return tuple(contains(curves[j-1], point) for j in labels)


def coord_text(v) -> str:
    v=sp.simplify(v)
    if v==0:return "0"
    if v==1:return "1"
    if v==-1:return "-1"
    if v==I:return "i"
    if v==-I:return "-i"
    raise ValueError(f"unexpected node coordinate {v}")


def solve(pairing, normal_positions, normal_labels, candidates, slot_order=None):
    if slot_order is None: slot_order=list(range(48))
    by_sig={}
    for label,point in candidates:
        sig=signature(CURVES,point,normal_labels)
        if sig in by_sig: raise ValueError(f"candidate signature collision: {by_sig[sig][0]} / {label}")
        by_sig[sig]=(label,point)
    if len(by_sig)!=48: raise ValueError(f"candidate signature count regression: {len(by_sig)}")
    result={}
    for k in slot_order:
        sig=tuple(int(pairing[92+k,pos]) for pos in normal_positions)
        if any(v not in (0,1) for v in sig): raise ValueError(f"non-01 exceptional/normal pairing at runtime slot {k}: {sig}")
        if sig not in by_sig: raise ValueError(f"unmatched Picard incidence signature at runtime slot {k}: {sig}")
        label,point=by_sig[sig]
        result[k]={"factor_index_0based":92+k,"runtime_exceptional_index_0based":k,"all140_label_1based":93+k,"node_label":label,"coords":[coord_text(v) for v in point],"selected_support_curve_labels_1based":[j for j,bit in zip(normal_labels,sig) if bit]}
    if len(result)!=48 or len({r["node_label"] for r in result.values()})!=48: raise ValueError("runtime-slot matching is not a 48/48 bijection")
    return result


CURVES=make_curves()


def main() -> None:
    artifact=json.loads(RESULT.read_text())
    bundle=load_retained(RETAINED,"s32ex5f_picard_bundle")
    marking=load_retained(MARKING,"s32ex5f_picard_marking")
    adapter=HperpIntegralPairingAdapter.from_retained(marking,bundle)
    pairing=adapter.pairing_matrix
    if pairing.shape!=(140,64): raise ValueError(f"pairing shape regression: {pairing.shape}")
    normal_positions=[pos for pos,label in enumerate(RETAINED_BASIS_KNOWN_LABELS_1BASED) if label<=92]
    normal_labels=[RETAINED_BASIS_KNOWN_LABELS_1BASED[pos] for pos in normal_positions]
    if normal_labels!=EXPECTED_SELECTED_NORMAL_LABELS: raise ValueError(f"selected normal-label regression: {normal_labels}")
    if len(normal_labels)!=26 or len(set(normal_labels))!=26: raise ValueError("selected normal-label count/distinctness regression")
    candidates=source_nodes()
    all92_sigs=[signature(CURVES,p,range(1,93)) for _,p in candidates]
    if len(set(all92_sigs))!=48: raise ValueError("all92 source-node incidence signatures are not unique")
    if {sum(sig) for sig in all92_sigs}!={10}: raise ValueError("source-node all92 incidence degree regression")
    selected_sigs=[signature(CURVES,p,normal_labels) for _,p in candidates]
    if len(set(selected_sigs))!=48: raise ValueError("selected26 source-node incidence signatures are not unique")
    natural=solve(pairing,normal_positions,normal_labels,candidates)
    reverse_candidates=solve(pairing,normal_positions,normal_labels,list(reversed(candidates)),list(reversed(range(48))))
    rotated=candidates[17:]+candidates[:17]
    rotated_slots=list(range(13,48))+list(range(13))
    rotated_result=solve(pairing,normal_positions,normal_labels,rotated,rotated_slots)
    if natural!=reverse_candidates or natural!=rotated_result: raise ValueError("matching changed under candidate/slot traversal permutation")
    scale_tests=(sp.Integer(2),-sp.Integer(3),I)
    for _,p in candidates:
        base=signature(CURVES,p,normal_labels)
        for scalar in scale_tests:
            if signature(CURVES,tuple(scalar*x for x in p),normal_labels)!=base: raise ValueError("projective-scale invariance regression")
    got_rows=[natural[k] for k in range(48)]
    if got_rows!=artifact["mapping"]: raise ValueError("retained canonical mapping does not match rederived Picard signature map")
    summary={"status":"PASS","runtime_slots":48,"candidate_nodes":48,"selected_normal_curve_labels":normal_labels,"selected_signature_dimension":26,"selected_signature_unique_count":len(set(selected_sigs)),"all92_signature_unique_count":len(set(all92_sigs)),"all92_incidence_degree_each":10,"collision_count":0,"bijection_count":len({r["node_label"] for r in got_rows}),"permutation_invariance_checks":3,"projective_scale_checks":48*len(scale_tests),"mapping_sha256":csha(got_rows),"pairing_adapter_certificate_sha256":adapter.certificate["canonical_sha256_without_this_field"]}
    for key,value in artifact["replay_expectations"].items():
        if summary.get(key)!=value: raise ValueError(f"replay expectation regression for {key}: {summary.get(key)!r} != {value!r}")
    print(json.dumps(summary,sort_keys=True,separators=(",",":")))


if __name__=="__main__":
    main()
