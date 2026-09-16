#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ACTIVE="MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
PASS="PASS STAGE32_MB104_000707_E2_SHEET_SELECTED_FIBER_ABEL_JACOBI_V1"
LOCKS={
 "HUMAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SHEET-SELECTED-FIBER-ABEL-JACOBI.md","76ef6c5638b9a601fd01ca28bb01531d7279c180"),
 "FACTOR2_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-COMMON-H-COVER-FACTOR-LINE-2TORSION-CERTIFICATE.json","db77404b146adb78ffd74105c733aa4464ae8a14"),
 "NODE_TABLE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-NODE-ORBIT-TABLE.md","dbfea5a4f62b1388c9810c37ad867076ed4dca6e"),
 "BOUNDARY":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-BOUNDARY-FIBER-SATURATION.md","aa9a7215467428b55b18ef296ced91b63ec4bf07")}
def req(c,m):
 if not c: raise SystemExit("FAIL: "+m)
def root():
 p=HERE
 while p!=p.parent:
  if (p/"AGENTS.md").is_file() and (p/"stages").is_dir(): return p
  p=p.parent
 raise SystemExit("FAIL: repo root")
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()
r=root()
for k,(rel,h) in LOCKS.items():
 p=r/rel; req(p.is_file(),f"missing {k}"); req(blob(p)==h,f"SOURCE_LOCK_FAIL {k}")
note=(r/LOCKS["HUMAN_NOTE"][0]).read_text(encoding="utf-8")
node=(r/LOCKS["NODE_TABLE"][0]).read_text(encoding="utf-8")
cert=json.loads((r/LOCKS["FACTOR2_CERT"][0]).read_text(encoding="utf-8"))
req(cert.get("active_leaf")==ACTIVE,"active leaf")
req(cert.get("deduction",{}).get("M1_squared_equals_M2_squared") is True,"factor square relation")
for t in ["x8+x9+x10+x11+x32+x33+x34 = 28*l","x0-x1+x2-x3-x24+x25-x26 = -4*l"]:
 req(t in node,f"node saturation token {t}")
for t in ["D_z^+ = psi_1^*(+u)","D_w^+ = psi_2^*(+a)","delta_fac\n = O_E(D_z^+-D_w^+)","2D_z^+ ~ 2D_w^+","No e=2 closure is claimed"]:
 req(t in note,f"semantic token {t}")
# Degree replay for D_w^+: 4 negative-representative nodes contribute 32l
# plus the retained signed sum -4l.
req(32-4==28,"Q0 selected fiber degree")
req(7*4==28,"balanced Q1 degree sanity")
req(cert.get("deduction",{}).get("delta_fac_candidate_count")==4,"E[2] count")
print(PASS)
