# Stage14-4bv — inert Fourier completion and thin-packet switching boundary

## Purpose

Stage14-4bt and merged s7-06 reduce a physical ordered edge to two distinct positive rational points on the same squarefree `j=1728` twist, with infinite-order difference. The open 4bu branch additionally identified the universal fixed quartic

```text
F(P,Q)=P*Q*(Q-P)*(Q+P)
```

and an inert-prime zero trace, but 4bu is not used as a theorem input here because it is not merged at the start of this stage.

This stage independently rebuilds the fixed-quartic squareclass receiver from merged 4bt/s7-04/s7-06, strengthens the inert-prime trace to an **exact additive Fourier transform**, and inserts that transform into a square-sieve packet. The result is a genuine power saving on every thick product-square packet. The remaining obstruction is isolated exactly: thin square-part packets, which cannot be declared sparse because squarefree numerators/denominators naturally have square-part equal to `1`.

The thin branch is then converted into a dual large-squarefree-coefficient receiver. No new whole-family exponent is claimed in 4bv.

---

## 1. Merged inputs and current ledger

We use only merged inputs:

- Stage14-4bt: squarefree twist parameter `n=k*xi`, `n>1`, one-dimensional twist receiver;
- Stage14-s7-04: joint reduced coordinates `u=P/Q`, `w=R/S`, `QS<<B`, product-square and same-difference-kernel conditions;
- Stage14-s7-06: the physical two-point difference on `E_n` is infinite order;
- Stage14-4br/4bs: current whole-family exponent `20/21` and the architecture barrier for the older size-splitting route.

At the start of 4bv,

```text
V(B) << B^(20/21+o(1)).
```

The open Stage14-4bu PR is compatibility-checked only; all identities needed below are rederived here.

---

## 2. Universal fixed-quartic squareclass

For a reduced coordinate

```text
u=P/Q,
0<P<Q,
gcd(P,Q)=1,
```

put

```text
xi = ker(PQ),
k  = ker(Q^2-P^2).
```

Since

```text
gcd(PQ,Q^2-P^2)=1,
```

we have `gcd(xi,k)=1`, and therefore

```text
n=xi*k
 = ker(PQ(Q^2-P^2))
 = ker(PQ(Q-P)(Q+P)).
```

Thus define the universal binary quartic

```text
boxed:
F(P,Q)=P*Q*(Q-P)*(Q+P).                         (2.1)
```

A physical joint pair `(P,Q),(R,S)` satisfies

```text
ker(F(P,Q))=ker(F(R,S)).                         (2.2)
```

The two original joint conditions are retained more finely by the coprime factorization `n=xi*k`; (2.2) is a safe majorant because a fixed squarefree `n` has only `B^o(1)` coprime factorizations.

---

## 3. Balanced denominator strip rederived

Merged s7-04 gives

```text
QS << B.
```

The number of reduced rationals with denominator at most `L` is `O(L^2)`, and the fixed-coordinate physical fiber has multiplicity `B^o(1)`. Hence

```text
min(Q,S)<=L
```

contributes

```text
O(L^2 B^o(1)).                                    (3.1)
```

The critical value matching the current `20/21` ceiling is

```text
L=B^(10/21).
```

Consequently any future strict improvement over `20/21` only needs the balanced strip

```text
Q,S >= B^(10/21-o(1)),
QS << B,
```

and therefore, dyadically,

```text
Q,S <= B^(11/21+o(1)).                             (3.2)
```

We write `Q~U`, `S~V` with

```text
B^(10/21-o(1)) <= U,V <= B^(11/21+o(1)),
UV << B.
```

---

## 4. Product-square descent

The product-square condition is

```text
PR/(QS) = rational square.
```

Equivalently,

```text
ker(PQ)=ker(RS)=xi.                                (4.1)
```

For each fixed common squarefree label `xi`, write uniquely up to the squarefree prime allocation

```text
P=a*x^2,
Q=b*y^2,
R=c*z^2,
S=d*w^2,                                           (4.2)
```

where

```text
a*b=c*d=xi,
```

`a,b,c,d` are squarefree and the pairs `(a,b)` and `(c,d)` are coprime. Prime allocation costs at most

```text
4^omega(xi)=B^o(1).                                (4.3)
```

