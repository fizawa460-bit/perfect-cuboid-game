#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import hashlib
import importlib.util
import json
import zlib
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
EXPECTED_CANONICAL = "e2c4d6e495fb613e33df1e865d3171aa759dbfb61fddd887b38301889ec688f1"
EXPECTED_MARKING = "e06291dddfc529fca2c0b0fe58dd43151faccd3d7997d9aa5797e1978227bb7c"
LOCKS = {
    "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    "stages/stage32/32-21/post-21bl-picard64-witness-adapter.json": "43eed149c5cbfc026f60ef5d86351e63ff59f89c",
    "stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py": "296e2005f822ae89c1aa085161553fe9ef76d077",
    "stages/stage32/residual-32-01-production/diagnose_stage32_post1473_x8_v4_cusp_quotient.py": "075389b05b035748320bd445a9f59270524f739a",
}
V4 = {
    "u": ((1, 4), (4, 1)),
    "v": ((5, 4), (0, 5)),
    "uv": ((5, 0), (4, 5)),
}


def csha(x: object) -> str:
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compose(p, q):
    return tuple(p[q[i] - 1] for i in range(len(p)))


def power(p, n):
    out = tuple(range(1, len(p) + 1))
    for _ in range(n):
        out = compose(out, p)
    return out


def cusp_canon(pair):
    a, c = pair[0] % 8, pair[1] % 8
    return min((a, c), ((-a) % 8, (-c) % 8))


def cusps():
    return sorted({cusp_canon((a, c)) for a in range(8) for c in range(8) if gcd(gcd(a, c), 8) == 1})


def cusp_perm(m, xs):
    idx = {x: i for i, x in enumerate(xs)}
    (a, b), (c, d) = m
    return tuple(idx[cusp_canon((a*x + b*y, c*x + d*y))] for x, y in xs)


def compose0(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", type=Path, required=True)
    args = ap.parse_args()

    for rel, want in LOCKS.items():
        got = git_blob_sha1(ROOT / rel)
        if got != want:
            raise SystemExit(f"source blob moved: {rel}: {got} != {want}")

    marking_mod = load_module(ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py", "s32_trace_marking")
    marking = marking_mod.load()
    if marking.get("canonical_sha256") != EXPECTED_MARKING:
        raise SystemExit("retained marking canonical moved")
    aut = marking.get("aut_action", {})
    if aut.get("schema") != "STAGE32_AUT_PERM_SOURCELOCK_V1":
        raise SystemExit("retained aut-action schema moved")
    perms = aut.get("permutations_1based")
    if not isinstance(perms, list) or len(perms) != 9:
        raise SystemExit("retained automorphism generator count moved")
    ident = tuple(range(1, 141))
    pp = []
    for p in perms:
        p = tuple(int(x) for x in p)
        if len(p) != 140 or sorted(p) != list(ident):
            raise SystemExit("retained automorphism permutation shape moved")
        pp.append(p)
    p1, p2 = pp[0], pp[1]
    if compose(p1, p1) != ident or compose(p2, p2) != ident:
        raise SystemExit("coordinate-swap generator ceased to be involutive")
    if compose(p1, p2) == compose(p2, p1):
        raise SystemExit("indices 1/2 unexpectedly commute; source trace must be revisited")
    prod = compose(p1, p2)
    if power(prod, 3) != ident or prod == ident:
        raise SystemExit("indices 1/2 product ceased to have order 3")

    xs = cusps()
    if len(xs) != 24:
        raise SystemExit("X8 cusp count moved")
    pu, pv, puv = (cusp_perm(V4[k], xs) for k in ("u", "v", "uv"))
    i0 = tuple(range(24))
    if any(compose0(p, p) != i0 for p in (pu, pv, puv)):
        raise SystemExit("deck representative ceased to be involutive on X8 cusps")
    if compose0(pu, pv) != puv or compose0(pv, pu) != puv:
        raise SystemExit("deck representatives ceased to form V4")
    if any(any(p[i] == i for i in range(24)) for p in (pu, pv, puv)):
        raise SystemExit("deck V4 ceased to act freely on X8 cusps")

    raw = json.loads(args.check.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_CANONICAL or csha(raw) != claimed:
        raise SystemExit("source-trace certificate canonical mismatch")
    print(json.dumps({
        "verdict": "PASS_PARTIAL_SOURCE_LOCK_DECK_TO_RETAINED_AUT_BRIDGE_OPEN",
        "retained_aut_generators": len(perms),
        "explicit_swap_indices_1_2_form_V4": False,
        "deck_mod8_V4_replayed": True,
        "next": raw["open_bridge"]["target"],
        "canonical_sha256": claimed,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
