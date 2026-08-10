# Stage14-4cl

Stage14-4cl consumes merged 4ck and the X2-compatible primitive-line packet.

The split quartic receiver is refined in two exact ways:

```text
1. after conditioning gcd(U,V)|X*Y and gcd(A,D)|r*s,
   primitive F(a,b)=a*b*(b-a)*(b+a) has pairwise-disjoint odd factor support,
   so the equal-value equation becomes a 4 x 4 good-prime allocation matrix;

2. switched-cell integrality gives
   R*J | D^4-A^4,
   alpha*delta | V^4-U^4,
   and every odd agreement prime is uniquely allocated to the -, +, or i
   cyclotomic factor on the opposite side.
```

At the unique conditional `7/8` corner, one xi-side cyclotomic branch has modulus at least `B^(1/6-o(1))` and one k-side branch at least `B^(5/24-o(1))`. This leaves nine dominant branch types.

New receiver:

```text
ReciprocalCyclotomicQuarticAllocationIncidence
```

No whole-family power saving is claimed yet.

```text
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
MAINLINE_H_NEEDED=false
NEXT=Stage14-4cm
```