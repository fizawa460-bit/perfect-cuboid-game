#!/usr/bin/env python3
import hashlib,json,subprocess,sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
ACTIVE="MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS={
"AMBIENT_MONODROMY_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-KUMMER-MONODROMY.md","0edeb77294919b9a7ad0dcce3030739b630c1fd1"),
"STACKS_KUMMER_SOURCE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STACKS-KUMMER-AMBIENT-ETALE-MONODROMY-SOURCE-NOTE.md","9ffdc5959baf3c28b98d46d99158f97f56c475c9"),
"AMBIENT_CHARACTER_FUNCTION":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-CHARACTER-FUNCTION.md","2bdb46e79be8a745880622c9c0643eb13ef20b26"),
"SQRT_BASECHANGE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SQRT-FACTOR-BASECHANGE-SEMANTICS.md","9d688ee48fd0df8d7ad4e2c6abc146fa2728ba7e"),
"RESIDUAL_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-RESIDUAL-SHEET-CHARACTER-CERTIFICATE.json","5e12d24f85d1fe27e53edab337bbacc45fb34cdb"),
"RESIDUAL_VERIFIER":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_residual_sheet_character.py","462df94d7abf6724b8d284c1894905e2bb3e9694"),
"HALF_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS-CERTIFICATE.json","28929222eb46b9d30be4fed9218143aa5fecaa78"),
"HALF_VERIFIER":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_one_factor_half_branch_class.py","3e43c9d3c7fb5096adf732203f4489e2c1fcd929"),
"HODGE_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SPLIT-HODGE-CONDUCTOR-CERTIFICATE.json","20511b7bfb81b5da37c76ebff8372a742bc7cf4b"),
"HODGE_VERIFIER":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_split_hodge_conductor.py","c592ade2eb02c13b58bbb6a51c0b33e46552585d"),
"INERTIA_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-SUPPORTED-INERTIA-RESIDUAL-SHEET-BOUNDARY-CERTIFICATE.json","a69ec41b301563eee20d4fd052e09dd68637f4a7"),
"INERTIA_VERIFIER":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_supported_inertia_residual_sheet_boundary.py","0523c4b537c0cae651e43188da0a1eaadcbdfe1e")}
REPLAYS=[("RESIDUAL_VERIFIER","PASS STAGE32_MB104_BALANCED16_000707_RESIDUAL_SHEET_CHARACTER_V1"),("HALF_VERIFIER","PASS STAGE32_MB104_BALANCED16_000707_ONE_FACTOR_HALF_BRANCH_CLASS_V1"),("HODGE_VERIFIER","PASS STAGE32_MB104_BALANCED16_000707_E2_SPLIT_HODGE_CONDUCTOR_V1"),("INERTIA_VERIFIER","PASS STAGE32_MB104_000707_E2_SUPPORTED_INERTIA_RESIDUAL_SHEET_BOUNDARY_V1")]
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
def main():
 r=root()
 for k,(rel,h) in LOCKS.items():
  p=r/rel; req(p.is_file(),f"missing {k}"); req(blob(p)==h,f"source lock {k}")
 for k,t in REPLAYS:
  cp=subprocess.run([sys.executable,str(r/LOCKS[k][0])],cwd=r,capture_output=True,text=True)
  req(cp.returncode==0,f"replay {k}: {cp.stdout}{cp.stderr}"); req(t in cp.stdout,f"token {k}")
 res=json.loads((r/LOCKS["RESIDUAL_CERT"][0]).read_text())
 half=json.loads((r/LOCKS["HALF_CERT"][0]).read_text())
 hodge=json.loads((r/LOCKS["HODGE_CERT"][0]).read_text())
 inert=json.loads((r/LOCKS["INERTIA_CERT"][0]).read_text())
 req(res["case_classification"]["e2_iff_eta_zero"] is True,"e2 eta=0")
 req(half["half_branch"]["relation"]=="2*L_abs ~ B_abs","half branch")
 req(hodge["conductor_budget"]["cross_sheet_delta_lower_bound"]=="y/2 >= 84*l^2","Hodge threshold")
 req(inert["routing"]["active_leaf"]==ACTIVE,"inertia leaf")
 req(inert["semantic_boundary"]["supported_node_plus_minus_exchanges_residual_G_over_H_sheets"] is False,"local +/- boundary")
 # retained exact chain; note identities are locked above
 delta=(2,1,-1); rhs=(2,2,0); B=(0,1,1); req(tuple(a-b for a,b in zip(rhs,B))==delta,"div(f_t)=2L_abs-B_abs")
 state=json.loads((HERE.parent.parent/"STATE.json").read_text())
 pri=json.loads((HERE.parent.parent/"PRIORITY-OVERRIDE-20260912.json").read_text())
 glob=(HERE/"GLOBAL-CLASSIFICATION-CHECKPOINT.md").read_text()
 req(state["next_obligation"]["active_leaf"]==ACTIVE,"STATE leaf")
 req(state["next_obligation"]["old_R8_route_status"]=="FROZEN_DOMINATED_UNTIL_PROGRESS_ENABLING_INPUT","STATE R8 frozen")
 req(state["mb104_checkpoint"]["ambient_kummer_conductor_chain_wrapper"]=="stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_ambient_kummer_conductor_chain.py","STATE wrapper")
 req(pri["next_execution_leaf"]==ACTIVE,"priority leaf")
 req(pri["direct_R8_alpha_lt_quarter_route"]=="FROZEN_UNTIL_PROGRESS_ENABLING_INPUT","priority R8 frozen")
 req(pri["ambient_kummer_conductor_chain_wrapper"]=="stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_ambient_kummer_conductor_chain.py","priority wrapper")
 req(ACTIVE in glob,"GLOBAL leaf")
 print("PASS STAGE32_MB104_000707_E2_AMBIENT_KUMMER_CONDUCTOR_CHAIN_V1")
 print("locked: ambient Kummer -> f_t -> weighted conductor character -> residual-lift conductor-pair map")
 print("firewall: e=2,e=4,000707 open; credit 0")
if __name__=="__main__": main()
