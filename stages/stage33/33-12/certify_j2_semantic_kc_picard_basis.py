#!/usr/bin/env python3
"""Exact Stage33-12 semantic Kc Picard basis certificate.

This replay removes dependence on Magma's enumeration order for ptsK.
It uses a compact exact interface extracted from the pinned Stoll Kc
intersection construction:
  * the 17 curve slots occurring in indlistK,
  * their exact 17x17 intersection Gram matrix,
  * incidences with the 12 A1 exceptional curves.

The pinned upstream source asserts that the original 20 indlistK classes
(the same 17 curve slots plus three ptsK exceptionals at Magma positions
2,5,10) generate PicK.  We do not need to know which semantic singulars
those three Magma positions denote.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

STOLL_REPO = "MichaelStollBayreuth/Verification"
STOLL_COMMIT = "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
STOLL_PATH = "Cuboids/cuboids.magma"
STOLL_INDLISTK = [2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54,64,67,72]
CURVE_SLOTS = STOLL_INDLISTK[:17]

POINTS = [
    {"label":"A1_B2+1_B3+1","coords":["1","0","0","0","1","1"]},
    {"label":"A1_B2+1_B3-1","coords":["1","0","0","0","1","-1"]},
    {"label":"A1_B2-1_B3+1","coords":["1","0","0","0","-1","1"]},
    {"label":"A1_B2-1_B3-1","coords":["1","0","0","0","-1","-1"]},
    {"label":"A2_B1+1_B3+1","coords":["0","1","0","1","0","1"]},
    {"label":"A2_B1+1_B3-1","coords":["0","1","0","1","0","-1"]},
    {"label":"A2_B1-1_B3+1","coords":["0","1","0","-1","0","1"]},
    {"label":"A2_B1-1_B3-1","coords":["0","1","0","-1","0","-1"]},
    {"label":"A3_B1+1_B2+1","coords":["0","0","1","1","1","0"]},
    {"label":"A3_B1+1_B2-1","coords":["0","0","1","1","-1","0"]},
    {"label":"A3_B1-1_B2+1","coords":["0","0","1","-1","1","0"]},
    {"label":"A3_B1-1_B2-1","coords":["0","0","1","-1","-1","0"]},
]

GRAM17 = [[-2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
 [0, -2, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
 [0, 0, -2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
 [0, 0, 0, -2, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
 [0, 0, 0, 0, -2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
 [0, 0, 0, 0, 0, -2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
 [1, 0, 0, 1, 0, 1, -2, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
 [1, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 1, 1, 2, 2],
 [0, 0, 0, 0, 1, 1, 1, 2, 0, 1, 1, 1, 1, 1, 1, 2, 2],
 [0, 1, 0, 0, 0, 0, 1, 0, 1, -2, 0, 0, 1, 0, 1, 1, 1],
 [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, -2, 0, 0, 1, 0, 1, 1],
 [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, -2, 0, 1, 0, 1, 1],
 [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, -2, 0, 0, 0, 2],
 [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, -2, 0, 0, 2],
 [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, -2, 2, 0],
 [1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 0, 0, 2, 0, 4],
 [1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2, 2, 0, 4, 0]]

INCIDENCE17X12 = [[0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
 [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
 [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
 [0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
 [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
 [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Exact pairings of CsK[22] with the semantic basis below.
CSK22_PAIRINGS = [1,1,0,0,0,0,1,0,2,0,0,0,1,1,1,2,2,1,0,0]

# Canonical semantic exceptionals: all negative nonzero B signs, one from each type.
SEMANTIC_EXCEPTIONAL_INDICES_0BASED = [3,7,11]


def det_bareiss(a: list[list[int]]) -> int:
    """Fraction-free exact determinant over Z."""
    n = len(a)
    m = [row[:] for row in a]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if m[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if m[r][k] != 0), None)
            if pivot is None:
                return 0
            m[k], m[pivot] = m[pivot], m[k]
            sign *= -1
        pivot = m[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                m[i][j] = (m[i][j] * pivot - m[i][k] * m[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            m[i][k] = 0
        for j in range(k + 1, n):
            m[k][j] = 0
    return sign * m[n - 1][n - 1]


def gram_for_exceptional_triple(triple: tuple[int, int, int]) -> list[list[int]]:
    g = [row[:] + [INCIDENCE17X12[r][c] for c in triple] for r, row in enumerate(GRAM17)]
    for a, c in enumerate(triple):
        row = [INCIDENCE17X12[r][c] for r in range(17)] + [0, 0, 0]
        row[17 + a] = -2
        g.append(row)
    assert all(g[i][j] == g[j][i] for i in range(20) for j in range(20))
    return g


def canonical_sha(obj: object) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    assert len(GRAM17) == 17 and all(len(r) == 17 for r in GRAM17)
    assert len(INCIDENCE17X12) == 17 and all(len(r) == 12 for r in INCIDENCE17X12)
    assert CURVE_SLOTS == [2,4,5,7,9,10,20,21,26,35,39,42,44,47,49,52,54]
    assert STOLL_INDLISTK[17:] == [64,67,72]

    det_counts: dict[int, int] = {}
    for triple in itertools.combinations(range(12), 3):
        d = det_bareiss(gram_for_exceptional_triple(triple))
        det_counts[d] = det_counts.get(d, 0) + 1
    assert det_counts == {0:120, -32:64, -128:32, -512:4}
    min_nonzero_abs_det = min(abs(d) for d in det_counts if d)
    assert min_nonzero_abs_det == 32

    semantic_gram = gram_for_exceptional_triple(tuple(SEMANTIC_EXCEPTIONAL_INDICES_0BASED))
    semantic_det = det_bareiss(semantic_gram)
    assert semantic_det == -32

    # Stoll's pinned source asserts that its 20 indlistK classes generate PicK.
    # Its unknown-order exceptional triple therefore has nonzero determinant and
    # by the exhaustive 12-choose-3 table has |disc PicK| >= 32.
    # Our semantic 20 classes form a PicK sublattice of determinant 32, hence
    # 32 = index^2 * |disc PicK|, so |disc PicK| <= 32.
    # Therefore |disc PicK|=32 and the semantic sublattice has index 1.
    picK_abs_discriminant = 32
    semantic_index_in_picK = 1

    # CsK[22] has the same pairing row as semantic basis vector #8 = CsK[21].
    assert CSK22_PAIRINGS == semantic_gram[7]
    csk22_coords = [0] * 20
    csk22_coords[7] = 1

    pinf_coords = [0] * 20
    pinf_coords[17] = 1
    assert POINTS[SEMANTIC_EXCEPTIONAL_INDICES_0BASED[0]]["coords"] == ["1","0","0","0","-1","-1"]

    cert = {
        "schema": "STAGE33_12_J2_SEMANTIC_KC_PICARD_BASIS_V1",
        "status": "COMPUTED_EXACT_NETWORK_FREE",
        "upstream_source_lock": {
            "repo": STOLL_REPO,
            "commit": STOLL_COMMIT,
            "path": STOLL_PATH,
            "load_bearing_assertion": "sub<PicK | [qPicK(BigK.j) : j in indlistK]> eq PicK",
            "indlistK_1based": STOLL_INDLISTK,
        },
        "semantic_point_order": POINTS,
        "curve_slots_1based": CURVE_SLOTS,
        "semantic_exceptional_indices_0based": SEMANTIC_EXCEPTIONAL_INDICES_0BASED,
        "semantic_exceptional_labels": [POINTS[i]["label"] for i in SEMANTIC_EXCEPTIONAL_INDICES_0BASED],
        "gram17": GRAM17,
        "incidence17x12": INCIDENCE17X12,
        "triple_determinant_distribution": {str(k): det_counts[k] for k in sorted(det_counts)},
        "minimum_nonzero_abs_triple_determinant": min_nonzero_abs_det,
        "semantic_gram20": semantic_gram,
        "semantic_gram20_determinant": semantic_det,
        "picK_abs_discriminant": picK_abs_discriminant,
        "semantic_basis_index_in_picK": semantic_index_in_picK,
        "j2_branch_carrier": {
            "curve": "CsK[22]",
            "marked_semantic_picK_coords": csk22_coords,
            "same_picK_class_as": "CsK[21]",
        },
        "j2_infinity_exceptional": {
            "point": "[1:0:0:0:-1:-1]",
            "semantic_label": "A1_B2-1_B3-1",
            "marked_semantic_picK_coords": pinf_coords,
        },
        "ptsk_order_dependency": "ELIMINATED",
        "magma_qPicK_coordinate_dependency": "ELIMINATED_BY_SEMANTIC_UNIMODULAR_BASIS",
        "smith_recomputation": False,
        "stage33_12_visible_progress_after_certificate": "4/5",
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
    }
    cert["canonical_sha256"] = canonical_sha(cert)

    out = Path(__file__).with_name("j2-semantic-kc-picard-basis.json")
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": cert["status"],
        "semantic_det": semantic_det,
        "picK_abs_discriminant": picK_abs_discriminant,
        "semantic_index_in_picK": semantic_index_in_picK,
        "j2_branch_carrier_coords": csk22_coords,
        "j2_infinity_exceptional_coords": pinf_coords,
        "canonical_sha256": cert["canonical_sha256"],
        "output": str(out),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
