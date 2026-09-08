#!/usr/bin/env python3
"""Goal4AK gen1: reproduce audited degree-31 denominator and prepare compact transport.

This leaf does not claim explicit F_B yet. It reconstructs the already-audited
numerator bytes from permanent repo chunks, replays the source-locked gen16
exact denominator materialization once, verifies all commitments, and emits a
small gzip denominator plus a compact manifest for later permanent repo
materialization. Local/BM/E1/Stage35/endpoint credit remains false.
"""
from __future__ import annotations

import argparse,base64,gzip,hashlib,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
MANIFEST=ROOT/'stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24-gzip-chunks.json'
GEN16=ROOT/'stages/stage35-ex/diagnose_stage35_ex_35_goal4aj_degree31_denominator_materialize_gen16.py'
SYNC=ROOT/'stages/stage35-ex/35ex-35/goal4aj-audited-claim-sync.json'

MANIFEST_BLOB='85b52e921f36fc445fd243db1a3b3f65bb298966'
GEN16_BLOB='c5dbf60343e037c947d9a3b813cb30e004f60fe6'
SYNC_BLOB='498a1e7554a8016863a6518cde91edd591f20b38'
NUM_SHA='358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb'
NUM_BYTES=208802
DEN_SHA='28d738a7a23df1ace371cabe3a476c270a54c6b7798e8172bd7111b14e25fc29'
DEN_BYTES=42489
DEN_TERMS=1542
DEN_CANONICAL='09683e1623b6c57ba1f96864fbcc47e51a878f032273a1da74327fa1b6b9122f'


def blob(p:Path)->str:
    b=p.read_bytes(); return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()

def csha(d:dict)->str:
    return hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def load_num()->bytes:
    m=json.loads(MANIFEST.read_text())
    texts=[]
    for row in m['parts']:
        p=ROOT/row['path']; b=p.read_bytes()
        assert hashlib.sha256(b).hexdigest()==row['text_sha256']
        texts.append(b.decode('ascii'))
    gz=base64.b64decode(''.join(texts),validate=True)
    raw=gzip.decompress(gz)
    assert len(raw)==NUM_BYTES and hashlib.sha256(raw).hexdigest()==NUM_SHA
    return raw

def reproduce_den()->tuple[bytes,dict]:
    cp=subprocess.run([sys.executable,'-B',str(GEN16)],text=True,capture_output=True,timeout=1500)
    if cp.returncode!=0: raise SystemExit('gen16 replay failed\n'+cp.stdout+'\n'+cp.stderr)
    lines=cp.stdout.splitlines()
    j=next((x for x in lines if x.startswith('GOAL4AJ_DEN31_GEN16_JSON=')),None)
    l=next((x for x in lines if x.startswith('GOAL4AJ_DEN31_LITERAL=')),None)
    if j is None or l is None or 'GOAL4AJ_DEN31_GEN16=DONE' not in lines: raise SystemExit('gen16 markers missing')
    meta=json.loads(j.split('=',1)[1]); den=l.split('=',1)[1].encode()
    assert meta['canonical_sha256']==DEN_CANONICAL
    assert meta['degree31']==31 and meta['degree31_expanded_term_count']==DEN_TERMS
    assert meta['degree31_literal_text_bytes']==DEN_BYTES
    assert meta['degree31_literal_sha256']==DEN_SHA
    assert meta['literal_denominator_coefficients_materialized'] is True
    assert meta['literal_F_B_materialized'] is False
    assert len(den)==DEN_BYTES and hashlib.sha256(den).hexdigest()==DEN_SHA
    return den,meta

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument('--output-dir',type=Path,required=True); a=ap.parse_args()
    assert blob(MANIFEST)==MANIFEST_BLOB
    assert blob(GEN16)==GEN16_BLOB
    assert blob(SYNC)==SYNC_BLOB
    sync=json.loads(SYNC.read_text())
    assert sync['goal4aj_audit']['hostile_audit_pass'] is True
    assert sync['literal_sections']['numerator_sha256']==NUM_SHA
    assert sync['literal_sections']['denominator_sha256']==DEN_SHA
    num=load_num(); den,meta=reproduce_den()
    out=a.output_dir; out.mkdir(parents=True,exist_ok=True)
    gz=gzip.compress(den,compresslevel=9,mtime=0)
    (out/'denominator.txt.gz').write_bytes(gz)
    cert={
      'schema':'STAGE35_EX_GOAL4AK_DENOMINATOR_TRANSPORT_GEN1_V1',
      'source_locks':{
        'goal4aj_claim_sync_blob_sha1':SYNC_BLOB,
        'numerator_manifest_blob_sha1':MANIFEST_BLOB,
        'gen16_blob_sha1':GEN16_BLOB,
        'gen16_canonical_sha256':DEN_CANONICAL,
      },
      'numerator_sha256':NUM_SHA,'numerator_text_bytes':len(num),'numerator_degree':31,
      'denominator_sha256':DEN_SHA,'denominator_text_bytes':len(den),'denominator_degree':31,
      'denominator_term_count':DEN_TERMS,
      'denominator_gzip_bytes':len(gz),'denominator_gzip_sha256':hashlib.sha256(gz).hexdigest(),
      'same_homogeneous_degree':True,
      'rational_function_pair_ready_for_permanent_repo_transport':True,
      'explicit_F_B_materialized':False,
      'local_evaluations_computed':False,'brauer_manin_obstruction_obtained':False,
      'E1_proved':False,'stage35_closed':False,'theorem_credit':False,'endpoint_credit':False,
      'planned_persisted_output_bytes':len(gz),
    }
    cert['canonical_sha256']=csha(cert)
    (out/'certificate.json').write_text(json.dumps(cert,indent=2,sort_keys=True)+'\n')
    print('GOAL4AK_DEN_TRANSPORT_GEN1_JSON='+json.dumps(cert,sort_keys=True,separators=(',',':')))
    print('GOAL4AK_DEN_TRANSPORT_GEN1=PASS')

if __name__=='__main__': main()
