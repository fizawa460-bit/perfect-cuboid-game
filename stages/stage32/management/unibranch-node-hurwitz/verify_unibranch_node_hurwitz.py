#!/usr/bin/env python3
"""Stage32 UNIBRANCH-NODE-HURWITZ: verify the unibranch node-count Hurwitz filter and its compressed-census effect.

Proposition (see CONTRACT.md): for an integral curve C on S with bijective normalization (unibranch), geometric
genus g in {0,1}, not a component of a fibre of either factor fibration S -> X(4),

    2*nu >= e + d - 4g + 4        (d = K.C, e = sum_i C.E_i, nu = #{i : C.E_i > 0}),

hence d <= 44 + 4g.

This verifier checks, fail-closed:
  1. the 92 non-exceptional known curves (all-140 intersection matrix recovered by the repository adapter, retained
     payloads loaded only through their loaders): the 80 curves covered by the proposition satisfy it, all with
     equality; the 12 boundary fibre components are reported separately;
  2. the audited N354 compressed census replays exactly ([17128, 38560956534397137634780102]);
  3. raising N354's support requirement from K to max(K, ceil((d+e)/2) - 2g + 2) leaves exactly the retained
     RESULT.json counts (530 strata, 511353002049 compressed N220 terminals/prefixes, 40 rows, all per-row data).

The counts are compressed terminals surviving necessary conditions, NOT complete Picard classes or curves.
No MAIN / FULL178 / effectivity / receiver / theorem / endpoint / merge credit.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RESULT = HERE / "RESULT.json"
sys.path.insert(0, str(ROOT / "stages/stage32/32-01-178/nodes/N220"))
sys.path.insert(0, str(ROOT / "stages/stage32/residual-32-01-production"))

import verify_n220_exact_symbolic_count as base           # noqa: E402
import verify_n220_exact_symbolic_count_fast as fast      # noqa: E402
from hperp_integral_adapter import HperpIntegralPairingAdapter  # noqa: E402

EXPECTED_N354 = [17128, 38560956534397137634780102]
EXPECTED_NEW = [530, 511353002049]


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def csha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def known_curves() -> dict:
    bundle = load_retained(ROOT / "stages/stage33/33-07/picard_base_rows_retained.py", "s32_unh_bundle")
    marking = load_retained(ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py", "s32_unh_marking")
    ad = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    full = ad.pairing_matrix * ad.class_coordinates_in_retained_basis.T
    if full != full.T:
        raise ValueError("recovered intersection matrix is not symmetric")
    out = {}
    for i in range(92):
        label = i + 1
        e = sum(int(full[i, k]) for k in range(92, 140))
        nu = sum(1 for k in range(92, 140) if full[i, k] > 0)
        num = sum(int(full[i, k]) for k in range(92)) + 5 * e
        if num % 19:
            raise ValueError(f"degree identity regression at label {label}")
        d = num // 19
        c2 = int(full[i, i])
        pa = (c2 + d + 2) // 2
        if c2 + d != 2 * pa - 2:
            raise ValueError(f"adjunction parity regression at label {label}")
        kind = "boundary_fibre_component" if 33 <= label <= 44 else ("conic" if pa == 0 else "genus1")
        lhs, rhs = 2 * nu, e + d - 4 * pa + 4
        s = out.setdefault(kind, {"count": 0, "holds": 0, "equality": 0, "profiles": set()})
        s["count"] += 1
        s["holds"] += lhs >= rhs
        s["equality"] += lhs == rhs
        s["profiles"].add((d, pa, e, nu))
    for s in out.values():
        s["profiles"] = sorted(s["profiles"])
    return out


def census() -> dict:
    manifest = base.load_canonical(ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json",
                                   base.EXPECTED_MANIFEST_CANONICAL)
    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178:
        raise ValueError("FULL178 row population regression")
    exact = base.build_exceptional_exact_mass_support()
    support_lt = fast.build_support_lt(exact)
    cum, run = [], 0
    for e in range(base.MAX_E + 1):
        run += sum(exact[e])
        cum.append(run)
    old, new, per_row = [0, 0], [0, 0], {}
    for row_id in rows:
        g, d = base.parse_row_id(row_id)
        K = ceil_div(d - 16 * g + 16, 4)
        for e in range(max(8 if g == 0 else 4, K), (19 * d) // 5 + 1):
            if d > e + 4 * g - 4 or (e & 1) or d < 2 * ceil_div(e, 6):
                continue
            block = 19 * d - 5 * e + 1
            old[0] += 1
            old[1] += (cum[e] - fast.rejected_fast(exact, support_lt, e=e, required=K)) * block
            surv = cum[e] - fast.rejected_fast(exact, support_lt, e=e,
                                               required=max(K, ceil_div(d + e, 2) - 2 * g + 2))
            if surv:
                new[0] += 1
                new[1] += surv * block
                r = per_row.setdefault(row_id, {"strata": 0, "terminals": 0, "e_range": [e, e]})
                r["strata"] += 1
                r["terminals"] += surv * block
                r["e_range"] = [min(r["e_range"][0], e), max(r["e_range"][1], e)]
    return {"n354_remaining": old, "new_remaining": new, "per_row": dict(sorted(per_row.items()))}


def main() -> None:
    retained = json.loads(RESULT.read_text())
    if retained.get("canonical_sha256_without_this_field") != csha(retained):
        raise ValueError("RESULT.json canonical regression")

    kc = known_curves()
    if [kc[k]["count"] for k in ("conic", "genus1", "boundary_fibre_component")] != [32, 48, 12]:
        raise ValueError(f"known-curve population regression: { {k: v['count'] for k, v in kc.items()} }")
    for k in ("conic", "genus1"):
        if kc[k]["holds"] != kc[k]["count"] or kc[k]["equality"] != kc[k]["count"]:
            raise ValueError(f"known-curve inequality regression for {k}: {kc[k]}")
    if kc["conic"]["profiles"] != [(2, 0, 6, 6)] or kc["genus1"]["profiles"] != [(4, 1, 4, 4)]:
        raise ValueError("known-curve profile regression")

    c = census()
    if c["n354_remaining"] != EXPECTED_N354:
        raise ValueError(f"audited N354 replay regression: {c['n354_remaining']}")
    if c["new_remaining"] != EXPECTED_NEW or len(c["per_row"]) != 40:
        raise ValueError(f"unibranch census regression: {c['new_remaining']} rows={len(c['per_row'])}")
    if c["per_row"] != retained["census"]["per_row"]:
        raise ValueError("per-row regression against RESULT.json")
    if retained["census"]["unibranch_node_hurwitz_remaining"] != EXPECTED_NEW:
        raise ValueError("RESULT.json headline regression")
    if any(retained["credit"].values()):
        raise ValueError("credit firewall regression")

    print("PASS: 80 known curves covered by the proposition satisfy 2nu >= e+d-4g+4, all with equality")
    print("PASS: audited N354 compressed census replays [17128, 38560956534397137634780102]")
    print("PASS: unibranch node-Hurwitz filter leaves [530, 511353002049] compressed terminals in 40 rows "
          "(not Picard classes); per-row data equal RESULT.json")
    print("PASS: zero credit; MAIN authority unchanged")


if __name__ == "__main__":
    main()
