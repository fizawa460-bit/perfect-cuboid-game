#!/usr/bin/env python3
"""Integer certificate for the complete old multiplicative closure; pure Python."""
import hashlib,json
from pathlib import Path
from collections import defaultdict
HERE=Path(__file__).resolve().parent

def load(name):return json.loads((HERE/name).read_text())

def addmul(a,b,q):
    for k,v in b.items():
        c=a.get(k,0)+q*v
        if c:a[k]=c
        else:a.pop(k,None)

def binary_basis(vectors):
    piv={};kernel=[]
    for i,v in enumerate(vectors):
        c=1<<i
        while v:
            p=v.bit_length()-1
            if p not in piv:piv[p]=(v,c);break
            w,d=piv[p];v^=w;c^=d
        if not v:kernel.append(c)
    return piv,kernel

def integer_basis(rows):
    piv={};kernel=[]
    for i,row in enumerate(rows):
        v=dict(row);c={i:1}
        while v:
            p=max(v)
            if p not in piv:piv[p]=(v,c);break
            w,d=piv[p];q,r=divmod(v[p],w[p])
            if q:addmul(v,w,-q);addmul(c,d,-q)
            if r:piv[p],(v,c)=(v,c),(w,d)
        if not v:kernel.append([list(x) for x in sorted(c.items())])
    return piv,kernel

def parity_mask(combo):
    return sum((e&1)<<i for i,e in combo)

def valuation_sum(combo,rows):
    value={}
    for i,e in combo:addmul(value,rows[i],e)
    return value

def matrix_certificate(rows):
    labels=sorted({p for row in rows for p in row});index={p:i for i,p in enumerate(labels)}
    vectors=[sum((e&1)<<index[p] for p,e in row.items()) for row in rows]
    mod2,ker2=binary_basis(vectors)
    piv,kernel=integer_basis(rows)
    assert len(piv)==len(mod2)
    assert len(kernel)==len(rows)-len(piv)
    assert len(binary_basis([parity_mask(k) for k in kernel])[0])==len(kernel)
    assert all(not valuation_sum(c,rows) for c in kernel)
    # Each pivot row is an integer combination of input rows. Its pivot columns
    # give a triangular full-rank minor of determinant +/-1.
    assert all(abs(v[p])==1 for p,(v,c) in piv.items())
    assert all(valuation_sum(sorted(c.items()),rows)==v for v,c in piv.values())
    return {'rows':len(rows),'columns':len(labels),'rank_mod2':len(mod2),
            'rank_rational':len(piv),'integer_kernel_dimension':len(kernel),
            'integer_kernel_mod2_rank':len(kernel),
            'primitive_integer_row_lattice':True,
            'formal_quotient_free_rank':len(labels)-len(piv)},kernel

