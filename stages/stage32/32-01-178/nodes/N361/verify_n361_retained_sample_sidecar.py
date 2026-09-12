#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
import types
from pathlib import Path

from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
RES = ROOT / "stages/stage32/residual-32-01-production"
S33 = ROOT / "stages/stage33/33-07"
RESULT = HERE / "RESULT.json"
N342_RESULT = HERE.parent / "N342/RESULT.json"

FAMILY = RES / "compressed_terminal_family.py"
INDEXER = RES / "compressed_terminal_indexer.py"
PAIRING = RES / "pairing_prefix_engine.py"
HPERP = RES / "hperp_integral_adapter.py"
BUNDLE = S33 / "picard_base_rows_retained.py"
MARKING = S33 / "stage32_picard_marking_retained.py"

EXPECTED_RESULT_BLOB = "31ddd705d9d5e163ce58f0a07817ed7012831680"
EXPECTED_RESULT_CANONICAL = "b03c70208db1ef352022e8c4260402b35cf04dd38b93ca71332d5fae2cbdeb25"
EXPECTED_N342_CANONICAL = "0a556575c4ad365d5f0816a60c380de16ca609310961e58f6e63834082a61c88"
EXPECTED_BUNDLE_CANONICAL = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
LOCKS = {
    FAMILY: "90ff82ed312dcc0cb32cf207935945f550e29170",
    INDEXER: "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    PAIRING: "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    HPERP: "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    BUNDLE: "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    MARKING: "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    N342_RESULT: "c44a5345e5f88f914023369323fb067ff964a18d",
}


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def module_from_bytes(name: str, path: Path, raw: bytes):
    mod = types.ModuleType(name)
    mod.__file__ = str(path)
    sys.modules[name] = mod
    exec(compile(raw, str(path), "exec"), mod.__dict__)
    return mod


def load_verified_modules():
    sources = {path: path.read_bytes() for path in LOCKS}
    for path, expected in LOCKS.items():
        got = git_blob_sha(sources[path])
        if got != expected:
            raise ValueError(f"source-lock drift {path}: {got} != {expected}")
    saved = {
        name: sys.modules.get(name)
        for name in (
            "compressed_terminal_family",
            "compressed_terminal_indexer",
            "pairing_prefix_engine",
            "hperp_integral_adapter",
            "n361_replay_bundle",
            "n361_replay_marking",
        )
    }
    try:
        family = module_from_bytes("compressed_terminal_family", FAMILY, sources[FAMILY])
        indexer = module_from_bytes("compressed_terminal_indexer", INDEXER, sources[INDEXER])
        pairing = module_from_bytes("pairing_prefix_engine", PAIRING, sources[PAIRING])
        hperp = module_from_bytes("hperp_integral_adapter", HPERP, sources[HPERP])
        bundle_mod = module_from_bytes("n361_replay_bundle", BUNDLE, sources[BUNDLE])
        marking_mod = module_from_bytes("n361_replay_marking", MARKING, sources[MARKING])
        return family, indexer, pairing, hperp, bundle_mod, marking_mod
    finally:
        for name, old in saved.items():
            if old is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = old


