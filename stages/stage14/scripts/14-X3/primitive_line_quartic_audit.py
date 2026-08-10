#!/usr/bin/env python3
"""Stage14-X3 quartic reduction and relaxed diagonal obstruction audit.

Finite enumeration is diagnostic.  The fixed-value B^o(1) statement is proved
by factor allocation in the result, and the relaxed obstruction is the exact
symbolic diagonal specialization.
"""

from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve()
ROOT = HERE.parents[4]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


x2 = load_module(
    "stage14_x2_x3",
    HERE.parents[1] / "14-X2" / "joint_packet_rank_one_audit.py",
)


def squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def quartic(a: int, b: int) -> int:
    return a * b * (b - a) * (b + a)


def primitive_squarefree_pairs(limit: int):
    for a in range(1, limit + 1):
        if not squarefree(a):
            continue
        for b in range(a + 1, limit + 1):
            if squarefree(b) and gcd(a, b) == 1:
                yield a, b


def factor_gcd_audit(a: int, b: int) -> None:
    factors = (a, b, b - a, b + a)
    for i in range(4):
        for j in range(i + 1, 4):
            # Primitive pairs make every odd common divisor impossible.
            assert gcd(factors[i], factors[j]) in (1, 2)


def quartic_fibers(limit: int):
    fibers = defaultdict(list)
    for a, b in primitive_squarefree_pairs(limit):
        factor_gcd_audit(a, b)
        fibers[quartic(a, b)].append((a, b))
    return fibers


def relaxed_diagonal_count(limit: int) -> int:
    # Equal coefficients and (U,V)=(A,D) satisfy the scaled equation exactly.
    return sum(1 for _ in primitive_squarefree_pairs(limit))


def check_boundaries(summary: dict) -> None:
    sources = {
        "x1": ROOT / "stages/stage14/14-X1/result.md",
        "four_ci": ROOT / "stages/stage14/14-4ci/result.md",
        "four_cj": ROOT / "stages/stage14/14-4cj/result.md",
        "s7_24": ROOT / "stages/stage14/14-s7-24/result.md",
        "x2": ROOT / "stages/stage14/14-X2/result.md",
        "x3": ROOT / "stages/stage14/14-X3/result.md",
    }
    text = {name: path.read_text() for name, path in sources.items()}
    assert "JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=true" in text["x1"]
    assert "COMMON_CORE_FULL_K_DUAL_XI_STRATIFIED_MULTIPLICITY_PROVED=false" in text["four_ci"]
    assert "XI_PHYSICAL_SHORT_SPAN_RANK=1" in text["four_cj"]
    assert "XI_PHYSICAL_ENDPOINT_SHORT_RANK_EXACT=1" in text["s7_24"]
    assert "PrimitiveLineCommonCoreNormalizedHostMultiplicity" in text["x2"]
    assert "RELAXED_DIAGONAL_FIXED_POWER_OBSTRUCTION=true" in text["x3"]
    assert "PHYSICAL_RECEIVER_COUNTEREXAMPLE_PROVED=false" in text["x3"]
    assert summary["target"] == "PrimitiveLineCommonCoreNormalizedHostMultiplicity"
    assert summary["obstruction"]["physical_receiver_counterexample_proved"] is False
    assert summary["new_power_saving_proved"] is False


def main() -> None:
    summary = json.loads(
        (ROOT / "stages/stage14/data/14-X3/primitive_line_quartic_summary.json").read_text()
    )
    check_boundaries(summary)
    expected = summary["finite_audit"]

    fibers = quartic_fibers(expected["pair_cutoff"])
    collision = fibers[expected["required_collision_value"]]
    assert collision == [tuple(x) for x in expected["required_collision_pairs"]]
    max_fiber = max(map(len, fibers.values()))
    assert max_fiber == expected["required_max_fixed_value_fiber_at_300"]

    diagonal = {n: relaxed_diagonal_count(n) for n in (50, 100, 200, 300)}
    assert all(diagonal[a] < diagonal[b] for a, b in zip(diagonal, list(diagonal)[1:]))

    physical = x2.finite_physical_audit(expected["physical_cutoff_Q"])
    physical_max = max(map(len, physical["residual_line"].values()))
    assert physical_max == expected["required_physical_residual_line_max_fiber"]

    hist = dict(sorted(Counter(map(len, fibers.values())).items()))
    print("Stage14-X3 primitive-line quartic audit: PASS")
    print(f"primitive squarefree quartic values={len(fibers)}")
    print(f"fixed-value fiber histogram={hist}")
    print(f"maximum fixed-value fiber={max_fiber}")
    print(f"F(1,6)=F(2,5)={quartic(1, 6)}")
    print(f"relaxed diagonal counts={diagonal}")
    print(f"physical Q<={expected['physical_cutoff_Q']} residual+line max fiber={physical_max}")
    print("relaxed diagonal obstruction=exact symbolic specialization")
    print("physical receiver counterexample and new power saving=not proved")


if __name__ == "__main__":
    main()
