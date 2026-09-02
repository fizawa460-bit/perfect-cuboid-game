#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXPECTED = "d652154f42aca4524ed37f2f38363c2c662e2ee63bd814419d716148b71de578"
LOCKS = {
    "stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json": "def8b60b726c02aa7ee97c0cc25b34f43525ec34",
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json": "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
    "stages/stage32/32-21/post-21bl-picard64-witness-adapter.json": "43eed149c5cbfc026f60ef5d86351e63ff59f89c",
    "stages/stage32/32-21/post-21bl-effectivity-gap-separation.json": "8b46b85a7fe7d1b366d0ada0a7db852f123e77e1",
    "stages/stage32/residual-32-01-production/post1490-o210-q4-picard64-deck-action-source-trace.json": "9e7bb8a152e565f2df7cd48ed6fa2b77ed810baf",
}
CANON = {
    "stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json": "eb31183bf519fec4ad5bb2d0799b3f0a64b7af893308e09ce0c33119b63440a1",
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json": "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8",
    "stages/stage32/32-21/post-21bl-picard64-witness-adapter.json": "ef3f21e4166d4bfcacce3503213b0a72afee5f5002ab7145de01fc9c54d47038",
    "stages/stage32/32-21/post-21bl-effectivity-gap-separation.json": "4afeb8a3add7c203fbbaa9ffdb5b4b4d357df8503979ee80617db654df73d4dc",
    "stages/stage32/residual-32-01-production/post1490-o210-q4-picard64-deck-action-source-trace.json": "e2c4d6e495fb613e33df1e865d3171aa759dbfb61fddd887b38301889ec688f1",
}

def csha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load(rel: str) -> dict:
    path = ROOT / rel
    if blob(path) != LOCKS[rel]:
        raise SystemExit(f"source blob moved: {rel}")
    obj = json.loads(path.read_text())
    if obj.get("canonical_sha256_without_this_field") != CANON[rel]:
        raise SystemExit(f"canonical moved: {rel}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", type=Path, required=True)
    args = ap.parse_args()

    raw = json.loads(args.check.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED or csha(raw) != claimed:
        raise SystemExit("correction canonical mismatch")

    cart = load("stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json")
    v6 = load("stages/stage32/32-21/post1473-v6-witness-body-recovered.json")
    adapter = load("stages/stage32/32-21/post-21bl-picard64-witness-adapter.json")
    gap = load("stages/stage32/32-21/post-21bl-effectivity-gap-separation.json")
    trace = load("stages/stage32/residual-32-01-production/post1490-o210-q4-picard64-deck-action-source-trace.json")

    square = cart["group_quotient_square"]
    if square["X"] != "P/H_diag (Beauville cover surface)" or not square["B"].startswith("P/G_diag") or square["X"] == square["B"]:
        raise SystemExit("X/B quotient-object distinction moved")

    witness = v6["witness"]
    recon = adapter["reconstruction"]
    quadratic = adapter["quadratic"]
    interp = adapter["interpretation"]
    if witness["picard_coordinates_sha256"] != "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726" or witness["self_intersection"] != 758:
        raise SystemExit("exact V6 witness moved")
    if recon["picard_coordinates_sha256"] != "0fcbe0c9cdf894a95704bcaf55536290fc2daa736387169c891e8262f2c565a7" or quadratic["picard_self_square"] != 858:
        raise SystemExit("post21bl representative moved")
    if witness["picard_coordinates_sha256"] == recon["picard_coordinates_sha256"]:
        raise SystemExit("distinct V6 and post21bl classes unexpectedly collapsed")
    if not interp.get("representative_sample_only") or not interp.get("picard_class_is_not_effective_curve_existence"):
        raise SystemExit("post21bl semantic firewall moved")
    if not gap["firewalls"].get("representative_sample_is_not_full178_numerical_credit") or gap["exact_gap_result"].get("actual_effective_curve_certificate_present"):
        raise SystemExit("effectivity-gap firewall moved")
    if trace["open_bridge"].get("individual_D_dot_tD_known") or trace["open_bridge"].get("deck_budget_split_known"):
        raise SystemExit("partial source trace unexpectedly claims split")
    if raw["correction"].get("compute_DtD_from_B_picard64_forbidden_without_adapter") is not True:
        raise SystemExit("correction firewall missing")
    if raw["open_bridge"].get("individual_D_dot_tD_known") or raw["scope"].get("O210_excluded"):
        raise SystemExit("correction overclaims closure")

    print(json.dumps({
        "verdict": "PASS_EXACT_SEMANTIC_OBJECT_MISMATCH_CORRECTED",
        "X_not_B": True,
        "exact_v6_not_post21bl_sample": True,
        "individual_D_dot_tD_known": False,
        "canonical_sha256": claimed,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
