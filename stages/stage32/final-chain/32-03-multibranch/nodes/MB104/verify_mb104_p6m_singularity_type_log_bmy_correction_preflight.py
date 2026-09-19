#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
BASE="stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
LOCKS={
 f"{BASE}/MB104-P6M-SINGULARITY-TYPE-LOG-BMY-CORRECTION-PREFLIGHT-WALL-20260919.md":"f1b0037a7207c6bb137a72ab1f337f2f2eb52e18",
 f"{BASE}/MB104-P6L-LOW-GENUS-MIYAOKA-BOGOMOLOV-PREFLIGHT-WALL-20260919.md":"a653c0077f1c751cbfffb982e870cddae731b5c5",
 f"{BASE}/MB104-P6F-BIG-NEF-EQUIGENERIC-RIGIDITY-GATE-20260919.md":"e89426128010ae97a10fbd908346f6cf07fff109",
 f"{BASE}/MB104-P6D2-AUTOMATIC-ODD-EQUALITY-20260919.md":"1194fdd228c394d79262579df3930b4d8f619cf9",
}
def blob(p):
 b=p.read_bytes(); return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def req(c,m):
 if not c: raise SystemExit("FAIL: "+m)
def main():
 root=Path(__file__).resolve().parents[6]
 for rel,sha in LOCKS.items():
  p=root/rel; req(p.is_file(),"missing "+rel); req(blob(p)==sha,"blob "+rel)
 d=json.loads(Path(__file__).with_name("MB104-P6M-SINGULARITY-TYPE-LOG-BMY-CORRECTION-PREFLIGHT-CERTIFICATE.json").read_text())
 for l in (1,2,3,10,100):
  delta=168*l*l+56*l
  req(delta>112*l,"quadratic delta dominates known linear contacts")
 req(d["retained_local_control"]["every_exceptional_contact_m1"] is True,"m=1")
 req(d["retained_local_control"]["all_AB_11_proved"] is False,"AB firewall")
 req(d["retained_local_control"]["off_exceptional_delta_controlled"] is False,"off delta firewall")
 req(d["asymptotics"]["uncontrolled_quadratic_singularity_mass"] is True,"quadratic gap")
 req(d["firewalls"]["refined_log_BMY_applied"] is False,"do not apply refined theorem")
 req(all(v is False for v in d["firewalls"].values()),"credit firewall")
 print("PASS: P6M singularity-type correction interface wall")
 print("delta=168*l^2+56*l; source-locked exceptional contacts=112*l")
 print("quadratic singularity-type mass remains uncontrolled")
 print("refined log/orbifold BMY not applied")
if __name__=="__main__": main()
