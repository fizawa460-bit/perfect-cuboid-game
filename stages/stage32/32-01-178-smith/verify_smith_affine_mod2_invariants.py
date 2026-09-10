#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import subprocess
import tempfile
from collections import Counter

AUDITED_HEAD = "e3c4a04d5010e6dca9428722e334890e2614297a"
COMPACT_REPO_PATH = "stages/stage32-ex1/verify_ex1_05af_s0_integral_ns_pullback_saturation.py"
EXPECTED_COMPACT_BLOB_SHA1 = "8591e5e25743b32b6768022052ae59746269d17e"
N = 100


def git_blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def load_compact():
    raw = subprocess.check_output(["git", "show", f"{AUDITED_HEAD}:{COMPACT_REPO_PATH}"])
    assert git_blob_sha1(raw) == EXPECTED_COMPACT_BLOB_SHA1
    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(raw); f.flush()
        spec = importlib.util.spec_from_file_location("stage32_ex1_compact_audited_affine", f.name)
        assert spec and spec.loader
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        return mod


def flat_bits(F):
    x = 0
    for a in range(10):
        for b in range(10):
            if F[a][b] & 1:
                x |= 1 << (10*a+b)
    return x


def gf2_basis(vectors):
    piv = {}
    for x in vectors:
        y = x
        while y:
            p = y.bit_length()-1
            if p in piv: y ^= piv[p]
            else:
                piv[p] = y
                break
    return piv


def nullspace_of_rows(row_basis):
    # Solve rows dot x = 0 over F2 by RREF on row equations.
    rows = list(row_basis.values())
    # Build RREF keyed by leading low bit for convenient free-variable solve.
    piv = {}
    for r in rows:
        y=r
        while y:
            p=(y & -y).bit_length()-1
            if p in piv: y ^= piv[p]
            else:
                piv[p]=y
                for q in list(piv):
                    if q!=p and ((piv[q]>>p)&1): piv[q] ^= y
                break
    pivot_cols=sorted(piv)
    free=[j for j in range(N) if j not in piv]
    out=[]
    for f in free:
        x=1<<f
        for p in reversed(pivot_cols):
            # Equation x_p + sum_{j!=p} r_j x_j =0.
            r=piv[p] ^ (1<<p)
            if (r & x).bit_count() & 1:
                x |= 1<<p
        out.append(x)
    # verify
    for x in out:
        assert all(((r & x).bit_count() & 1)==0 for r in rows)
    return out


def support(x):
    return [[j//10,j%10] for j in range(N) if (x>>j)&1]


def parity(x):
    return x.bit_count() & 1


def main():
    c=load_compact()
    Fset=set()
    for r in c.RES3:
        opts=[c.gopts(n,"i" if j==c.SELECTED[r] else "id") for j,n in enumerate(c.NORMS)]
        for t in c.lifts[r]:
            for gp in itertools.product(*opts):
                F,ok=c.build(t,gp); assert ok
                Fset.add(flat_bits(F))
    assert len(Fset)==1536
    xs=sorted(Fset)
    x0=xs[0]
    diffs=[x^x0 for x in xs[1:]]
    basis=gf2_basis(diffs)
    rank=len(basis)
    null=nullspace_of_rows(basis)
    codim=len(null)
    assert rank+codim==N

    constraints=[]
    for v in null:
        val=parity(v & x0)
        constraints.append({"support":support(v),"weight":v.bit_count(),"constant":val})
    constraints.sort(key=lambda z:(z["weight"],z["constant"],z["support"]))

    # Enumerate the whole dual invariant space only if tractable, to find truly minimal odd constraints.
    min_odd_weight=None; min_odd=[]; min_even_weight=None; min_even=[]
    if codim <= 20:
        for mask in range(1,1<<codim):
            v=0
            for i,b in enumerate(null):
                if (mask>>i)&1: v ^= b
            val=parity(v & x0); w=v.bit_count()
            if val:
                if min_odd_weight is None or w<min_odd_weight:
                    min_odd_weight=w; min_odd=[support(v)]
                elif w==min_odd_weight and len(min_odd)<32:
                    min_odd.append(support(v))
            else:
                if min_even_weight is None or w<min_even_weight:
                    min_even_weight=w; min_even=[support(v)]
                elif w==min_even_weight and len(min_even)<32:
                    min_even.append(support(v))

    fixed=[]
    for j in range(N):
        vals={(x>>j)&1 for x in xs}
        if len(vals)==1: fixed.append({"entry":[j//10,j%10],"value":next(iter(vals))})

    out={
      "schema":"STAGE32_32_01_178_SMITH_AFFINE_MOD2_INVARIANTS_V1",
      "source":{"source_pr":1728,"hostile_review":5147627146,"audited_exact_head":AUDITED_HEAD,"builder_blob_sha1":EXPECTED_COMPACT_BLOB_SHA1},
      "family":{"unique_legal_F_mod2":len(xs),"ambient_bits":N,"affine_span_dimension":rank,"affine_codimension":codim,"fixed_coordinate_count":len(fixed),"fixed_coordinates":fixed},
      "dual_affine_constraints":{"basis":constraints,"enumerated_full_dual_space":codim<=20,"minimal_constant_one_weight":min_odd_weight,"minimal_constant_one_supports":min_odd,"minimal_constant_zero_weight":min_even_weight,"minimal_constant_zero_supports":min_even},
      "smith_link":{"smith_coord0_old_source":"F[4,0]=1 or F[4,9]=1 depending on JI; both are fixed-one affine constraints","basis_independent_interpretation_established":False},
      "credit":{"main_pruning_credit":False,"full178_completion":False,"theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_claim":False}
    }
    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    out["canonical_sha256_without_this_field"]=hashlib.sha256(raw).hexdigest()
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__": main()
