#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

EXPECTED = "eb31183bf519fec4ad5bb2d0799b3f0a64b7af893308e09ce0c33119b63440a1"
LOCKS = {
    "post1473-specific-class-multibranch-beauville-odd-branch-wall.md": "cb20a9b287430c2e238f79d3151500c262905468",
    "post1473-x8-v4-cusp-quotient.json": "00eaebc3c57f6b5e3696c7bcd60eac5a53121f72",
    "post1484-v6-modular-factor-bidegree-source-note.md": "deeecac5599f3b542b445cd87c2070dae488bc85",
    "post1484-o210-q4-common-double-cover-pic2-reduction.json": "ef470127011b49c041facbae10adbe16a15583b7",
    "post1473-product-cover-v4-character-rank-reduction.json": "01ab580662a76ccda0fc0e3cc44f09f705825942",
    "post1484-o210-q4-common-double-cover-cartesian-source-note.md": "17cbb4ab56ed0d7ab7ade59b135547de475eebe6",
}

def blob_sha(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    body = dict(obj); body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--check", required=True, type=Path); args = ap.parse_args()
    here = Path(__file__).resolve().parent
    for name, expected in LOCKS.items():
        raw = (here / name).read_bytes()
        if blob_sha(raw) != expected:
            raise ValueError(f"source lock moved: {name}")
    cert = json.loads(args.check.read_text())
    if canonical(cert) != EXPECTED or cert.get("canonical_sha256_without_this_field") != EXPECTED:
        raise ValueError("certificate canonical moved")
    sq = cert["group_quotient_square"]
    if "order 8" not in sq["G"] or "normal index 2" not in sq["H"]:
        raise ValueError("subgroup data moved")
    cc = cert["carrier_consequence"]
    if cc["same_quadratic_extension"] is not True or "square" not in cc["squareclass_consequence"]:
        raise ValueError("common-cover identity moved")
    if "=0" not in cc["Pic2_consequence"]:
        raise ValueError("Pic2 zero consequence moved")
    v = cert["verdict"]
    if v["O210_excluded"] is not False or v["common_double_cover_identity_for_actual_carrier"] is not True:
        raise ValueError("verdict moved")
    if v["next_exact_leaf"] != "O210_Q4_SIMULTANEOUS_105_81_CORRESPONDENCE_GEOMETRY":
        raise ValueError("next leaf moved")
    print("PASS", EXPECTED)

if __name__ == "__main__": main()
