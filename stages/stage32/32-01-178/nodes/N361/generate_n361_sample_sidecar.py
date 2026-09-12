#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
import types
from pathlib import Path

import z3
from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RES = ROOT / "stages/stage32/residual-32-01-production"
S33 = ROOT / "stages/stage33/33-07"
N342_RESULT = HERE.parent / "N342/RESULT.json"

FAMILY = RES / "compressed_terminal_family.py"
INDEXER = RES / "compressed_terminal_indexer.py"
PAIRING = RES / "pairing_prefix_engine.py"
HPERP = RES / "hperp_integral_adapter.py"
BUNDLE = S33 / "picard_base_rows_retained.py"
MARKING = S33 / "stage32_picard_marking_retained.py"

LOCKS = {
    FAMILY: "90ff82ed312dcc0cb32cf207935945f550e29170",
    INDEXER: "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    PAIRING: "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    HPERP: "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    BUNDLE: "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    MARKING: "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    N342_RESULT: "c44a5345e5f88f914023369323fb067ff964a18d",
}
EXPECTED_N342_CANONICAL = "0a556575c4ad365d5f0816a60c380de16ca609310961e58f6e63834082a61c88"
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"

ROW_ID = "g0-d176"
GENUS = 0
DEGREE = 176
EXCEPTIONAL_MASS = 48
NORMAL_MASS = 3104
FILTERED_RANK = 3
X4 = 3


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def module_from_verified_bytes(name: str, path: Path, raw: bytes):
    mod = types.ModuleType(name)
    mod.__file__ = str(path)
    sys.modules[name] = mod
    exec(compile(raw, str(path), "exec"), mod.__dict__)
    return mod


def load_verified_modules():
    raw = {path: path.read_bytes() for path in LOCKS}
    for path, expected in LOCKS.items():
        got = git_blob_sha(raw[path])
        if got != expected:
            raise ValueError(f"source-lock drift {path}: {got} != {expected}")

    saved = {
        name: sys.modules.get(name)
        for name in (
            "compressed_terminal_family",
            "compressed_terminal_indexer",
            "pairing_prefix_engine",
            "hperp_integral_adapter",
            "n361_bundle",
            "n361_marking",
        )
    }
    try:
        family = module_from_verified_bytes(
            "compressed_terminal_family", FAMILY, raw[FAMILY]
        )
        indexer = module_from_verified_bytes(
            "compressed_terminal_indexer", INDEXER, raw[INDEXER]
        )
        pairing = module_from_verified_bytes(
            "pairing_prefix_engine", PAIRING, raw[PAIRING]
        )
        hperp = module_from_verified_bytes(
            "hperp_integral_adapter", HPERP, raw[HPERP]
        )
        bundle_mod = module_from_verified_bytes("n361_bundle", BUNDLE, raw[BUNDLE])
        marking_mod = module_from_verified_bytes("n361_marking", MARKING, raw[MARKING])
        return family, indexer, pairing, hperp, bundle_mod, marking_mod
    finally:
        for name, old in saved.items():
            if old is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = old


def linexpr(row, vars_):
    terms = [int(a) * v for a, v in zip(row, vars_) if int(a)]
    return z3.Sum(terms) if terms else z3.IntVal(0)


