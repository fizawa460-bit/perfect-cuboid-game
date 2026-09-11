#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from sympy import Matrix
from z3 import Int, Mod, SolverFor, Sum, get_version_string, sat, unknown, unsat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EX5 = ROOT / "stages/stage32-ex5/breadth-cycle-2"
sys.path.insert(0, str(EX5))

import bc2_18_n354_survivor_exceptional_mod8_decomposition as d18

SCHEMA = "STAGE32_FULL178_CUT102_FINITE_RING_DIRECT_COMPLETION_V1"
CUT101 = HERE / "CUT101-source-lock-checkpoint.json"
BC224 = EX5 / "bc2-24-explicit-fibre-degree-partition-checkpoint.json"
EXPECTED_CUT101_BLOB = "fce-placeholder-replaced-by-runtime-contract"
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


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def checked_json(path: Path, blob: str, canonical: str | None = None) -> dict:
    if git_blob_sha(path) != blob:
        raise ValueError(f"blob lock moved: {path}")
    obj = json.loads(path.read_text())
    if canonical is not None:
        if obj.get("canonical_sha256_without_this_field") != canonical:
            raise ValueError(f"canonical field moved: {path}")
        q = dict(obj)
        q.pop("canonical_sha256_without_this_field", None)
        if csha(q) != canonical:
            raise ValueError(f"canonical replay moved: {path}")
    return obj


def row_sum(m: Matrix, labels: list[int]) -> Matrix:
    out = Matrix.zeros(1, m.cols)
    for label in labels:
        out += m.row(label - 1)
    return out