Now

```text
Q^2-P^2 = b^2*y^4-a^2*x^4,
S^2-R^2 = d^2*w^4-c^2*z^4.
```

Define

```text
G_ab(x,y)=b^2*y^4-a^2*x^4.                         (4.4)
```

The same-difference-kernel condition becomes

```text
G_ab(x,y)*G_cd(z,w) = square.                      (4.5)
```

This is the exact packet to which the inert-prime square sieve is applied.

---

## 5. Exact inert-prime projective trace

Let `p` be an odd prime with

```text
p == 3 (mod 4),
p not dividing a*b.
```

Let `chi_p` be the quadratic character with `chi_p(0)=0`.

Because `G_ab` is homogeneous of degree four and the degree is even,

```text
chi_p(G_ab(lambda*x,lambda*y))=chi_p(G_ab(x,y))
```

for every `lambda != 0`. Hence the trace is constant on projective lines.

For `y!=0`, put `t=x/y`. The complete projective sum is

```text
sum_t chi_p(1-(a/b)^2*t^4) + chi_p(-a^2).
```

For `p=3 mod 4`, inversion on `F_p^*` gives

```text
sum_t chi_p(1-c^2*t^4)=1
```

for every unit `c`, while `chi_p(-1)=-1`. Therefore the projective sum vanishes exactly:

```text
boxed:
sum_[x:y] chi_p(G_ab(x,y)) = 0.                   (5.1)
```

Equivalently,

```text
boxed:
sum_{x,y mod p} chi_p(G_ab(x,y)) = 0.             (5.2)
```

---

## 6. Exact additive Fourier transform

Define

```text
T_ab,p(h,k)
 = sum_{x,y mod p}
   chi_p(G_ab(x,y))*e_p(h*x+k*y).                  (6.1)
```

The projective homogeneity makes this transform elementary. Decompose all nonzero `(x,y)` into projective lines. For a fixed projective point,

```text
sum_{lambda in F_p^*} e_p(lambda*(h*x+k*y))
```

is `p-1` when `h*x+k*y=0` and `-1` otherwise. The total projective trace is zero by (5.1). Thus for `(h,k)!=(0,0)` only the unique orthogonal projective line remains, represented by `(x,y)=(k,-h)`.

Hence

```text
boxed:
T_ab,p(h,k)
 = p*chi_p(b^2*h^4-a^2*k^4),                      (6.2)
```

for `(h,k)!=(0,0)`, while

```text
T_ab,p(0,0)=0.                                     (6.3)
```

In particular every additive Fourier mode satisfies the sharp bound

```text
boxed:
|T_ab,p(h,k)| <= p.                                (6.4)
```

This is strictly stronger than a zero-frequency cancellation statement.

By CRT, for every odd squarefree modulus `m` whose prime factors are all `3 mod 4` and are coprime to `ab`, the corresponding Fourier transform has size

```text
<= m
```

at every frequency, up to the harmless `m^o(1)` bookkeeping from the CRT prime factors.

---

## 7. Arbitrary rectangle completion

Let `I,J` be integer intervals of lengths `X,Y`. Fourier completion modulo an inert squarefree modulus `m` and (6.4) give

```text
boxed:
S_ab,m(I,J)
:= sum_{x in I, y in J} chi_m(G_ab(x,y))
<< B^o(1) * ( X*Y/m + X + Y + m ).                 (7.1)
```

The `XY/m` term comes from one zero frequency paired with one nonzero frequency after periodic block decomposition; the fully zero mode vanishes exactly.

Primitive/coprimality restrictions are inserted by Mobius inversion and cost only `B^o(1)`. Auxiliary primes dividing `2abcdxyzw` are charged as the usual finite-divisor bad-prime error and also cost `B^o(1)` per state.

---

## 8. One square-sieve packet

Fix one product-square packet `(a,b,c,d)` and dyadic square-part boxes

```text
x in I_X,
y in I_Y,
z in I_Z,
w in I_W.
```

Put

```text
M = X*Y*Z*W.                                       (8.1)
```

Let `P_L` be inert primes `p=3 mod 4` in `[L,2L]`, after deleting the finite bad-prime set. The square sieve applied to (4.5) gives, up to `B^o(1)`,

