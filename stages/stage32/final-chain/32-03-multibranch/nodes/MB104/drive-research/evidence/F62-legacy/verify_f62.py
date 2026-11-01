#!/usr/bin/env python3
"""Read-only F62 checks. The geometric theorem applications are in the note.

The four-conjugate norm calculation is independent of the closed norm
formula in norm_slices.py. F61 is an explicit conditional input boundary.
"""
from pathlib import Path
import argparse,json,hashlib,subprocess,sys,tempfile,zipfile
import norm_slices as n
ROOT=Path(__file__).resolve().parent

def multiply_biquadratic(x,y,u2,v2):
    out=[[],[],[],[]]
    for a,pa in enumerate(x):
        for b,pb in enumerate(y):
            value=n.mul(pa,pb)
            if a&b&1:value=n.mul(value,u2)
            if a&b&2:value=n.mul(value,v2)
            out[a^b]=n.add(out[a^b],value)
    return out
def conjugate_norm(parts,t):
    q=pow(t,4,97);iv=pow(16,-1,97)
    u2=[4*(q+4)*iv%97,0,0,0,(q+4)*iv%97]
    v2=[-4*(q-4)*iv%97,0,0,0,(q-4)*iv%97]
    value=[[1],[],[],[]]
    for u_sign,v_sign in [(1,1),(-1,1),(1,-1),(-1,-1)]:
        signs=[1,u_sign,v_sign,u_sign*v_sign]
        value=multiply_biquadratic(value,[n.scale(p,s) for p,s in zip(parts,signs)],u2,v2)
    assert value[1:]==[[],[],[]]
    return value[0]

def claims():
    return {'scope':'SOURCE_CONDITIONAL_MODEL_MATH_UNAUDITED_ZERO_CREDIT',
            'prior_m1_section_dimension':572,'exceptional_curve_degree':16,
            'exceptional_restriction_dimension_bound':17,'restriction_kernel_lower_bound':555,
            'linear_system_image_dimension':2,'no_fixed_curve_components':True,
            'all_m_integral_local_model_existence':True,
            'all_m_ordinary_branches_per_supported_A1':'16*m','supported_A1_nodes':14,'excluded_A1_nodes':34,
            'strict_class':'m*(14H-8*sum(E_support))',
            'strict_self_intersection_coefficient':1344,'canonical_intersection_coefficient':224,
            'arithmetic_genus':'672*m^2+112*m+1','genus_one_required_delta':'672*m^2+112*m',
            'geometric_genus_one_proved':False,'normalization_genus_determined':False,
            'norm_split_proved':False,'actual_source_adapter_proved':False,
            'candidate_exclusion':0,'MB104':'OPEN','theorem_credit':0,'independent_F62_audit':False}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--certificate',type=Path,default=ROOT/'F62-certificate.json');p.add_argument('--replay-f61',action='store_true');a=p.parse_args()
    cert=json.loads(a.certificate.read_text());assert cert['schema']=='MB104-F62-RESEARCH-CERT-v1'
    assert cert['claims']==claims(),'claim scope mismatch'
    columns,vectors=n.inputs();observed=json.loads((ROOT/'F62-norm-slices97.json').read_text());computed=n.calculate();assert observed==computed
    for row in observed['slices']:
        assert row['degree']==[112,112] and all(row['leading_coefficients'])
        for x,expected in zip(vectors,row['norms']):
            actual=conjugate_norm(n.section_slice(columns,x,row['fixed_leg'],row['value']),row['value'])
            assert actual==expected,'four-conjugate norm mismatch'
        assert n.add(n.mul(row['bezout'][0],row['norms'][0]),n.mul(row['bezout'][1],row['norms'][1]))==[1]
    assert [r['fixed_leg'] for r in observed['slices']]==['z','w']
    assert 572-(16+1)==555>0
    assert 14**2*16-8**2*14*2==1344 and 14*16==224
    assert 1344//2==672 and 224//2==112
    for name,h in cert['files_sha256'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h,'input checksum mismatch: '+name
    assert set(cert)=={'schema','claims','files_sha256'}
    if a.replay_f61:
        with tempfile.TemporaryDirectory(prefix='f62-prior-replay-') as tmp:
            tmp=Path(tmp)
            with zipfile.ZipFile(ROOT/'MB104-F61-20261028.zip') as z:z.extractall(tmp)
            subprocess.run([sys.executable,str(tmp/'verify_f61.py')],check=True,capture_output=True,text=True)
    print(json.dumps({'status':'PASS','coprime_full_degree_norm_slices':2,'four_conjugate_norms_checked':4,
                      'exceptional_dimension_contradiction':'572>17',
                      'all_m_integral_existence':'conditional geometric deduction; see proof',
                      'genus_one_proved':False,'candidate_exclusion':0,'MB104':'OPEN'}))
if __name__=='__main__':
    try:main()
    except Exception as exc:print('FAIL: '+str(exc),file=sys.stderr);sys.exit(1)
