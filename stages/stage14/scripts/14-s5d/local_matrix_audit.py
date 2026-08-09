#!/usr/bin/env python3
import itertools, json, math

PRIMES=[3,5,7,11,13,17,19,23,29,31]


def legendre(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1


def squares(p):
    return {x*x%p for x in range(p)}


def brute_row(kind,p,d1,d2,d3):
    sq=squares(p)
    # RHS normalized to one square unit at the two nonbad differences.
    for u1,u2,u3 in itertools.product(range(p), repeat=3):
        z1=d1*u1*u1%p; z2=d2*u2*u2%p; z3=d3*u3*u3%p
        if kind=='S':
            if (z1-z2)%p==0 and (z3-z1-1)%p==0:return True
        elif kind=='X':
            if (z3-z1)%p==0 and (z1-z2-1)%p==0:return True
        else:
            if (z3-z2)%p==0 and (z1-z2-1)%p==0:return True
    return False


def predicted(kind,p,d1,d2,d3):
    if kind=='S':return legendre(d3,p)==1
    if kind=='H':return legendre(d1,p)==1
    return legendre(d2,p)==1 or legendre(-d2,p)==1


def audit_odd():
    checked=0
    for p in PRIMES:
        units=range(1,p)
        # one representative for each quadratic-character triple with product +1
        reps={1:next(a for a in units if legendre(a,p)==1),-1:next(a for a in units if legendre(a,p)==-1)}
        for bits in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]:
            d1,d2,d3=[reps[b] for b in bits]
            for kind in 'SXH':
                got=brute_row(kind,p,d1,d2,d3)
                want=predicted(kind,p,d1,d2,d3)
                assert got==want,(p,kind,bits,got,want)
                checked+=1
    return checked

Q2_REPS=(1,3,5,7,2,6,10,14)

def q2_class_mul(a,b):
    x=a*b
    v=0
    while x%2==0:
        v^=1;x//=2
    u=x%8
    if u not in (1,3,5,7):raise AssertionError(u)
    return (2 if v else 1)*u

def q2_product_square(a,b,c):
    return q2_class_mul(q2_class_mul(a,b),c)==1

def q2_states():
    triples=[t for t in itertools.product(Q2_REPS,repeat=3) if q2_product_square(*t)]
    assert len(triples)==64
    selected=[t for t in triples if (t[0]%2==0 and t[1]%2==1 and t[2]%2==0)]
    unselected=[t for t in triples if all(x%2 for x in t)]
    return triples,selected,unselected

if __name__=='__main__':
    triples,selected,unselected=q2_states()
    out={
      'stage':'14-s5d',
      'odd_character_rows_checked':audit_odd(),
      'odd_primes_checked':PRIMES,
      'q2_squareclass_triples_product_square':len(triples),
      'q2_selected_13_parity_states':len(selected),
      'q2_unselected_parity_states':len(unselected),
      'all_odd_bad_prime_rows_explicit':True,
      'p2_complete_local_matrix_derived':False,
      'next':'14-s5e'
    }
    print(json.dumps(out,indent=2,sort_keys=True))