def main() -> None:
    raw_result = RESULT.read_bytes()
    if git_blob_sha(raw_result) != EXPECTED_RESULT_BLOB:
        raise ValueError("N361 retained RESULT blob regression")
    result = json.loads(raw_result)
    claimed = result.pop("canonical_sha256_without_this_field", None)
    if claimed != EXPECTED_RESULT_CANONICAL or csha(result) != claimed:
        raise ValueError("N361 retained RESULT canonical regression")
    result["canonical_sha256_without_this_field"] = claimed

    if result["schema"] != "STAGE32_32_01_178_N361_SAMPLE_SIDECAR_GENERATION_V1":
        raise ValueError("N361 result schema regression")
    if result["sample_count"] != 1:
        raise ValueError("N361 sample count regression")
    rec = result["record"]
    if rec["terminal_identity"] != "g0-d176|e=48|rank=37830303724188":
        raise ValueError("N361 terminal identity regression")
    if len(rec["picard64_coordinates"]) != 64 or len(rec["selected64_pairings"]) != 64:
        raise ValueError("N361 64-vector shape regression")
    if rec["coverage_source"]["creates_full178_coverage"] is not False:
        raise ValueError("N361 sample must not create FULL178 coverage")
    for key in (
        "main_pruning_credit",
        "full178_complete",
        "effectivity_final",
        "irreducible_member",
        "n350_registered",
        "merge_authorized",
    ):
        if rec["credit"][key] is not False:
            raise ValueError(f"N361 credit firewall regression: {key}")
    if rec["credit"]["sample_sidecar_only"] is not True:
        raise ValueError("N361 sample-only marker regression")

    expected_locks = {str(path.relative_to(ROOT)): sha for path, sha in LOCKS.items()}
    if rec["witness_source_locks"] != expected_locks:
        raise ValueError("N361 witness source-lock record regression")

    n342 = json.loads(N342_RESULT.read_text())
    n342_body = dict(n342)
    n342_claimed = n342_body.pop("canonical_sha256_without_this_field", None)
    if n342_claimed != EXPECTED_N342_CANONICAL or csha(n342_body) != n342_claimed:
        raise ValueError("N342 canonical regression")
    if rec["filtered_rank_historical_locator"] not in n342["sat_x4"][rec["row_id"]]:
        raise ValueError("N361 sample no longer belongs to retained N342 boundary set")

    family, indexer_mod, pairing, hperp, bundle_mod, marking_mod = load_verified_modules()
    bundle = bundle_mod.load()
    marking = marking_mod.load()
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE_CANONICAL:
        raise ValueError("retained Picard bundle canonical regression")

    adapter = hperp.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = Matrix(adapter.pairing_matrix)
    G = Matrix(bundle["picard_gram_64x64"])
    selected_labels = [int(v) for v in pairing.INDLIST]
    Psel = P.extract([v - 1 for v in selected_labels], list(range(64)))

    coords = [int(v) for v in rec["picard64_coordinates"]]
    cv = Matrix(coords)
    selected = [int(v) for v in (Psel * cv)]
    if selected != rec["selected64_pairings"]:
        raise ValueError("N361 selected64 pairing replay regression")

    all_pairings = [int((P.row(r) * cv)[0]) for r in range(140)]
    if csha(all_pairings) != rec["all140_pairings_sha256"]:
        raise ValueError("N361 all140 pairing commitment regression")
    if all_pairings[92:] != [1] * 48:
        raise ValueError("N361 exceptional [1]^48 replay regression")
    if min(all_pairings[:92]) < 0 or sum(all_pairings[:92]) != 3104:
        raise ValueError("N361 normal pairing replay regression")
    if all_pairings[48] != 3:
        raise ValueError("N361 x4 replay regression")

    if csha(coords) != rec["picard64_coordinates_sha256"]:
        raise ValueError("N361 Picard64 coordinate commitment regression")
    psel_plain = [[int(Psel[i, j]) for j in range(64)] for i in range(64)]
    gram_plain = [[int(G[i, j]) for j in range(64)] for i in range(64)]
    if csha(psel_plain) != rec["selected_pairing_matrix_sha256"]:
        raise ValueError("N361 selected64 matrix commitment regression")
    if csha(gram_plain) != rec["gram64_sha256"]:
        raise ValueError("N361 Gram64 commitment regression")
    self_square = int((cv.T * G * cv)[0])
    if self_square != rec["self_square"] or self_square != -1784:
        raise ValueError("N361 self-square replay regression")

    _, known_degree, _, _, hmeta = hperp._parse_hperp(marking["hperp_text"])
    basis_labels = [int(v) for v in hperp.RETAINED_BASIS_KNOWN_LABELS_1BASED]
    degree_coeffs = [int(known_degree[v - 1]) for v in basis_labels]
    degree = sum(degree_coeffs[j] * coords[j] for j in range(64))
    if degree != rec["d"] or degree != 176:
        raise ValueError("N361 degree replay regression")
    if hmeta["hperp_text_sha256"] != rec["hperp_text_sha256"]:
        raise ValueError("N361 Hperp commitment regression")

    terminal = [int(v) for v in rec["compressed_terminal_pairings"]]
    if not family.terminal_predicate(terminal, e=rec["e"], d=rec["d"]):
        raise ValueError("N361 compressed terminal predicate regression")
    old = indexer_mod.CompressedTerminalIndexer(rec["e"], rec["d"])
    rank = int(old.rank(terminal))
    if rank != rec["terminal_rank"] or list(old.unrank(rank)) != terminal:
        raise ValueError("N361 old canonical rank replay regression")

    m = 16 // __import__("math").gcd(rec["d"], 16)
    numerator = m * m * rec["d"] * rec["d"] - 16 * m * m * self_square
    if numerator % 16:
        raise ValueError("N361 Hperp scalar integrality regression")
    negative_hperp_square_n = numerator // 16
    if negative_hperp_square_n != 3720:
        raise ValueError("N361 Hperp scalar replay regression")

    print(json.dumps({
        "verdict": "PASS_N361_RETAINED_SELECTED64_SAMPLE_SIDECAR_REPLAY",
        "terminal_identity": rec["terminal_identity"],
        "picard64_coordinates_sha256": rec["picard64_coordinates_sha256"],
        "selected_pairing_matrix_sha256": rec["selected_pairing_matrix_sha256"],
        "self_square": self_square,
        "negative_hperp_square_N": negative_hperp_square_n,
        "sample_sidecar_only": True,
        "main_pruning_credit": False,
        "full178_complete": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
