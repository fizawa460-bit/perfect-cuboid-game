#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
INDEX = ROOT / "docs/stage14-toolbox/index.json"
ATLAS = ROOT / "docs/stage14-toolbox/pythagorean-euclid-formulas.md"
RESULT = ROOT / "stages/stage14/14-toolbox-ad/result.md"
STAGE_CODE = re.compile(r"^Stage14-toolbox-([a-z]{2})$")

EXPECTED = {
    "TB-FORMULA-primitive-euclid-face": ("FORMULA", 364, "c51992e2373c0f7f265275c211684f6bd5ef9ccf"),
    "TB-FORMULA-half-angle-normalization": ("FORMULA", 364, "c51992e2373c0f7f265275c211684f6bd5ef9ccf"),
    "TB-FORMULA-physical-two-face-gluing": ("FORMULA", 360, "42f4315b0659bd402a94adeb8822588ea153305a"),
    "TB-LEMMA-third-face-transfer": ("LEMMA", 364, "c51992e2373c0f7f265275c211684f6bd5ef9ccf"),
    "TB-FORMULA-half-angle-cross-square": ("FORMULA", 369, "e9916a9e21dc305fa30e240d3db962a26af1653b"),
    "TB-WARNING-pythagorean-orientation-and-converse": ("WARNING", 369, "e9916a9e21dc305fa30e240d3db962a26af1653b"),
}

SECTIONS = [
    "## INPUT",
    "## OUTPUT",
    "## VARIABLE DICTIONARY",
    "## USED BY",
    "## DO NOT USE FOR",
    "## PROVENANCE NOTES",
]


def fail(msg: str) -> None:
    raise AssertionError(msg)


def sqroot(n: int) -> int | None:
    if n < 0:
        return None
    r = math.isqrt(n)
    return r if r * r == n else None


def half_angle(S: int, X: int, H: int) -> tuple[int, int, int]:
    if S % 2 == 0:
        kappa = 1
        minus_sq = H - S
        plus_sq = H + S
    else:
        kappa = 2
        if (H - S) % 2 or (H + S) % 2:
            fail("odd-S half-angle parity failure")
        minus_sq = (H - S) // 2
        plus_sq = (H + S) // 2
    tm = sqroot(minus_sq)
    tp = sqroot(plus_sq)
    if tm is None or tp is None:
        fail(f"half-angle square failure for {(S, X, H)}")
    if kappa * tm * tp != X:
        fail("half-angle X reconstruction failure")
    if kappa * (tp * tp - tm * tm) // 2 != S:
        fail("half-angle S reconstruction failure")
    if kappa * (tp * tp + tm * tm) // 2 != H:
        fail("half-angle H reconstruction failure")
    return kappa, tm, tp


def primitive_faces(limit: int = 30) -> list[tuple[int, int, int]]:
    faces: list[tuple[int, int, int]] = []
    for m in range(2, limit + 1):
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            E = 2 * m * n
            O = m * m - n * n
            H = m * m + n * n
            if E * E + O * O != H * H:
                fail("Euclid identity failure")
            if math.gcd(E, O) != 1:
                fail("primitive Euclid gcd failure")
            for S, X in ((E, O), (O, E)):
                if S * S + X * X != H * H:
                    fail("oriented Pythagorean failure")
                half_angle(S, X, H)
                faces.append((S, X, H))
    return faces


