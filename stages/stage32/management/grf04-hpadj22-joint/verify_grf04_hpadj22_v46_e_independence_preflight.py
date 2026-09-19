#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
ART=HERE/"GRF04-HPADJ22-V46-E-INDEPENDENCE-PREFLIGHT.json"
ART_BLOB="3bbfd8d4e69a46d32e00dd8147e6892ce34a79c7"
ART_CANON="9892eda3ae91f2388b62571e4d6aee69afaa456dcd8214397d122a798e2ba805"
PILOT=HERE/"GRF04-HPADJ22-V46-BOUNDED-PILOT-RETAINED.json"
PILOT_BLOB="6b0bceeb562433045449f928343ad5fcd9073af4"
PILOT_CANON="713cb7725bf9ddf0fb38f7efba5c8e2ac6f5a25757b3e9f7ac4347e3827c4db9"
PROJ=ROOT/"stages/stage32/management/grf04-quadratic-capacity/verify_grf04_main_bc_qt_integer_projection_preflight.py"
PROJ_BLOB="6b85abcd693586191eb83a7f275b8dd5d9c69b18"

def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)

def blob(p):
    b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()

def canon(o):
    x=dict(o); x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def locked_json(p,b,c,label):
    req(p.is_file(), "missing "+label)
    req(blob(p)==b,label+" blob drift")
    o=json.loads(p.read_text(encoding="utf-8"))
    req(o.get("canonical_sha256_without_this_field")==c,label+" stored canonical drift")
    req(canon(o)==c,label+" canonical drift")
    return o

def main():
    art=locked_json(ART,ART_BLOB,ART_CANON,"e-independence preflight")
    pilot=locked_json(PILOT,PILOT_BLOB,PILOT_CANON,"bounded pilot")
    req(PROJ.is_file() and blob(PROJ)==PROJ_BLOB,"integer projection verifier drift")
    locks=art["source_locks"]
    req(locks["hpadj16_source_blob_sha1"]=="61805f8b6d661c29805b6966e2453ed411d73189","retained HPADJ16 source lock")
    req(locks["hpadj22_bounded_gate_blob_sha1"]=="98d84c925af74c35b99001b08d8428f997ab63ea","retained HPADJ22 gate source lock")
    req(locks["integer_projection_verifier_blob_sha1"]==PROJ_BLOB,"retained projection source lock")
    req(pilot["source_locks"]["hpadj22_source_head"]=="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2","pilot source head")
    req(pilot["source_locks"]["direct_count_blob_sha1"]=="e965ab0a6ea51938006882ca2110016f48b3768e","pilot direct-count source")
    req(pilot["source_locks"]["old_hpadj22_worker_blob_sha1"]=="2c998a190baaf5f29b33a91fd9efedbb036cef46","pilot HPADJ22 worker source")

    checked=0
    for d in range(8,193,2):
        x4_max=4*d-1
        for e in range(0,3*d+1,2):
            n=19*d-5*e
            req(n>=4*d,f"n lower-bound regression {(d,e,n)}")
            req(x4_max<n,f"x4/n separation regression {(d,e,x4_max,n)}")
            checked+=1

    r=pilot["result"]
    req(r["hpadj22_bounded_exact_survivors"]==345693595,"pilot HPADJ22 count")
    req(r["joint_bounded_exact_survivors"]==310971189,"pilot joint count")
    req(r["exact_improvement"]==34722406 and r["strict_row_count"]==10 and r["strict_all_rows"] is True,
        "pilot strict witness")
    req(art["proof"]["consequence"].startswith("the min(n, raw_hi) cap"),"proof consequence drift")
    req(art["next_gate"]["full178_scaleout_authorized"] is False,"premature scaleout authorization")
    for k,v in art["firewalls"].items():
        req(v is False,"firewall "+k)
    print(f"PASS: GRF04 x4 interval e-independence verified over {checked} finite (d,e) pairs")
    print("PASS: exact rewrite may count x4 intersection once and multiply by eligible-e count")
    print("PASS: retained historical source-lock identities are bound; exact source checkout replay is delegated to the high-d benchmark job")\n    print("PASS: bounded strict pilot retained with zero MAIN credit; high-d benchmark remains next gate")

if __name__=="__main__":
    main()
