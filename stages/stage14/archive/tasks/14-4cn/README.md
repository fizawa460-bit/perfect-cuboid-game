# Stage14-4cn

Stage14-4cn consumes merged `14-4cm` and merged `s7-27`.

The full signed quotient quadruple is already divisor-bounded for fixed residual data.  Because each signed agreement pair is coprime,

```text
x=L_x^+/L_x^-,
y=L_k^+/L_k^-
```

are primitive rational coordinates and determine the four odd allocation moduli exactly.

After the fixed quotient rescaling

```text
u=(c_x^+/c_x^-)*x=(D+A)/(D-A),
v=(c_k^+/c_k^-)*y=(Q+P)/(Q-P),
```

the physical `(2,2)` equation becomes

```text
(u^2-1)(v^2-1)=lambda*u*v,

lambda=16*r*s*X*Y*epsilon_x*epsilon_k
       /(c_x^-c_x^+c_k^-c_k^+).
```

Physical packets have `u,v>1` and `lambda>0`.  The projective curve is singular only at `lambda=0,±4`; the only physical singular coefficient is `lambda=4`, where the physical component is

```text
D*(Q-P)=A*(Q+P).
```

The receiver therefore splits into an explicit Cayley singular branch and a smooth genus-one reciprocal Edwards/Jacobi branch.  The whole-family exponent remains `7/8`.

```text
MAINLINE_H_NEEDED=true
MAINLINE_BLOCKED_BY_H=false
MAINLINE_H_REQUESTED_OBJECT=PhysicalReciprocalEdwardsGenusOneAverageIncidence
NEXT=Stage14-4co
```
