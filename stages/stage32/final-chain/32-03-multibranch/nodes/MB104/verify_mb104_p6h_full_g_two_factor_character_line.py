#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

BASE="stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
LOCKS={
 f"{BASE}/MB104-P6D2-AUTOMATIC-ODD-EQUALITY-CERTIFICATE.json":"3924212bb64e2f377dc8be2311ed6e15ba764cbf",
 f"{BASE}/MB104-P6G-SIX-VALUE-HURWITZ-FEASIBILITY-CERTIFICATE.json":"0139b814d2cfdb18e3a066903ae3b8a626bff9c3",
}

def req(c:bool,m:str)->None:
 if not c: raise SystemExit('FAIL: '+m)

def blob(p:Path)->str:
 b=p.read_bytes()
 return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def main()->None:
 root=Path(__file__).resolve().parents[6]
 for rel,sha in LOCKS.items():
  p=root/rel
  req(p.is_file(),'missing '+rel)
  req(blob(p)==sha,'blob '+rel)
 c=json.loads(Path(__file__).with_name('MB104-P6H-FULL-G-TWO-FACTOR-CHARACTER-LINE-CERTIFICATE.json').read_text())
 req(c['group']['rank']==3,'G rank')
 req(c['group']['inertia_types']==3,'inertia types')
 req(c['group']['total_branch_values']==6,'branch values')
 # For three independent inertia generators, nonzero character weights are 1^3,2^3,3^1.
 req(c['character_weights']['weight1']['count']==3,'weight1 count')
 req(c['character_weights']['weight2']['count']==3,'weight2 count')
 req(c['character_weights']['weight3']['count']==1,'weight3 count')
 req(c['character_weights']['weight3']['base_building_line_degree']==3,'weight3 line degree')
 degM=c['per_l']['factor_degree']
 degRam=c['per_l']['total_ramification_degree']
 req(degRam==2*degM,'elliptic RH degree')
 # N_all=M^3(-Ram), and O(Ram)=M^2, hence N_all=M.
 req(3*degM-degRam==degM,'weight3 degree reduction')
 req(c['weight3_reduction']['N_all_equals_M_i'] is True,'N_all=M')
 req(c['weight3_reduction']['M1_isomorphic_M2'] is True,'M1=M2')
 u=c['per_l']['unramified_type_degrees']
 r=c['per_l']['ramified_type_degrees']
 req([2*(degM-x) for x in r]==u,'character branch divisor degrees')
 req(c['weight1_reduction']['degrees_l']==r,'type ram degrees')
 req(c['weight1_reduction']['typewise_ramification_linearly_equivalent'] is True,'typewise equivalence')
 req(all(v is False for v in c['firewalls'].values()),'credit firewall')
 print('PASS: P6H full-G two-factor character-line coupling')
 print('weight-3 character: M1 ~= M2')
 print('weight-1 characters: typewise ramification divisor classes match')
 print('carrier existence remains OPEN')

if __name__=='__main__':
 main()