def main() -> None:
    n342 = json.loads(N342_RESULT.read_text())
    body342 = dict(n342)
    claimed342 = body342.pop("canonical_sha256_without_this_field", None)
    if claimed342 != EXPECTED_N342_CANONICAL or csha(body342) != claimed342:
        raise ValueError("N342 retained result canonical regression")
    if not n342["aggregate"]["all_have_exact_old_rank_locator"]:
        raise ValueError("N342 old-rank locator authority regression")
    if X4 not in n342["sat_x4"][ROW_ID]:
        raise ValueError("selected sample is no longer in retained N342 terminal set")

    family, indexer_mod, pairing, hperp, bundle_mod, marking_mod = load_verified_modules()
    bundle = bundle_mod.load()
    marking = marking_mod.load()
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle canonical regression")

    adapter = hperp.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    G = Matrix(bundle["picard_gram_64x64"])
    if P.shape != (140, 64) or G.shape != (64, 64) or G != G.T:
        raise ValueError("retained Picard matrix shape/symmetry regression")

    selected_labels = [int(v) for v in pairing.INDLIST]
    Psel = P.extract([v - 1 for v in selected_labels], list(range(64)))
    if Psel.shape != (64, 64) or Psel.det() == 0:
        raise ValueError("selected64 pairing matrix regression")

    _, known_degree, _, _, hmeta = hperp._parse_hperp(marking["hperp_text"])
    basis_labels = [int(v) for v in hperp.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    degree_coeffs = [int(known_degree[v - 1]) for v in basis_labels]

    x = [z3.Int(f"c{i}") for i in range(64)]
    all_pairing_expr = [
        linexpr([int(P[r, j]) for j in range(64)], x) for r in range(140)
    ]
    degree_expr = linexpr(degree_coeffs, x)

    solver = z3.SolverFor("QF_LIA")
    solver.set(timeout=30000)
    for r in range(92, 140):
        solver.add(all_pairing_expr[r] == 1)
    for r in range(92):
        solver.add(all_pairing_expr[r] >= 0)
    solver.add(z3.Sum(all_pairing_expr[:92]) == NORMAL_MASS)
    solver.add(all_pairing_expr[48] == X4)
    solver.add(degree_expr == DEGREE)

    status = solver.check()
    if status != z3.sat:
        reason = solver.reason_unknown() if status == z3.unknown else str(status)
        raise ValueError(f"N361 sample witness generation failed: {reason}")
    model = solver.model()
    coords = [int(model.eval(v, model_completion=True).as_long()) for v in x]
    cv = Matrix(coords)
    all_pairings = [int((P.row(r) * cv)[0]) for r in range(140)]
    selected_pairings = [all_pairings[v - 1] for v in selected_labels]

    if all_pairings[92:] != [1] * 48:
        raise ValueError("sample exceptional vector replay regression")
    if min(all_pairings[:92]) < 0 or sum(all_pairings[:92]) != NORMAL_MASS:
        raise ValueError("sample normal pairings replay regression")
    if all_pairings[48] != X4:
        raise ValueError("sample x4 replay regression")
    if sum(degree_coeffs[j] * coords[j] for j in range(64)) != DEGREE:
        raise ValueError("sample degree replay regression")
    if Psel * cv != Matrix(selected_pairings):
        raise ValueError("selected64 pairing replay regression")

    filtered_terminal = [1, 1, 1, 1, X4, 1, 1, 1, 1, 1, 1]
    if not family.terminal_predicate(
        filtered_terminal, e=EXCEPTIONAL_MASS, d=DEGREE
    ):
        raise ValueError("sample compressed-terminal predicate regression")
    old = indexer_mod.CompressedTerminalIndexer(EXCEPTIONAL_MASS, DEGREE)
    terminal_rank = int(old.rank(filtered_terminal))
    if list(old.unrank(terminal_rank)) != filtered_terminal:
        raise ValueError("canonical rank roundtrip regression")

    source_locks = {
        str(path.relative_to(ROOT)): expected for path, expected in LOCKS.items()
    }
    record = {
        "schema": "STAGE32_32_01_178_SELECTED64_SURVIVOR_SIDECAR_V1",
        "row_id": ROW_ID,
        "g": GENUS,
        "e": EXCEPTIONAL_MASS,
        "terminal_rank": terminal_rank,
        "terminal_identity": f"{ROW_ID}|e={EXCEPTIONAL_MASS}|rank={terminal_rank}",
        "d": DEGREE,
        "filtered_rank_historical_locator": FILTERED_RANK,
        "compressed_terminal_pairings": filtered_terminal,
        "selected64_pairings": selected_pairings,
        "picard64_coordinates": coords,
        "selected_pairing_matrix_sha256": csha(
            [[int(Psel[i, j]) for j in range(64)] for i in range(64)]
        ),
        "gram64_sha256": csha(
            [[int(G[i, j]) for j in range(64)] for i in range(64)]
        ),
        "picard64_coordinates_sha256": csha(coords),
        "all140_pairings_sha256": csha(all_pairings),
        "self_square": int((cv.T * G * cv)[0]),
        "hperp_text_sha256": hmeta["hperp_text_sha256"],
        "witness_source_locks": source_locks,
        "coverage_source": {
            "kind": "DETERMINISTIC_RESEARCH_SAMPLE_FROM_RETAINED_N342_BOUNDARY_SET",
            "n342_result_canonical_sha256": EXPECTED_N342_CANONICAL,
            "creates_full178_coverage": False,
            "current_main_pruning_credit": False,
        },
        "credit": {
            "sample_sidecar_only": True,
            "main_pruning_credit": False,
            "full178_complete": False,
            "effectivity_final": False,
            "irreducible_member": False,
            "n350_registered": False,
            "merge_authorized": False,
        },
    }
    out = {
        "schema": "STAGE32_32_01_178_N361_SAMPLE_SIDECAR_GENERATION_V1",
        "node_id": "N361",
        "status": "SAMPLE_SIDECAR_GENERATED_NO_MAIN_CREDIT",
        "sample_count": 1,
        "record": record,
    }
    out["canonical_sha256_without_this_field"] = csha(out)
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
