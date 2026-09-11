#!/usr/bin/env python3
import hashlib,itertools,json,math,runpy,subprocess
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
EW='stages/stage36/36-09EW/rho-t6-profile-parametric-realization-preflight.json'
ESV='stages/stage36/verify_stage36_36_09ES.py'
EH='stages/stage36/36-09EH/rho-fixed-p-rankzero-torsion-criterion-preflight.json'
EK='stages/stage36/36-09EK/rho-sel2-literal-orbit-closure-preflight.json'
SOURCE='stages/stage36/36-09EX/rho-t6-controlled-radical-relaxation-source-lock.md'
CERT='stages/stage36/36-09EX/rho-t6-controlled-radical-relaxation-preflight.json'

def blob(p):return subprocess.check_output(['git','hash-object',str(ROOT/p)],text=True).strip()
def load(p):return json.loads((ROOT/p).read_text())
expected={
 EW:'dce14a68463c8c95d33c3397a79fd120a8b064dd',
 ESV:'e32e84f5fa0957f9b08904928d563f3815e64264',
 EH:'d95bf71f3cbed1d3fd12eaa0d235d2aa83539d37',
 EK:'f6af11a0f7fd8a303531b2a587b7446c382a84c5',
 SOURCE:'4c627fcd603c4c333a472b583fcbad2e236e5a5a',
 CERT:'75663e2fbde9189a9c570a2075b76490151cd0b6',
}
for p,s in expected.items():assert blob(p)==s,(p,blob(p),s)

c=load(CERT); ew=load(EW); eh=load(EH); ek=load(EK)
assert c['entry_authority']['v280_exact_head']=='fbf7ed844e859dfb46d5852d3fef94ab66dcae75'
assert c['entry_authority']['v280_exact_head_ci']=='34409767705/102661214291'
assert ew['registry_impact']['provisional_expanded_registry_count']==44
assert eh['rational_4torsion_test']['order4_iff']=='8h in Q^2 or -8h in Q^2'
assert ek['literal_orbit_theorem']['positive_literal_orbit_complete'] is True

ns=runpy.run_path(str(ROOT/ESV))
matrix_from_pattern=ns['matrix_from_pattern']; rank=ns['rank']; legbit=ns['legbit']; phash=ns['phash']

def is_prime(n):
    if n < 2:return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n==p:return True
        if n%p==0:return False
    d=n-1;s=0
    while d%2==0:s+=1;d//=2
    for a in (2,325,9375,28178,450775,9780504,1795265022):
        if a%n==0:continue
        x=pow(a,d,n)
        if x in (1,n-1):continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1:break
        else:return False
    return True

def prod_factor_map(f):
    z=1
    for p,e in f.items():
        assert is_prime(p),(p,e)
        z*=p**e
    return z

def canonical_from_support(SD,SP,SQ,eps='shallow'):
    verts=[(q,'D',q%8) for q in SD]+[(q,'P',q%8) for q in SP]+[(q,'Q',q%8) for q in SQ]
    odd=[q for q,_,_ in verts]
    leg={(q,r):legbit(r,q) for q in odd for r in odd if q!=r}
    best=None
    for swap in (False,True):
        lm={'P':'Q','Q':'P','D':'D'} if swap else {'P':'P','Q':'Q','D':'D'}
        groups=defaultdict(list)
        for q,label,m8 in verts:groups[(lm[label],m8)].append(q)
        keys=sorted(groups)
        choices=[list(itertools.permutations(groups[k])) for k in keys]
        for parts in itertools.product(*choices):
            order=[];attrs=[]
            for k,part in zip(keys,parts):
                for q in part:order.append(q);attrs.append(k)
            L=[[0 if i==j else leg[(order[i],order[j])] for j in range(len(order))] for i in range(len(order))]
            obj={'eps':eps,'vertices':[[x,y] for x,y in attrs],'legendre_bits':L}
            enc=json.dumps(obj,separators=(',',':'),sort_keys=True)
            if best is None or enc<best[0]:best=(enc,obj)
    return best[1]

def psi3_coeffs(a,b):
    N=a*a-b*b;M=a*a+b*b;d=a*b
    return [-64*N*N*d*d*(M**4+4*N*N*d*d),-192*N*N*d*d*M*M,-96*N*N*d*d,4*M*M,3]

def has_root_mod(coeffs,q):
    for x in range(q):
        y=0
        for z in reversed(coeffs):y=(y*x+z)%q
        if y==0:return True
    return False