```text
N_packet
<< M/L
 + average_{p!=q in P_L}
   |S_ab,pq(I_X,I_Y) * S_cd,pq(I_Z,I_W)|.          (8.2)
```

Using (7.1), with `m=pq~L^2`,

```text
boxed:
N_packet
<< B^o(1) * [
     M/L
     +(XY/L^2+X+Y+L^2)
      (ZW/L^2+Z+W+L^2)
   ].                                               (8.3)
```

This is the first exact inert-Fourier square-sieve adapter for the physical same-twist packet.

---

## 9. Thick packets receive a fixed power saving

Define the packet thickness

```text
H = min(X,Y,Z,W).                                   (9.1)
```

Assume `H>=2` and choose

```text
L = H^(1/2),
```

so the square-sieve modulus `pq` has scale `H`.

Because `X,Y>=H`,

```text
X+Y+H <= 3XY/H,
```

and symmetrically

```text
Z+W+H <= 3ZW/H.
```

Therefore (8.3) yields

```text
boxed:
N_packet << B^o(1) * M * H^(-1/2).                 (9.2)
```

The product-square universe summed over all squarefree labels and prime allocations has total packet volume

```text
sum M << U*V*B^o(1) << B^(1+o(1)).                 (9.3)
```

Hence the sector in which every packet has

```text
H >= B^tau
```

satisfies

```text
boxed:
N_thick(B;tau) << B^(1-tau/2+o(1)).                (9.4)
```

The critical value for the current `20/21` ceiling is

```text
tau=2/21.                                          (9.5)
```

Thus for any fixed `eta>0`,

```text
H >= B^(2/21+eta)
```

gives the strict sector improvement

```text
boxed:
N_thick << B^(20/21-eta/2+o(1)).                   (9.6)
```

So inert-prime one-Cauchy dispersion genuinely works on thick packets.

---

## 10. Why the thin sector cannot be discarded

The complement is

```text
min(X,Y,Z,W) < B^(2/21+o(1)).                      (10.1)
```

This is not a sparse pathology. In the decomposition

```text
P=a*x^2,
```

a squarefree numerator has `x=1`. Thus a positive-density-looking arithmetic population can live in the thin square-part sector. Any argument that simply charges (10.1) as a small-coordinate exception is invalid.

This is the precise obstruction encountered by the direct inert-prime square sieve.

---

## 11. Small numerator sector and the dual coefficient switch

The balanced denominator strip has

```text
Q,S <= B^(11/21+o(1)).
```

If, say,

```text
P <= B^(3/7),
```

then the number of possible reduced `(P,Q)` is at most

```text
B^(3/7+11/21+o(1))
 = B^(20/21+o(1)),                                  (11.1)
```

and fixed-coordinate partner multiplicity is `B^o(1)`. The same holds for `R`.

Therefore, after an arbitrarily small margin is inserted, any sector that can strictly beat the current ceiling may assume

```text
P,R >= B^(3/7-o(1)).                               (11.2)
```

Now suppose the numerator square-part is thin:

```text
x < B^(2/21+o(1)).
```

Since `P=a*x^2`, (11.2) forces

```text
boxed:
a >= B^(5/21-o(1)).                                (11.3)
```

Likewise, because `Q>=B^(10/21-o(1))`, a thin denominator square-part

```text
y < B^(2/21+o(1))
```

forces

```text
boxed:
b >= B^(2/7-o(1)).                                 (11.4)
```

The same alternatives hold for `c,d` on the second coordinate.

Hence every hard thin packet carries a **large squarefree coefficient**. This is the correct complementary variable, not an error term.

---

## 12. Dual coefficient Fourier identity

The switch is supported by another exact inert-prime identity.

For fixed nonzero square-part variables `x,y`, consider the coefficient polynomial

```text
H_xy(a,b)=y^4*b^2-x^4*a^2.                         (12.1)
```

This is homogeneous of degree two, and `chi_p(H_xy)` is again projectively invariant. The projective sum is

```text
sum_t chi_p(t^2-c^2) + 1 = 0,                      (12.2)
```

for every nonzero `c`. Exactly the same projective-line argument as Section 6 gives

```text
boxed:
sum_{a,b mod p}
 chi_p(H_xy(a,b))*e_p(h*a+k*b)
 = p*chi_p(y^4*h^2-x^4*k^2)                        (12.3)
```

