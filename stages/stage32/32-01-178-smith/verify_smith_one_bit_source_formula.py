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

AUDITED_HEAD="e3c4a04d5010e6dca9428722e334890e2614297a"
PATH="stages/stage32-ex1/verify_ex1_05af_s0_integral_ns_pullback_saturation.py"
BLOB="8591e5e25743b32b6768022052ae59746269d17e"


def git_blob_sha1(raw: bytes)->str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode()+raw).hexdigest()


def load():
    raw=subprocess.check_output(["git","show",f"{AUDITED_HEAD}:{PATH}"])
    assert git_blob_sha1(raw)==BLOB
    with tempfile.NamedTemporaryFile(suffix=".py") as f:
        f.write(raw); f.flush()
        spec=importlib.util.spec_from_file_location("old",f.name); assert spec and spec.loader
        m=importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
        return m


def parity_table(m):
    rows=[]
    for r in m.RES3:
        b=m.bits(r)
        # middle Gaussian block is index 1; its b-coordinate is odd iff that block is selected as type i.
        g2b = 1 if m.SELECTED[r]==1 else 0
        val=(b[2]+b[3]+g2b)&1
        rows.append({"residue":r,"a12_mod2":b[2],"b12_mod2":b[3],"g2b_mod2":g2b,"one_bit":val})
    return rows


def main():
    m=load()
    # Exact integer formulas obtained from the retained linear construction SUM*M*SUMINV2/2.
    # Verify them on every 6144 legal source F rather than trusting symbolic transcription.
    checked=0
    for r in m.RES3:
        opts=[m.gopts(n,"i" if j==m.SELECTED[r] else "id") for j,n in enumerate(m.NORMS)]
        for t in m.lifts[r]:
            a11,b11,a12,b12,a21,b21,a22,b22=t
            for gp in itertools.product(*opts):
                F,ok=m.build(t,gp); assert ok
                g2a,g2b=gp[1]
                assert F[4][0] == -2*b11-a12+b12-g2b
                assert F[4][9] == -2*b11-a12+b12+g2b
                assert (F[4][0]-F[4][9])%2==0
                assert F[4][0]%2 == (a12+b12+g2b)%2
                assert F[4][9]%2 == (a12+b12+g2b)%2
                checked+=1
    assert checked==6144
    table=parity_table(m)
    assert all(x["one_bit"]==1 for x in table)
    out={
      "schema":"STAGE32_32_01_178_SMITH_ONE_BIT_SOURCE_FORMULA_V1",
      "source":{"source_pr":1728,"hostile_review":5147627146,"audited_exact_head":AUDITED_HEAD,"builder_blob_sha1":BLOB},
      "exact_formula":{"F40":"-2*b11-a12+b12-g2b","F49":"-2*b11-a12+b12+g2b","common_mod2":"a12+b12+g2b","legal_F_checked":checked},
      "residue_parity_table":table,
      "interpretation":{"smith_coord0_is_not_scalar_g_d_e_data":True,"old_source_forcing":"the retained three mod-2 residues plus selected Gaussian block type force the common bit to 1","current_full178_adapter_established":False,"warning":"Do not import residues 73,97,235 as current FULL178 survivors; they are old source provenance only."},
      "credit":{"main_pruning_credit":False,"full178_completion":False,"theorem_credit":False,"endpoint_credit":False,"perfect_cuboid_claim":False}
    }
    raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
    out["canonical_sha256_without_this_field"]=hashlib.sha256(raw).hexdigest()
    print(json.dumps(out,sort_keys=True,separators=(",",":")))

if __name__=="__main__": main()
