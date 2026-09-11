#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from sympy import Matrix
from z3 import Int, SolverFor, Sum, get_version_string, sat, unknown, unsat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
sys.path.insert(0, str(EX5))

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18

SCHEMA = "STAGE32_FULL178_CUT102_FINITE_RING_DIRECT_COMPLETION_V2"
BC224 = EX5 / "bc2-24-explicit-fibre-degree-partition-checkpoint.json"
EXPECTED_BC224_BLOB = "37e12dc0bf40e0dec862784f5567bd247d451742"
EXPECTED_BC224_CANONICAL = "ac6f8afff29a4ac969b1fd32251499f299395261c1aa96a813502cfe2b22472f"
EXPECTED_D18_BLOB = "1e2ed93cae3c5b446c8d90c1ae2250be83289c79"
EXPECTED_RETAINED_BLOB = "82e4d450a1d852e34f6615440fb88a029c6e54eb"
EXPECTED_MARKING_BLOB = "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"
EXPECTED_STREAM = "752a7618e5a4301aea16a3a4983081e02fb26451a21d84e4b8e60b8d11f84db7"
PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
NORMAL_COUNT = 92
PICARD_RANK = 64
NORMAL_MASS = 112
TARGET_E = 8
TARGET_D = 8
DEFAULT_PRIMES = [2, 3, 5, 7, 11, 13, 17, 31, 127]
TARGETS = [584, 1000, 1003, 1014, 1030, 1048, 1050, 1056, 1064, 1066, 1103, 1106, 1117, 1119, 1133, 1198, 1218, 1224, 1243]


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def left_kernel_mod_p(P: Matrix, prime: int) -> tuple[list[list[int]], int]:
    a = [[int(P[col, row]) % prime for col in range(P.rows)] for row in range(P.cols)]
    nrows, ncols = len(a), len(a[0])
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c], -1, prime)
        a[r] = [(v * inv) % prime for v in a[r]]
        for i in range(nrows):
            if i == r or not a[i][c]:
                continue
            q = a[i][c]
            a[i] = [(x - q * y) % prime for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == nrows:
            break
    pset = set(pivots)
    basis = []
    for f in (c for c in range(ncols) if c not in pset):
        v = [0] * ncols
        v[f] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-a[i][f]) % prime
        if any(sum(v[i] * int(P[i, j]) for i in range(P.rows)) % prime for j in range(P.cols)):
            raise ValueError(f"left-kernel replay failed mod {prime}")
        basis.append(v)
    return basis, len(pivots)


def row_sum(m: Matrix, labels: list[int]) -> Matrix:
    out = Matrix.zeros(1, m.cols)
    for label in labels:
        out += m.row(label - 1)
    return out


