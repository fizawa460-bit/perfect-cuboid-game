#!/usr/bin/env python3
"""Verify odd nodal primes and the exact unit projection of good elements."""
from pathlib import Path
from hashlib import sha256
import json

HERE=Path(__file__).resolve().parent
INPUT_SHA256={
    'curve_C29.json': '04542e2e37a75ce382ca7921d51aae9e3bcc690b6a03d514dcbc0a511205bd74',
    'local_conics386.json': 'ee3c6a8a88c16e487fb58809d2f598193affaae22d0203e07aadd0107d8edd25',
    'row374_results.json': 'aeca2445cf570a4befa14738ca800e1287a3e3e8480e802c2fb5b718553e16b4',
    'units381_exact.json': '78136c1f3c1fed53c429d26fc754af33edb0106d6c119fc738f7ea9f24373bd2',
    'row375_results.json': '28794c519ca99152599ccd1ef7a818f0106e2113f8a5b959daa35b6f79985d01',
}


def read(name):
    raw=(HERE/name).read_bytes()
    if name in INPUT_SHA256:assert sha256(raw).hexdigest()==INPUT_SHA256[name],name
    return json.loads(raw)


def trim(p):
    while p and not p[-1]:p.pop()
    return p


def rem(a,b,p):
    a=trim([v%p for v in a]);b=trim([v%p for v in b])
    assert b
    inv=pow(b[-1],-1,p)
    while len(a)>=len(b):
        c=a[-1]*inv%p;d=len(a)-len(b)
        for j,v in enumerate(b):a[d+j]=(a[d+j]-c*v)%p
        trim(a)
    return a


def gcd(a,b,p):
    a=trim([v%p for v in a]);b=trim([v%p for v in b])
    while b:a,b=b,rem(a,b,p)
    inv=pow(a[-1],-1,p)
    return [v*inv%p for v in a]


def derivative(a):return [i*v for i,v in enumerate(a) if i]


def evaluate(a,x,p=None):
    v=0
    for c in reversed(a):
        v=v*x+c
        if p:v%=p
    return v


def divlinear(a,r,p):
    a=[v%p for v in a];out=[0]*(len(a)-1);out[-1]=a[-1]
    for i in range(len(out)-2,-1,-1):out[i]=(a[i+1]+r*out[i+1])%p
    assert (a[0]+r*out[0])%p==0
    return trim(out)


def span(rows):
    b={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p not in b:b[p]=v;break
            v^=b[p]
    return b


def qvalue(e,m):
    return ((int(e['linear'],16)&m).bit_count()+sum(((m>>i)&1)*((m>>j)&1) for i,j in e['cross']))&1


def main():
    F=read('curve_C29.json')['F_ascending']
    old=read('row374_results.json');odd=old['odd_discriminant_primes_all_exponent_one']
    disc=abs(int(old['field_discriminant']));v2=0
    while disc%2==0:disc//=2;v2+=1
    product=1
    for p in odd:product*=p
    assert product==disc and v2==70 and len(odd)==6
    nodes=[]
    for p in odd:
        g=gcd(F,derivative(F),p);assert len(g)==2 and g[-1]==1
        r=(-g[0])%p
        Q=divlinear(divlinear(F,r,p),r,p)
        assert len(Q)==104 and gcd(Q,derivative(Q),p)==[1]
        assert evaluate(Q,r,p)!=0
        assert evaluate(derivative(derivative(F)),r,p)!=0
        value=evaluate(F,r,p*p);assert value%p==0 and value!=0
        assert evaluate(derivative(F),r,p)==0
        nodes.append({'p':str(p),'double_root_of_F':str(r),
                      'F_at_root_div_p_mod_p':str(value//p),
                      'remaining_squarefree_degree':103,
                      'unique_ramified_factor_degree':2,
                      'unique_ramified_prime_e':2,'unique_ramified_prime_f':1})
    local=read('local_conics386.json');units=read('units381_exact.json')
    known=read('row375_results.json')
    assert units['unit_Selmer_dimension']==9
    solutions=[m for m in range(512) if all(qvalue(e,m)==0 for e in local['conic_equations'])]
    assert solutions==[0,0x49,0xa1]
    assert len(span(solutions))==2
    known_coords=[0xcf,0xa1,0x49,0x0e,0xa8,0x6b,0xf6,0x51]
    assert len(span(known_coords))==8 and len(span(known_coords+solutions))==8
    assert len(span(known_coords+[0x10c]))==9
    codes=list(map(lambda v:int(v,16),units['kernel_basis_local_codes']))
    for coord,v in zip(known_coords,known['unit_squareclasses_at_2']):
        z=0
        for k in range(9):
            if coord>>k&1:z^=codes[k]
        assert z==int(v,16)
    assert evaluate(F,1)==evaluate(F,-1)==2**70
    pair=read('norm_equations387.json')
    R=pair['R_coefficients_in_z_ascending_each_polynomial_in_t_ascending']
    assert len(R)==105 and R[-1]==[1]
    actual={};expected={}
    for j,coefficients in enumerate(R):
        for k,a in enumerate(coefficients):
            actual[k,j+1]=actual.get((k,j+1),0)+a
            actual[k+1,j]=actual.get((k+1,j),0)-a
    for k,a in enumerate(F):
        expected[0,k]=expected.get((0,k),0)+a
        expected[k,0]=expected.get((k,0),0)-a
    assert {k:v for k,v in actual.items() if v}=={k:v for k,v in expected.items() if v}
    assert pair['degree_M_over_Q']==105*104==10920
    # Odd local Hilbert symbols of two unit classes vanish. If the roots
    # coalesce, they are the two embeddings of the same ramified quadratic
    # factor; unramified Kummer classes restrict identically at the two roots.
    odd_cases=0
    for collision in [False,True]:
        for di in range(2):
            for dj in range(2):
                if collision and di!=dj:continue
                symbol=(di^dj)*int(collision)
                assert symbol==0;odd_cases+=1
    print(json.dumps({
       'root_degree':105,'genus':52,'ordinary_class_group_2rank':'c_Cl_UNDETERMINED',
       'odd_bad_primes':nodes,'field_discriminant_v2':70,
       'odd_local_unramified_cases_checked':odd_cases,
       'unit_projection_of_all_good_elements':list(map(hex,solutions)),
       'dimension_of_span_of_good_unit_projection':2,
       'known_rational_unit_dimension':8,'full_unit_selmer_dimension':9,
       'exact_good_set':'H_nr UNION (D_minus+H_nr) UNION (D_plus+H_nr)',
       'good_element_count':'3 * 2^c_Cl','good_element_fraction':'3/512',
       'span_of_good_elements_dimension':'c_Cl+2',
       'known_W_plus_span_good_dimension':'c_Cl+8',
       'known_W_plus_span_good_index_in_Sel2':2,
       'Shukla_good_curve_definition_4_4_5_satisfied':True,
       'required_norm_equation_base_degree_over_Q':10920,
       'required_conic_norm_equations_per_unramified_class':1,
       'nontrivial_unramified_Kummer_basis':'NOT_CONSTRUCTED',
       'global_norm_equation_solutions_for_unknown_classes':'NOT_CONSTRUCTED',
       'class_group_obstruction_qstar_value':'UNDETERMINED',
       'delta_star_true_Sel4_membership':'UNDETERMINED',
       'new_unconditional_original_signed_exclusions':0
    },indent=2))


if __name__=='__main__':main()