FACT={
1154147:{'u':{17:1,67891:1},'b':{2309023:1},'q':{4617317:1},'s':{89:1,1033:1,16558609:1},'t':{286831:1,906727:1}},
1774067:{'u':{1774067:1},'b':{3548863:1},'q':{7096997:1},'s':{31:1,47:1,2468723329:1},'t':{17:1,107441:1,336361:1}},
3806027:{'u':{3806027:1},'b':{7612783:1},'q':{15224837:1},'s':{16555247380913:1},'t':{89:1,42281:1,751273:1}},
3909347:{'u':{13:1,300719:1},'b':{7819423:1},'q':{11:1,1421647:1},'s':{31:2,12697:1,1431449:1},'t':{97:1,30748491721:1}},
4115987:{'u':{4115987:1},'b':{8232703:1},'q':{941:1,17497:1},'s':{19361541620273:1},'t':{17:1,31:1,199:1,31525889:1}},
5355827:{'u':{5355827:1},'b':{11:1,973853:1},'q':{71:1,301747:1},'s':{617:1,53132452489:1},'t':{79697:1,70238681:1}},
5941307:{'u':{5941307:1},'b':{11883343:1},'q':{23765957:1},'s':{40341861487793:1},'t':{233:1,2153:1,13731673:1}},
6526787:{'u':{281:1,23227:1},'b':{37:1,352819:1},'q':{26107877:1},'s':{1801:1,3137:1,8617129:1},'t':{239:1,174007:1,199889:1}},
}

previous_orbits=[
['1/2','1/3','2','3'],['1/5','2/3','3/2','5'],['2/7','5/9','7/2','9/5'],
['2/9','7/11','9/2','11/7'],['6/43','37/49','43/6','49/37'],['3/47','22/25','25/22','47/3'],
['1/277','138/139','139/138','277'],['1/333','166/167','167/166','333'],
['134/863','729/997','863/134','997/729'],['4802/5531','5531/4802','729/10333','10333/729'],
['3203734/3204463','3204463/3203734','729/6408197','6408197/729']]
prev={Fraction(x) for o in previous_orbits for x in o}
assert len(prev)==44

seen=set(); hashes=set()
for row in c['templates']:
    u=row['u']; k=729
    assert u in FACT and u%34440==17627 and u%11480==6147 and u%3==2 and u%5==2
    a=2*u;b=2*u+k;q=4*u+k
    assert math.gcd(a,b)==1
    s=(8*u*u-k*k)//7;t=(8*u*u+8*k*u+k*k)//41
    vals={'u':u,'b':b,'q':q,'s':s,'t':t}
    f=FACT[u]
    assert all(prod_factor_map(f[x])==vals[x] for x in vals),(u,vals,f)
    assert any(len(f[x])>1 or any(e>1 for e in f[x].values()) for x in vals)
    SD=sorted({3}|set(f['u'])|set(f['b'])|set(f['q']))
    SP=sorted({7}|set(f['s']))
    SQ=sorted({41}|set(f['t']))
    assert not (set(SD)&set(SP) or set(SD)&set(SQ) or set(SP)&set(SQ))
    P=7*s;Q=-41*t;D=P*P-Q*Q
    N=a*a-b*b;d=a*b
    assert D==8*N*d==-(2**4)*(3**6)*u*b*q
    obj=canonical_from_support(SD,SP,SQ)
    h=phash(obj); hashes.add(h)
    assert h==row['canonical_pattern_sha256']
    profile=','.join(f"{lab}{m8}" for lab,m8 in obj['vertices'])
    assert profile==row['profile']
    M,n=matrix_from_pattern(obj);r=rank(M)
    assert n==row['n'] and r==row['rank']==2*n-2
    assert 2*n-r==row['sel2_dimension']==2
    rr=math.isqrt(abs(D));assert rr*rr!=abs(D)
    coeff=[z%5 for z in psi3_coeffs(a,b)]
    assert coeff==[4,0,4,0,3] and not has_root_mod(coeff,5)
    orbit=[Fraction(a,b),Fraction(b,a),Fraction(k,q),Fraction(q,k)]
    assert [f"{x.numerator}/{x.denominator}" for x in orbit]==row['literal_orbit']
    assert not (set(orbit)&prev) and not (set(orbit)&seen)
    seen.update(orbit)

assert len(hashes)==8 and len(seen)==32 and len(prev|seen)==76
cr=c['controlled_radical_result']
assert cr['exact_primality_of_all_five_EW_values_is_necessary'] is False
assert cr['new_template_count']==8 and cr['expanded_exact_sufficient_template_count']==17
assert cr['all_pattern_matrices_rank_2n_minus_2'] is True
assert cr['template_matching_global_sufficient_for_sel2_dimension_2'] is True
impact=c['registry_impact'];assert impact=={'previous_count':44,'new_orbits':8,'new_parameters':32,'disjoint':True,'provisional_count':76}
assert c['route_result']['next_leaf']=='36-09EY_RHO_T6_RADICAL_REFINEMENT_RANK_COMPRESSION_PREFLIGHT'
assert c['route_result']['next_leaf_entry_allowed'] is False
for key,val in c['scope_firewalls'].items():assert val is False,(key,val)
print('36-09EX verified: eight composite controlled-radical patterns T10..T17 have abstract support rank 2n-2; eight exact EH-clean literal orbits add 32 provisional fixed-p exclusions (44->76). No exhaustivity/infinitude/parent receiver/endpoint credit.')
