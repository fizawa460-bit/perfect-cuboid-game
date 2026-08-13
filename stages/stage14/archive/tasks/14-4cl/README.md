# Stage14-4cl

Stage14-4cl consumes merged 4ck and X3.

The X3 relaxed proportional/diagonal obstruction is eliminated by the physical cross-role locks:

```text
U/A=V/D
=> R*delta*X*s = J*alpha*Y*r
=> oddpart(R*delta) | Y*r
   and oddpart(J*alpha) | X*s,
```

which contradicts the balanced endpoint by a fixed exponent gap `1/4`.

The surviving off-proportional quartic receiver is then refined exactly:

```text
- gcd(U,V)|X*Y and gcd(A,D)|r*s, so moving gcds cost B^o(1);
- primitive F(a,b)=a*b*(b-a)*(b+a) has disjoint odd factor support;
- the equal-value equation becomes a 4 x 4 good-prime allocation matrix;
- switch integrality gives
    R*J | D^4-A^4,
    alpha*delta | V^4-U^4;
- each odd agreement prime is uniquely allocated to -, +, or i;
- i-branch primes are 1 mod 4.
```

At the sharp corner the dominant cyclotomic moduli are at least `B^(1/6-o(1))` and `B^(5/24-o(1))`, leaving nine branch types.

New receiver:

```text
OffDiagonalReciprocalCyclotomicQuarticAllocationIncidence
```

No whole-family power saving is claimed yet.

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
MAINLINE_H_NEEDED=false
NEXT=Stage14-4cm
```