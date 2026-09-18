#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
from fractions import Fraction

CERT=Path(__file__).with_name("MB104-W5-SOLO-ORDER2-ACTIVE-SUPPORT-CERTIFICATE.json")
MASK=int("000707000f0f",16)

def req(x,m):
    if not x:
        raise SystemExit("FAIL: "+m)

def gi(s):
    table={"0":0j,"1":1+0j,"-1":-1+0j,"i":1j,"-i":-1j}
    req(s in table,"unsupported Gaussian integer "+s)
    return table[s]

def rank(mat):
    a=[list(map(complex,row)) for row in mat]
    m=len(a); n=len(a[0]) if m else 0
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if abs(a[i][c])>1e-9),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]
        a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i==r: continue
            q=a[i][c]
            if abs(q)>1e-9:
                a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

def canon(z):
    for x in z:
        if x!=0:
            s=x; break
    return tuple(complex(round((x/s).real),round((x/s).imag)) for x in z)

def nodes():
    out=[]
    for j in range(3):
        for sa in (1,-1):
            for s1 in (1,-1):
                for s2 in (1,-1):
                    z=[0j]*7
                    z[j]=sa
                    o=[t for t in range(3) if t!=j]
                    z[3+o[0]]=s1
                    z[3+o[1]]=s2
                    z[6]=1
                    out.append(tuple(z))
    for j in range(3):
        o=[t for t in range(3) if t!=j]
        a,b=o
        for sr in (1,-1):
            for ep in (1,-1):
                for eq in (1,-1):
                    z=[0j]*7
                    z[a]=1
                    z[b]=1j*sr
                    z[3+a]=1j*ep
                    z[3+b]=-eq*sr
                    out.append(tuple(z))
    req(len(out)==48 and len(set(map(canon,out)))==48,"48-node model")
    return out

def main():
    c=json.loads(CERT.read_text())
    req(c["schema"]=="STAGE32_MB104_W5_SOLO_ORDER2_ACTIVE_SUPPORT_V1","schema")
    req(c["status"]=="W5_SOLO_ORDER2_EXHAUSTED_HIGHER_ORDER_OPEN_NO_CREDIT","status")

    support={i for i in range(48) if (MASK>>i)&1}
    req(sorted(support)==c["active_nodes"],"active support mask")

    V=nodes()
    y1={i for i in support if V[i][3]==0}
    y2={i for i in support if V[i][4]==0}
    req(sorted(y1)==c["active_support_partition"]["y1_zero"],"y1 partition")
    req(sorted(y2)==c["active_support_partition"]["y2_zero"],"y2 partition")
    req(not (y1 & y2) and y1|y2==support,"7+7 partition")

    # The support hyperplane is exact on the retained 48-node model.
    hyp={i for i,z in enumerate(V) if abs(z[6]-z[0]-z[1]-1j*z[2])<1e-9}
    req(hyp==support,"support hyperplane cuts exactly active 14 nodes")

    rows=[[gi(x) for x in row] for row in c["stacked_active_support_conditions"]["rref_nonzero_rows"]]
    req(len(rows)==12 and all(len(row)==13 for row in rows),"RREF shape")
    req(rank(rows)==12,"RREF rank 12")

    ker=[gi(x) for x in c["stacked_active_support_conditions"]["kernel_generator"]]
    req(len(ker)==13,"kernel length")
    for row in rows:
        req(abs(sum(row[j]*ker[j] for j in range(13)))<1e-9,"kernel equation")
    req(sum(1 for x in ker if abs(x)>1e-9)==4,"kernel sparsity")
    req(c["stacked_active_support_conditions"]["kernel_dimension"]==1,"kernel dimension")
    req(c["source_space"]["dimension"]-c["stacked_active_support_conditions"]["exact_rank"]==1,"rank-nullity")

    # Kernel vector is (-1-x2-i*x3+z)*eta in the declared basis.
    expected=[0,0,0,0,0,0,-1,-1,-1j,0,0,0,1]
    req(all(abs(ker[i]-expected[i])<1e-9 for i in range(13)),"kernel generator interpretation")

    req(c["unique_regular_form"]["homogeneous"]=="(z-x1-x2-i*x3)*eta","unique form")
    req(c["consequence"]["order2_intrinsic_regular_improvement_exists"] is False,"no order2 improvement")
    req(c["consequence"]["W5_closed_negatively"] is False,"higher order remains open")
    req(c["remaining_user_selected_solo_routes"]==["W20","W16"],"remaining solo routes")

    for k,v in c["credit_firewall"].items():
        req(v is False,"credit "+k)

    print("PASS STAGE32_MB104_W5_SOLO_ORDER2_ACTIVE_SUPPORT_V1")
    print("active14=exact support hyperplane; stacked rank=12 kernel_dim=1")
    print("unique_regular_form=(z-x1-x2-i*x3)*eta")
    print("W5=order2_exhausted higher_order_open no_credit")

if __name__=="__main__":
    main()
