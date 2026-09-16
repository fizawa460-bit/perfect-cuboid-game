#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
import types
from pathlib import Path

import sympy
from sympy import Matrix

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
RES = ROOT / "stages/stage32/residual-32-01-production"
S33 = ROOT / "stages/stage33/33-07"
TOP1 = ROOT / "stages/stage32/32-01-178/topdown-01"

PAIRING = RES / "pairing_prefix_engine.py"
HPERP = RES / "hperp_integral_adapter.py"
MARKING = S33 / "stage32_picard_marking_retained.py"
CONTRACT = TOP1 / "FULL178-SCALEOUT-CONTRACT.json"

LOCKS = {
    PAIRING: "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    HPERP: "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    MARKING: "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    CONTRACT: "ca1b195a3ee8e786707e1ef50b404ee8c19f1429",
}
EXPECTED_LABEL_SET = {49, 93, 94, 95, 96, 97, 98, 99, 101, 102, 103}


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def qstr(v: sympy.Expr) -> str:
    v = sympy.factor(v)
    return str(v)


def primitive_integer_vector(v: Matrix) -> list[int]:
    dens = [int(sympy.denom(x)) for x in v]
    lcm = 1
    for d in dens:
        lcm = sympy.ilcm(lcm, d)
    out = [int(x * lcm) for x in v]
    g = 0
    for x in out:
        g = sympy.igcd(g, abs(x))
    if g:
        out = [x // g for x in out]
    first = next((x for x in out if x), 0)
    if first < 0:
        out = [-x for x in out]
    return out


def verified_sources() -> dict[Path, bytes]:
    sources = {p: p.read_bytes() for p in LOCKS}
    for p, expected in LOCKS.items():
        got = git_blob_sha1(sources[p])
        if got != expected:
            raise RuntimeError(f"source-lock drift: {p.relative_to(ROOT)} got={got} expected={expected}")
    return sources


def load_modules(sources: dict[Path, bytes]):
    saved = {name: sys.modules.get(name) for name in ("pairing_prefix_engine", "hperp_integral_adapter", "td02_marking")}
    loaded = {}
    try:
        for name, path in (
            ("pairing_prefix_engine", PAIRING),
            ("hperp_integral_adapter", HPERP),
            ("td02_marking", MARKING),
        ):
            mod = types.ModuleType(name)
            mod.__file__ = str(path)
            sys.modules[name] = mod
            loaded[name] = mod
            exec(compile(sources[path], str(path), "exec"), mod.__dict__)
        return loaded
    finally:
        for name, old in saved.items():
            if old is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = old


def main() -> None:
    sources = verified_sources()
    contract = json.loads(sources[CONTRACT])
    labels = [int(x) for x in contract["mathematical_refinement"]["assignment_order_1based"]]
    if len(labels) != 11 or set(labels) != EXPECTED_LABEL_SET:
        raise RuntimeError(f"FULL178 label-order/set regression: {labels}")

    mods = load_modules(sources)
    marking = mods["td02_marking"].load()
    hp = mods["hperp_integral_adapter"]
    q, degree, linear, _caps, meta = hp._parse_hperp(marking["hperp_text"])

    rows = [j - 1 for j in labels]
    a = linear.extract(rows, list(range(63)))
    dvec = [int(degree[j - 1]) for j in labels]
    rank = int(a.rank())
    left_kernel = [primitive_integer_vector(v) for v in a.T.nullspace()]

    result = {
        "schema": "STAGE32_32_01_178_TD02_GRF04_HPERP_PROBE_V1",
        "source_blobs": {str(p.relative_to(ROOT)): h for p, h in LOCKS.items()},
        "labels_1based": labels,
        "degrees": dvec,
        "a_shape": list(a.shape),
        "a_rank": rank,
        "left_kernel_primitive_integer": left_kernel,
        "hperp_text_sha256": meta["hperp_text_sha256"],
        "q_determinant": int(meta["q_determinant"]),
        "credit": {
            "main": False,
            "theorem": False,
            "effectivity": False,
            "endpoint": False,
            "stage32_closed": False,
            "merge": False,
        },
    }

    if rank == 11:
        # Q is the positive-definite norm form on H^perp used by the retained
        # adapter: <C,C'> = deg(C)deg(C')/16 - ell(C) Q^-1 ell(C')^T.
        # Hence S=A Q^-1 A^T is the exact positive-definite constraint Gram.
        s = sympy.simplify(a * q.inv() * a.T)
        if s != s.T:
            raise RuntimeError("S symmetry regression")
        leading = [sympy.factor(s[:k, :k].det()) for k in range(1, 12)]
        if not all(v > 0 for v in leading):
            raise RuntimeError(f"S failed exact Sylvester positivity: {leading}")
        sinv = sympy.simplify(s.inv())
        result.update(
            s_matrix=[[qstr(s[i, j]) for j in range(11)] for i in range(11)],
            s_inverse=[[qstr(sinv[i, j]) for j in range(11)] for i in range(11)],
            s_determinant=qstr(sympy.factor(s.det())),
            s_leading_principal_minors=[qstr(v) for v in leading],
            s_positive_definite=True,
        )

    result["canonical_sha256_without_this_field"] = csha(result)
    out = HERE / "TD02-GRF04-HPERP-PROBE.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
