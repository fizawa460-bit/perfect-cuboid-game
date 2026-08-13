# Stage14-4ck

Stage14-4ck consumes merged `14-4ci`, `14-4cj`, `14-s7-24`, and the merged X1 charge adapter.

The remaining eight-cell multiplicity is reduced exactly to four agreement cells.  For fixed residual triple, primitive physical root direction, and endpoint-small data,

```text
S*T
 = H_k^+ H_k^-/(q_k R J),

beta*gamma
 = H_xi^+ H_xi^-/(q_xi alpha delta),
```

so the switched-cell splits cost only `B^o(1)`.

The four agreement cells obey the exact common quartic equation

```text
(g1*g2) q_k (r1*r2)(s1*s2)
  F(R*x1*x2, J*y1*y2)
=
2 q_xi (x1*x2)(y1*y2)
  F(alpha*r1*r2, delta*s1*s2),

F(a,b)=a*b*(b-a)*(b+a).
```

New receiver:

```text
CommonCoreBinaryQuarticAgreementIncidence
```

No fixed-power saving is claimed yet; the whole-family exponent remains `7/8`.

```text
MAINLINE_H_NEEDED=false
NEXT=Stage14-4cl
```
