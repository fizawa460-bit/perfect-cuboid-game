#!/usr/bin/env python3
"""Ten bounded failure cases under normal and optimized Python, in temp copies."""
import argparse,hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def require(v,msg):
    if not v:raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
def main():
    p=argparse.ArgumentParser();p.add_argument('--write-certificate',action='store_true');a=p.parse_args()
    original=json.loads((ROOT/'F64-certificate.json').read_text())
    names=list(original['files_sha256'])+['F64-certificate.json']
    before={x:sha(ROOT/x) for x in names};rows=[]
    cases=['false_genus_one_existence','wrong_generic_genus','double_node_count','wrong_intersection',
           'missing_chart','wrong_cubic_monomial','corrupt_prior_with_updated_checksum','missing_prior',
           'false_credit','empty_hash_table']
    for case in cases:
        with tempfile.TemporaryDirectory(prefix='f64-negative-') as d:
            r=Path(d)
            for name in names:shutil.copy2(ROOT/name,r/name)
            c=json.loads((r/'F64-certificate.json').read_text());updated=False
            if case=='false_genus_one_existence':c['claims']['genus_one_locus_existence_proved']=True
            elif case=='wrong_generic_genus':c['computed']['genus_table'][0]['smooth_half_genus']=448
            elif case=='double_node_count':c['claims']['all_m_generic_off_support_ordinary_nodes']='672*m^2'
            elif case=='wrong_intersection':c['computed']['intersections']['intersection_matrix'][0][2]=2
            elif case=='missing_chart':c['computed']['canonical_charts']['charts'].pop()
            elif case=='wrong_cubic_monomial':c['computed']['cubic_jets']['monomials'][0][0]=2
            elif case=='corrupt_prior_with_updated_checksum':
                q=r/'MB104-F63-20261029.zip';raw=bytearray(q.read_bytes());raw[len(raw)//2]^=1;q.write_bytes(raw)
                c['files_sha256'][q.name]=sha(q);updated=True
            elif case=='missing_prior':(r/'MB104-F63-20261029.zip').unlink()
            elif case=='false_credit':c['claims']['theorem_credit']=999
            elif case=='empty_hash_table':c['files_sha256']={}
            dump(r/'F64-certificate.json',c)
            for mode in ('normal','optimized'):
                command=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(r/'verify_f64.py')]
                run=subprocess.run(command,capture_output=True,text=True)
                require(run.returncode!=0,'negative accepted: '+case+' '+mode)
                rows.append({'case':case,'mode':mode,'rejected':True,'payload_checksum_updated':updated})
    require(before=={x:sha(ROOT/x) for x in names},'input changed')
    result={'schema':'MB104-F64-NEGATIVE-TESTS-v1','tests':rows,'all_20_rejected':True,'inputs_preserved':True}
    out=ROOT/'F64-negative-tests.json'
    if a.write_certificate:dump(out,result)
    else:require(json.loads(out.read_text())==result,'negative certificate mismatch')
    print(json.dumps({'status':'PASS','negative_checks':20,'inputs_preserved':True}))
if __name__=='__main__':main()
