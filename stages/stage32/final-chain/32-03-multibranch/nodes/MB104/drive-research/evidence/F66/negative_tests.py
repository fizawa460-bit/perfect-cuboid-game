#!/usr/bin/env python3
"""Ten certificate/payload failures in both Python modes; originals unchanged."""
import argparse,hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def require(v,m):
    if not v:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,c):p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-certificate',action='store_true');a=ap.parse_args()
    original=json.loads((ROOT/'F66-certificate.json').read_text())
    names=list(original['files_sha256'])+['F66-certificate.json'];before={n:sha(ROOT/n) for n in names}
    cases=['false_exclusion','unmarked_data_accepted','all_nodal_claim','rank_sufficient_claim',
      'six_dependencies_removed','wrong_koszul_sign','wrong_toy_derivative',
      'altered_prior_with_updated_checksum','missing_prior','empty_hash_table'];rows=[]
    for case in cases:
        with tempfile.TemporaryDirectory(prefix='f66-negative-') as d:
            r=Path(d)
            for n in names:shutil.copy2(ROOT/n,r/n)
            c=json.loads((r/'F66-certificate.json').read_text());updated=False
            if case=='false_exclusion':c['claims']['candidate_exclusion']=1
            elif case=='unmarked_data_accepted':c['claims']['requires_complete_marked_mixed_node_set']=False
            elif case=='all_nodal_claim':c['claims']['all_candidates_nodal']=True
            elif case=='rank_sufficient_claim':c['claims']['rank_condition_sufficient_for_global_norm']=True
            elif case=='six_dependencies_removed':c['computed']['evaluation_cokernel_coefficients']=[0,0,0]
            elif case=='wrong_koszul_sign':c['computed']['equivariant_toy']['koszul_kernel_character']=1
            elif case=='wrong_toy_derivative':c['computed']['equivariant_toy']['derivative_matrix'][0][0]=1
            elif case=='altered_prior_with_updated_checksum':
                p=r/'MB104-F65-20261029.zip';raw=bytearray(p.read_bytes());raw[len(raw)//2]^=1;p.write_bytes(raw)
                c['files_sha256'][p.name]=sha(p);updated=True
            elif case=='missing_prior':(r/'MB104-F65-20261029.zip').unlink()
            else:c['files_sha256']={}
            dump(r/'F66-certificate.json',c)
            for mode in ('normal','optimized'):
                cmd=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(r/'verify_f66.py')]
                run=subprocess.run(cmd,capture_output=True,text=True)
                require(run.returncode!=0,'negative accepted: '+case+' '+mode)
                rows.append({'case':case,'mode':mode,'rejected':True,'payload_checksum_updated':updated})
    require(before=={n:sha(ROOT/n) for n in names},'original payload changed')
    out={'schema':'MB104-F66-NEGATIVE-TESTS-v1','tests':rows,'all_20_rejected':True,'inputs_preserved':True}
    if a.write_certificate:dump(ROOT/'F66-negative-tests.json',out)
    else:require(json.loads((ROOT/'F66-negative-tests.json').read_text())==out,'negative report mismatch')
    print(json.dumps({'status':'PASS','negative_checks':20,'inputs_preserved':True}))
if __name__=='__main__':main()
