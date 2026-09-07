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


def image(block: set[int], g: tuple[int, ...]) -> set[int]:
    return {g[i - 1] + 1 for i in block}


def compose(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a[b[i]] for i in range(len(a)))


def order(g: tuple[int, ...]) -> int:
    identity = tuple(range(len(g)))
    x = identity
    for n in range(1, 129):
        x = compose(g, x)
        if x == identity:
            return n
    raise ValueError("order >128")


def block_perm(blocks: list[set[int]], g: tuple[int, ...]) -> tuple[int, ...]:
    out=[]
    for b in blocks:
        ib=image(b,g)
        hits=[j for j,c in enumerate(blocks) if ib==c]
        if len(hits)!=1:
            raise ValueError("block image ambiguity")
        out.append(hits[0])
    return tuple(out)


def source_signature(bits7: tuple[int,...], source_supports:list[set[int]]) -> tuple[int,...]:
    return tuple(int(len({bits7[i] for i in supp})==1) for supp in source_supports)


def main() -> None:
    marking=load_retained(ST33 / "stage32_picard_marking_retained.py", "s32_az_inventory")
    raw=[tuple(x-1 for x in g) for g in marking["aut_action"]["permutations_1based"]]
    G=close_permutation_group(marking["aut_action"]["permutations_1based"])
    if len(raw)!=9 or len(G)!=1536:
        raise ValueError(f"generator/group regression: {len(raw)}, {len(G)}")
    av=run_json(AV); zd=run_json(ZD); cell=run_json(CELL)
    zblocks=[set(b["exceptional_labels_1based"]) for b in zd["retained"]["unordered_Z1_Z2_Z3_exact_partitions"][0]["blocks"]]
    chosen=cell["support_design_survivors"][0]["candidate_indices_zero_based"]
    candidates=av["coordinate_W1_W2_W3_C_recovery"]["single_hyperplane_candidates"]
    wblocks=[set(candidates[i]["exceptional_labels_1based"]) for i in chosen]
    blocks=zblocks+wblocks
    H=[g for g in G if all(image(b,g)==b for b in blocks)]
    if len(H)!=64:
        raise ValueError("kernel regression")

    pairings=[[(0,3),(1,2)],[(0,2),(1,3)],[(0,1),(2,3)]]
    cells=[]; supports=[]
    for zi,pairs in enumerate(pairings):
        for wi,wj in pairs:
            cells.append(zblocks[zi]&wblocks[wi]&wblocks[wj])
            zero={zi,3+wi,3+wj}
            supports.append(set(range(7))-zero)
    def rsig(g):
        return tuple(int(all(g[p-1]+1==p for p in c)) for c in cells)

    # Exact AW C2^6 labeling of H, in coordinate order
    # [b1,b2,b3,a1,a2,a3,c], modulo global sign and represented with c-bit=0.
    flips=[]
    for k in range(7):
        bits7=(tuple(1 if i==k else 0 for i in range(6))+(0,)) if k<6 else (1,1,1,1,1,1,0)
        sig=source_signature(bits7,supports)
        hits=[h for h in H if rsig(h)==sig]
        if len(hits)!=1:
            raise ValueError(f"flip recovery {k}: {len(hits)}")
        flips.append(hits[0])
    identity=tuple(range(140))
    h_to_bits={}
    for bits6 in itertools.product((0,1),repeat=6):
        h=identity
        for k,bit in enumerate(bits6):
            if bit:
                h=compose(flips[k],h)
        h_to_bits[h]=bits6
    if len(h_to_bits)!=64:
        raise ValueError("H bit labeling regression")

    records=[]
    for j,g in enumerate(raw):
        wp=block_perm(wblocks,g); zp=block_perm(zblocks,g)
        rec={
            "generator_index_zero_based":j,
            "order":order(g),
            "WC_permutation_zero_based":list(wp),
            "Z_permutation_zero_based":list(zp),
            "in_sign_kernel":g in h_to_bits,
            "fixed_exceptional_count":sum(g[p-1]+1==p for p in range(93,141)),
        }
        if g in h_to_bits:
            bits=h_to_bits[g]
            rec["kernel_bits_b1_b2_b3_a1_a2_a3_mod_global_c0"]=list(bits)
            rec["semantic_single_sign_flip"]=(sum(bits)==1)
            rec["semantic_single_sign_coordinate"]=(list(bits).index(1) if sum(bits)==1 else None)
        records.append(rec)

    print(json.dumps({
        "mode":"SCRATCH_POST1648AZ_RETAINED_GENERATOR_INVENTORY",
        "retained_generator_count":len(raw),
        "retained_group_order":len(G),
        "sign_kernel_order":len(H),
        "coordinate_order_for_kernel_bits":["b1","b2","b3","a1","a2","a3"],
        "projective_gauge":"c_sign_bit_is_zero; global sign quotiented",
        "records":records,
        "firewalls":{
            "scratch_only":True,
            "raw_generator_semantic_names_assumed":False,
            "full_source_to_retained_group_isomorphism_verified":False,
            "explicit_48_node_bijection_obtained":False,
            "v6_carrier_excluded":False,
            "Q602_excluded":False,
            "O210_excluded":False,
            "O212_plus_advance_allowed":False,
        }
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
