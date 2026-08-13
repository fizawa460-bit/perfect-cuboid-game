from itertools import product

checks=0
for u,v,A,B in product(range(-4,5), repeat=4):
    if A==0 and B==0:
        continue
    gp=(u*A-v*B, u*B+v*A)
    gm=(u*A+v*B, -u*B+v*A)
    # gamma+ - gamma- = 2 i B gamma0
    assert gp[0]-gm[0] == -2*v*B
    assert gp[1]-gm[1] ==  2*u*B
    # gamma+ + gamma- = 2 A gamma0
    assert gp[0]+gm[0] == 2*u*A
    assert gp[1]+gm[1] == 2*v*A
    # conjugate prime power preserves norm factor
    assert gp[0]*gp[0]+gp[1]*gp[1] == (u*u+v*v)*(A*A+B*B)
    assert gm[0]*gm[0]+gm[1]*gm[1] == (u*u+v*v)*(A*A+B*B)
    checks += 1
print({'arithmetic_pair_checks':checks,'status':'ok'})
