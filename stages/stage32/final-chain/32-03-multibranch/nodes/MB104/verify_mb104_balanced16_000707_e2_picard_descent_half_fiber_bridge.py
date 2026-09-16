#!/usr/bin/env python3
"""Exact Picard64 half-fiber bridge; denylisted payload never reaches stdout."""
from __future__ import annotations
import hashlib, importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-DESCENT-HALF-FIBER-BRIDGE-CERTIFICATE.json"
PASS = "PASS STAGE32_MB104_000707_E2_PICARD_DESCENT_HALF_FIBER_BRIDGE_V2"
LOCKS = {
 "PICARD_BASE_RETAINED":("stages/stage33/33-07/picard_base_rows_retained.py","82e4d450a1d852e34f6615440fb88a029c6e54eb"),
 "PICARD_MARKING_RETAINED":("stages/stage33/33-07/stage32_picard_marking_retained.py","5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7"),
 "INTEGRAL_ADAPTER":("stages/stage32/residual-32-01-production/hperp_integral_adapter.py","fb1eb380ca786e42a6b00c5ef454b0e79fdba771"),
 "DIRECT_BRIDGE":("stages/stage32/residual-32-01-production/direct_picard_slice_bridge.py","be48bd94304d0217727c5c3368761d347cb22eaa"),
 "PICARD_DESCENT_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-PICARD-DESCENT-PARITY-CERTIFICATE.json","7621932b87a7558d473bc99a09b46bcb04a433a0"),
 "HALF_FIBER_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ABSENT-HALF-FIBER-PICARD.md","b7221c44a7c9c4d8c16bb4045ed4cfff379699bc"),
 "HALF_FIBER_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ABSENT-HALF-FIBER-PICARD-CERTIFICATE.json","5fdae0e985be1875417442203835879a206312a8"),
 "HALF_BRANCH_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS.md","e22de5a6f4be163268e699cde03d37e1e564d43b"),
 "HALF_BRANCH_CERT":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-ONE-FACTOR-HALF-BRANCH-CLASS-CERTIFICATE.json","28929222eb46b9d30be4fed9218143aa5fecaa78"),
 "GENERALIZED_JACOBIAN_NOTE":("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-GENERALIZED-JACOBIAN-GLUING-CHARACTER.md","b2816ce1a8554a9bee33acfb6cc76df066d73b74")}

def req(v,msg):
 if not v: raise SystemExit("FAIL: "+msg)
def root():
 p=HERE
 while p!=p.parent:
  if (p/'AGENTS.md').is_file() and (p/'stages').is_dir(): return p
  p=p.parent
 raise SystemExit('FAIL: repo root')
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()
def csha(v): return hashlib.sha256(json.dumps(v,separators=(',',':')).encode()).hexdigest()
def load(p,n):
 s=importlib.util.spec_from_file_location(n,p); req(s is not None and s.loader is not None,n)
 m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m.load()

def main():
 r=root(); cert=json.loads(CERT.read_text())
 req({x['id']:(x['path'],x['blob_sha1']) for x in cert['source_locks']}==LOCKS,'lock table')
 for k,(p,h) in LOCKS.items(): req((r/p).is_file() and blob(r/p)==h,'SOURCE_LOCK_FAIL '+k)
 base=load(r/LOCKS['PICARD_BASE_RETAINED'][0],'mb104_hf_base')
 mark=load(r/LOCKS['PICARD_MARKING_RETAINED'][0],'mb104_hf_mark')
 residual=r/'stages/stage32/residual-32-01-production'; sys.path.insert(0,str(residual))
 from hperp_integral_adapter import HperpIntegralPairingAdapter
 from direct_picard_slice_bridge import DirectPicardSliceBridge
 a=HperpIntegralPairingAdapter.from_retained(mark,base); b=DirectPicardSliceBridge.from_retained(mark,base)
 C=a.class_coordinates_in_retained_basis; H=list(map(int,b.hyperplane_coordinates))
 packets=[list(range(16,24)),list(range(40,48))]
 Es=[[sum(int(C[92+i,j]) for i in ns) for j in range(64)] for ns in packets]
 halves=[]
 for E in Es:
  v=[H[j]-E[j] for j in range(64)]; req(all(x%2==0 for x in v),'half integrality'); halves.append([x//2 for x in v])
 diff=[halves[0][j]-halves[1][j] for j in range(64)]
 req(all(2*diff[j]==Es[1][j]-Es[0][j] for j in range(64)),'difference identity')
 exact=cert['exact_lattice_result']
 req(csha(halves[0])==exact['L_a_coordinate_sha256'],'La hash')
 req(csha(halves[1])==exact['L_b_coordinate_sha256'],'Lb hash')
 req(csha(diff)==exact['L_a_minus_L_b_coordinate_sha256'],'difference hash')
 pc=json.loads((r/LOCKS['PICARD_DESCENT_CERT'][0]).read_text())
 req(pc['exact_result']['absent_span_rank']==15 and pc['exact_result']['membership_equation_rank']==14,'prior descent')
 req(pc['interpretation']['canonical_conditions']=='x_j = 0 mod 2 for every supported node j','even allocations')
 note=(r/LOCKS['HALF_FIBER_NOTE'][0]).read_text()
 req('2 (Q_a-Q_b)' in note and 'sum_(p in T_b)E_p - sum_(p in T_a)E_p' in note,'half-fiber semantics')
 hb=json.loads((r/LOCKS['HALF_BRANCH_CERT'][0]).read_text())
 req(hb['half_branch']['relation']=='2*L_abs ~ B_abs','half-branch relation')
 req(hb['carrier_restriction']['carrier_disjoint_from_B_abs'] is True and hb['carrier_restriction']['eta_equals_Delta_restriction'] is True,'half-branch restriction')
 gj=(r/LOCKS['GENERALIZED_JACOBIAN_NOTE'][0]).read_text()
 req('K_C[2] := Ker(Pic(C)[2] -> Pic(E)[2])' in gj and 'conductor/gluing character: kappa' in gj,'generalized Jacobian semantics')
 fw=cert['interpretation_firewall']; req(fw['packet_to_half_fiber_adapter_materialized'] is False and fw['geometric_bridge_requires_packet_adapter'] is True,'packet firewall')
 req(fw['unconditional_bridge']=='2*(M_a-M_b)=l*(E_b-E_a)','unconditional bridge')
 gb=cert['geometric_bridge_conditional']
 req(gb['singular_carrier_restriction_difference']=='kappa^l' and gb['normalization_only_evaluates_conductor'] is False,'singular bridge')
 h=cert['retained_hashes']; req(base['canonical_sha256']==h['picard_base_canonical_sha256'],'base canonical')
 req(mark['canonical_sha256']==h['marking_canonical_sha256'],'mark canonical')
 req(a.certificate['canonical_sha256_without_this_field']==h['adapter_canonical_sha256'],'adapter canonical')
 req(b.certificate['canonical_sha256_without_this_field']==h['bridge_canonical_sha256'],'bridge canonical')
 req(all(v is False for v in cert['credit_firewall'].values()),'credit firewall')
 print(PASS)
 print('absent_rank=15 H_corrections=2 halves_integral=true lattice_bridge=exact geometric_bridge=conditional singular_ratio=kappa^l e2_closed=false')
if __name__=='__main__': main()