def left_kernel_mod_p(P: Matrix, prime: int) -> tuple[list[list[int]], int]:
    # Nullspace of P^T over F_p.  Each returned h satisfies h*P = 0 mod p.
    a = [[int(P[col, row]) % prime for col in range(P.rows)] for row in range(P.cols)]
    nrows = len(a)
    ncols = len(a[0])
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        pivot = next((i for i in range(r, nrows) if a[i][c] % prime), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c] % prime, -1, prime)
        a[r] = [(v * inv) % prime for v in a[r]]
        for i in range(nrows):
            if i == r or a[i][c] % prime == 0:
                continue
            q = a[i][c] % prime
            a[i] = [(x - q * y) % prime for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == nrows:
            break
    free = [c for c in range(ncols) if c not in set(pivots)]
    basis: list[list[int]] = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for i, pc in enumerate(pivots):
            v[pc] = (-a[i][f]) % prime
        if any(sum(v[i] * int(P[i, j]) for i in range(P.rows)) % prime for j in range(P.cols)):
            raise ValueError(f"left-kernel replay failed mod {prime}")
        basis.append(v)
    return basis, len(pivots)


def load_interface() -> tuple[Matrix, list[list[list[int]]], list[int], list[tuple[list[int], list[int]]], dict]:
    if git_blob_sha(Path(d18.__file__).resolve()) != EXPECTED_D18_BLOB:
        raise ValueError("BC2-18 enumerator source lock moved")
    if git_blob_sha(d18.RETAINED) != EXPECTED_RETAINED_BLOB:
        raise ValueError("retained Picard bundle source lock moved")
    if git_blob_sha(d18.MARKING) != EXPECTED_MARKING_BLOB:
        raise ValueError("retained marking source lock moved")
    bc224 = checked_json(BC224, EXPECTED_BC224_BLOB, EXPECTED_BC224_CANONICAL)
    targets = [int(v) for v in bc224["result"]["residual_unknown_parent_indices"]]
    expected_targets = [584, 1000, 1003, 1014, 1030, 1048, 1050, 1056, 1064, 1066, 1103, 1106, 1117, 1119, 1133, 1198, 1218, 1224, 1243]
    if targets != expected_targets:
        raise ValueError("BC2-24 retained target list moved")

    c17 = json.loads(d18.BC2_17_EVIDENCE.read_text())
    if c17.get("canonical_sha256_without_this_field") != d18.EXPECTED_BC2_17_CANONICAL:
        raise ValueError("BC2-17 evidence canonical moved")
    fixed = {int(k): int(v) for k, v in c17["retarget"]["fixed_exceptional_pairings"].items()}
    if len(fixed) != 10 or sum(fixed.values()) != 2:
        raise ValueError("fixed exceptional pairing regression")

    bundle = d18.load_retained(d18.RETAINED, "s32cut102_bundle")
    marking = d18.load_retained(d18.MARKING, "s32cut102_marking")
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
    fibre_coeffs: list[Matrix] = []
    for factor_index, pack in enumerate(PACKS, start=1):
        seen: list[int] = []
        factor_blocks: list[list[int]] = []
        funcs: list[Matrix] = []
        for boundary in pack:
            inc = [j for j in range(93, 141) if int(full[boundary - 1, j - 1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"incidence regression at boundary {boundary}")
            seen.extend(inc)
            factor_blocks.append(inc)
            funcs.append(2 * P.row(boundary - 1) + row_sum(P, inc))
        if sorted(seen) != list(range(93, 141)):
            raise ValueError(f"exceptional partition regression factor {factor_index}")
        if any(f != funcs[0] for f in funcs[1:]):
            raise ValueError(f"fibre functional regression factor {factor_index}")
        blocks.append(factor_blocks)
        fibre_coeffs.append(funcs[0])
    if 19 * (fibre_coeffs[0] + fibre_coeffs[1]) != row_sum(P, list(range(1, 93))) + 5 * row_sum(P, list(range(93, 141))):
        raise ValueError("degree-sum functional regression")

    labels = [int(v) for v in d18.INDLIST]
    Psel = P.extract([label - 1 for label in labels], list(range(PICARD_RANK)))
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

    parents: list[tuple[list[int], list[int]]] = []
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
        rec = {"selected_exceptional_pairings": yE, "selected_residual_mass": sum(comp), "x4_allowed_residues_mod8": allowed}
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")
        parents.append((yE, allowed))
    if len(parents) != 7336 or stream.hexdigest() != EXPECTED_STREAM:
        raise ValueError("BC2-18 feasible parent stream regression")
    return P, blocks, exceptional_labels, parents, {"fixed": fixed, "targets": targets}


def make_solver(P: Matrix, blocks: list[list[list[int]]], prime: int, timeout_ms: int):
    kernel, rank = left_kernel_mod_p(P, prime)
    y = [Int(f"y_{prime}_{i+1}") for i in range(140)]
    solver = SolverFor("QF_LIA")
    solver.set(timeout=timeout_ms)
    for i in range(NORMAL_COUNT):
        solver.add(y[i] >= 0, y[i] <= NORMAL_MASS)
    for i in range(NORMAL_COUNT, 140):
        solver.add(y[i] >= 0, y[i] <= TARGET_E)
    solver.add(Sum(y[:NORMAL_COUNT]) == NORMAL_MASS)
    solver.add(Sum(y[NORMAL_COUNT:]) == TARGET_E)

    fibre_exprs = []
    for pack, factor_blocks in zip(PACKS, blocks):
        vals = [2 * y[b - 1] + Sum([y[j - 1] for j in block]) for b, block in zip(pack, factor_blocks)]
        for v in vals[1:]:
            solver.add(v == vals[0])
        fibre_exprs.append(vals[0])
    n1, n2 = fibre_exprs
    solver.add(n1 + n2 == TARGET_D, n1 >= 0, n1 <= TARGET_D, n2 >= 0, n2 <= TARGET_D)
    for label in range(93, 141):
        solver.add(y[label - 1] <= TARGET_D // 2)
    for block1 in blocks[0]:
        s1 = Sum([y[j - 1] for j in block1])
        for block2 in blocks[1]:
            solver.add(s1 + Sum([y[j - 1] for j in block2]) <= TARGET_D)

    for h in kernel:
        terms = [int(h[i]) * y[i] for i in range(140) if h[i] % prime]
        solver.add(Mod(Sum(terms), prime) == 0)
    return solver, y, n1, {"prime": prime, "rank_mod_p": rank, "left_kernel_dimension": len(kernel)}


def classify_parent(solver, y, n1, timeout_partition: bool) -> dict:
    result = solver.check()
    if result == unsat:
        return {"result": "unsat", "method": "whole finite-ring relaxation"}
    if result == sat:
        model = solver.model()
        vals = [int(model.eval(v, model_completion=True).as_long()) for v in y]
        return {"result": "sat", "method": "finite-ring relaxation witness", "all140_pairings_sha256": csha(vals)}
    if result != unknown:
        raise ValueError("unexpected z3 result")
    if not timeout_partition:
        return {"result": "unknown", "reason_unknown": solver.reason_unknown()}

    branches = []
    saw_sat = False
    saw_unknown = False
    for degree in range(TARGET_D + 1):
        solver.push()
        solver.add(n1 == degree)
        r = solver.check()
        rec = {"n1": degree, "result": str(r)}
        if r == unknown:
            saw_unknown = True
            rec["reason_unknown"] = solver.reason_unknown()
        elif r == sat:
            saw_sat = True
        elif r != unsat:
            raise ValueError("unexpected partition result")
        branches.append(rec)
        solver.pop()
        if saw_sat:
            break
    if saw_sat:
        return {"result": "sat", "method": "finite-ring relaxation partition witness", "branches": branches}
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
    if not primes or any(p < 2 for p in primes):
        raise ValueError("nonempty prime list required")
    for p in primes:
        if any(p % q == 0 for q in range(2, int(p ** 0.5) + 1)):
            raise ValueError(f"nonprime modulus: {p}")
    if args.per_check_timeout_ms <= 0:
        raise ValueError("timeout must be positive")

    cut101 = json.loads(CUT101.read_text())
    if cut101.get("status") != "PASS_SOURCE_LOCKED_RETAINED_COMPLETION_SCOPE_FROZEN":
        raise ValueError("CUT101 checkpoint status moved")
    P, blocks, exceptional_labels, parents, meta = load_interface()
    fixed = meta["fixed"]
    targets = meta["targets"]

    unresolved = set(targets)
    obstruction_by_parent: dict[int, dict] = {}
    prime_records = []
    for prime in primes:
        solver, y, n1, linear = make_solver(P, blocks, prime, args.per_check_timeout_ms)
        for label, value in fixed.items():
            solver.add(y[label - 1] == value)
        recs = []
        for parent_index in targets:
            if parent_index not in unresolved:
                continue
            yE, _allowed = parents[parent_index]
            solver.push()
            for label, value in zip(exceptional_labels, yE):
                solver.add(y[label - 1] == value)
            rec = classify_parent(solver, y, n1, not args.no_partition_on_unknown)
            rec["parent_index"] = parent_index
            recs.append(rec)
            solver.pop()
            if rec["result"] == "unsat":
                obstruction_by_parent[parent_index] = {"prime": prime, "method": rec["method"]}
                unresolved.remove(parent_index)
        prime_records.append({**linear, "parents_checked": len(recs), "unsat_parent_indices": [r["parent_index"] for r in recs if r["result"] == "unsat"], "sat_parent_indices": [r["parent_index"] for r in recs if r["result"] == "sat"], "unknown_parent_indices": [r["parent_index"] for r in recs if r["result"] == "unknown"], "records": recs})
        if not unresolved:
            break

    obstructed = sorted(obstruction_by_parent)
    residual = sorted(unresolved)
    if not residual:
        status = "CANDIDATE_ALL_19_RETAINED_UNKNOWN_FINITE_RING_UNSAT_NEEDS_CUT103_SCOPE_CERTIFICATE"
    elif obstructed:
        status = "CANDIDATE_PARTIAL_RETAINED_FINITE_RING_OBSTRUCTION_NEEDS_CUT103_SCOPE_CERTIFICATE"
    else:
        status = "BOUNDED_FINITE_RING_SCREEN_NONEXCLUDING_ON_19_RETAINED_UNKNOWN"

    body = {
        "schema": SCHEMA,
        "stage": "32",
        "surface": "full178-cut",
        "node": "CUT102",
        "status": status,
        "z3_version": get_version_string(),
        "source_locks": {
            "cut101_checkpoint_status": cut101["status"],
            "bc2_24_checkpoint_blob_sha1": EXPECTED_BC224_BLOB,
            "bc2_24_checkpoint_canonical_sha256": EXPECTED_BC224_CANONICAL,
            "bc2_18_enumerator_blob_sha1": EXPECTED_D18_BLOB,
            "retained_picard_bundle_blob_sha1": EXPECTED_RETAINED_BLOB,
            "retained_marking_blob_sha1": EXPECTED_MARKING_BLOB,
            "bc2_18_feasible_stream_sha256": EXPECTED_STREAM
        },
        "target": {
            "row_id": "g1-d008", "g": 1, "d": 8, "e": 8,
            "retained_unknown_parent_indices": targets,
            "retained_unknown_parent_count": len(targets),
            "other_unretained_unknown_identity_count": 172,
            "other_unretained_unknown_identities_inferred": False
        },
        "method": {
            "relaxation": "bounded all140 pairing vector in the mod-p column image of the exact retained 140x64 Picard pairing matrix",
            "necessity": "every exact integral Picard64 completion reduces to this finite-ring image; UNSAT is monotone, SAT has no exact-feasibility credit",
            "exact_side_constraints_replayed": ["normal/nonnegative bounds", "exceptional/nonnegative bounds", "normal mass=112", "exceptional mass=8", "fixed terminal exceptional pairings", "retained selected-exceptional parent", "two fibre functionals with n1+n2=8", "exceptional diagonal <=4", "all factor-cross block-sum <=8"],
            "primes_requested": primes,
            "per_check_timeout_ms": args.per_check_timeout_ms,
            "partition_n1_on_unknown": not args.no_partition_on_unknown
        },
        "result": {
            "finite_ring_obstructed_parent_indices": obstructed,
            "finite_ring_obstructed_parent_count": len(obstructed),
            "residual_parent_indices": residual,
            "residual_parent_count": len(residual),
            "obstruction_by_parent": {str(k): v for k, v in sorted(obstruction_by_parent.items())},
            "prime_records": prime_records
        },
        "credit": {
            "cut102_candidate_obstruction_count": len(obstructed),
            "cut103_scope_certificate_complete": False,
            "stage32_main_pruning_credit": False,
            "whole_first_block_unsat": False,
            "full178_complete": False,
            "theorem_credit": False,
            "endpoint_credit": False
        },
        "firewalls": {
            "bc2_25_identity_refinement_performed": False,
            "unretained_172_identities_inferred": False,
            "n356_candidate_assumed_consumed": False,
            "main_authority_mutated": False,
            "merge_authorized": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    body["canonical_sha256_without_this_field"] = csha(body)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(body, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": status, "obstructed": len(obstructed), "residual": len(residual), "output": str(args.output)}))


if __name__ == "__main__":
    main()
