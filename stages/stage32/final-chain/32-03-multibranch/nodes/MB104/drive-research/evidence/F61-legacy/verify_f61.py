#!/usr/bin/env python3
"""Read-only full replay of the F61 finite certificate and exact rank proof.

Requires Python 3 standard library and a C++17 compiler for two bounded
determinants. No historical verifier, external Python package, or CRT search
is used by this replay. Characteristic-zero lifting is proved in the note.
"""
from pathlib import Path
import argparse,contextlib,hashlib,io,json,subprocess,sys,tempfile
import build_f61_matrix as builder
import check_excluded_nodes as excluded
from check_f61_witness import gcd,dot

ROOT=Path(__file__).resolve().parent

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def expected_claims():
    return {'matrix_shape':[896,1464], 'field':'Q(i)', 'exact_rank':892,
            'full_section_space_dimension':572, 'normalized_fiber_affine_dimension':571,
            'rank_892_minor_determinant_mod97':32, 'evaluation_893_minor_determinant_mod97':50,
            'independent_exact_left_relations':4, 'gaussian_identities_checked':5856,
            'm1_distinct_cover_branches_per_supported_node':16,
            'excluded_A1_nodes':34,'m1_squarefree_tangent_forms':True,
            'two_tangent_forms_coprime_at_all_14':True,
            'all_m_local_construction':'products of distinct members of the lifted pencil',
            'all_m_integral_curve_proved':False,'genus_one_proved':False,
            'actual_source_adapter_audited':False,'candidate_exclusion':0,
            'MB104':'OPEN','theorem_credit':0,'independent_F61_audit':False}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--certificate',type=Path,default=ROOT/'F61-certificate.json');a=p.parse_args()
    cert=json.loads(a.certificate.read_text())
    assert cert['schema']=='MB104-F61-RESEARCH-CERT-v1'
    assert cert['claims']==expected_claims(), 'claim metadata mismatch'
    for relative,digest in cert['files_sha256'].items():
        assert sha(ROOT/relative)==digest,'input/source checksum mismatch: '+relative
    witness=json.loads((ROOT/'witness97.json').read_text())
    assert witness['characteristic_zero_lift']=='NOT_YET_ESTABLISHED', 'discovery record must preserve its original scope'
    vectors=witness['witnesses'];assert len(vectors)==2 and all(len(x)==1464 for x in vectors)
    with tempfile.TemporaryDirectory(prefix='f61-replay-') as tmp:
        tmp=Path(tmp);old=builder.ROOT;builder.ROOT=tmp
        try:
            with contextlib.redirect_stdout(io.StringIO()):builder.main()
        finally:builder.ROOT=old
        for name in ('A97.bin','leading97.bin','evaluations97.bin','matrix97.json'):
            assert (tmp/name).read_bytes()==(ROOT/name).read_bytes(),'matrix reconstruction mismatch: '+name
        raw=(tmp/'A97.bin').read_bytes();lead=(tmp/'leading97.bin').read_bytes();ev=(tmp/'evaluations97.bin').read_bytes()
        forms=[]
        for k,x in enumerate(vectors):
            assert all(dot(raw[r*1464:(r+1)*1464],x)==0 for r in range(896)),'jet equations fail'
            assert [dot(ev[:1464],x),dot(ev[1464:],x)]==[1,1]
            fx=[[dot(lead[(n*17+j)*1464:(n*17+j+1)*1464],x) for j in range(17)] for n in range(14)]
            assert fx==witness['leading_forms'][k], 'leading form certificate differs'
            assert all(f[0] and f[-1] and len(gcd(f,[(j*f[j])%97 for j in range(1,17)]))==1 for f in fx)
            forms.append(fx)
        assert all(len(gcd(f,g))==1 for f,g in zip(*forms))
        # Rebuild the 34-node evaluations in a disposable directory.
        (tmp/'witness97.json').write_bytes((ROOT/'witness97.json').read_bytes());old=excluded.ROOT;excluded.ROOT=tmp
        try:
            with contextlib.redirect_stdout(io.StringIO()):excluded.main()
        finally:excluded.ROOT=old
        assert (tmp/'F61-excluded-nodes97.json').read_bytes()==(ROOT/'F61-excluded-nodes97.json').read_bytes()
        assert all(all(row['values']) for row in json.loads((tmp/'F61-excluded-nodes97.json').read_text())['nodes'])
        proc=subprocess.run([sys.executable,str(ROOT/'check_exact_relations.py')],text=True,capture_output=True,check=True)
        exact=json.loads(proc.stdout)
        assert exact['rank_upper_bound']==892 and exact['checked_gaussian_identities']==5856
        (tmp/'rank97.txt').write_bytes((ROOT/'rank97.txt').read_bytes())
        executable=tmp/'verify_minors'
        subprocess.run(['g++','-O3','-std=c++17',str(ROOT/'verify_f61_minors.cpp'),'-o',str(executable)],capture_output=True,text=True,check=True)
        minor=json.loads(subprocess.run([str(executable),str(tmp)],capture_output=True,text=True,check=True).stdout)
        assert minor=={'prime':97,'rank_892_minor_determinant':32,'evaluation_893_minor_determinant':50}
    assert set(cert)=={'schema','claims','files_sha256'},'unexpected certificate fields'
    print(json.dumps({'status':'PASS','exact_rank':892,'full_kernel_dimension':572,
                      'fixed_fiber_affine_dimension':571,'four_exact_dependencies':True,
                      'two_mod97_witnesses_ordinary_at_14':True,'all_34_excluded_nodes_avoided':True,
                      'characteristic_zero_step':'unit-minor lifting; see proof note',
                      'candidate_exclusion':0,'MB104':'OPEN'}))

if __name__=='__main__':
    try:main()
    except Exception as exc:
        print('FAIL: '+str(exc),file=sys.stderr);sys.exit(1)
