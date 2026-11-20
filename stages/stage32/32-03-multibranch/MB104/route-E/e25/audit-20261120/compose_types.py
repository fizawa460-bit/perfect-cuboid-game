# E25 audit (Prop. M, step 3): numeric sanity check of "type multiplies by deg kappa" and
# "Omega_p = unramified preimage of Omega_c" on composite pairs p_i = c_i ∘ kappa with c_1 = id, c_2 = U
# (degree-1 legs, |B ∩ U^{-1}B| = 4 or 3) and kappa(z) = A(z^k) branched over two points of B ∩ U^{-1}B.
import itertools, numpy as np
B=[0,np.inf,1,-1,1j,-1j]; LAB=[0,0,1,1,2,2]
def hom(z): return np.array([1,0],complex) if z==np.inf else np.array([z,1],complex)
H=[hom(z) for z in B]
def mob(x,y):
    def fr(p):
        M=np.array([p[0],p[1]]).T; l=np.linalg.solve(M,p[2]); return M*l
    return fr(y)@np.linalg.inv(fr(x))
def idx(w):
    for k,v in enumerate(H):
        if abs(w[0]*v[1]-w[1]*v[0])<1e-9*np.linalg.norm(w): return k
    return None
def odd_set(M, kappaA, k):
    # p = M ∘ A ∘ (z -> z^k): cone points = unramified preimages of B; return list of (point, label)
    Minv=np.linalg.inv(M@kappaA)
    pts=[]
    for b,lab in zip(H,LAB):
        w=Minv@b            # value of z^k
        if abs(w[0])<1e-12 or abs(w[1])<1e-12: continue   # 0 or inf: fully ramified for kappa
        r=w[0]/w[1]
        for m in range(k):
            pts.append((r**(1/k)*np.exp(2j*np.pi*m/k),lab))
    return pts
def types(P1,P2):
    def key(z): return complex(round(z.real,8),round(z.imag,8))
    D1={key(z):l for z,l in P1}; D2={key(z):l for z,l in P2}
    m1=len(set(D1)-set(D2)); m2=len(set(D2)-set(D1)); com=set(D1)&set(D2)
    h=sum(1 for z in com if D1[z]!=D2[z])
    return (m1,m2),h,len(D1),len(D2)
ok=True; seen=0
for tx in itertools.permutations(range(6),3):
    U=mob([H[0],H[1],H[2]],[H[k] for k in tx])
    Uinv=np.linalg.inv(U)
    pre=[idx(Uinv@b) for b in H]       # U^{-1}(B) ∩ B as indices
    inter=[k for k in range(6) if idx(U@H[k]) is not None]
    if len(inter) not in (3,4): continue
    # degree-1 pair (id, U): type (|B \ U^{-1}B|, |U^{-1}B \ B|), labels on common points
    c1=[(H[k][0]/H[k][1] if H[k][1]!=0 else np.inf,LAB[k]) for k in range(6)]
    for b0,b1 in itertools.combinations(inter,2):
        A=mob([H[0],H[1],H[2]],[H[b0],H[b1],H[[k for k in range(6) if k not in (b0,b1)][0]]])
        for k in (2,):   # kappa must have indices <= 2 (slack 0), so k = 2 here
            P1=odd_set(np.eye(2),A,k); P2=odd_set(U,A,k)
            tp,hp,n1,n2=types(P1,P2)
            # c-level: kappa = A∘z^k is unramified over every point except A(0), A(inf) = B[b0], B[b1]
            mc=(6-len(inter),6-len(inter))
            hc_unram=sum(1 for q in inter if q not in (b0,b1) and LAB[q]!=LAB[idx(U@H[q])])
            good=(tp==(k*mc[0],k*mc[1]) and hp==k*hc_unram and n1==n2==2*k+4)
            ok&=good; seen+=1
print('cases',seen,'PASS' if ok else 'FAIL')
