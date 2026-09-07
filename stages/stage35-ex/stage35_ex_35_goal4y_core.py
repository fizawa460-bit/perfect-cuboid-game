#!/usr/bin/env python3
from __future__ import annotations
import json, runpy
from pathlib import Path
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

ROOT=Path(__file__).resolve().parents[2]
ns=runpy.run_path(str(ROOT/'stages/stage35-ex/verify_stage35_ex_35_goal4x.py'))

# Goal4X exact lattices / Smith changes of basis.
B=sp.Matrix(ns['B'])                         # 32 boundary classes in Pic(Sbar)=Z^64
S=sp.Matrix(ns['S'].to_Matrix())             # domain basis change, D=S*B*T
T=sp.Matrix(ns['T'].to_Matrix())             # Pic(Sbar) basis change
D=sp.Matrix(ns['D'].to_Matrix())
Sinv=S.inv(); Tinv=T.inv()
assert all(x.q==1 for x in Sinv) and all(x.q==1 for x in Tinv)
assert S*B*T==D
R=29; Q=35; NBD=32; NP=64
assert D[:R,:R]==sp.diag(*[D[i,i] for i in range(R)])
assert all(abs(int(D[i,i]))==1 for i in range(R))
assert D[R:,:]==sp.zeros(3,64)

ccP=sp.Matrix(ns['cc']); ctP=sp.Matrix(ns['ct']); IP=sp.eye(NP)
ccQ=sp.Matrix(ns['Ac']); ctQ=sp.Matrix(ns['At']); IQ=sp.eye(Q)
Pact={0:IP,1:ccP,2:ctP,3:ccP*ctP}
Qact={0:IQ,1:ccQ,2:ctQ,3:ccQ*ctQ}
labels={0:'1',1:'cc',2:'ct',3:'ccct'}

# Recover the exact permutation action on the 32 geometric boundary components.
rows={tuple(int(x) for x in B.row(i)):i for i in range(NBD)}
assert len(rows)==NBD
Dact={0:sp.eye(NBD)}
for g,A in [(1,ccP),(2,ctP),(3,ccP*ctP)]:
    G=sp.zeros(NBD)
    for i in range(NBD):
        image=B.row(i)*A
        key=tuple(int(x) for x in image)
        assert key in rows, (g,i,key)
        G[i,rows[key]]=1
    assert G*B==B*A
    Dact[g]=G

# Kernel of Div_D -> Pic(Sbar): rank 3 = geometric unit lattice U(Ubar).
Kact={}
for g in range(4):
    Gnew=S*Dact[g]*Sinv
    assert all(x.q==1 for x in Gnew)
    assert Gnew[R:,:R]==sp.zeros(3,R)
    Kact[g]=Gnew[R:,R:]
    assert Kact[g]*Kact[g]==sp.eye(3)
assert Kact[1]*Kact[2]==Kact[2]*Kact[1]
kernel_basis_old=[[int(x) for x in S.row(i)] for i in range(R,NBD)]

# Extract two exact order-2 generators of H^1(V4,Pic(Ubar)) from Goal4X's Smith form.
Tk=sp.Matrix(ns['Tk'].to_Matrix())
Tc=sp.Matrix(ns['Tc'].to_Matrix())
Tcinv=Tc.inv()
Dc=sp.Matrix(ns['Dc'].to_Matrix())
z1rank=int(ns['z1rank']); rk=2*Q-z1rank
assert z1rank==14 and rk==56
positions=[i for i in range(z1rank) if abs(int(Dc[i,i]))==2]
assert len(positions)==2, positions


def h1_generator(pos:int):
    e=sp.zeros(1,z1rank); e[0,pos]=1
    # Row-span SNF convention: transformed ambient coordinate is v*Tc.
    kcoord=e*Tcinv
    full=sp.zeros(2*Q,1)
    for i in range(z1rank): full[rk+i,0]=kcoord[0,i]
    z=Tk*full
    zr=z.T
    x=zr[:,:Q]; y=zr[:,Q:]
    assert x*(IQ+ccQ)==sp.zeros(1,Q)
    assert y*(IQ+ctQ)==sp.zeros(1,Q)
    assert x*(IQ-ctQ)==y*(IQ-ccQ)
    f={0:sp.zeros(1,Q),1:x,2:y,3:x*ctQ+y}
    for g in range(4):
        for h in range(4):
            assert f[g^h]==f[g]*Qact[h]+f[h]
    return f, [int(v) for v in zr]