def audit_physical_transfers(faces: list[tuple[int, int, int]]) -> tuple[int, int]:
    hits = 0
    cross_square_hits = 0
    # The square test selects exact small physical-gluing identities from the
    # primitive face pair universe. No claim is made that an arbitrary pair is physical.
    for S, X, H in faces:
        for S2, X2, H2 in faces:
            G2 = S * S * H2 * H2 + X * X * S2 * S2
            G = sqroot(G2)
            if G is None:
                continue
            g = math.gcd(S, S2)
            if G % g:
                continue
            dspace = G // g
            cross_gcd = math.gcd(H, X2)
            if dspace % cross_gcd:
                continue
            scale = g * cross_gcd
            if (H * S2) % scale or (S * X2) % scale:
                continue

            S3 = H * S2 // scale
            X3 = S * X2 // scale
            H3 = dspace // cross_gcd
            if S3 * S3 + X3 * X3 != H3 * H3:
                fail("third-face Pythagorean failure")
            if math.gcd(S3, X3) != 1:
                fail("third-face primitive reduction failure")
            if H3 > dspace:
                fail("third-face height failure")
            if X3 * S2 * H != S3 * X2 * S:
                fail("third-face recovery ratio failure")
            if dspace != cross_gcd * H3:
                fail("space diagonal recovery failure")

            geom = (S3 * X2) ** 2 - (X3 * S2) ** 2
            y = sqroot(geom)
            if y is None or y == 0:
                fail("transferred square condition failure")

            k2, a, b = half_angle(S2, X2, H2)
            k3, c, d = half_angle(S3, X3, H3)
            A0 = a * b * (d * d - c * c)
            C0 = c * d * (b * b - a * a)
            f1 = a * d - b * c
            f2 = a * d + b * c
            f3 = b * d - a * c
            f4 = b * d + a * c
            delta = A0 * A0 - C0 * C0
            if delta != f1 * f2 * f3 * f4:
                fail("four-bilinear factorization failure")
            yd = sqroot(delta)
            if yd is None or yd == 0:
                fail("half-angle transferred square failure")
            # Compare geometric and normalized square up to the exact kappa scale.
            if 4 * geom != (k2 * k3) ** 2 * delta:
                fail("kappa-scaled cross-square reconstruction failure")

            hits += 1
            cross_square_hits += 1

    if hits < 10:
        fail(f"too few deterministic physical transfer samples: {hits}")
    return hits, cross_square_hits


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    atlas = ATLAS.read_text(encoding="utf-8")
    result = RESULT.read_text(encoding="utf-8")
    cards = {c["id"]: c for c in data["cards"]}
    if len(cards) != len(data["cards"]):
        fail("duplicate card ids")
    if len(cards) < 18:
        fail(f"ad expects at least 18 canonical cards, got {len(cards)}")

    for card_id, (ctype, pr, merge_sha) in EXPECTED.items():
        card = cards.get(card_id)
        if card is None:
            fail(f"missing ad card: {card_id}")
        if card["type"] != ctype or card["status"] != "CURRENT":
            fail(f"wrong type/status for {card_id}")
        if card["source_pr"] != pr or card["source_merge_sha"] != merge_sha:
            fail(f"wrong provenance for {card_id}")
        path = ROOT / card["path"]
        if not path.exists():
            fail(f"missing card path: {card['path']}")
        text = path.read_text(encoding="utf-8")
        for section in SECTIONS:
            if section not in text:
                fail(f"{card_id} missing section {section}")
        for source in card["source_files"]:
            if not (ROOT / source).exists():
                fail(f"missing source {source} for {card_id}")

    m = STAGE_CODE.fullmatch(data["next_stage"])
    if not m or m.group(1) < "ae":
        fail("toolbox registry must be at ae or later after ad")
    if not str(data.get("next_theme", "")).strip():
        fail("toolbox next theme must be nonempty")

    for lock in [
        "E = 2mn",
        "H-S = kappa*t_-^2",
        "G^2 = H^2*S2^2 + S^2*X2^2",
        "S3=H*S2/(g*c)",
        "Delta0=A0^2-C0^2",
        "Orientation is data",
    ]:
        if lock not in atlas:
            fail(f"atlas missing lock: {lock}")

    source_locks = {
        "stages/stage14/14-s6-06/result.md": "PHYSICAL_GLUE_THIRD_PYTHAGOREAN_IDENTITY=true",
        "stages/stage14/14-s6-07/result.md": "THIRD_PRIMITIVE_PYTHAGOREAN_FACE_EXACT=true",
        "stages/stage14/14-s6-08/result.md": "HALF_ANGLE_CROSS_SQUARE_FOUR_BILINEAR_FACTORIZATION=true",
    }
    for path, lock in source_locks.items():
        if lock not in (ROOT / path).read_text(encoding="utf-8"):
            fail(f"source boundary missing {lock}")

    for lock in [
        "STAGE14_TOOLBOX_AD=COMPLETE_PYTHAGOREAN_EUCLID_CONVERSION_FORMULA_ATLAS",
        "CANONICAL_NEW_CARD_COUNT=6",
        "F2_F3_SQUARE_CONDITION_SUFFICIENT_FOR_PHYSICALITY=false",
        "OPEN_PR_USED_AS_CANONICAL_SOURCE=false",
        "TOOLBOX_OWNS_NEW_STAGE14_THEOREM=false",
        "NEXT=Stage14-toolbox-ae local 2-descent and five-column interface",
    ]:
        if lock not in result:
            fail(f"result boundary missing {lock}")

    faces = primitive_faces(30)
    transfer_hits, square_hits = audit_physical_transfers(faces)

    print(json.dumps({
        "stage": "14-toolbox-ad",
        "classification": "PYTHAGOREAN_EUCLID_CONVERSION_FORMULA_AUDIT",
        "oriented_primitive_faces_checked": len(faces),
        "physical_transfer_samples_checked": transfer_hits,
        "half_angle_cross_square_samples_checked": square_hits,
        "new_card_count": len(EXPECTED),
        "next_stage": data["next_stage"],
        "toolbox_owns_new_theorem": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
