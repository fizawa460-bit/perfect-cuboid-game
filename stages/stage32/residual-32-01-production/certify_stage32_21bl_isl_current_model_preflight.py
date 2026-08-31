#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing as mp
import time
import traceback
from pathlib import Path

import islpy as isl
from z3 import (
    Z3_OP_ADD,
    Z3_OP_AND,
    Z3_OP_EQ,
    Z3_OP_GE,
    Z3_OP_LE,
    Z3_OP_MUL,
    Z3_OP_SUB,
    Z3_OP_UMINUS,
    is_int_value,
    sat,
)

from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bl_joint_integer_closure import (
    EXPECTED_TRIPLES,
    bands_for,
    build_joint,
)
from direct_picard_reynolds_lattice_diagnostic import csha

SCHEMA = "STAGE32_21BL_ISL_CURRENT_MODEL_PREFLIGHT_V1"
RANK = 59


def linear(expr):
    if is_int_value(expr):
        return {}, int(expr.as_long())
    if expr.num_args() == 0:
        name = expr.decl().name()
        if not name.startswith("ri_"):
            raise ValueError(f"unexpected non-coordinate leaf: {expr}")
        return {name: 1}, 0
    kind = expr.decl().kind()
    if kind == Z3_OP_ADD:
        coeffs, const = {}, 0
        for child in expr.children():
            cc, c0 = linear(child)
            const += c0
            for name, value in cc.items():
                coeffs[name] = coeffs.get(name, 0) + value
        return {k: v for k, v in coeffs.items() if v}, const
    if kind == Z3_OP_SUB:
        children = list(expr.children())
        coeffs, const = linear(children[0])
        coeffs = dict(coeffs)
        for child in children[1:]:
            cc, c0 = linear(child)
            const -= c0
            for name, value in cc.items():
                coeffs[name] = coeffs.get(name, 0) - value
        return {k: v for k, v in coeffs.items() if v}, const
    if kind == Z3_OP_UMINUS:
        cc, c0 = linear(expr.arg(0))
        return {k: -v for k, v in cc.items()}, -c0
    if kind == Z3_OP_MUL:
        # Z3 preserves unsimplified constant products such as 1*0*ri_0.
        # Parse every child as an affine form first, fold all constant-only
        # factors exactly, and permit at most one genuinely variable factor.
        # A zero constant factor annihilates the whole product exactly.
        scalar = 1
        variable_factor = None
        for child in expr.children():
            cc, c0 = linear(child)
            if not cc:
                scalar *= int(c0)
                if scalar == 0:
                    return {}, 0
                continue
            if variable_factor is not None:
                raise ValueError(f"nonlinear product: {expr}")
            variable_factor = (cc, int(c0))
        if variable_factor is None:
            return {}, scalar
        cc, c0 = variable_factor
        return {k: scalar * v for k, v in cc.items()}, scalar * c0
    raise ValueError(f"unsupported arithmetic operator: {expr.decl()} / {expr}")


def subtract(lhs, rhs):
    lc, l0 = linear(lhs)
    rc, r0 = linear(rhs)
    out = dict(lc)
    for name, value in rc.items():
        out[name] = out.get(name, 0) - value
    return {k: v for k, v in out.items() if v}, l0 - r0


def affine_text(coeffs: dict[str, int], const: int, ordered_names: list[str]) -> str:
    parts = [str(int(const))]
    for name in ordered_names:
        value = int(coeffs.get(name, 0))
        if value > 0:
            parts.append(f"+ {value}*{name}")
        elif value < 0:
            parts.append(f"- {abs(value)}*{name}")
    return " ".join(parts)


def flatten_assertion(expr):
    if expr.decl().kind() == Z3_OP_AND:
        out = []
        for child in expr.children():
            out.extend(flatten_assertion(child))
        return out
    return [expr]


