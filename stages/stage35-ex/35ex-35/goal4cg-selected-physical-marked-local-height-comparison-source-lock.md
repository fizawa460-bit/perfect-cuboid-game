# Stage35-EX Goal4CG — selected physical marked local-height comparison

Status: **PROVISIONAL_EXACT_EXPLICIT_UPPER_AND_PETSCHE_BLOCKER_PENDING_HOSTILE_AUDIT_NO_E1_CREDIT**.

This checkpoint executes the single post-Goal4CF obligation
`SELECTED_PHYSICAL_MARKED_LOCAL_HEIGHT_COMPARISON_PREFLIGHT`.  It keeps the
Goal4CF deterministic direction selector and the actual integer space diagonal
`W`.  The purpose is to make the marked-point upper height numerical, then test
whether the retained discriminant lower bound can produce a strict canonical-
height contradiction without assuming a uniform Szpiro bound.

No E1, Stage35, Stage29-parent, endpoint, or Perfect Cuboid credit is promoted.

## 1. Retained authority and inputs

- branch parent: `2ffe07f31d56caf78261d032b7e5a78d500dd146`;
- audited mathematical authority: V74 / Goal4AK, review `5142248509`;
- independently audited intermediate boundary: Goal4BS, review `5151846948`;
- Goal4CF remains provisional and supplies the selected global minimal model
  and
  `log|Delta_min(E_*)| >= 10 log W - log(12288)`;
- the Goal4BD forward marked-point formulas are used only on the physical
  endpoint population;
- MAIN-STATE is not rewritten.

The selected pair is one of AB, AC, BC with Goal4CF's reduced-pair-height
selector and fixed tie order.  Reorder the two reduced legs only to match the
cyclic BD orientation, writing them `(m,n)` so that

```text
p=-m/n,
q=(p^2-1)/(2p)=r/s,
r=n^2-m^2,
s=2mn,
t=m^2+n^2.
```

This changes at most the sign of Goal4CF's `r`; the curve, minimal model,
discriminant, conductor, and all height bounds below are unchanged.

Let `g` be the gcd removed from the selected raw edge pair, let `K` be the
opposite raw edge, and let

```text
d_m^2=(g*m)^2+K^2,
d_n^2=(g*n)^2+K^2,
W^2=g^2*(m^2+n^2)+K^2.
```

On a physical endpoint `d_m,d_n,W` are positive integers.  BD gives
`z=d_m/d_n`.

## 2. Exact marked x-coordinate on the Goal4CF minimal model

The BD point on

```text
E_q: Y^2=X*(X-1)*(X+q^2)
```

has

```text
c0=(p^2-1)/(2p^2),
X=c0*(z-p)/(z+1/p).
```

Substituting `p=-m/n` and `z=d_m/d_n` gives

```text
X = -r/(2mn) * (n*d_m+m*d_n)/(m*d_m-n*d_n).       (CG-1)
```

The AW integral coordinate is `x=s^2 X`.  Goal4CF then uses `x=4u`,
so the selected marked point on the global minimal model satisfies

```text
u = -(mn*r/2) * (n*d_m+m*d_n)/(m*d_m-n*d_n).       (CG-2)
```

The denominator cannot vanish.  Indeed,

```text
(m*d_m-n*d_n)*(m*d_m+n*d_n)
 = (m^2-n^2)*W^2
 = -r*W^2 != 0.                                    (CG-3)
```

The inequality uses the retained open `m!=n` and positivity of `W`.

## 3. Numerical naive x-height upper bound

Write the unreduced fraction in (CG-2) as

```text
U = -m*n*r*(n*d_m+m*d_n),
V = 2*(m*d_m-n*d_n).
```

Let `H(u)=max(|num(u)|,|den(u)|)` for the reduced rational coordinate.
Since reduction can only decrease height, `H(u)<=max(|U|,|V|)`.

Because `r^2+s^2=t^2`, `s=2mn`, and
`g^2*t <= W^2`, we have

```text
mn <= W^2/2,
|r| <= W^2,
(m+n)^2 <= 2t <= 2W^2,
d_m,d_n < W.
```

Hence

```text
|U| < W^6.
```

Also `|V| <= 2(m+n)W <= 2*sqrt(2)*W^2 <= W^6` for integer
`W>=2`.  Therefore

```text
H(u) <= W^6,
h_x(P_*) := log H(u) <= 6 log W.                     (CG-4)
```

This is an actual numerical coefficient, not the old Goal4M `O(log W)`.

## 4. Self-contained canonical-height upper bound

For the Goal4CF minimal model

```text
v^2+u*v
 = u^3 + ((r^2-s^2-1)/4)u^2 - (r^2*s^2/16)u,
```

the standard `b`-invariants are

```text
b2=r^2-s^2,
b4=-r^2*s^2/8,
b6=0,
b8=-r^4*s^4/256.
```

The duplication formula for the x-coordinate is

```text
x([2]Q)=F(x(Q))/G(x(Q)),
F(X,Z)=X^4-b4*X^2*Z^2-2*b6*X*Z^3-b8*Z^4,
G(X,Z)=4*X^3*Z+b2*X^2*Z^2+2*b4*X*Z^3+b6*Z^4.
```

Here

```text
F(X,Z)=(X^2+(r^2*s^2/16)Z^2)^2.
```

For coprime integer homogeneous coordinates with
`H=max(|X|,|Z|)`, the coefficient 1-norms give

```text
H(x([2]Q)) <= C(E_*) H^4,
C(E_*) <= max(
  1+r^2*s^2/8+r^4*s^4/256,
  4+|r^2-s^2|+r^2*s^2/4
).
```

