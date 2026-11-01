#!/usr/bin/env python3
"""Ten bounded failure cases, normal and -O, with all mutations in temp copies."""
import argparse,hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def require(v,msg):
    if not v:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-certificate',action='store_true');a=ap.parse_args()
    original=json.loads((ROOT/'F65-certificate.json').read_text());names=list(original['files_sha256'])+['F65-certificate.json']
    before={n:sha(ROOT/n) for n in names};rows=[]
    cases=['false_existence','false_exclusion','zero_h1_shortcut','wrong_norm_codimension','wrong_gluing_rank',
           'wrong_nodal_cokernel','wrong_null_graph','altered_prior_with_updated_checksum','missing_prior','empty_hash_table']
    for case in cases:
        with tempfile.TemporaryDirectory(prefix='f65-negative-') as d:
            r=Path(d)
            for name in names:shutil.copy2(ROOT/name,r/name)
            c=json.loads((r/'F65-certificate.json').read_text());updated=False
            if case=='false_existence':c['claims']['genus_one_existence_proved']=True
            elif case=='false_exclusion':c['claims']['candidate_exclusion']=1
            elif case=='zero_h1_shortcut':c['claims']['all_m_h1_Y']=0
            elif case=='wrong_norm_codimension':c['computed']['norm_codim_coefficients'][0]=-4
            elif case=='wrong_gluing_rank':c['computed']['table'][0]['F37_gluing_rank_if_inputs_exist']=440
            elif case=='wrong_nodal_cokernel':c['computed']['table'][0]['nodal_map_cokernel_if_exists']=0
            elif case=='wrong_null_graph':c['computed']['X']['matrix'][0][1]=1
            elif case=='altered_prior_with_updated_checksum':
                p=r/'MB104-F64-20261029.zip';raw=bytearray(p.read_bytes());raw[len(raw)//2]^=1;p.write_bytes(raw);c['files_sha256'][p.name]=sha(p);updated=True
            elif case=='missing_prior':(r/'MB104-F64-20261029.zip').unlink()
            else:c['files_sha256']={}
            dump(r/'F65-certificate.json',c)
            for mode in ('normal','optimized'):
                command=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(r/'verify_f65.py')]
                z=subprocess.run(command,capture_output=True,text=True)
                require(z.returncode!=0,'negative accepted: '+case+' '+mode)
                rows.append({'case':case,'mode':mode,'rejected':True,'payload_checksum_updated':updated})
    require(before=={n:sha(ROOT/n) for n in names},'input payload changed')
    out={'schema':'MB104-F65-NEGATIVE-TESTS-v1','tests':rows,'all_20_rejected':True,'inputs_preserved':True}
    path=ROOT/'F65-negative-tests.json'
    if a.write_certificate:dump(path,out)
    else:require(json.loads(path.read_text())==out,'negative result mismatch')
    print(json.dumps({'status':'PASS','negative_checks':20,'inputs_preserved':True}))
if __name__=='__main__':main()