def load_interface():
    if git_blob_sha(Path(d18.__file__).resolve()) != EXPECTED_D18_BLOB:
        raise ValueError("BC2-18 source lock moved")
    if git_blob_sha(d18.RETAINED) != EXPECTED_RETAINED_BLOB:
        raise ValueError("retained Picard bundle source lock moved")
    if git_blob_sha(d18.MARKING) != EXPECTED_MARKING_BLOB:
        raise ValueError("retained marking source lock moved")
    if git_blob_sha(BC224) != EXPECTED_BC224_BLOB:
        raise ValueError("BC2-24 checkpoint blob moved")
    bc224 = json.loads(BC224.read_text())
    if bc224.get("canonical_sha256_without_this_field") != EXPECTED_BC224_CANONICAL:
        raise ValueError("BC2-24 checkpoint canonical moved")
    q = dict(bc224)
    q.pop("canonical_sha256_without_this_field", None)
    if csha(q) != EXPECTED_BC224_CANONICAL:
        raise ValueError("BC2-24 checkpoint canonical replay moved")
    if [int(v) for v in bc224["result"]["residual_unknown_parent_indices"]] != TARGETS:
        raise ValueError("BC2-24 retained target list moved")

    c17 = json.loads(d18.BC2_17_EVIDENCE.read_text())
    if c17.get("canonical_sha256_without_this_field") != d18.EXPECTED_BC2_17_CANONICAL:
        raise ValueError("BC2-17 evidence canonical moved")
    fixed = {int(k): int(v) for k, v in c17["retarget"]["fixed_exceptional_pairings"].items()}

    bundle = d18.load_retained(d18.RETAINED, "s32cut102v2_bundle")
    marking = d18.load_retained(d18.MARKING, "s32cut102v2_marking")
    if bundle.get("canonical_sha256") != d18.EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained bundle canonical moved")
    if marking.get("canonical_sha256") != d18.EXPECTED_MARKING_CANONICAL:
        raise ValueError("retained marking canonical moved")
    adapter = d18.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    coords = Matrix(adapter.class_coordinates_in_retained_basis)
    gram = Matrix(bundle["picard_gram_64x64"])
    if P.shape != (140, 64) or coords.shape != (140, 64) or gram.shape != (64, 64):
        raise ValueError("retained matrix shape regression")
    full = coords * gram * coords.T

    blocks: list[list[list[int]]] = []
    fibre_coeffs = []
    for factor_index, pack in enumerate(PACKS, start=1):
        seen, factor_blocks, funcs = [], [], []
        for boundary in pack:
            inc = [j for j in range(93, 141) if int(full[boundary - 1, j - 1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"incidence regression boundary {boundary}")
            seen.extend(inc)
            factor_blocks.append(inc)
            funcs.append(2 * P.row(boundary - 1) + row_sum(P, inc))
        if sorted(seen) != list(range(93, 141)) or any(f != funcs[0] for f in funcs[1:]):
            raise ValueError(f"fibre partition regression factor {factor_index}")
        blocks.append(factor_blocks)
        fibre_coeffs.append(funcs[0])
    if 19 * (fibre_coeffs[0] + fibre_coeffs[1]) != row_sum(P, list(range(1, 93))) + 5 * row_sum(P, list(range(93, 141))):
        raise ValueError("degree-sum functional regression")

    labels = [int(v) for v in d18.INDLIST]
    Psel = P.extract([label - 1 for label in labels], list(range(64)))
    Pinv = Psel.inv()
    den = d18.lcm_denominator(Pinv)
    if den != 8:
        raise ValueError("selected64 denominator regression")
    Bq = Pinv * den
    if any(q.q != 1 for q in Bq):
        raise ValueError("selected64 inverse scaling regression")
    B = Matrix([[int(Bq[i, j]) for j in range(Bq.cols)] for i in range(Bq.rows)])
    normal_pos = [j for j, label in enumerate(labels) if label <= NORMAL_COUNT]
    exceptional_pos = [j for j, label in enumerate(labels) if label > NORMAL_COUNT]
    exceptional_labels = [labels[j] for j in exceptional_pos]
    free_labels = [label for label in exceptional_labels if label not in fixed]
    hfull = d18.build_hnf_extension_check(B, den, exceptional_pos, normal_pos)
    x4pos = labels.index(49)
    hx4 = d18.build_hnf_extension_check(B, den, exceptional_pos + [x4pos], [j for j in normal_pos if j != x4pos])

    parents = []
    stream = hashlib.sha256()
    for comp in d18.weak_compositions_at_most(6, len(free_labels)):
        by = dict(fixed)
        by.update({label: int(value) for label, value in zip(free_labels, comp)})
        yE = [int(by[label]) for label in exceptional_labels]
        allowed = [r for r in range(den) if d18.feasible(hx4, yE + [r])]
        ok = d18.feasible(hfull, yE)
        if ok != bool(allowed):
            raise ValueError("HNF/x4 extension regression")
        if not ok:
            continue
        record = {"selected_exceptional_pairings": yE, "selected_residual_mass": sum(comp), "x4_allowed_residues_mod8": allowed}
        stream.update(json.dumps(record, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        parents.append((yE, allowed))
    if len(parents) != 7336 or stream.hexdigest() != EXPECTED_STREAM:
        raise ValueError("BC2-18 parent stream regression")
    return P, blocks, exceptional_labels, parents, fixed


def make_solver(P: Matrix, blocks, fixed: dict[int, int], prime: int, timeout_ms: int):
    kernel, rank = left_kernel_mod_p(P, prime)
    y = [Int(f"y_{prime}_{i+1}") for i in range(140)]
    s = SolverFor("QF_LIA")
    s.set(timeout=timeout_ms)
    for i in range(NORMAL_COUNT):
        s.add(y[i] >= 0, y[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT, 140):
        s.add(y[i] >= 0, y[i] <= TARGET_E)
    s.add(Sum(y[:NORMAL_COUNT]) == NORMAL_MASS, Sum(y[NORMAL_COUNT:]) == TARGET_E)
    for label, value in fixed.items():
        s.add(y[label - 1] == value)

    fibre = []
    for pack, factor_blocks in zip(PACKS, blocks):
        vals = [2 * y[b - 1] + Sum([y[j - 1] for j in block]) for b, block in zip(pack, factor_blocks)]
        for v in vals[1:]:
            s.add(v == vals[0])
        fibre.append(vals[0])
    n1, n2 = fibre
    s.add(n1 + n2 == TARGET_D, n1 >= 0, n1 <= TARGET_D, n2 >= 0, n2 <= TARGET_D)
    for label in range(93, 141):
        s.add(y[label - 1] <= TARGET_D // 2)
    for block1 in blocks[0]:
        a = Sum([y[j - 1] for j in block1])
        for block2 in blocks[1]:
            s.add(a + Sum([y[j - 1] for j in block2]) <= TARGET_D)
    for h in kernel:
        terms = [int(h[i]) * y[i] for i in range(140) if h[i] % prime]
        s.add(Sum(terms) % prime == 0)
    return s, y, n1, {"prime": prime, "rank_mod_p": rank, "left_kernel_dimension": len(kernel)}


def classify(s, y, n1, partition: bool):
    r = s.check()
    if r == unsat:
        return {"result": "unsat", "method": "whole finite-ring relaxation"}
    if r == sat:
        model = s.model()
        vals = [int(model.eval(v, model_completion=True).as_long()) for v in y]
        return {"result": "sat", "method": "finite-ring relaxation witness", "all140_pairings_sha256": csha(vals)}
    if r != unknown:
        raise ValueError("unexpected solver result")
    if not partition:
        return {"result": "unknown", "reason_unknown": s.reason_unknown()}
    branches, saw_sat, saw_unknown = [], False, False
    for degree in range(TARGET_D + 1):
        s.push(); s.add(n1 == degree); br = s.check()
        rec = {"n1": degree, "result": str(br)}
        if br == unknown:
            saw_unknown = True; rec["reason_unknown"] = s.reason_unknown()
        elif br == sat:
            saw_sat = True
        elif br != unsat:
            raise ValueError("unexpected partition result")
        branches.append(rec); s.pop()
        if saw_sat:
            break
    if saw_sat:
        return {"result": "sat", "method": "finite-ring n1 partition witness", "branches": branches}
    if not saw_unknown and len(branches) == TARGET_D + 1:
        return {"result": "unsat", "method": "exhaustive n1 finite-ring partition", "branches": branches}
    return {"result": "unknown", "method": "n1 finite-ring partition", "branches": branches}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--primes", default=",".join(map(str, DEFAULT_PRIMES)))
    ap.add_argument("--per-check-timeout-ms", type=int, default=3000)
    ap.add_argument("--no-partition-on-unknown", action="store_true")
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    primes = [int(v) for v in args.primes.split(",") if v.strip()]
    if not primes or any(p < 2 or any(p % q == 0 for q in range(2, int(p ** 0.5) + 1)) for p in primes):
        raise ValueError("prime moduli required")
    if args.per_check_timeout_ms <= 0:
        raise ValueError("positive timeout required")

    P, blocks, exceptional_labels, parents, fixed = load_interface()
    unresolved = set(TARGETS)
    obstruction_by_parent = {}
    prime_records = []
    for prime in primes:
        s, y, n1, linear = make_solver(P, blocks, fixed, prime, args.per_check_timeout_ms)
        records = []
        for parent_index in TARGETS:
            if parent_index not in unresolved:
                continue
            yE, _ = parents[parent_index]
            s.push()
            for label, value in zip(exceptional_labels, yE):
                s.add(y[label - 1] == value)
            rec = classify(s, y, n1, not args.no_partition_on_unknown)
            rec["parent_index"] = parent_index
            records.append(rec)
            s.pop()
            if rec["result"] == "unsat":
                obstruction_by_parent[parent_index] = {"prime": prime, "method": rec["method"]}
                unresolved.remove(parent_index)
        prime_records.append({**linear, "parents_checked": len(records), "unsat_parent_indices": [r["parent_index"] for r in records if r["result"] == "unsat"], "sat_parent_indices": [r["parent_index"] for r in records if r["result"] == "sat"], "unknown_parent_indices": [r["parent_index"] for r in records if r["result"] == "unknown"], "records": records})
        if not unresolved:
            break

    obstructed, residual = sorted(obstruction_by_parent), sorted(unresolved)
    status = ("CANDIDATE_ALL_19_RETAINED_UNKNOWN_FINITE_RING_UNSAT_NEEDS_CUT103_SCOPE_CERTIFICATE" if not residual else "CANDIDATE_PARTIAL_RETAINED_FINITE_RING_OBSTRUCTION_NEEDS_CUT103_SCOPE_CERTIFICATE" if obstructed else "BOUNDED_FINITE_RING_SCREEN_NONEXCLUDING_ON_19_RETAINED_UNKNOWN")
    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT102",
        "status": status,
        "z3_version": get_version_string(),
        "source_locks": {"bc2_24_checkpoint_blob_sha1": EXPECTED_BC224_BLOB, "bc2_24_checkpoint_canonical_sha256": EXPECTED_BC224_CANONICAL, "bc2_18_enumerator_blob_sha1": EXPECTED_D18_BLOB, "retained_picard_bundle_blob_sha1": EXPECTED_RETAINED_BLOB, "retained_marking_blob_sha1": EXPECTED_MARKING_BLOB, "bc2_18_feasible_stream_sha256": EXPECTED_STREAM},
        "target": {"row_id": "g1-d008", "g": 1, "d": 8, "e": 8, "retained_unknown_parent_indices": TARGETS, "retained_unknown_parent_count": 19, "other_unretained_unknown_identity_count": 172, "other_unretained_unknown_identities_inferred": False},
        "method": {"relaxation": "bounded all140 pairing vector in mod-p column image of exact retained 140x64 Picard pairing matrix", "necessity": "every exact integral Picard64 completion reduces to this finite-ring image; UNSAT is monotone while SAT has no exact-feasibility credit", "exact_side_constraints_replayed": ["normal/nonnegative bounds", "exceptional/nonnegative bounds", "normal mass=112", "exceptional mass=8", "fixed terminal exceptional pairings", "retained selected-exceptional parent", "two fibre functionals with n1+n2=8", "exceptional diagonal <=4", "all factor-cross block-sum <=8"], "primes_requested": primes, "per_check_timeout_ms": args.per_check_timeout_ms, "partition_n1_on_unknown": not args.no_partition_on_unknown},
        "result": {"finite_ring_obstructed_parent_indices": obstructed, "finite_ring_obstructed_parent_count": len(obstructed), "residual_parent_indices": residual, "residual_parent_count": len(residual), "obstruction_by_parent": {str(k): v for k, v in sorted(obstruction_by_parent.items())}, "prime_records": prime_records},
        "credit": {"cut102_candidate_obstruction_count": len(obstructed), "cut103_scope_certificate_complete": False, "stage32_main_pruning_credit": False, "whole_first_block_unsat": False, "full178_complete": False, "theorem_credit": False, "endpoint_credit": False},
        "firewalls": {"bc2_25_identity_refinement_performed": False, "unretained_172_identities_inferred": False, "n356_candidate_assumed_consumed": False, "main_authority_mutated": False, "merge_authorized": False, "perfect_cuboid_existence_claim": False, "perfect_cuboid_nonexistence_claim": False}
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": status, "obstructed": len(obstructed), "residual": len(residual), "output": str(args.output)}))


if __name__ == "__main__":
    main()
