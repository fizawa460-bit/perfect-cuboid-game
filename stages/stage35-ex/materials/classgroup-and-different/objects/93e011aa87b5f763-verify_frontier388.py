#!/usr/bin/env python3
"""Replay the finite 6,768-norm frontier. This does not certify generation."""
import json
from verify_row388 import HERE,load,binary_basis

def main():
    factors={int(p):d for p,d in load('frontier_factorizations388.json').items()}
    for p in range(3,6769,2):
        prime=all(p%d for d in range(2,__import__('math').isqrt(p)+1))
        assert not prime or p in factors
    labels=[(2,0),(2,1)]+[(p,j) for p,(ds,es) in sorted(factors.items()) for j in range(len(ds))]
    ix={p:i for i,p in enumerate(labels)}
    vs=[sum((e&1)<<ix[p,j] for p,j,e in r['valuations']) for r in load('profiles388.json')]
    vs += [sum((e&1)<<ix[p,j] for j,e in enumerate(es)) for p,(ds,es) in sorted(factors.items())]
    basis,_=binary_basis(vs)
    # Reduce via all descending pivots, including those below free coordinates.
    def reduce(v):
        for p in sorted(basis,reverse=True):
            if v>>p&1:v^=basis[p][0]
        return v
    fb=[(2,0,128)]+[(p,j,p**d) for p,(ds,es) in sorted(factors.items()) for j,d in enumerate(ds) if p**d<=6768]
    fb.sort(key=lambda a:(a[2],a[0],a[1]));piv={};chosen=[];zeros=[]
    for a in fb:
        p,j,n=a;v=reduce(1<<ix[p,j])
        if not v:zeros.append(a)
        while v:
            k=v.bit_length()-1
            if k not in piv:piv[k]=v;chosen.append(a);break
            v^=piv[k]
    result={'bound':6768,'finite_factorbase_size':len(fb),
            'individually_zero_mod_relation2':len(zeros),'formal_span_dimension':len(piv),
            'selected_prime_ideal_labels_and_norms':[list(a) for a in chosen],
            'zero_labels_and_norms':[list(a) for a in zeros],
            'generation_of_Cl_mod2':'NOT_CERTIFIED',
            'warning':'formal span dimension is not the class-group 2-rank'}
    assert result==load('frontier388.json')
    assert (len(fb),len(zeros),len(piv))==(878,488,332)
    assert chosen[0]==(349,2,349)
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