class Principalizer:
    """If the ideal of a factored old product is square, return its principal half.

    This is a factored principal-IDEAL generator, not a square root of alpha.
    The returned unit epsilon satisfies alpha = epsilon * beta^2.
    """
    def __init__(self,rows,kernel):
        self.rows=rows;self.kernel=kernel
        self.basis,_=binary_basis([parity_mask(k) for k in kernel])
    def split(self,exponents):
        assert len(exponents)==len(self.rows)
        val=valuation_sum([(i,e) for i,e in enumerate(exponents) if e],self.rows)
        assert all(e%2==0 for e in val.values())
        v=sum((e&1)<<i for i,e in enumerate(exponents));mask=0
        while v:
            p=v.bit_length()-1
            assert p in self.basis
            w,c=self.basis[p];v^=w;mask^=c
        unit={}
        for j,k in enumerate(self.kernel):
            if mask>>j&1:addmul(unit,dict(k),1)
        assert not valuation_sum(sorted(unit.items()),self.rows)
        beta={}
        for i,e in enumerate(exponents):
            d=e-unit.get(i,0);assert d%2==0
            if d:beta[i]=d//2
        assert valuation_sum(sorted(beta.items()),self.rows)=={p:e//2 for p,e in val.items()}
        return {'unit_exponents':sorted(unit.items()),'principal_half_exponents':sorted(beta.items())}

def main():
    sources=load('source_identity.json')
    for name,digest in sources.items():
        assert hashlib.sha256((HERE/'parent381'/name).read_bytes()).hexdigest()==digest
    profiles=load('profiles388.json');factors={int(p):v for p,v in load('factorizations388.json').items()}
    parent=HERE/'parent381'
    read=lambda n:json.loads((parent/n).read_text())
    raw=[{'coefficients':[2],'odd_factorization':[]},{'coefficients':[-1,1],'odd_factorization':[]},
         {**read('dyadic_principal.json'),'odd_factorization':[]}]+read('principal_witnesses.json')+read('new_relations.json')
    assert len(raw)==len(profiles)==4143
    rows=[{(p,j):e for p,j,e in r['valuations']} for r in profiles]
    for i,(r,vs) in enumerate(zip(raw,rows)):
        assert len(vs)==len(profiles[i]['valuations']) and all(e>0 for e in vs.values())
        for p,e in r['odd_factorization']:
            fs,es=factors[p]
            assert sum(fs[j]*vs.get((p,j),0) for j in range(len(fs)))==e
        if i>=3:
            assert sorted([p,j] for (p,j),e in vs.items() if p!=2 and e&1)==r['mod2_labels']
    bare,kernel=matrix_certificate(rows)
    expected=load('kernel_certificate388.json')
    assert kernel==expected['integer_unit_relations']
    rational_ps=sorted(factors)
    extended=rows+[{(p,j):e for j,e in enumerate(factors[p][1])} for p in rational_ps]
    ext,ker_ext=matrix_certificate(extended)
    assert kernel==ker_ext
    masks=[parity_mask(k) for k in kernel]
    codes=[]
    for k in kernel:
        code=0
        for i,e in k:
            if e&1:code^=int(profiles[i]['local_unit_code'],16)
        codes.append(code)
    code_basis,square_rel=binary_basis(codes)
    assert len(code_basis)==55 and len(square_rel)==44
    # The known full unit basis is inside this exact integer kernel.
    unit_witnesses=read('unit_basis_witnesses.json');unit_images=read('units381_exact.json')['basis_images']
    assert len(unit_witnesses)==len(unit_images)==55
    for w,image in zip(unit_witnesses,unit_images):
        assert not valuation_sum(w['combination'],rows)
        u=0
        for i,e in w['combination']:
            if e&1:u^=int(profiles[i]['local_unit_code'],16)
        assert u==int(w['unit_code'],16)==int(image['unit_local_code'],16)
        v=u
        while v:
            p=v.bit_length()-1;assert p in code_basis;v^=code_basis[p][0]
    square_masks=[]
    for c in square_rel:
        m=0;u=0
        for i in range(len(kernel)):
            if c>>i&1:m^=masks[i];u^=codes[i]
        assert not u
        square_masks.append(m)
    assert len(binary_basis(square_masks)[0])==44
    assert expected['unit_relation_local_codes']==[hex(c) for c in codes]
    assert expected['global_square_relation_masks4143']==[hex(c) for c in square_masks]
    # Certify principalization on a basis of the entire even-valuation lattice.
    # Its generators are the 99 kernel parity lifts and twice each generator.
    split=Principalizer(extended,ker_ext)
    for k in kernel:
        a=[0]*len(extended)
        for i,e in k:a[i]=e
        split.split(a)
    result={'bare':bare,'with_all_norm_support_rationals':ext,
            'rational_prime_generators':len(rational_ps),'unit_kernel_local_rank':55,
            'global_square_relations_dimension':44,
            'bare_positive_norm_squareclass_image_dimension':bare['rows']-44,
            'extended_positive_norm_squareclass_image_dimension':ext['rows']-44,
            'closure_intersection_V':'exactly the known 55-dimensional norm-one unit space',
            'closure_intersection_Sel2':'exactly the known 9-dimensional unit Selmer space',
            'closure_intersection_Hnr_dimension':0,
            'full_class_group_2_rank':'UNDETERMINED',
            'qstar':'UNDETERMINED','new_unconditional_signed_exclusions':0}
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