for `(h,k)!=(0,0)`, and zero at `(0,0)`.

Thus the thin branch has a second flat Fourier transform available **after switching from square parts to squarefree coefficients**.

The unresolved issue is combinatorial rather than local-analytic: the shared squarefree label constraint `ab=cd=xi` couples these coefficients across the two coordinates. A future stage must organize this shared-label hyperbola without losing the Fourier cancellation.

---

## 13. New main-track receiver

4bv closes the following branches:

1. small denominator: already `<=B^(20/21+o(1))`;
2. balanced denominator + thick square-part packet: strict improvement for thickness `>B^(2/21)`;
3. balanced denominator + small numerator: `<=B^(20/21+o(1))`.

The only branch that can still control the whole-family ceiling is therefore

```text
balanced Q,S,
P,R >= B^(3/7-o(1)),
at least one square-part < B^(2/21+o(1)),
and the corresponding squarefree coefficient is large
  (>=B^(5/21-o(1)) for a numerator coefficient,
   >=B^(2/7-o(1)) for a denominator coefficient),
with ab=cd=xi.
```

This is the **adaptive square-part / squarefree-coefficient switching receiver**.

The next stage must keep the shared label `xi` intact while applying the coefficient-side Fourier identity (12.3). It must not sum absolute values over `xi` before the switch, because that loses the desired fixed power.

---

## 14. What is and is not proved

Proved in 4bv:

- universal fixed-quartic squareclass rederived from merged inputs;
- product-square squarefree-factor packetization;
- exact inert-prime projective trace for `G_ab`;
- exact additive Fourier transform (6.2);
- arbitrary rectangle bound (7.1);
- square-sieve packet inequality (8.3);
- thick-packet saving `M*H^(-1/2)`;
- whole thick-sector bound `B^(1-tau/2+o(1))`;
- critical thickness exponent `2/21`;
- strict improvement on every `tau>2/21` thick sector;
- small numerator threshold `3/7`;
- thin numerator coefficient lower bound `5/21`;
- thin denominator coefficient lower bound `2/7`;
- exact dual coefficient Fourier transform (12.3).

Not proved:

- a strict improvement over `20/21` for the full family;
- a global bound for the shared-label thin coefficient sector;
- square-root scale;
- perfect cuboid nonexistence.

The failure is now sharply localized: preserve `ab=cd=xi` while switching the dispersion variable from a thin square part to a large squarefree coefficient.

---

## Boundary

```text
STAGE14_4BV=INERT_FOURIER_COMPLETION_AND_THIN_PACKET_COEFFICIENT_SWITCH
MERGED_4BT_IMPORTED=true
MERGED_S7_06_IMPORTED=true
OPEN_4BU_USED_AS_THEOREM_INPUT=false
FIXED_BINARY_QUARTIC_REDERIVED=true
PRODUCT_SQUARE_PACKETIZATION_EXACT=true
INERT_PROJECTIVE_TRACE_ZERO=true
INERT_ADDITIVE_FOURIER_TRANSFORM_EXACT=true
INERT_FOURIER_MODE_BOUND=p
INERT_RECTANGLE_BOUND=XY/m+X+Y+m
FIXED_PACKET_SQUARE_SIEVE_ADAPTER_PROVED=true
THICK_PACKET_RELATIVE_SAVING=H^(-1/2)
THICK_SECTOR_BOUND=B^(1-tau/2+o(1))
CRITICAL_SQUAREPART_THICKNESS_EXPONENT=2/21
THICK_SECTOR_STRICTLY_BEATS_20_21_FOR_TAU_GT_2_21=true
SMALL_NUMERATOR_THRESHOLD=3/7
THIN_NUMERATOR_IMPLIES_SQUAREFREE_COEFFICIENT_GE_B^(5/21-o(1))=true
THIN_DENOMINATOR_IMPLIES_SQUAREFREE_COEFFICIENT_GE_B^(2/7-o(1))=true
DUAL_COEFFICIENT_FOURIER_TRANSFORM_EXACT=true
NEXT_PRIMARY_RECEIVER=SHARED_XI_ADAPTIVE_SQUAREPART_COEFFICIENT_SWITCH
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4bw
```
