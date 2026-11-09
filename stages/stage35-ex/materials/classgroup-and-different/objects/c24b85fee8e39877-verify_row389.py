#!/usr/bin/env python3
"""Pure Python certificate: new ideal relations, exact 2-divisibility witnesses.
Number-field profiles are bound to the parent and checked by rebuild_new389.py.
"""
from pathlib import Path
from math import comb,prod
import json,hashlib,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'parent388'))
from verify_row388 import integer_basis,valuation_sum,parity_mask

def load(n):return json.loads((HERE/n).read_text())
class LowSpan:
    def __init__(self):self.piv={}
    def add(self,v):
        while v:
            p=(v&-v).bit_length()-1
            if p not in self.piv:self.piv[p]=v;return True
            v^=self.piv[p]
        return False
    def reduce(self,v):
        for p in sorted(self.piv):
            if v>>p&1:v^=self.piv[p]
        return v
    def __len__(self):return len(self.piv)

def main():
    pdir=HERE/'parent388'
    for n,digest in load('parent_identity389.json').items():
        assert hashlib.sha256((pdir/n).read_bytes()).hexdigest()==digest
    old=json.loads((pdir/'profiles388.json').read_text());oldf={int(p):d for p,d in json.loads((pdir/'frontier_factorizations388.json').read_text()).items()}
    new=load('new_relations389.json');factors={int(p):d for p,d in load('factorizations389.json').items()};ps=sorted(factors)
    assert all(factors[p]==d for p,d in oldf.items())
    assert factors.keys()==oldf.keys()|{p for r in new for p,e in r['odd_factorization']}
    assert all(sum(f*e for f,e in zip(ds,es))==105 for ds,es in factors.values())
    bc=[[comb(i,j) for i in range(j,105)] for j in range(105)]
    for r in new:
        h=r['coefficients'];k=r['denominator_exponent'];assert len(h)<=105 and k>=0 and r['norm_sign'] in [-1,1]
        assert r['absolute_norm']>0 and len(r['odd_factorization'])==len({p for p,e in r['odd_factorization']})
        # Exact maximal-order integrality, independent of numerical embeddings.
        for j in range(min(105,3*k)):
            c=sum(a*b for a,b in zip(h[j:],bc[j]));assert c%2**(k-j//3)==0
        v={(p,j):e for p,j,e in r['valuations']};assert len(v)==len(r['valuations']) and all(e>0 for e in v.values())
        assert sorted([p,j] for (p,j),e in v.items() if p!=2 and e&1)==r['mod2_labels']
        for p,e in r['odd_factorization']:
            assert p in factors and e>0
            ds,es=factors[p];assert sum(f*v.get((p,j),0) for j,f in enumerate(ds))==e
        assert {p for p,j in v if p!=2}=={p for p,e in r['odd_factorization']}
        assert r['absolute_norm']==2**(7*v.get((2,0),0)+28*v.get((2,1),0))*prod(p**e for p,e in r['odd_factorization'])
    labels=[(2,0),(2,1)]+[(p,j) for p,(ds,es) in sorted(factors.items()) for j in range(len(ds))];ix={p:i for i,p in enumerate(labels)}
    oldrows=[{(p,j):e for p,j,e in r['valuations']} for r in old]
    rationalrows=[{(p,j):e for j,e in enumerate(factors[p][1])} for p in ps]
    newrows=[{(p,j):e for p,j,e in r['valuations']} for r in new]
    rows=oldrows+rationalrows+newrows;base_n=len(oldrows)+len(rationalrows)
    vectors=[sum((e&1)<<ix[p] for p,e in r.items()) for r in rows]
    span=LowSpan()
    for v in vectors[:base_n]:span.add(v)
    fb=[(2,0,128)]+[(p,j,p**d) for p,(ds,es) in sorted(factors.items()) for j,d in enumerate(ds) if p**d<=6768];fb.sort(key=lambda a:(a[2],a[0],a[1]))
    old_zero=[a for a in fb if not span.reduce(1<<ix[a[:2]])];old_fb=LowSpan()
    for a in fb:old_fb.add(span.reduce(1<<ix[a[:2]]))
    assert len(fb)==878 and len(old_zero)==488 and len(old_fb)==332
    alpha=load('alpha349.json');ar=new[alpha['new_generator_index']]
    assert ar['absolute_norm']==alpha['norm']==3595674059
    assert ar['denominator_exponent']==alpha['denominator_exponent']==34
    assert [ar['norm_sign']*x for x in ar['coefficients']]==alpha['positive_norm_numerator']
    assert ar['valuations']==alpha['principal_ideal_factors']==[[67,1,1],[349,2,1],[367,0,1],[419,1,1]]
    assert all(not span.reduce(1<<ix[tuple(a)]) for a in alpha['old_zero_auxiliary_classes'])
    curve=json.loads((pdir/'parent381'/'curve_C29.json').read_text());g=[0]*106
    for i,c in enumerate(curve['A_star_ascending']):g[2*i]=c*(-1)**i
    for i,c in enumerate(curve['B_star_ascending']):g[2*i+1]=c*(-1)**i
    table={r['p']:r for r in json.loads((pdir/'parent381'/'row378_exact.json').read_text())['prime_tables']}
    for q,j,rho in alpha['linear_rho_residues']:
        assert sum(c*pow(rho,i,q) for i,c in enumerate(g))%q==0
        f=table[q]['factors_ascending'][j];assert len(f)==2
        assert sum(c*pow(-rho*rho,i,q) for i,c in enumerate(f))%q==0
        assert sum(c*pow(rho,i,q) for i,c in enumerate(alpha['positive_norm_numerator']))%q==0
    assert sum(c*pow(20,i,773) for i,c in enumerate(g))%773==0
    independent=[]
    for i,v in enumerate(vectors[base_n:]):
        if span.add(v):independent.append(i)
    cert=load('relation_certificate389.json');assert cert['independent_new_relation_indices']==independent
    zero=[];remaining=[];fbspan=LowSpan()
    for a in fb:
        v=span.reduce(1<<ix[a[:2]])
        if not v:zero.append(a)
        if fbspan.add(v):remaining.append(a)
    assert [list(a) for a in zero]==cert['zero_prime_ideals']
    assert [list(a) for a in remaining]==cert['remaining_formal_basis']
    newly_zero=sorted(set(zero)-set(old_zero));given=[]
    for w in cert['new_zero_witnesses']:
        a=tuple(w['prime_ideal']);given.append(a)
        for indices,bound in [(w['old_generator_indices'],4143),(w['new_generator_indices'],len(new))]:
            assert len(indices)==len(set(indices)) and all(0<=i<bound for i in indices)
        assert len(w['rational_primes'])==len(set(w['rational_primes']))
        selected=w['old_generator_indices']+[4143+ps.index(p) for p in w['rational_primes']]+[base_n+i for i in w['new_generator_indices']]
        value=valuation_sum([(i,1) for i in selected],rows)
        assert sorted(p for p,e in value.items() if e&1)==[a[:2]]
        half={(p,j):e for p,j,e in w['half_ideal_factors']};assert all(e>0 for e in half.values())
        twice={p:2*e for p,e in half.items()};twice[a[:2]]=twice.get(a[:2],0)+1
        assert value==twice # exact (alpha)=P*I^2, so [P]=-2[I].
    assert sorted(given)==newly_zero
    kp=LowSpan()
    for k in cert['integer_kernel']:
        assert not valuation_sum(k,rows);assert kp.add(parity_mask(k))
    assert len(kp)==len(rows)-len(span)
    piv,derived_kernel=integer_basis(rows)
    assert cert['integer_kernel']==derived_kernel
    assert all(abs(v[k])==1 for k,(v,c) in piv.items())
    assert all(valuation_sum(sorted(c.items()),rows)==v for v,c in piv.values())
    unit=load('unit_kernel389.json');rational_codes={int(k):int(v,16) for k,v in unit['rational_unit_codes_mod8'].items()}
    codes=[int(r['local_unit_code'],16) for r in old]+[rational_codes[p%8] for p in ps]+[int(r['local_unit_code'],16) for r in new]
    images=[];uspan=LowSpan()
    for k in cert['integer_kernel']:
        u=0
        for i,e in k:
            if e&1:u^=codes[i]
        images.append(u);uspan.add(u)
    assert [hex(u) for u in images]==unit['integer_kernel_local_codes'];assert len(uspan)==55
    sspan=LowSpan()
    for s in unit['global_square_relations_as_generator_masks']:
        mask=int(s,16);assert not kp.reduce(mask);assert sspan.add(mask)
        v=u=0
        for i in range(len(rows)):
            if mask>>i&1:v^=vectors[i];u^=codes[i]
        assert not v and not u
    assert len(sspan)==unit['global_square_relations_dimension']==len(kp)-55==271
    expected=load('results389.json')
    result={'new_exact_generators':len(new),'new_independent_principal_relation_dimension':len(independent),
     'support_rational_primes':len(ps),'new_prime_decompositions':len(factors.keys()-oldf.keys()),'finite_factorbase_bound':6768,'finite_factorbase_size':len(fb),
     'old_individually_zero':len(old_zero),'new_individually_zero':len(zero),'newly_certified_zero_count':len(newly_zero),
     'old_formal_span_dimension':len(old_fb),'new_formal_span_dimension':len(fbspan),'formal_dimension_drop':len(old_fb)-len(fbspan),
     'first_remaining_formal_direction':list(remaining[0]) if remaining else None,
     'integer_matrix_rows':len(rows),'integer_matrix_columns':len(labels),'rank_Q':len(piv),'rank_F2':len(span),'integer_kernel_dimension':len(kp),
     'integer_kernel_mod2_rank':len(kp),'all_integer_pivots_are_units':True,'p349_j2_zero':(349,2,349) in zero,
     'classgroup_mod2_generation':'NOT_CERTIFIED','c_Cl':'UNDETERMINED','qstar':'UNDETERMINED','new_unconditional_signed_exclusion':0}
    assert result==expected
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