# Lift Q=Pic(Ubar) vectors to P=Pic(Sbar) by zeroing the killed 29 Smith coordinates.
def liftP(qrow:sp.Matrix)->sp.Matrix:
    pnew=sp.zeros(1,NP)
    for j in range(Q): pnew[0,R+j]=qrow[0,j]
    p=pnew*Tinv
    assert p*T==pnew
    assert all(x.q==1 for x in p)
    return p

# Lift a boundary-image Pic vector to the 32-component divisor permutation lattice.
def liftD(prow:sp.Matrix)->sp.Matrix:
    pnew=prow*T
    assert pnew[:,R:]==sp.zeros(1,Q)
    dnew=sp.zeros(1,NBD)
    for i in range(R):
        val=sp.Rational(pnew[0,i],D[i,i])
        assert val.q==1
        dnew[0,i]=val
    d=dnew*S
    assert all(x.q==1 for x in d)
    assert d*B==prow
    return d

# Normalized right-module differential C^2(G,K)->C^3(G,K), G=V4.
nonid=[1,2,3]
pairs=[(g,h) for g in nonid for h in nonid]
triples=[(g,h,k) for g in nonid for h in nonid for k in nonid]


def build_delta2_matrix():
    A=sp.zeros(len(triples)*3,len(pairs)*3)
    pindex={p:i for i,p in enumerate(pairs)}
    def add(eq_g,eq_h,eq_k,outcoord,pair,mat,sign=1):
        if pair[0]==0 or pair[1]==0: return
        j0=pindex[pair]*3
        # variable row v contributes v*mat to output row.
        for b in range(3):
            A[(triples.index((eq_g,eq_h,eq_k))*3)+outcoord,j0+b]+=sign*mat[b,outcoord]
    for ti,(g,h,k) in enumerate(triples):
        for a in range(3):
            # de(g,h,k)=e(g,h)*k + e(gh,k) - e(g,hk) - e(h,k)
            if g and h:
                j0=pindex[(g,h)]*3
                for b in range(3): A[ti*3+a,j0+b]+=Kact[k][b,a]
            gh=g^h
            if gh and k: A[ti*3+a,pindex[(gh,k)]*3+a]+=1
            hk=h^k
            if g and hk: A[ti*3+a,pindex[(g,hk)]*3+a]-=1
            if h and k: A[ti*3+a,pindex[(h,k)]*3+a]-=1
    return A

A2=build_delta2_matrix()


def dm(M:sp.Matrix):
    return DomainMatrix([[ZZ(int(x)) for x in row] for row in M.tolist()],M.shape,ZZ)


def solve_integral(A:sp.Matrix,b:sp.Matrix):
    DD,LL,RR=smith_normal_decomp(dm(A))
    Dm=sp.Matrix(DD.to_Matrix()); Lm=sp.Matrix(LL.to_Matrix()); Rm=sp.Matrix(RR.to_Matrix())
    bp=Lm*b
    rank=sum(1 for i in range(min(Dm.rows,Dm.cols)) if Dm[i,i]!=0)
    y=sp.zeros(A.cols,1)
    for i in range(rank):
        val=sp.Rational(bp[i,0],Dm[i,i]); assert val.q==1, ('nonintegral',i,val)
        y[i,0]=val
    for i in range(rank,A.rows): assert bp[i,0]==0, ('inconsistent',i,bp[i,0])
    x=Rm*y
    assert all(v.q==1 for v in x)
    assert A*x==b
    return x,rank