Since `|r|,|s|<=t<=W^2` and `W>=2`, each displayed coefficient sum is
at most `W^16`.  Thus for every nonzero multiple of the non-torsion marked
point,

```text
h_x([2]Q) <= 4 h_x(Q)+16 log W.                       (CG-5)
```

Iterating and using the standard definition

```text
hhat(P)=1/2 * lim_{j->infinity} 4^(-j) h_x([2^j]P)
```

gives

```text
hhat(P_*) <= 1/2 h_x(P_*) + 8/3 log W
           <= 17/3 log W.                             (CG-6)
```

No external Weil-height/canonical-height comparison constant is needed for
(CG-6); it follows directly from the duplication map on the retained minimal
model.

## 5. Exact conductor packet and the Szpiro direction

Goal4CF proves `c4_min=r^4+r^2*s^2+s^4` is a unit at every prime dividing
the minimal discriminant.  Therefore every bad prime is multiplicative and
has conductor exponent one.

Put `R=|r*s*t|` and `e=v2(s)>=2`.  Since

```text
Delta_min=(R/4)^4,
```

the conductor is exactly

```text
N(E_*) = rad_odd(R)                         if e=2,
N(E_*) = 2*rad_odd(R)                       if e>=3.   (CG-7)
```

Consequently

```text
N(E_*) <= R/4
```

and, for Petsche's Szpiro ratio,

```text
sigma(E_*) = log|Delta_min|/log N(E_*) >= 4.           (CG-8)
```

This is a lower bound on sigma, not the missing uniform upper bound.

Petsche, *Small rational points on elliptic curves over number fields*,
NYJM 12 (2006), Theorem 2, gives over Q

```text
hhat(P) >= log|Delta_min| /
  (10^15*sigma^6*log^2(104613*sigma^2)).
```

Primary source:
<https://nyjm.albany.edu/j/2006/12-16v.pdf>, printed pp.258-260,
especially equation (1), Theorem 2, and Ogg's-formula consequence
`sigma>=1`.

Combining the best possible value allowed by (CG-8), namely `sigma=4`, with
Goal4CF's coefficient `10` shows that the coefficient in front of `log W`
supplied by this Petsche+CF comparison is at most

```text
10/(10^15*4^6*log^2(104613*16))
 < 1.19e-20.                                           (CG-9)
```

The explicit marked upper coefficient in (CG-6) is `17/3`.  Therefore the
retained Petsche/Goal4CF lower bound and the new explicit upper bound do not
produce a strict coefficient win, even in the most favorable `sigma=4`
case.  Since no uniform upper bound on sigma is proved, the actual Petsche
coefficient may be smaller still.

This is a failure of this explicit comparison, not a theorem that every
future height argument is impossible.

## 6. Why the individual local route is not yet a replacement lower bound

Petsche's local decomposition at multiplicative places contains a Bernoulli
component term depending on the component parameter of the point.  The
positive `Delta/12` lower bound used for points in the nonsingular subgroup
`E_0(Q_p)` therefore cannot simply be summed for an arbitrary marked point.

The source-marked coordinate already exposes the missing component control.
For an odd prime `ell|r`, if

```text
m*d_m-n*d_n != 0 mod ell,
```

then (CG-2) is integral with `u=0 mod ell`; on the reduction with `ell|r`
the point `(u,v)=(0,0)` is the nodal singular point.  If the denominator also
vanishes mod `ell`, cancellation/component analysis is required instead.
Current CF/BD source identities do not supply a uniform theorem choosing one
case with a favorable component index at every bad prime.  Analogous
cancellation questions occur at primes dividing `s`.

Thus a direct source-marked local lower bound strong enough to replace
Petsche remains an open, strictly smaller obligation:

```text
UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL.
```

No claim is made that such control is impossible.

## 7. Verification and audit boundary

The companion verifier checks:

- source-lock blobs retained from Goal4CF/Goal4AW/Goal4M/Goal4BD;
- the exact oriented BD marked-coordinate adapter on the retained three
  Euler-brick diagnostics (coordinate algebra only; they are not physical
  perfect cuboids);
- (CG-3) and `H(u)<=W^6` on those diagnostics;
- the duplication invariants and coefficient bounds;
- the exact conductor formula and `N<=R/4` on 2,000 coprime
  opposite-parity reduced pairs with `1<=m<n<100`;
- the numerical best-case Petsche coefficient comparison;
- the certificate digest and this source-lock digest.

The finite panels are regression checks only.  The unbounded claims are the
algebraic proofs above.

Checkpoint:

```text
CYCLE_ROUTE_STATUS=BLOCKED_EXPLICIT_UPPER_OBTAINED_NO_LOWER_COEFFICIENT_WIN
CYCLE_ACTIVE_RECEIVER=NONE_PENDING_HOSTILE_AUDIT
CYCLE_LIVE_CANDIDATES=0
CYCLE_UNTESTED_CANDIDATES=0
CYCLE_PARKING_AUDIT_COMPLETE=false
NEXT=HOSTILE_AUDIT_GOAL4CG_THEN_BREADTH_REOPEN
```

Still false:

```text
UNIFORM_SZPIRO_UPPER_BOUND=false
STRICT_CANONICAL_HEIGHT_COEFFICIENT_WIN=false
UNIFORM_MARKED_BAD_PRIME_COMPONENT_INDEX_CONTROL=false
FINITE_HEIGHT_REDUCTION=false
E1_proved=false
R29_PESCH_E1_closed=false
stage35_closed=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
HOSTILE_AUDIT_PASS=false
MERGE_AUTHORIZED=false
```

Goal4CG is intentionally a negative/blocked but exact research checkpoint.  It
is the requested clean hostile-audit boundary before any new breadth pass.
