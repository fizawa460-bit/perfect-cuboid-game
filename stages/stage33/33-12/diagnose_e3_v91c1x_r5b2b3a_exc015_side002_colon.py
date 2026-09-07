#!/usr/bin/env python3
from __future__ import annotations

import json
import sympy as sp

from materialize_e3_v91c1x_r5b2b3a_24_side_exceptional_crossing_uniformizer_charts_v2 import (
    B2A, B2A_SHA, B2B1, B2B1_SHA, B2B2, B2B2_SHA, I,
    clean, decode_element, load_locked, affine_node_and_side_forms,
    tangent_direction, rees_surface, rank_at,
)


def principal_colon_generators(polys, f, variables):
    t = sp.Symbol("t_colon")
    G = sp.groebner(
        [t * g for g in polys] + [(1 - t) * f],
        t, *variables, order="lex", extension=I,
    )
    inter = [clean(g.as_expr()) for g in G.polys if not g.as_expr().has(t)]
    if not inter:
        raise SystemExit("intersection elimination returned no generators")
    quot = []
    for h in inter:
        q, r = sp.div(h, f, *variables, extension=I)
        q, r = clean(q), clean(r)
        if r != 0 or clean(h - f * q) != 0:
            raise SystemExit(f"intersection generator not divisible by f: {h}")
        quot.append(q)
    return sp.groebner(quot, *variables, order="grevlex", extension=I)


def first_nonvanishing_colon_witness(J, g, variables, point_sub):
    GJ = sp.groebner(J, *variables, order="grevlex", extension=I)
    if clean(GJ.reduce(sp.expand(g))[1]) == 0:
        return sp.Integer(1), sp.Integer(1), True
    C = principal_colon_generators(J, g, variables)
    for p in C.polys:
        h = clean(p.as_expr())
        val = clean(h.subs(point_sub))
        if val != 0:
            rem = clean(GJ.reduce(sp.expand(h * g))[1])
            if rem != 0:
                raise SystemExit("colon witness failed multiplication membership")
            return h, val, False
    return None, None, False


def main():
    b2a = load_locked(B2A, B2A_SHA)
    b2b1 = load_locked(B2B1, B2B1_SHA)
    b2b2 = load_locked(B2B2, B2B2_SHA)
    local_by_eid = {r["exceptional_id"]: r for r in b2b1["local_germ_rows"]}
    b2b2_by_eid = {r["exceptional_id"]: r for r in b2b2["exceptional_rows"]}

    side = 2
    side_row = next(r for r in b2a["side_rows"] if int(r["side_index_1based"]) == side)
    crossing = next(r for r in side_row["crossings"] if r["exceptional_id"] == "EXC_015")
    eid = crossing["exceptional_id"]
    parameter = crossing["side_parameter"]
    local_row = local_by_eid[eid]
    _point, _affine_pivot, _affine_nonpivot, d, side_forms = affine_node_and_side_forms(local_row, side)
    direction = tangent_direction(local_row, side, parameter)
    valid_pivots = [j for j, x in enumerate(direction) if clean(x) != 0]
    chart_p = valid_pivots[0]
    d2, e, u, nonp, sub, _pull_surface, strict_surface = rees_surface(local_row, chart_p)
    if list(d2) != list(d):
        raise SystemExit("displacement convention drift")
    pull_side = [clean(f.subs(sub)) for f in side_forms]
    strict_side = [clean(f / e) for f in pull_side]
    stored_chart = b2b2_by_eid[eid]["charts"][chart_p]

    pivot_dir = direction[chart_p]
    u_values = [clean(direction[j] / pivot_dir) for j in nonp]
    crossing_sub = {e: sp.Integer(0), **{u[k]: u_values[k] for k in range(5)}}
    variables = [e, *u]
    if any(clean(f.subs(crossing_sub)) != 0 for f in strict_surface + strict_side):
        raise SystemExit("crossing point misses strict ideals")

    surface_rank, _ = rank_at(strict_surface, variables, crossing_sub)
    rows = []
    for idx, s in enumerate(strict_side):
        side_rank, _ = rank_at(strict_surface + [s], variables, crossing_sub)
        cross_rank, cross_J = rank_at(strict_surface + [s, e], variables, crossing_sub)
        row = {"candidate_index": idx, "side_rank": side_rank, "cross_rank": cross_rank}
        if side_rank != 5 or cross_rank != 6:
            row["eligible"] = False
            rows.append(row)
            continue
        det = clean(cross_J.det())
        detval = clean(det.subs(crossing_sub))
        row["eligible"] = detval != 0
        row["cross_det"] = str(det)
        row["cross_det_value"] = str(detval)
        if detval == 0:
            rows.append(row)
            continue
        J = list(strict_surface) + [s]
        witnesses = []
        all_ok = True
        lam = det
        for gidx, g in enumerate(strict_side):
            h, val, already = first_nonvanishing_colon_witness(J, g, variables, crossing_sub)
            if h is None:
                witnesses.append({"generator_index": gidx, "found": False})
                all_ok = False
                continue
            witnesses.append({
                "generator_index": gidx,
                "found": True,
                "already_in_J": already,
                "witness": str(h),
                "value": str(val),
            })
            lam = clean(lam * h)
        row["colon_witnesses"] = witnesses
        row["all_colon_witnesses_nonvanishing"] = all_ok
        row["lambda"] = str(lam)
        row["lambda_value"] = str(clean(lam.subs(crossing_sub)))
        rows.append(row)

    print(json.dumps({
        "success": True,
        "marker": "R5B2B3A_EXC015_SIDE002_COLON_DIAGNOSTIC",
        "exceptional_id": eid,
        "side": side,
        "parameter": parameter,
        "chart_p": chart_p,
        "chart_id": stored_chart["chart_id"],
        "surface_rank": surface_rank,
        "candidate_rows": rows,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