def one_class(pos:int):
    f,zraw=h1_generator(pos)
    lp={g:liftP(f[g]) for g in range(4)}
    d={}
    for g in range(4):
        for h in range(4):
            delta=lp[g]*Pact[h]+lp[h]-lp[g^h]
            d[(g,h)]=liftD(delta)
    # The second connecting cocycle lands in the rank-3 unit kernel.
    k3={}
    target=[]
    for g,h,k in triples:
        kval=d[(g,h)]*Dact[k]+d[(g^h,k)]-d[(g,h^k)]-d[(h,k)]
        knew=kval*Sinv
        assert knew[:,:R]==sp.zeros(1,R)
        kv=knew[:,R:]
        k3[(g,h,k)]=kv
        target.extend(int(v) for v in kv)
    targetv=sp.Matrix(target)
    ecoord,delta_rank=solve_integral(A2,targetv)
    eco={}
    for g in range(4):
        for h in range(4): eco[(g,h)]=sp.zeros(1,3)
    for pi,pair in enumerate(pairs):
        eco[pair]=sp.Matrix([[int(ecoord[pi*3+a,0]) for a in range(3)]])
    # Correct the chosen Div_D 2-cochain by a unit-kernel 2-cochain.
    r={}
    for g in range(4):
        for h in range(4):
            enew=sp.zeros(1,NBD)
            if g and h:
                for a in range(3): enew[0,R+a]=eco[(g,h)][0,a]
            eold=enew*S
            r[(g,h)]=d[(g,h)]-eold
    for g,h,k in triples:
        chk=r[(g,h)]*Dact[k]+r[(g^h,k)]-r[(g,h^k)]-r[(h,k)]
        assert chk==sp.zeros(1,NBD)
    # Shapiro-style finite residue character coordinates on boundary orbits.
    seen=set(); orbit_data=[]; flat=[]
    for i in range(NBD):
        if i in seen: continue
        orb=sorted({next(j for j in range(NBD) if Dact[g][i,j]==1) for g in range(4)})
        seen.update(orb); rep=min(orb)
        stab=[g for g in range(4) if Dact[g][rep,rep]==1]
        non=[g for g in stab if g]
        bits={labels[g]:int(r[(g,g)][0,rep])%2 for g in non}
        if len(stab)==4:
            assert bits['ccct']==(bits['cc']^bits['ct'])
            flat.extend([bits['cc'],bits['ct']])
        elif len(stab)==2:
            flat.append(bits[labels[non[0]]])
        else:
            assert len(stab)==1
        orbit_data.append({'rep_component_1based':rep+1,'orbit_1based':[j+1 for j in orb],
                           'stabilizer':[labels[g] for g in stab], 'character_bits':bits})
    return {
      'smith_h1_position_0based':pos,
      'h1_cocycle_cc':zraw[:Q],
      'h1_cocycle_ct':zraw[Q:],
      'unit_transgression_3cocycle_is_coboundary':True,
      'delta2_solver_rank':delta_rank,
      'finite_boundary_residue_vector_bits':flat,
      'finite_boundary_residue_support_0based':[i for i,b in enumerate(flat) if b],
      'boundary_orbit_residue_data':orbit_data,
    }

classes=[one_class(pos) for pos in positions]
rv=[c['finite_boundary_residue_vector_bits'] for c in classes]
assert len(rv[0])==len(rv[1])
assert any(rv[0]) and any(rv[1]) and rv[0]!=rv[1]
# two nonzero unequal vectors are independent over F2 in a 2-dimensional span.

# Boundary orbit inventory: 24 fixed components + four cc-swapped pairs is expected.
fixed=sum(1 for x in classes[0]['boundary_orbit_residue_data'] if len(x['orbit_1based'])==1)
pairs2=sum(1 for x in classes[0]['boundary_orbit_residue_data'] if len(x['orbit_1based'])==2)
assert fixed==24 and pairs2==4
assert len(rv[0])==52

out={
 'success':True,
 'unit_kernel_rank':3,
 'unit_kernel_action_cc':[[int(x) for x in row] for row in Kact[1].tolist()],
 'unit_kernel_action_ct':[[int(x) for x in row] for row in Kact[2].tolist()],
 'unit_kernel_basis_boundary_coordinates':kernel_basis_old,
 'boundary_orbits_fixed':fixed,
 'boundary_orbits_size2':pairs2,
 'finite_residue_character_coordinate_count':52,
 'h1_two_generator_positions_0based':positions,
 'both_two_step_transgressions_vanish':True,
 'two_residue_vectors_independent':True,
 'classes':classes,
}
print('GOAL4Y_PROBE '+json.dumps(out,sort_keys=True))
