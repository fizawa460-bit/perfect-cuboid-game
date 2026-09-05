# Stage35-EX 35EX-29 — reciprocal common-factor Kummer compression

Status: `PROVISIONAL_EXACT_RECIPROCAL_COMMON_FACTOR_KUMMER_COMPRESSION_NO_CREDIT`

This unit starts only after hostile-audit PASS of 35EX-28 at exact head
`908047d41b3f856cb5e6083793fb4815666b64b3`, exact-head CI
`33932898366 / 101215004429`, merged as
`0ebf2cfec83a39b016f61b996a0dd533d242de87`, and after the mandatory
post-35EX-28 fresh exhaustive-view / blind-rediscovery audit.

The selected route is not a new five-elliptic decomposition. 35EX-23/24 already
audited that structure. The present leaf uses the newly completed K1--K4
rational-source receiver and removes one redundant coordinate before any
receiver-restricted local/global test.

No E1, R29, Stage35, or perfect-cuboid closure is claimed.

## 1. Audited input

Retain the 35EX-28 positive nondegenerate chamber

```text
A = alpha^2,
A > 1,
beta > A,

K1: u = 2*A*(beta^2-1)/(beta*(A^2-1)),
K2: b^2 = (A*beta+1)/(A+beta),
K3: kappa^2 = (beta-A)*(A*beta-1),
K4: lambda^2 = (beta^2-1)*(A^2*beta^2-1),
```

with exact order

```text
1 < (A^2+1)/(2*A) < b^2 < A < beta.
```

Put

```text
s = b^2,
c = (A^2+1)/(2*A).
```

Thus

```text
1 < c < s < A.
```

## 2. Eliminate beta exactly through K2

From K2,

```text
s*(A+beta) = A*beta+1,
```

hence, because `A-s != 0` on the retained chamber,

```text
beta = (A*s-1)/(A-s).                               (BETA)
```

Substituting this into K1 gives the deterministic rational coordinate

```text
u = 2*A*(s^2-1)/((A-s)*(A*s-1)).                    (U)
```

Therefore `beta` and `u` carry no additional square condition once `A,s` are
fixed on this open.

## 3. K3 becomes a reciprocal two-branch square

Using `(BETA)`,

```text
beta-A
 = 2*A*(s-c)/(A-s),

A*beta-1
 = 2*A*(c*s-1)/(A-s).
```

Therefore K3 is exactly equivalent to

```text
r^2 = (s-c)*(c*s-1),                                (R1)
```

under the rational change

```text
r = kappa*(A-s)/(2*A),
kappa = 2*A*r/(A-s).
```

No squareclass factor has been discarded: this is an exact iff on the retained
open.

## 4. K4 shares the same linear factor

Direct substitution of `(BETA)` gives

```text
(beta^2-1)*(A^2*beta^2-1)
 = s*(A^2-1)^2*(s^2-1)
   * 2*A*(c*s-1)/(A-s)^4.
```

Since `s=b^2` and `A=alpha^2`, define

```text
ell = lambda*(A-s)^2/(alpha*b*(A^2-1)).
```

Then K4 is exactly equivalent to

```text
ell^2 = 2*(c*s-1)*(s^2-1).                          (R2)
```

Conversely,

```text
lambda = alpha*b*(A^2-1)*ell/(A-s)^2
```

reconstructs K4 exactly. Again this is an iff, not a necessary-only
squareclass reduction.

## 5. Exact compressed full receiver

Consequently, on the 35EX-28 retained chamber, K1--K4 are equivalent to

```text
A = alpha^2,
s = b^2,
c = (A^2+1)/(2*A),

1 < c < s < A,

R1: r^2   = (s-c)*(c*s-1),
R2: ell^2 = 2*(c*s-1)*(s^2-1),

beta = (A*s-1)/(A-s),
u    = 2*A*(s^2-1)/((A-s)*(A*s-1)).
```

The inverse reconstruction is

