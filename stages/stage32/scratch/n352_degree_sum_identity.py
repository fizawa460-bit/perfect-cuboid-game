#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
from pathlib import Path
from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
N345 = ROOT / "stages/stage32/32-01-178/nodes/N345/verify_n345_kernel14_integral_self_square.py"
BOUNDARY_PACKS = [[33, 36, 37, 40, 41, 44], [34, 35, 38, 39, 42, 43]]
EXPECTED_BUNDLE = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    n345 = load_module(N345, "s32_n352_n345")
    bundle = n345.load_retained(n345.RETAINED, "s32_n352_bundle")
    marking = n345.load_retained(n345.MARKING, "s32_n352_marking")
    if bundle.get("canonical_sha256") != EXPECTED_BUNDLE:
        raise ValueError("bundle regression")
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise ValueError("marking regression")

    adapter = n345.HperpIntegralPairingAdapter.from_retained(marking, bundle)
    P = adapter.pairing_matrix
    coords = adapter.class_coordinates_in_retained_basis
    gram = Matrix(bundle["picard_gram_64x64"])
    full = coords * gram * coords.T

    fibre_pair_rows = []
    for pack in BOUNDARY_PACKS:
        fibre_rows = []
        seen = []
        for label in pack:
            inc = [j for j in range(93, 141) if int(full[label - 1, j - 1]) == 1]
            if len(inc) != 8:
                raise ValueError(f"incidence regression {label}")
            seen.extend(inc)
            Fcoords = 2 * coords.row(label - 1)
            for j in inc:
                Fcoords += coords.row(j - 1)
            fibre_rows.append(Fcoords * gram)
        if sorted(seen) != list(range(93, 141)):
            raise ValueError("exceptional partition regression")
        if any(row != fibre_rows[0] for row in fibre_rows[1:]):
            raise ValueError("fibre equivalence regression")
        fibre_pair_rows.append(fibre_rows[0])

    normal_total = Matrix([[sum(int(P[r, c]) for r in range(92)) for c in range(64)]])
    exceptional_total = Matrix([[sum(int(P[r, c]) for r in range(92, 140)) for c in range(64)]])
    degree19 = normal_total + 5 * exceptional_total
    factor_sum19 = 19 * (fibre_pair_rows[0] + fibre_pair_rows[1])
    delta = factor_sum19 - degree19
    nonzero = [(i, int(delta[0, i])) for i in range(64) if int(delta[0, i]) != 0]

    print({
        "identity_19_times_factor_sum_equals_degree19": not nonzero,
        "nonzero_delta_count": len(nonzero),
        "nonzero_delta": nonzero,
        "consequence_if_true": "d=n1+n2 on the retained Picard64 lattice",
    })
    if nonzero:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
