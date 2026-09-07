#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import itertools
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ST33 = ROOT / "stages" / "stage33" / "33-07"
sys.path.insert(0, str(HERE))
from pairing_prefix_engine import close_permutation_group  # noqa: E402

AV = HERE / "diagnose_stage32_post1648av_canonical_coordinate_hyperplane_recovery.py"
ZD = HERE / "diagnose_stage32_post1648aw_boundary_Z_hyperplane_blocks.py"
CELL = HERE / "diagnose_stage32_post1648aw_Z_Wpair_support_cells.py"
V6 = ROOT / "stages" / "stage32" / "32-21" / "post1473-v6-witness-body-recovered.json"

UNITS = (0j, 1+0j, -1+0j, 1j, -1j)


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def run_json(path: Path) -> dict:
    p = subprocess.run([sys.executable, "-B", str(path)], cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(p.stdout)


def canon(v: tuple[complex, ...]) -> tuple[complex, ...]:
    for x in v:
        if x != 0:
            inv = 1 / x
            out = []
            for y in v:
                z = y * inv
                re = int(round(z.real)); im = int(round(z.imag))
                out.append(complex(re, im))
            return tuple(out)
    raise ValueError("zero projective vector")


def eqs(v: tuple[complex, ...]) -> bool:
    a1,a2,a3,b1,b2,b3,c=v
    return (
        a1*a1+b1*b1 == c*c and
        a2*a2+b2*b2 == c*c and
        a3*a3+b3*b3 == c*c and
        a1*a1+a2*a2+a3*a3 == c*c
    )


def source_nodes() -> list[tuple[complex, ...]]:
    sing_triples = [
        {0,3,6}, {1,4,6}, {2,5,6},
        {1,2,3}, {0,2,4}, {0,1,5},
    ]
    out=set()
    for v in itertools.product(UNITS, repeat=7):
        if all(x == 0 for x in v) or not eqs(v):
            continue
        zeros={i for i,x in enumerate(v) if x == 0}
        if any(t <= zeros for t in sing_triples):
            out.add(canon(v))
    key=lambda v: tuple((int(z.real),int(z.imag)) for z in v)
    return sorted(out,key=key)


def compose(a: tuple[int,...], b: tuple[int,...]) -> tuple[int,...]:
    return tuple(a[b[i]] for i in range(len(a)))


def source_map(v: tuple[complex,...], kind: str) -> tuple[complex,...]:
    a1,a2,a3,b1,b2,b3,c=v
    if kind == "t12":
        w=(a2,a1,a3,b2,b1,b3,c)
    elif kind == "t13":
        w=(a3,a2,a1,b3,b2,b1,c)
    elif kind == "sigma":
        w=(a1,a2,-1j*c,-1j*b2,1j*b1,b3,1j*a3)
    elif kind.startswith("sign_"):
        coord=int(kind.split("_")[1])
        q=list(v); q[coord] = -q[coord]; w=tuple(q)
    else:
        raise ValueError(kind)
    return canon(w)


def perm_from_map(nodes, kind):
    idx={v:i for i,v in enumerate(nodes)}
    return tuple(idx[source_map(v,kind)] for v in nodes)


def perm_conjugate(a,b):
    # a b a, used only for involutive a.
    return compose(a, compose(b,a))


def image(block:set[int], g:tuple[int,...]) -> set[int]:
    return {g[i-1]+1 for i in block}


def block_perm(blocks:list[set[int]], g:tuple[int,...]) -> tuple[int,...]:
    out=[]
    for b in blocks:
        ib=image(b,g)
        hits=[j for j,c in enumerate(blocks) if ib==c]
        if len(hits)!=1:
            raise ValueError("retained block image ambiguity")
        out.append(hits[0])
    return tuple(out)


def fmt(z:complex) -> str:
    a=int(round(z.real)); b=int(round(z.imag))
    if a==0 and b==0: return "0"
    if a==1 and b==0: return "1"
    if a==-1 and b==0: return "-1"
    if a==0 and b==1: return "i"
    if a==0 and b==-1: return "-i"
    return f"{a}{b:+d}i"


def main() -> None:
    marking=load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_az_full")
    raw=[tuple(x-1 for x in g) for g in marking["aut_action"]["permutations_1based"]]
    G=close_permutation_group(marking["aut_action"]["permutations_1based"])
    if len(raw)!=9 or len(G)!=1536:
        raise ValueError("retained generator/group regression")

    av=run_json(AV); zd=run_json(ZD); cell=run_json(CELL)
    zblocks=[set(b["exceptional_labels_1based"]) for b in zd["retained"]["unordered_Z1_Z2_Z3_exact_partitions"][0]["blocks"]]
    chosen=cell["support_design_survivors"][0]["candidate_indices_zero_based"]
    candidates=av["coordinate_W1_W2_W3_C_recovery"]["single_hyperplane_candidates"]
    wblocks=[set(candidates[i]["exceptional_labels_1based"]) for i in chosen]

    # Lock the exact semantic quotient patterns of the three retained non-sign generators.
    expected_q=[
        ((1,0,2,3),(1,0,2)),  # t12
        ((2,1,0,3),(2,1,0)),  # t13
        ((3,1,2,0),(0,2,1)),  # t13 sigma t13
    ]
    actual_q=[(block_perm(wblocks,raw[j]),block_perm(zblocks,raw[j])) for j in range(3)]
    if actual_q != expected_q:
        raise ValueError(f"raw generator semantic quotient regression: {actual_q}")

    nodes=source_nodes()
    if len(nodes)!=48:
        raise ValueError(f"source node enumeration regression: {len(nodes)}")
    idx={v:i for i,v in enumerate(nodes)}
    t12=perm_from_map(nodes,"t12")
    t13=perm_from_map(nodes,"t13")
    sigma=perm_from_map(nodes,"sigma")
    sigma13=perm_conjugate(t13,sigma)
    # retained raw signs are a1,a2,a3,b1,b2,b3 respectively.
    src=[t12,t13,sigma13]
    for coord in (0,1,2,3,4,5):
        src.append(perm_from_map(nodes,f"sign_{coord}"))
    SG=close_permutation_group([tuple(x+1 for x in g) for g in src])
    if len(SG)!=1536:
        raise ValueError(f"source generated node-action group regression: {len(SG)}")

    # Exact source hyperplane blocks in semantic order b1,b2,b3 and a1,a2,a3,c.
    sz=[{i for i,v in enumerate(nodes) if v[3+j]==0} for j in range(3)]
    sw=[{i for i,v in enumerate(nodes) if v[k]==0} for k in (0,1,2,6)]
    if sorted(map(len,sz)) != [16,16,16] or sorted(map(len,sw)) != [24,24,24,24]:
        raise ValueError("source hyperplane block size regression")
    source_anchor=sz[0] & sw[0] & sw[3]
    retained_anchor=zblocks[0] & wblocks[0] & wblocks[3]
    if len(source_anchor)!=8 or len(retained_anchor)!=8:
        raise ValueError("eight-node anchor regression")

    # Solve all generator-by-generator equivariant bijections from the source anchor cell.
    solutions=[]
    for s0 in sorted(source_anchor):
        for e0 in sorted(retained_anchor):
            f={s0:e0}; inv={e0:s0}; queue=[s0]; ok=True
            while queue and ok:
                s=queue.pop()
                e=f[s]
                for j in range(9):
                    s2=src[j][s]
                    e2=raw[j][e-1]+1
                    if s2 in f and f[s2]!=e2:
                        ok=False; break
                    if e2 in inv and inv[e2]!=s2:
                        ok=False; break
                    if s2 not in f:
                        f[s2]=e2; inv[e2]=s2; queue.append(s2)
            if ok and len(f)==48 and set(f.values())==set(range(93,141)):
                solutions.append(f)

    if len(solutions)!=1:
        raise ValueError(f"expected unique full equivariant bijection, got {len(solutions)}")
    f=solutions[0]

    # Check semantic block membership for all 48 points, independently of generator propagation.
    for s,e in f.items():
        for j in range(3):
            if ((s in sz[j]) != (e in zblocks[j])):
                raise ValueError("Z/b semantic block mismatch")
        for j in range(4):
            if ((s in sw[j]) != (e in wblocks[j])):
                raise ValueError("W/C semantic block mismatch")

    # Check all nine generator squares/action intertwining explicitly on all 48 nodes.
    intertwining_checks=0
    for j in range(9):
        for s,e in f.items():
            if f[src[j][s]] != raw[j][e-1]+1:
                raise ValueError("generator intertwining regression")
            intertwining_checks += 1

    v6=json.loads(V6.read_text())
    masses=v6["exceptional_intersections"]
    if len(masses)!=48 or sum(masses)!=266:
        raise ValueError("V6 exceptional vector regression")

    records=[]
    for s in sorted(f):
        e=f[s]
        v=nodes[s]
        zeros=[name for name,z in zip(("a1","a2","a3","b1","b2","b3","c"),v) if z==0]
        records.append({
            "source_node_index_zero_based":s,
            "source_projective_coordinates_a1_a2_a3_b1_b2_b3_c":[fmt(z) for z in v],
            "source_zero_coordinates":zeros,
            "retained_exceptional_label_1based":e,
            "v6_exceptional_intersection_multiplicity":masses[e-93],
        })

    print(json.dumps({
        "mode":"SCRATCH_POST1648AZ_FULL_48NODE_EQUIVARIANT_BIJECTION",
        "source_node_count":len(nodes),
        "source_node_action_group_order":len(SG),
        "retained_group_order":len(G),
        "source_anchor_cell_size":len(source_anchor),
        "retained_anchor_cell_size":len(retained_anchor),
        "basepair_trials":len(source_anchor)*len(retained_anchor),
        "full_equivariant_bijection_solution_count":len(solutions),
        "generator_correspondence":[
            "retained_g0 = source_t12",
            "retained_g1 = source_t13",
            "retained_g2 = source_t13_sigma_t13",
            "retained_g3 = source_sign_a1",
            "retained_g4 = source_sign_a2",
            "retained_g5 = source_sign_a3",
            "retained_g6 = source_sign_b1",
            "retained_g7 = source_sign_b2",
            "retained_g8 = source_sign_b3",
        ],
        "generator_intertwining_checks":intertwining_checks,
        "semantic_hyperplane_membership_checks":48*7,
        "explicit_48_node_bijection_obtained":True,
        "v6_exceptional_mass_total_under_source_node_labels":sum(r["v6_exceptional_intersection_multiplicity"] for r in records),
        "records":records,
        "next_exact_route":"USE_THE_EXPLICIT_SOURCE_NODE_LABELS_TO_TEST_WETHER_THE_V6_MULTIPLICITY_VECTOR_SATISFIES_ADDITIONAL_SOURCE_GEOMETRIC_OR_LOCAL_TANGENT_CONSTRAINTS_BEYOND_HYPERPLANE_MASS",
        "firewalls":{
            "scratch_only":True,
            "full_source_to_retained_48node_action_adapter_obtained":True,
            "picard_curve_level_source_adapter_beyond_exceptional_nodes_obtained":False,
            "v6_carrier_excluded":False,
            "Q602_excluded":False,
            "O210_excluded":False,
            "O212_plus_advance_allowed":False,
        }
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