```text
b      = a chosen square root of s,
beta   = (A*s-1)/(A-s),
kappa  = 2*A*r/(A-s),
lambda = alpha*b*(A^2-1)*ell/(A-s)^2,
u      = 2*A*(s^2-1)/((A-s)*(A*s-1)).
```

Thus this is a strict coordinate compression of the exact full rational-source
receiver, not a larger over-cover.

## 6. Common squareclass and the third implied character

Write

```text
M = s-c,
L = c*s-1,
N = s^2-1.
```

R1 and R2 say

```text
M*L is a square,
2*L*N is a square.
```

Multiplying and cancelling the square `L^2` gives the implied third character

```text
rho^2 = 2*(s-c)*(s^2-1),                            (R3)
rho = r*ell/(c*s-1).
```

All denominators are nonzero because `s>c>1`.

This is useful bookkeeping for future local work: the two active Kummer
conditions share exactly the factor `c*s-1`; it must not be charged twice.

## 7. Reciprocal algebraic symmetry

The branch set visible in the square equations is

```text
{0, infinity, -1, +1, c, 1/c}.
```

Under

```text
s -> 1/s,
```

R1 transforms by a rational square:

```text
(s-c)*(c*s-1)
 -> ((s-c)*(c*s-1))/s^2.
```

R2 transforms to the R3 radicand divided by `s^3`:

```text
2*(c*s-1)*(s^2-1)
 -> 2*(s-c)*(s^2-1)/s^3.
```

Because `s=b^2`, `s^3=b^6` is itself a rational square. Hence the algebraic
three-character package `{R1,R2,R3}` is permuted by reciprocal inversion.

This does **not** preserve the physical positive chamber: `s>1` maps to
`1/s<1`. Therefore no physical descent, point bijection, or theorem credit is
claimed from this involution alone.

## 8. Relation to historical genus-5 / five-elliptic work

Blind rediscovery of a six-branch multiquadratic cover is not new theorem
credit. 35EX-23 already gave the exact genus-5 character decomposition and
35EX-24 the five-elliptic isogeny/twist compression. The present result is
different and narrower:

```text
35EX-23/24: decompose the earlier full fiber by characters;
35EX-29: after K4 completion, eliminate beta and expose the exact shared
         Kummer factor in the rational-source receiver.
```

Any future character decomposition of R1/R2 must cite the audited 35EX-23/24
package rather than re-crediting it.

## 9. Arsenal routing and next arithmetic gate

Formal `S34-W03` now matches the compressed receiver as a router: a future leaf
may prove the exact R1+R2 receiver intersection empty or degenerate without
classifying every point on each auxiliary curve.

It does not itself supply such an exclusion. `S34-W02` remains locked because
no certified uniform full Mordell-Weil group is available for the moving
family. `S31-W01` remains a fiberwise birational adapter only.

The preserved next arithmetic candidate is therefore receiver-specific
joint-local/global classification on the compressed R1/R2 system.

## 10. Result

```text
K2_BETA_ELIMINATION_EXACT=true
K1_U_RECONSTRUCTION_EXACT=true
K3_R1_IFF_EXACT=true
K4_R2_IFF_EXACT=true
FULL_K1_K4_TO_R1_R2_RECEIVER_IFF=true
COMMON_KUMMER_FACTOR_CS_MINUS_1_EXACT=true
THIRD_CHARACTER_R3_IMPLIED=true
RECIPROCAL_BRANCH_SET_EXACT=true
RECIPROCAL_ALGEBRAIC_CHARACTER_PERMUTATION=true
RECIPROCAL_PHYSICAL_CHAMBER_PRESERVED=false
GENUS5_FIVE_ELLIPTIC_NEW_CREDIT=false
JOINT_LOCAL_OBSTRUCTION_PROVED=false
RECEIVER_INTERSECTION_CLOSED=false
UNIFORM_FULL_MW_PROVED=false
E1_PROVED=false
STAGE35_CLOSED=false
```

The common-factor compression is a stronger exact receiver formulation, so a
fresh breadth audit is required after hostile PASS before selecting the next
arithmetic leaf.
