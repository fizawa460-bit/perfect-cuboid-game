# Stage35-EX Goal4AT source lock — marked residual Kummer squareclass local support

Scope: continue the single LIVE route selected by provisional Goal4AS. Audited Stage35-EX authority remains V74 / Goal4AK. Goal4AT is a provisional exact source-recovery/local-support leaf stacked on the exact-green Goal4AS result. It does not promote Goal4AS or any later stacked leaf to hostile-audited authority and does not prove E1, Stage35, or any Perfect Cuboid theorem.

## Exact parent and routing inputs

Goal4AS is exact-green at

```text
head = 8615800bdcf37bba1d6a16a0c08f14a6cf7a6448
aggregate = 34284856812
verify-stage35-ex-current = 102259661960
```

and gives the marked physical Kummer shape

```text
E_q: Y^2 = X*(X-1)*(X+q^2),
delta(P)=([X],[X-1],[X+q^2])=(d,d,1).
```

The active question is to classify the residual class `d` locally and decide whether the already-retained source primitivity/valuation information forces `d=1`, a fixed finite squareclass family, or a new obstruction.

The matching Arsenal router is provisional `S35-PW01` (`PARAMETRIC_SQUARECLASS_COMPATIBILITY_GRAPH`). It is used only as a factor/gcd squareclass procedure. Its contract expressly does not turn a live parameter-dependent reservoir into a fixed finite squareclass family.

## Return to the primitive endpoint

Write the positive primitive integer endpoint as

```text
gcd(A,B,C)=1,

D_AB^2 = A^2+B^2,
D_AC^2 = A^2+C^2,
D_BC^2 = B^2+C^2,
W^2    = A^2+B^2+C^2.
```

The Goal4K nested Pythagorean parameters and Goal4L elliptic adapter recover, on the source-marked positive branch,

```text
p   = -B/C,
q   = (C^2-B^2)/(2*B*C),
h_q = -(B^2+C^2)/(2*B*C),
c   = (B^2-C^2)/(2*B^2),
z   = D_AB/D_AC.
```

Substituting into

```text
X = c*(z-p)/(z+1/p)
```

and using the face/space square equations gives the exact source formula

```text
X =
  (C*D_AB+B*D_AC)*(B*D_AB+C*D_AC)
  / (2*B*C*W^2).                                      (AT-1)
```

Indeed

```text
(B^2-C^2)*W^2
 = B^2*D_AB^2-C^2*D_AC^2
 = (B*D_AB-C*D_AC)*(B*D_AB+C*D_AC).
```

Subtracting 1 and using `D_BC^2=B^2+C^2` gives

```text
X-1 =
  D_BC^2*(D_AB*D_AC-B*C)
  / (2*B*C*W^2).                                      (AT-2)
```

Therefore the residual Kummer class is

```text
d = [(D_AB*D_AC-B*C)/(2*B*C)] in Q*/Q*^2.             (AT-3)
```

All endpoint lengths are positive and `D_AB*D_AC>B*C`, so this representative is positive. There is no `-1` squareclass support on the positive physical branch.

## Complementary-factor square identity

Define

```text
N_minus = D_AB*D_AC-B*C,
N_plus  = D_AB*D_AC+B*C.
```

Then

```text
N_minus*N_plus
 = D_AB^2*D_AC^2-B^2*C^2
 = (A*W)^2.                                            (AT-4)
```

Let

```text
G = gcd(N_minus,N_plus).
```

Because

```text
N_plus-N_minus = 2*B*C,
```

we have

```text
G | 2*B*C.                                             (AT-5)
```

Now write `N_minus=G*r0` and `N_plus=G*s0`. The two quotients are coprime and

```text
r0*s0 = (A*W/G)^2.
```

Hence each quotient is an integer square. There exist positive integers `r,s` such that

```text
N_minus = G*r^2,
N_plus  = G*s^2,
G*(s^2-r^2) = 2*B*C,
r*s = A*W/G.                                           (AT-6)
```

Combining `(AT-3)` and `(AT-6)` yields the exact one-reservoir description

```text
d = [G/(2*B*C)] = [(2*B*C)/G].                         (AT-KUMMER-GCD)
```

This is the Goal4AT local-support theorem. The entire residual marked Kummer class is the complementary squareclass of one source gcd reservoir `G` inside `2BC`.

Prime-by-prime, for every prime `ell`,

