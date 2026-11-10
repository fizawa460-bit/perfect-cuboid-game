"""Exact finite raw collision checks; no asymptotic conclusion from census."""
import collections,csv,hashlib,json,math,pathlib
import functools
flags=bytearray(b"\1")*4_000_001
flags[:2]=b"\0\0"
for p in range(2,math.isqrt(4_000_000)+1):
    if flags[p]: flags[p*p::p]=b"\0"*((4_000_000-p*p)//p+1)
primes=[p for p in range(2,len(flags)) if flags[p]]

ROOT=pathlib.Path(__file__).resolve().parent
B=4_000_000
SOURCE=ROOT.parent/'attachments/098192f5-df13-43ac-93a2-55f349dbac19/M3-T11-208-verification.json'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='3bce05e1ded1adabf70dd597de2e76ed8c0d4fdc96f604a2b5b7de239280adcd'
def sq(n):return n>=0 and math.isqrt(n)**2==n
@functools.lru_cache(None)
def fac(n):
    result={}
    for p in primes:
        if p*p>n:break
        while n%p==0:result[p]=result.get(p,0)+1;n//=p
    if n>1:result[n]=1
    return result
def split(n):
    f=fac(n);k=math.prod(p for p,e in f.items() if e%2);y=math.isqrt(n//k)
    assert k*y*y==n
    return k,y
def valuation(n,p):
    t=0
    while n%p==0:t+=1;n//=p
    return t,n
def local(n,p):
    t,u=valuation(n,p)
    return t%2==0 and (u%8==1 if p==2 else pow(u%p,(p-1)//2,p)==1)

records=[]
for row in csv.DictReader((ROOT/'M3-T11-221-raw-census.tsv').open(),delimiter='\t'):
    d={k:int(v) for k,v in row.items()}
    e=[d[k] for k in ['a','b','c']];R=d['R']
    assert 0<e[0]<=e[1]<=e[2] and math.gcd(*e)==1 and sum(t*t for t in e)==R*R and R<=B
    eligible=[i for i in range(3) if sq(R*R-e[i]**2)]
    assert len(eligible)==d['integral_faces']>=2
    # The bounded census has no endpoint. Never use this to delete endpoints
    # from the theoretical population; their canonical pair needs212/214.
    assert len(eligible)==2
    a=e[3-sum(eligible)];M=R*R-a*a;k,y=split(M)
    h=math.gcd(R,a);eps=2 if a%2 else 1
    am=(R-a)//(eps*h);ap=(R+a)//(eps*h)
    assert M==(eps*h)**2*am*ap and math.gcd(am,ap)==1
    cc=math.prod(math.gcd(R,e[i]) for i in eligible)
    assert cc==d['c_raw_max']
    rprimes=list(fac(R));mask=all(local(t,p) for t in [am,ap] for p in [2]+rprimes)
    records.append(dict(edges=e,R=R,shared_edge=a,M=M,kappa=k,y=y,c_chart=cc,h=h,M_2R=mask,distinct=len(set(e))==3))

keys=[tuple(r['edges']) for r in records]
assert len(keys)==len(set(keys))
old=json.loads(SOURCE.read_text())['records']
assert {tuple(r['edges']) for r in records if r['R']<=10**6}=={tuple(r['edges']) for r in old}
other={tuple(map(int,l.split())) for l in (ROOT/'M3-T11-221-euclid-keys.tsv').read_text().splitlines()}
assert set(keys)==other

def stats(pop):
    nu=collections.Counter(r['M'] for r in pop);mu=collections.Counter(r['kappa'] for r in pop)
    eq=sum(v*v for v in nu.values());es=sum(v*v for v in mu.values())
    D=max(nu.values(),default=0);n=len(pop)
    assert es>=eq
    pairs=[]
    for i,x in enumerate(pop):
        for y in pop[i+1:]:
            if x['kappa']!=y['kappa'] or x['M']==y['M']:continue
            g=math.gcd(x['y'],y['y']);r=x['y']//g;s=y['y']//g;L=x['kappa']*g*g
            assert math.gcd(r,s)==1 and math.gcd(x['M'],y['M'])==L
            assert x['M']==L*r*r and y['M']==L*s*s
            assert math.isqrt(x['M']*y['M'])**2==x['M']*y['M']
            pairs.append(dict(left=x,right=y,common_value_gcd=L,reduced_dilation=[r,s]))
    assert es-eq==2*len(pairs)
    # Explicit D version of the short-multiplier upper bound: no hidden
    # B^o factor is tested numerically.
    checks=[]
    for Y in [1,2,5,10,20,50,100,200,500,1000,10000,100000]:
        short=sum(2 for p in pairs if min(p['left']['y'],p['right']['y'])<=Y)
        assert short<=2*Y*D*n
        checks.append([Y,short,2*Y*D*n])
    for K in [1,10,100,10000,10**6,10**8,10**10]:
        high=sum(v*v for k,v in mu.items() if k>=K)
        assert high<=n*D*math.isqrt(B*B//K)
    return dict(N=n,distinct_values=len(nu),distinct_squareclasses=len(mu),max_value_multiplicity=D,max_squareclass_multiplicity=max(mu.values(),default=0),E_equal=eq,E_squareclass=es,E_off=es-eq,collision_examples=pairs[:5],short_multiplier_checks=checks)

raw=stats(records)
X=stats([r for r in records if r['distinct'] and r['M_2R'] and r['c_chart']**6>B])
windows=[]
for bound in [10**6,2*10**6,B]:
    pop=[r for r in records if r['R']<=bound]
    for gn,gd in [(1,6),(3,16),(5,24),(11,48)]:
        q=[r for r in pop if r['distinct'] and r['M_2R'] and r['c_chart']**gd>bound**gn]
        z=stats(q);windows.append(dict(B=bound,gamma=f'{gn}/{gd}',**{k:z[k] for k in ['N','E_equal','E_squareclass','E_off','max_squareclass_multiplicity']}))

# Formal coefficient countermodel: NOT an actual raw cuboid family.
models=[]
for T in [16,32,64,128]:
    bound=T*T;n=T;ys=list(range(bound//2,bound//2+n))
    ms=[2*y*y for y in ys]
    assert len(set(ms))==n and max(ms)<=bound*bound
    assert all(split(m)[0]==2 for m in ms)
    models.append(dict(B=bound,N=n,E_equal=n,E_off=n*(n-1),squareclass=2,min_y=min(ys),type='FORMAL_NOT_PHYSICAL'))

out=dict(card='M3-T11-221',scope='exact short-multiplier/high-kernel collision bound plus divisor-only relaxation NO_GO; finite raw diagnostics',B=B,source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),independent_census_key_match=True,old_1million_key_match=True,raw=raw,X_star_gamma_one_sixth=X,threshold_windows=windows,formal_countermodels=models,files={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'raw_census_221.cpp',ROOT/'raw_census_euclid_221.cpp',ROOT/'M3-T11-221-raw-census.tsv',ROOT/'M3-T11-221-euclid-keys.tsv',pathlib.Path(__file__)]},independent_audit='NOT RUN',global_credit=0)
(ROOT/'M3-T11-221-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['raw','X_star_gamma_one_sixth','formal_countermodels','files']},ensure_ascii=False))
print(json.dumps({'raw':{k:v for k,v in raw.items() if k!='short_multiplier_checks'},'X_star':{k:v for k,v in X.items() if k!='short_multiplier_checks'}},ensure_ascii=False))
