#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp

import materialize_e3_v91c1x_r5b3b3b_classify_20_novel_carriers_and_unify_27 as b

HERE = Path(__file__).resolve().parent
B3B2_PATH = HERE / "e3-v91c1x-r5b3b2-a2-02-formal-tame-symbol-hidden-carrier-inventory.json"
B3B3B_PATH = HERE / "e3-v91c1x-r5b3b3b-classify-20-novel-carriers-and-unify-27.json"
C1_PATH = HERE / "e3-v91c1x-r5b3b3c1-offboundary-norm-factorization.json"
B3B2_SHA = "52429d1197e1383daef8c25acdb1224822d7f5c22ecb7046c8b47766438a547e"
B3B3B_SHA = "7f52f0988cb82983afc0759272e2420e73944b4258940aeffc8a9923816c4a7d"
C1_SHA = "5c092fcec6720d0097d6e7509ce37b1506d7a099015a1a6a004250513d0f29f3"
AUTHORITY = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
CANDIDATE = "V91C1X_R5B3B3C1_FACTOR_ONLY_OFFBOUNDARY_FULL_SIGN_NORMS"
NEXT_LEAF = "V91C1X_R5B3B3C2_RESOLVED_SURFACE_PRIME_DECOMPOSITION_AND_COMBINED_TAME_RESIDUES_OVER_C1_FACTORS"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def locked_json(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    declared = body.pop("canonical_sha256", None)
    actual = csha(body)
    if declared != expected or actual != expected:
        raise SystemExit(
            f"canonical lock moved: {path.name} declared={declared} actual={actual} expected={expected}"
        )
    return obj


def factor_key(row):
    return (
        int(row["factor_total_degree"]),
        int(row["multiplicity"]),
        row["normalized_factor_sha256"],
        int(row["normalized_factor_term_count"]),
    )


def singular_factor(poly: sp.Poly, cid: str):
    expr = sp.sstr(poly.as_expr()).replace("**", "^").replace("I", "i")
    script = (
        "ring r=(0,i),(a1,a2,a3),dp;\n"
        "minpoly=i2+1;\n"
        f"poly f={expr};\n"
        "list L=factorize(f);\n"
        "ideal F=L[1];\n"
        "intvec M=L[2];\n"
        "int n=size(F);\n"
        'print("COUNT|"+string(n));\n'
        "for (int k=1; k<=n; k=k+1) {\n"
        '  print("MULT|"+string(M[k]));\n'
        '  print("FACTOR|"+string(F[k]));\n'
        "}\n"
    )
    path = None
    try:
        with tempfile.NamedTemporaryFile("w", suffix=".sing", delete=False, encoding="utf-8") as fh:
            fh.write(script)
            path = fh.name
        proc = subprocess.run(["Singular", "-q", path], text=True, capture_output=True, check=True)
    except FileNotFoundError as exc:
        raise SystemExit("Singular executable not found") from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(f"Singular failed for {cid}: {exc.stderr}") from exc
    finally:
        if path is not None:
            Path(path).unlink(missing_ok=True)

    lines = [x.strip() for x in proc.stdout.splitlines() if x.strip()]
    count_rows = [x for x in lines if x.startswith("COUNT|")]
    mults = [int(x.split("|", 1)[1]) for x in lines if x.startswith("MULT|")]
    raws = [x.split("|", 1)[1] for x in lines if x.startswith("FACTOR|")]
    if len(count_rows) != 1:
        raise SystemExit(f"Singular COUNT parse failed for {cid}")
    count = int(count_rows[0].split("|", 1)[1])
    if len(mults) != count or len(raws) != count:
        raise SystemExit(f"Singular factor/multiplicity parse failed for {cid}")

    local = {"a1": b.BASE[0], "a2": b.BASE[1], "a3": b.BASE[2], "i": sp.I}
    rebuilt = sp.Poly(1, *b.BASE, extension=sp.I)
    factors = []
    scalar_count = 0
    for raw, mult in zip(raws, mults):
        fac = sp.Poly(sp.sympify(raw.replace("^", "**"), locals=local), *b.BASE, extension=sp.I)
        rebuilt *= fac**mult
        if fac.total_degree() == 0:
            scalar_count += 1
            continue
        normalized = b.normalize_norm(fac)
        factors.append(
            {
                "factor_total_degree": int(fac.total_degree()),
                "multiplicity": int(mult),
                "normalized_factor_sha256": csha(normalized),
                "normalized_factor_term_count": len(normalized),
            }
        )
    if sp.Poly(rebuilt - poly, *b.BASE, extension=sp.I) != sp.Poly(0, *b.BASE, extension=sp.I):
        raise SystemExit(f"exact polynomial reconstruction failed for {cid}")
    degree_multiset = sorted(
        d for row in factors for d in [row["factor_total_degree"]] * row["multiplicity"]
    )
    if sum(degree_multiset) != 16:
        raise SystemExit(f"factor degree sum moved for {cid}: {degree_multiset}")
    return {
        "factor_count_distinct": len(factors),
        "factor_count_with_multiplicity": sum(x["multiplicity"] for x in factors),
        "squarefree_factorization": all(x["multiplicity"] == 1 for x in factors),
        "factor_degree_multiset": degree_multiset,
        "singular_scalar_factor_count": scalar_count,
        "factors": factors,
    }


def compare_factorization(got, claimed, label):
    for key in (
        "factor_count_distinct",
        "factor_count_with_multiplicity",
        "squarefree_factorization",
        "factor_degree_multiset",
        "singular_scalar_factor_count",
    ):
        if got[key] != claimed[key]:
            raise SystemExit(f"{label}: {key} mismatch got={got[key]} claimed={claimed[key]}")
    if sorted(map(factor_key, got["factors"])) != sorted(map(factor_key, claimed["factors"])):
        raise SystemExit(f"{label}: irreducible factor metadata mismatch")


def main():
    b3b2 = locked_json(B3B2_PATH, B3B2_SHA)
    b3b3b = locked_json(B3B3B_PATH, B3B3B_SHA)
    c1 = locked_json(C1_PATH, C1_SHA)

    if c1["candidate"] != CANDIDATE:
        raise SystemExit("C1 candidate moved")
    if c1["entry"]["authority"] != AUTHORITY or c1["entry"]["stage33_progress"] != "6/11":
        raise SystemExit("C1 authority/progress firewall moved")
    if c1["next_exact_leaf"] != NEXT_LEAF:
        raise SystemExit("C1 next leaf moved")
    if c1["source_locks"]["r5b3b2_formal_symbol_carrier_inventory_sha256"] != B3B2_SHA:
        raise SystemExit("C1 B3B2 source lock mismatch")
    if c1["source_locks"]["r5b3b3b_unified_boundary_classification_sha256"] != B3B3B_SHA:
        raise SystemExit("C1 B3B3B source lock mismatch")

    firewall = c1["credit_firewall"]
    if not firewall or any(value is not False for value in firewall.values()):
        raise SystemExit(f"C1 credit firewall opened: {firewall}")
    status = c1["construction_status"]
    forbidden_true = (
        "all_offboundary_carrier_hyperplane_sections_prime_decomposed_on_resolved_surface",
        "combined_tame_residue_squareclasses_audited",
        "offboundary_codimension_one_residue_cancellation_verified",
        "single_global_a2_02_kummer_or_brauer_representative_materialized",
        "literal_mu2_2_cocycle_materialized",
        "same_representative_swap23_transport_materialized",
        "triple_overlap_action_difference_identity_verified",
    )
    if any(status[key] for key in forbidden_true):
        raise SystemExit("C1 construction status overclaims post-factorization credit")
    if status["offboundary_norm_irreducible_factorization_materialized"] is not True:
        raise SystemExit("C1 factorization materialization flag missing")

    rows = {r["carrier_id"]: r for r in b3b2["finite_linear_carrier_inventory"]["carrier_rows"]}
    off_ids = list(b3b3b["unified_27_classification"]["off_boundary_carrier_ids"])
    if len(off_ids) != 23 or len(set(off_ids)) != 23:
        raise SystemExit(f"off-boundary set moved: {len(off_ids)}")
    if any(cid not in rows for cid in off_ids):
        raise SystemExit("off-boundary carrier escaped B3B2 inventory")

    groups = defaultdict(list)
    polys = {}
    normalized_by_sha = {}
    for cid in off_ids:
        poly = b.full_sign_norm_poly(rows[cid]["normalized_coefficients_Qi"])
        if poly.total_degree() != 16:
            raise SystemExit(f"full sign norm degree moved: {cid}")
        normalized = b.normalize_norm(poly)
        sha = csha(normalized)
        if sha in normalized_by_sha and normalized_by_sha[sha] != normalized:
            raise SystemExit(f"normalized norm hash collision: {sha}")
        normalized_by_sha.setdefault(sha, normalized)
        groups[sha].append(cid)
        polys[cid] = poly
    if len(groups) != 19:
        raise SystemExit(f"unique normalized norm count moved: {len(groups)}")

    ex = c1["exact_factorization"]
    if ex["off_boundary_carrier_count"] != 23:
        raise SystemExit("certificate off-boundary count mismatch")
    if ex["unique_normalized_full_sign_norm_count"] != 19:
        raise SystemExit("certificate unique norm count mismatch")
    if ex["duplicate_carrier_count_avoiding_repeated_factorization"] != 4:
        raise SystemExit("certificate duplicate reuse count mismatch")

    claimed_reps = {r["normalized_full_sign_norm_sha256"]: r for r in ex["unique_norm_representative_rows"]}
    if set(claimed_reps) != set(groups):
        raise SystemExit("certificate representative norm SHA set mismatch")

    replay_by_sha = {}
    for pos, (sha, ids) in enumerate(sorted(groups.items()), 1):
        rep = ids[0]
        claimed = claimed_reps[sha]
        if claimed["representative_carrier_id"] != rep:
            raise SystemExit(f"representative moved for {sha}")
        if claimed["carrier_ids"] != ids or claimed["carrier_count"] != len(ids):
            raise SystemExit(f"norm-group membership moved for {sha}")
        print(f"replay [{pos:02d}/19] rep={rep} carriers={ids}", flush=True)
        replay = singular_factor(polys[rep], rep)
        compare_factorization(replay, claimed, f"representative {rep}")
        replay_by_sha[sha] = replay

    claimed_carriers = ex["carrier_rows"]
    if [r["carrier_id"] for r in claimed_carriers] != off_ids:
        raise SystemExit("certificate carrier order/list mismatch")
    nonsquarefree = []
    degree_patterns = Counter()
    factor_to_carriers = defaultdict(set)
    for claimed in claimed_carriers:
        cid = claimed["carrier_id"]
        normalized = b.normalize_norm(polys[cid])
        sha = csha(normalized)
        if claimed["normalized_full_sign_norm_sha256"] != sha:
            raise SystemExit(f"carrier norm SHA mismatch: {cid}")
        rep = groups[sha][0]
        if claimed["factored_via_representative_carrier_id"] != rep:
            raise SystemExit(f"carrier representative mismatch: {cid}")
        if claimed["factorization_reused_from_equal_normalized_norm"] != (cid != rep):
            raise SystemExit(f"carrier reuse flag mismatch: {cid}")
        compare_factorization(replay_by_sha[sha], claimed, f"carrier {cid}")
        if not claimed["squarefree_factorization"]:
            nonsquarefree.append(cid)
        degree_patterns[tuple(claimed["factor_degree_multiset"])] += 1
        for fac in claimed["factors"]:
            factor_to_carriers[fac["normalized_factor_sha256"]].add(cid)

    if len(nonsquarefree) != 7 or ex["nonsquarefree_carrier_ids"] != nonsquarefree:
        raise SystemExit(f"nonsquarefree carrier set mismatch: {nonsquarefree}")
    if ex["nonsquarefree_carrier_count"] != 7 or ex["squarefree_carrier_count"] != 16:
        raise SystemExit("squarefree/nonsquarefree aggregate moved")
    histogram = {"+".join(map(str, k)): v for k, v in sorted(degree_patterns.items())}
    if ex["factor_degree_pattern_histogram"] != histogram:
        raise SystemExit(f"factor pattern histogram mismatch: {histogram}")
    if ex["unique_irreducible_factor_sha256_count"] != len(factor_to_carriers):
        raise SystemExit("unique irreducible factor SHA count mismatch")
    if not ex["all_and_only_r5b3b3b_off_boundary_carriers_processed"]:
        raise SystemExit("all/off-boundary processed flag false")
    if not ex["all_unique_representative_factorizations_reconstructed_exactly"]:
        raise SystemExit("exact representative reconstruction flag false")
    if not ex["all_factor_degree_sums_equal_16"]:
        raise SystemExit("factor-degree-sum flag false")

    expected_nonsquarefree = ["LIN_008", "LIN_015", "LIN_020", "LIN_025", "LIN_013", "LIN_019", "LIN_024"]
    if nonsquarefree != expected_nonsquarefree:
        raise SystemExit(f"nonsquarefree exact IDs moved: {nonsquarefree}")

    print(
        f"R5B3B3C1_REPLAY_OK c1_sha={C1_SHA} offboundary=23 unique_norms=19 reuse=4 squarefree=16 nonsquarefree=7",
        flush=True,
    )


if __name__ == "__main__":
    main()