```text
v_ell(d) mod 2
 = v_ell(2*B*C)-v_ell(G) mod 2.                        (AT-v)
```

In particular,

```text
ell odd and ell not dividing B*C  =>  v_ell(d) even.
```

Thus every odd prime in `d` must already occur in `B*C`. At `ell=2` and at odd primes dividing `BC`, the remaining parity is exactly the live allocation between `G` and `2BC`; Goal4AT does not silently replace that allocation by a constant coefficient set.

## Exact interaction with the primitive gcd dictionary

The retained six-variable decomposition writes

```text
B = x*z*b,
C = y*z*c,
```

with the source-locked coprimality/parity dictionary. Hence

```text
[2*B*C] = [2*x*y*b*c]
```

because `z^2` is a square. This can simplify a later reservoir analysis, but it does not determine `[G]`: the current source facts do not force a fixed squareclass for `G`.

The existing two-adic theorem says exactly one edge is odd, the other two are divisible by 4, and the two even-edge 2-adic valuations are unequal. Goal4AT keeps this information source-locked, but does not claim that it alone determines `v2(G)` or trivializes the 2-part of `d`.

## Local non-finiteness test

Goal4F already gives, for every odd prime `ell != 3,5` and every `m>=1`, a full `Q_ell`-local four-square endpoint

```text
(ell^m,3,4)
```

up to edge permutation. Relabel the symmetric endpoint equations as

```text
(A,B,C)=(3,ell^m,4).
```

Choose the local square-root branch with

```text
D_AC=5,
D_AB^2=9+ell^(2m),   D_AB == +/-3 mod ell.
```

Then for `ell != 3,5`,

```text
N_minus = 5*D_AB-4*ell^m,
N_plus  = 5*D_AB+4*ell^m
```

are both `ell`-adic units, so

```text
v_ell(G)=0,
v_ell(2BC)=m,
v_ell(d)=m mod 2.                                     (AT-local)
```

Taking `m` odd shows that an arbitrary odd prime `ell != 3,5` can occur in the local residual class `d`. This is a **local non-obstruction statement only**. It does not assert a global endpoint for any such `ell`, nor does it prove that the global marked classes realized by actual endpoints have unbounded support.

Consequently the currently retained primitivity/valuation/local-equation information does not force `d=1` and does not produce a fixed finite global squareclass family. The new gain is instead an exact reduction from an opaque marked class to one dynamic source gcd reservoir.

## Route verdict

```text
GOAL4AT_EXACT_SOURCE_FORMULA=true
GOAL4AT_ONE_GCD_RESERVOIR_REDUCTION=true
GOAL4AT_ODD_SUPPORT_SUBSET_BC=true
GOAL4AT_ARBITRARY_NONFORCED_ODD_PRIME_LOCAL_ENTRY=true

D_TRIVIAL_PROVED=false
FIXED_FINITE_GLOBAL_SQUARECLASS_FAMILY_PROVED=false
TWO_DIVISIBILITY_PROVED=false
INFINITE_DESCENT_PROVED=false
```

The live route has therefore sharpened but not closed. The next exact leaf is

```text
35EX-35_GOAL4AU_MARKED_KUMMER_GCD_RESERVOIR_PRIME_ALLOCATION_PREFLIGHT
```

with the bounded question:

```text
use the primitive pair-gcd decomposition and the three face Pythagorean
structures to classify G prime-by-prime; test whether the complement
(2BC)/G is forced square on any branch, or whether a genuinely new
cross-face compatibility is required.
```

Do not treat a failure to force the complement square as a proof that `d` is globally nontrivial.

## Credit firewall

Certified provisionally only:

- the exact source formulas `(AT-1)`–`(AT-3)`;
- the complementary-factor square identity `(AT-4)`;
- `G|2BC` and the square quotients `(AT-6)`;
- `d=[(2BC)/G]`;
- odd support of `d` is contained in the odd prime support of `BC`;
- arbitrary `ell != 3,5` can enter `d` in the exact Goal4F local relaxation.

Not certified:

- `d=1` or `d!=1` for a global endpoint;
- a fixed finite global squareclass family;
- a complete 2-Selmer group;
- 2-divisibility of the marked point;
- an infinite descent;
- a new Brauer-Manin obstruction;
- E1, R29-PESCH-E1, Stage35, endpoint, or Perfect Cuboid existence/nonexistence closure.