def relation_text(expr, ordered_names: list[str]) -> tuple[str, tuple[dict[str, int], int, str]]:
    kind = expr.decl().kind()
    if kind not in (Z3_OP_LE, Z3_OP_GE, Z3_OP_EQ) or expr.num_args() != 2:
        raise ValueError(f"unsupported Boolean assertion: {expr}")
    coeffs, const = subtract(expr.arg(0), expr.arg(1))
    affine = affine_text(coeffs, const, ordered_names)
    if kind == Z3_OP_LE:
        relation = "<="
    elif kind == Z3_OP_GE:
        relation = ">="
    else:
        relation = "="
    return f"({affine}) {relation} 0", (coeffs, const, relation)


def verify_point(relations, point: dict[str, int]) -> None:
    for coeffs, const, relation in relations:
        value = int(const) + sum(int(c) * int(point[name]) for name, c in coeffs.items())
        if relation == "<=" and not value <= 0:
            raise ValueError(f"exact witness <= regression: {value}")
        if relation == ">=" and not value >= 0:
            raise ValueError(f"exact witness >= regression: {value}")
        if relation == "=" and not value == 0:
            raise ValueError(f"exact witness = regression: {value}")


def make_namespace(cfg: dict) -> argparse.Namespace:
    return argparse.Namespace(
        source_lock=Path(cfg["source_lock"]),
        formula_lock=Path(cfg["formula_lock"]),
        pair_lock=Path(cfg["pair_lock"]),
        audit_lock=Path(cfg["audit_lock"]),
        seventh_lock=Path(cfg["seventh_lock"]),
        eighth_lock=Path(cfg["eighth_lock"]),
        ninth_lock=Path(cfg["ninth_lock"]),
        tenth_lock=Path(cfg["tenth_lock"]),
        retained=Path(cfg["retained"]),
        marking=Path(cfg["marking"]),
        per_check_timeout_ms=5000,
    )


