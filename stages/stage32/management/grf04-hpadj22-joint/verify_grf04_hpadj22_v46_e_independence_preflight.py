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
H16=ROOT/"stages/stage32-ex5/hpadj-16_ex5/derive_q_quadratic_b_shard_mass_lp_bound.py"
H16_BLOB="61805f8b6d661c29805b6966e2453ed411d73189"
H22=ROOT/"stages/stage32-ex5/hpadj-22_ex5/bounded_exact_deletion_correlation.py"
H22_BLOB="98d84c925af74c35b99001b08d8428f997ab63ea"
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
    req(H16.is_file() and blob(H16)==H16_BLOB,"HPADJ16 source drift")
    req(H22.is_file() and blob(H22)==H22_BLOB,"HPADJ22 bounded gate drift")
    req(PROJ.is_file() and blob(PROJ)==PROJ_BLOB,"integer projection verifier drift")

    h16=H16.read_text(encoding="utf-8")
    h22=H22.read_text(encoding="utf-8")
    for token in [
        "n_min = 8 * h",
        "req(f0(h, g, b, c, n_min) > 0",
        "return left, lo",
    ]:
        req(token in h16,"HPADJ16 a0_interval source token drift: "+token)
    req("upper = min((19*d)//5, 3*d, 3*d - (b-c))" in h22,
        "HPADJ22 eligible_e upper-bound source token drift")

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
    print("PASS: bounded strict pilot retained with zero MAIN credit; high-d benchmark remains next gate")

if __name__=="__main__":
    main()
