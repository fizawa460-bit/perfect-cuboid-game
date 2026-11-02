#!/usr/bin/env python3
"""Twelve independent bounded certificate/payload failures, in both modes."""
import argparse,hashlib,json,shutil,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def require(v,m):
    if not v:raise ValueError(m)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,c):p.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--write-certificate',action='store_true');a=ap.parse_args()
    original=json.loads((ROOT/'F67-certificate.json').read_text())
    names=list(original['files_sha256'])+['F67-certificate.json'];before={n:sha(ROOT/n) for n in names};rows=[]
    cases=['false_finite_window','false_candidate_exclusion','point_support_shortcut','first_order_sufficient',
      'deformation_failure_excludes_base','lost_nilpotent','wrong_triple_second_order',
      'wrong_hilbert_jet_order','wrong_six_cokernel','altered_prior_updated_checksum','missing_prior','empty_hash_table']
    for case in cases:
        with tempfile.TemporaryDirectory(prefix='f67-negative-') as d:
            r=Path(d)
            for n in names:shutil.copy2(ROOT/n,r/n)
            c=json.loads((r/'F67-certificate.json').read_text());updated=False
            if case=='false_finite_window':c['claims']['population_wide_finite_window_proved']=True
            elif case=='false_candidate_exclusion':c['claims']['candidate_exclusion']=1
            elif case=='point_support_shortcut':c['claims']['requires_full_marked_collision_scheme_not_just_support']=False
            elif case=='first_order_sufficient':c['claims']['first_order_test_sufficient_for_full_norm']=True
            elif case=='deformation_failure_excludes_base':c['claims']['failure_of_chosen_deformation_excludes_base_candidate']=True
            elif case=='lost_nilpotent':c['computed']['local_ordinary_triple']['collision_algebra_basis']=['1']
            elif case=='wrong_triple_second_order':c['computed']['local_ordinary_triple']['required_second_order_coefficient']=[]
            elif case=='wrong_hilbert_jet_order':c['computed']['ordinary_partition_hilbert_examples'][3]['jets_sufficient']=0
            elif case=='wrong_six_cokernel':c['computed']['jet_cokernel_coefficients']=[0,0,0]
            elif case=='altered_prior_updated_checksum':
                p=r/'MB104-F66-20261029.zip';raw=bytearray(p.read_bytes());raw[len(raw)//2]^=1;p.write_bytes(raw)
                c['files_sha256'][p.name]=sha(p);updated=True
            elif case=='missing_prior':(r/'MB104-F66-20261029.zip').unlink()
            else:c['files_sha256']={}
            dump(r/'F67-certificate.json',c)
            for mode in ('normal','optimized'):
                cmd=[sys.executable]+(['-O'] if mode=='optimized' else [])+[str(r/'verify_f67.py')]
                run=subprocess.run(cmd,capture_output=True,text=True)
                require(run.returncode!=0,'negative accepted: '+case+' '+mode)
                rows.append({'case':case,'mode':mode,'rejected':True,'payload_checksum_updated':updated})
    require(before=={n:sha(ROOT/n) for n in names},'original inputs changed')
    out={'schema':'MB104-F67-NEGATIVE-TESTS-v1','tests':rows,'all_24_rejected':True,'inputs_preserved':True}
    if a.write_certificate:dump(ROOT/'F67-negative-tests.json',out)
    else:require(json.loads((ROOT/'F67-negative-tests.json').read_text())==out,'negative report mismatch')
    print(json.dumps({'status':'PASS','negative_checks':24,'inputs_preserved':True}))
if __name__=='__main__':main()
