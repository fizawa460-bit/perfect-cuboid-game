#!/usr/bin/env python3
"""Audit every observed elliptic fiber with PARI/GP.

The stage-three relation file contains 255 points on 193 specialized elliptic
curves. This script runs PARI's unconditional 2-descent rank computation on all
193 observed lambda fibers, including the 143 singleton fibers omitted from the
previous repeated-fiber audit.

When the number of observed bounded seed points equals the certified rank and
their height pairing is nondegenerate, the script also calls ellsaturation.
This certifies that the enlarged subgroup has index not divisible by primes
below the chosen bound. A regulator ratio of one shows that the observed seed
subgroup itself was already saturated for those primes. It does not certify
full saturation at larger primes.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(record: dict[str, Any]) -> Fraction:
    return Fraction(int(record["numerator"]), int(record["denominator"]))


def gp_fraction(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def curve_coefficients(lam: Fraction) -> tuple[Fraction, Fraction]:
    a2 = 4 * lam * lam + (lam * lam + 1) ** 2
    a4 = 4 * lam * lam * (lam * lam + 1) ** 2
    return a2, a4


def parse_integer(raw: str, name: str) -> int:
    match = re.search(rf"^{re.escape(name)}=(-?\d+)\s*$", raw, re.MULTILINE)
    if not match:
        raise RuntimeError(f"missing {name} in PARI output:\n{raw}")
    return int(match.group(1))


def parse_text(raw: str, name: str) -> str | None:
    match = re.search(rf"^{re.escape(name)}=(.+)$", raw, re.MULTILINE)
    return None if match is None else match.group(1).strip()


def point_to_gp(point_record: dict[str, Any]) -> str:
    if point_record.get("infinity"):
        raise ValueError("an observed cuboid point unexpectedly maps to infinity")
    x = parse_fraction(point_record["x"])
    y = parse_fraction(point_record["y"])
    return f"[{gp_fraction(x)},{gp_fraction(y)}]"


def load_fibers(relations_path: Path) -> list[dict[str, Any]]:
    payload = json.loads(relations_path.read_text(encoding="utf-8"))
    points = payload.get("points", [])
    by_index = {int(point["source_index"]): point for point in points}
    grouped: dict[str, list[int]] = defaultdict(list)
    for point in points:
        grouped[str(point["lambda"])].append(int(point["source_index"]))

    repeated_by_lambda = {
        str(fiber["lambda"]): fiber
        for fiber in payload.get("repeated_fibers", [])
    }
    fibers: list[dict[str, Any]] = []
    for lam_text, source_indices in grouped.items():
        repeated = repeated_by_lambda.get(lam_text)
        if repeated is None:
            seed_indices = [source_indices[0]]
        else:
            seed_indices = [
                int(index)
                for index in repeated["bounded_relation_search"][
                    "basis_source_indices"
                ]
            ]
        fibers.append(
            {
                "lambda": lam_text,
                "source_indices": sorted(source_indices),
                "point_count": len(source_indices),
                "seed_source_indices": seed_indices,
                "seed_points": [
                    by_index[index]["weierstrass_point"] for index in seed_indices
                ],
            }
        )
    return sorted(fibers, key=lambda item: Fraction(item["lambda"]))


def curve_and_points_gp(fiber: dict[str, Any]) -> tuple[str, str]:
    lam = Fraction(fiber["lambda"])
    a2, a4 = curve_coefficients(lam)
    curve = f"ellinit([0,{gp_fraction(a2)},0,{gp_fraction(a4)},0])"
    points = "[" + ",".join(
        point_to_gp(point) for point in fiber["seed_points"]
    ) + "]"
    return curve, points


def rank_script(fiber: dict[str, Any], effort: int) -> str:
    curve, points = curve_and_points_gp(fiber)
    return f"""default(realprecision,80);