def exact_worker(cfg: dict) -> dict:
    args = make_namespace(cfg)
    triples = list(prism_triples())
    ordinal = int(cfg["ordinal"])
    if len(triples) != EXPECTED_TRIPLES or not 0 <= ordinal < EXPECTED_TRIPLES:
        raise ValueError("21bl prism/ordinal regression")
    triple = triples[ordinal]
    solver, r, ri, target, table = build_joint(args)
    bands = bands_for(triple, table)
    solver.add(r[50] == triple[0], r[55] == triple[1], r[27] == triple[2])
    for j, (lo, hi) in bands.items():
        solver.add(r[j] >= lo, r[j] <= hi)

    names = [f"ri_{j}" for j in range(RANK)]
    pieces = []
    relation_payload = []
    for assertion in solver.assertions():
        for atom in flatten_assertion(assertion):
            text, relation = relation_text(atom, names)
            pieces.append(text)
            relation_payload.append(relation)
    set_text = "{ [" + ", ".join(names) + "] : " + " and ".join(pieces) + " }"
    problem_sha = hashlib.sha256(set_text.encode()).hexdigest()

    ctx = isl.Context()
    start = time.perf_counter()
    integer_set = isl.Set.read_from_str(ctx, set_text)
    empty = bool(integer_set.is_empty())
    solve_seconds = time.perf_counter() - start

    witness = None
    original_z3_replay = None
    if empty:
        status = "UNSAT"
    else:
        status = "SAT"
        point = integer_set.sample_point()
        witness = [int(point.get_coordinate_val(isl.dim_type.set, j).to_python()) for j in range(RANK)]
        point_map = {name: witness[j] for j, name in enumerate(names)}
        verify_point(relation_payload, point_map)

        # Cross-backend witness firewall: replay the exact sampled integer point
        # into the original current 21bl Z3 assertion set. A translated SAT point
        # receives no credit unless the source model itself accepts it exactly.
        for j, value in enumerate(witness):
            solver.add(ri[j] == int(value))
        replay_result = solver.check()
        original_z3_replay = str(replay_result)
        if replay_result != sat:
            raise ValueError(f"ISL witness rejected by original 21bl Z3 model: {replay_result}")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21bl",
        "mode": "EXACT_ISL_PRESBURGER_PREFLIGHT_ON_CURRENT_21BL_59D_JOINT_INTEGER_MODEL",
        "ordinal": ordinal,
        "triple": list(triple),
        "target": target,
        "current_exact_bands": {str(j): list(v) for j, v in sorted(bands.items())},
        "exact_problem": {
            "integer_rank": RANK,
            "assertion_count": len(relation_payload),
            "problem_text_sha256": problem_sha,
            "same_integerized_21bl_assertions_as_z3_solver": True,
            "fixed_triple_constraints_included": True,
            "six_lossless_coordinate_bands_included": True,
            "all_42_pair_cuts_inherited_from_21bf": True,
            "floating_point_relaxation_used": False,
            "sat_witness_requires_original_z3_replay": True,
        },
        "result": {
            "status": status,
            "solve_wall_seconds": solve_seconds,
            "witness_r_reduced": witness,
            "witness_sha256": csha(witness) if witness is not None else None,
            "original_z3_replay_status": original_z3_replay,
        },
        "interpretation": {
            "sat_is_exact_fixed_projection_integer_witness_only": status == "SAT",
            "unsat_prunes_only_this_fixed_triple": status == "UNSAT",
            "resource_wall_is_not_unsat": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "preflight_only": True,
            "full_3234_scaleout_authorized_by_this_result": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    return payload


def child_entry(queue, cfg: dict) -> None:
    try:
        queue.put(("ok", exact_worker(cfg)))
    except Exception:
        queue.put(("error", traceback.format_exc()))


def timeout_payload(cfg: dict, wall_seconds: int) -> dict:
    triples = list(prism_triples())
    ordinal = int(cfg["ordinal"])
    return {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21bl",
        "mode": "EXACT_ISL_PRESBURGER_PREFLIGHT_ON_CURRENT_21BL_59D_JOINT_INTEGER_MODEL",
        "ordinal": ordinal,
        "triple": list(triples[ordinal]),
        "result": {"status": "UNKNOWN_RESOURCE_WALL", "wall_timeout_seconds": wall_seconds},
        "interpretation": {
            "resource_wall_is_not_unsat": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True,
        },
        "safety": {
            "preflight_only": True,
            "full_3234_scaleout_authorized_by_this_result": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    for name in ("source_lock", "formula_lock", "pair_lock", "audit_lock", "seventh_lock", "eighth_lock", "ninth_lock", "tenth_lock", "retained", "marking"):
        ap.add_argument("--" + name.replace("_", "-"), type=Path, required=True)
    ap.add_argument("--ordinal", type=int, default=1617)
    ap.add_argument("--wall-seconds", type=int, default=90)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    cfg = {name: str(getattr(args, name)) for name in ("source_lock", "formula_lock", "pair_lock", "audit_lock", "seventh_lock", "eighth_lock", "ninth_lock", "tenth_lock", "retained", "marking")}
    cfg["ordinal"] = int(args.ordinal)

    ctx = mp.get_context("spawn")
    queue = ctx.Queue()
    proc = ctx.Process(target=child_entry, args=(queue, cfg))
    proc.start()
    proc.join(args.wall_seconds)
    if proc.is_alive():
        proc.terminate(); proc.join(10)
        payload = timeout_payload(cfg, args.wall_seconds)
    else:
        if queue.empty():
            raise RuntimeError(f"21bl ISL worker exited {proc.exitcode} without result")
        kind, value = queue.get()
        if kind != "ok":
            raise RuntimeError(f"21bl ISL worker failed:\n{value}")
        payload = value

    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["result"]["status"],
        "ordinal": payload["ordinal"],
        "triple": payload["triple"],
        "canonical": payload["canonical_sha256_without_this_field"],
        "solve_wall_seconds": payload["result"].get("solve_wall_seconds"),
    }), flush=True)


if __name__ == "__main__":
    main()
