#!/usr/bin/env python3
"""Concrete Stage23 checkpoint20 candidate-family test.

Ansatz from two Euclid triples sharing the even leg:
  (m,n)=(x*y,z), (r,s)=(x*z,y)
so mn=rs=xyz and
  a=2xyz,
  b=x^2 y^2-z^2,
  c=x^2 z^2-y^2.
Then a^2+b^2 and a^2+c^2 are squares identically, while
  a^2+b^2+c^2=(x^4+1)(y^4+z^4).

This script tests positivity, strict ordering, exactly-two faces, integral space
diagonal, primitivity, and height. It does not infer asymptotics from its finite
search window.
"""
from math import gcd, isqrt


def square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r*r == n


def candidate(x: int, y: int, z: int):
    a = 2*x*y*z
    b = x*x*y*y-z*z
    c = x*x*z*z-y*y
    hab2 = a*a+b*b
    hac2 = a*a+c*c
    hbc2 = b*b+c*c
    d2 = a*a+b*b+c*c
    assert hab2 == (x*x*y*y+z*z)**2
    assert hac2 == (x*x*z*z+y*y)**2
    assert d2 == (x**4+1)*(y**4+z**4)
    edges = sorted((a,b,c))
    positive = min(a,b,c) > 0
    strict = edges[0] < edges[1] < edges[2]
    exactly_two = square(hab2) and square(hac2) and not square(hbc2)
    space = square(d2)
    primitive = gcd(a,gcd(b,c)) == 1
    return {
        "x":x,"y":y,"z":z,"a":a,"b":b,"c":c,
        "A":edges[0],"B":edges[1],"C":edges[2],
        "d":isqrt(d2) if space else 0,
        "positive":positive,"strict":strict,"exactly_two":exactly_two,
        "space":space,"primitive":primitive,
        "height2":d2,
    }


def main():
    hits=[]
    for x in range(1, 11):
        for y in range(1, 101):
            for z in range(y+1, 101):
                row=candidate(x,y,z)
                if all(row[k] for k in ("positive","strict","exactly_two","space","primitive")):
                    hits.append(row)
    print("primitive Stage19 hits in x<=10, 1<=y<z<=100:", len(hits))
    for r in hits:
        print(r)

    # Explicit scaling test of the first primitive hit. y,z -> t*y,t*z
    # scales a,b,c,d by t^2, hence every t>1 is nonprimitive.
    if hits:
        h=hits[0]
        print("scaling ray from first hit:")
        for t in range(1,6):
            r=candidate(h["x"],t*h["y"],t*h["z"])
            print(t, r)

if __name__ == "__main__":
    main()