E={curve};
P={points};
print("ALL_POINTS_ON_CURVE=",vecmin(vector(#P,k,ellisoncurve(E,P[k]))));
T=elltors(E);
print("TORSION_ORDER=",T[1]);
print("TORSION_STRUCTURE=",T[2]);
R=ellrank(E,{effort},P);
print("RANK_LOWER=",R[1]);
print("RANK_UPPER=",R[2]);
print("SHA2_INFO=",R[3]);
print("FOUND_GENERATOR_COUNT=",#R[4]);
print("ROOT_NUMBER=",ellrootno(E));
print("OBSERVED_REGULATOR=",matdet(ellheightmatrix(E,P)));
quit;
"""


def saturation_script(fiber: dict[str, Any], saturation_bound: int) -> str:
    curve, points = curve_and_points_gp(fiber)
    return f"""default(realprecision,80);
E={curve};
P={points};
regP=matdet(ellheightmatrix(E,P));
W=ellsaturation(E,P,{saturation_bound});
regW=matdet(ellheightmatrix(E,W));
ratio=regP/regW;
ratioInt=round(ratio);
print("SATURATED_REGULATOR=",regW);
print("SATURATION_INDEX_SQUARED=",ratioInt);
print("SATURATION_INDEX_SQUARED_ERROR=",abs(ratio-ratioInt));
print("SATURATION_INDEX=",if(issquare(ratioInt),sqrtint(ratioInt),-1));
print("SATURATED_GENERATOR_COUNT=",#W);
quit;
"""


def run_process(gp: str, script: str, timeout: int) -> tuple[str, str | None]:
    try:
        completed = subprocess.run(
            [gp, "-q"],
            input=script,
            text=True,
            capture_output=True,
            timeout=timeout,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        return "timeout", str(exc)
    raw = completed.stdout + completed.stderr
    if completed.returncode != 0 or "***" in raw:
        return "pari_error", raw
    return "success", raw


def regulator_is_nondegenerate(raw_value: str | None) -> bool:
    if raw_value is None:
        return False
    try:
        return abs(Decimal(raw_value)) > Decimal("1e-50")
    except InvalidOperation:
        return False


def run_fiber(
    gp: str,
    fiber: dict[str, Any],
    effort: int,
    saturation_bound: int,
    timeout: int,
) -> dict[str, Any]:
    status, payload = run_process(gp, rank_script(fiber, effort), timeout)
    if status != "success":
        return {
            **fiber,
            "status": status,
            "effort": effort,
            "timeout_seconds": timeout if status == "timeout" else None,
            "error": payload,
        }
    assert payload is not None
    raw = payload
    lower = parse_integer(raw, "RANK_LOWER")
    upper = parse_integer(raw, "RANK_UPPER")
    observed_regulator = parse_text(raw, "OBSERVED_REGULATOR")
    eligible = (
        lower == upper
        and lower == len(fiber["seed_points"])
        and lower > 0
        and regulator_is_nondegenerate(observed_regulator)
    )
    result: dict[str, Any] = {
        **fiber,
        "status": "success",
        "effort": effort,
        "all_seed_points_on_curve": bool(parse_integer(raw, "ALL_POINTS_ON_CURVE")),
        "torsion_order": parse_integer(raw, "TORSION_ORDER"),
        "torsion_structure_raw": parse_text(raw, "TORSION_STRUCTURE"),
        "rank_lower_bound": lower,
        "rank_upper_bound": upper,
        "rank_exact": lower == upper,
        "sha_2_information": parse_integer(raw, "SHA2_INFO"),
        "found_generator_count": parse_integer(raw, "FOUND_GENERATOR_COUNT"),
        "root_number": parse_integer(raw, "ROOT_NUMBER"),
        "observed_regulator_raw": observed_regulator,
        "saturation_eligible": eligible,
        "saturation_ran": False,
        "saturation_status": "not_eligible",
        "saturation_bound": saturation_bound,
        "raw_pari_rank_output": raw,
    }
    if not eligible:
        return result

    sat_status, sat_payload = run_process(
        gp, saturation_script(fiber, saturation_bound), timeout
    )
    result["saturation_status"] = sat_status
    if sat_status != "success":
        result["saturation_error"] = sat_payload
        return result
    assert sat_payload is not None
    result.update(
        {
            "saturation_ran": True,
            "saturated_regulator_raw": parse_text(
                sat_payload, "SATURATED_REGULATOR"
            ),
            "saturation_index_squared": parse_integer(
                sat_payload, "SATURATION_INDEX_SQUARED"
            ),
            "saturation_index_squared_error_raw": parse_text(
                sat_payload, "SATURATION_INDEX_SQUARED_ERROR"
            ),
            "saturation_index": parse_integer(sat_payload, "SATURATION_INDEX"),
            "saturated_generator_count": parse_integer(
                sat_payload, "SATURATED_GENERATOR_COUNT"
            ),
            "raw_pari_saturation_output": sat_payload,
        }
    )
    return result


def audit(
    relations_path: Path,
    effort: int,
    retry_effort: int,
    saturation_bound: int,
    timeout: int,
    workers: int,
) -> dict[str, Any]:
    gp = shutil.which("gp")
    if gp is None:
        raise RuntimeError("PARI/GP executable 'gp' was not found")
    fibers = load_fibers(relations_path)

    def run_many(targets: list[dict[str, Any]], run_effort: int) -> list[dict[str, Any]]:
        collected: list[dict[str, Any]] = []
        with ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {
                executor.submit(
                    run_fiber,
                    gp,
                    fiber,
                    run_effort,
                    saturation_bound,
                    timeout,
                ): fiber
                for fiber in targets
            }
            for future in as_completed(futures):
                collected.append(future.result())
        return collected

    results = run_many(fibers, effort)
    retry_targets = [
        {
            key: result[key]
            for key in (
                "lambda",
                "source_indices",
                "point_count",
                "seed_source_indices",
                "seed_points",
            )
        }
        for result in results
        if result.get("status") == "success" and not result.get("rank_exact", False)
    ]
    if retry_effort > effort and retry_targets:
        retried = run_many(retry_targets, retry_effort)
        retried_by_lambda = {str(item["lambda"]): item for item in retried}
        results = [
            retried_by_lambda.get(str(item["lambda"]), item) for item in results
        ]
    results.sort(key=lambda item: Fraction(str(item["lambda"])))

    successes = [item for item in results if item["status"] == "success"]
    exact = [item for item in successes if item["rank_exact"]]
    singleton = [item for item in successes if item["point_count"] == 1]
    saturation_runs = [item for item in successes if item["saturation_ran"]]
    saturation_failures = [
        item
        for item in successes
        if item["saturation_eligible"] and not item["saturation_ran"]
    ]
    saturated_observed = [
        item for item in saturation_runs if item.get("saturation_index") == 1
    ]
    enlarged = [
        item for item in saturation_runs if int(item.get("saturation_index", 1)) > 1
    ]

    rank_interval_histogram = Counter(
        f"{item['rank_lower_bound']}..{item['rank_upper_bound']}"
        for item in successes
    )
    exact_rank_histogram = Counter(str(item["rank_lower_bound"]) for item in exact)
    singleton_exact_rank_histogram = Counter(
        str(item["rank_lower_bound"]) for item in singleton if item["rank_exact"]
    )
    torsion_histogram = Counter(
        str(item["torsion_structure_raw"]) for item in successes
    )
    saturation_index_histogram = Counter(
        str(item["saturation_index"]) for item in saturation_runs
    )

    return {
        "valid": len(successes) == len(results)
        and all(item["all_seed_points_on_curve"] for item in successes)
        and not saturation_failures,
        "source": relations_path.as_posix(),
        "fiber_count": len(results),
        "singleton_fiber_count": sum(item["point_count"] == 1 for item in results),
        "repeated_fiber_count": sum(item["point_count"] > 1 for item in results),
        "success_count": len(successes),
        "timeout_count": sum(item["status"] == "timeout" for item in results),
        "pari_error_count": sum(item["status"] == "pari_error" for item in results),
        "exact_rank_count": len(exact),
        "unresolved_rank_count": len(successes) - len(exact),
        "rank_interval_histogram": dict(sorted(rank_interval_histogram.items())),
        "exact_rank_histogram": dict(sorted(exact_rank_histogram.items())),
        "singleton_exact_rank_histogram": dict(
            sorted(singleton_exact_rank_histogram.items())
        ),
        "torsion_structure_histogram": dict(sorted(torsion_histogram.items())),
        "saturation_bound": saturation_bound,
        "saturation_eligible_count": sum(
            item["saturation_eligible"] for item in successes
        ),
        "saturation_run_count": len(saturation_runs),
        "saturation_failure_count": len(saturation_failures),
        "observed_seed_subgroup_saturated_below_bound_count": len(
            saturated_observed
        ),
        "observed_seed_subgroup_enlarged_count": len(enlarged),
        "saturation_index_histogram": dict(sorted(saturation_index_histogram.items())),
        "fibers": results,
        "scope": {
            "certified": [
                "rank over Q for fibers whose PARI lower and upper bounds agree",
                "torsion structure returned by PARI for every successful fiber",
                (
                    "for every successful saturation run, the returned subgroup "
                    f"has index not divisible by primes below {saturation_bound}"
                ),
            ],
            "not_certified": [
                "full saturation at primes at or above the saturation bound",
                "that singleton observed points generate rank-two fibers",
                "a uniform rank bound for unobserved rational lambda",
                "a global point-counting bound on the K3 surface",
                "N_2=o(N_1)",
            ],
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--relations",
        type=Path,
        default=Path("data/two_face_cuboids_1e6_mordell_weil_relations.json"),
    )
    parser.add_argument("--effort", type=int, default=0)
    parser.add_argument("--retry-effort", type=int, default=2)
    parser.add_argument("--saturation-bound", type=int, default=100)
    parser.add_argument("--timeout-per-fiber", type=int, default=180)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--write-report", type=Path, required=True)
    args = parser.parse_args()
    if args.saturation_bound < 2:
        parser.error("saturation bound must be at least 2")
    if args.workers < 1:
        parser.error("workers must be positive")

    report = audit(
        args.relations,
        args.effort,
        args.retry_effort,
        args.saturation_bound,
        args.timeout_per_fiber,
        args.workers,
    )
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(
        json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    summary = {key: value for key, value in report.items() if key != "fibers"}
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
