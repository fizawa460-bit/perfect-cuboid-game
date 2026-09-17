#!/usr/bin/env python3
import json, subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
def run(name,token):
 p=subprocess.run(["python",str(HERE/name)],capture_output=True,text=True)
 req(p.returncode==0 and token in p.stdout,name)
def main():
 c=json.loads((HERE/"ARMSTRONG-H1-PROMOTION-HANDOFF-CERTIFICATE.json").read_text())
 d=c["dependencies"]
 req(d["fixed_relations"]==128 and d["relation_matrix_shape"]==[459,64] and d["unimodular_witness_determinant"]==1,"matrix contract")
 run(Path(d["source_completeness_verifier"]),"PASS STAGE32_MB104_ARMSTRONG_FIBER_PRODUCT_H1_SOURCE_COMPLETENESS_V1")
 run(Path(d["ambient_h1_verifier"]),"PASS STAGE32_MB104_000707_E2_AMBIENT_H1_TORSION_KILL_V1")
 req(c["released_scope"]["ambient_H1_zero"] and c["released_scope"]["Pic_torsion_zero"] and c["released_scope"]["w_linearly_trivial"],"released chain")
 req(not any(c["firewall"].values()),"credit firewall")
 print("PASS STAGE32_MB104_ARMSTRONG_H1_PROMOTION_HANDOFF_V1")
if __name__=="__main__": main()
