from itertools import product

checks=0
for A,B,u,v in product(range(-4,5), repeat=4):
    if A==0 and B==0:
        continue
    gp=(u*A-v*B, u*B+v*A)
    gm=(u*A+v*B, -u*B+v*A)
    # matrix sum/difference identities
    assert gp[0]+gm[0] == 2*A*u
    assert gp[1]+gm[1] == 2*A*v
    assert gp[0]-gm[0] == -2*B*v
    assert gp[1]-gm[1] ==  2*B*u
    # coordinate sign product identities: each coordinate has S^2-D^2 form
    assert gp[0]*gm[0] == (A*u)**2 - (B*v)**2
    assert gp[1]*gm[1] == (A*v)**2 - (B*u)**2
    checks += 1

# residue stabilizer sanity: if plus/minus forms coincide mod q, divisibility XOR is zero
residue_checks=0
for q in (3,5,7,9,11):
    for lp,lm in product(range(-30,31), repeat=2):
        if (lp-lm) % q == 0:
            assert ((lp % q)==0) == ((lm % q)==0)
            residue_checks += 1

print({'matrix_and_cone_checks':checks,'residue_stabilizer_checks':residue_checks,'status':'ok'})
