# MB104 Z41 — exact tricanonical descent on the Birkar contraction — 2026-09-19

Status: **PRE-AUDIT EXACT Q-GORENSTEIN / TRICANONICAL CONTRACTION STRUCTURE / NO CREDIT**

## Input

For each of the three surviving balanced supports,

```text
0000770000ff,
00007b0000ff,
000707000f0f,
```

the retained Z3 package gives

```text
P = 7H - 4 sum_(i in Sigma) E_i,
P^2=336,
K_S=H,
P big and nef,
P semiample,
Null(P) completely classified.
```

Let

```text
phi:S -> Y
```

be the birational contraction defined by a sufficiently divisible multiple of P.

Birkar Theorem 1.4 is the applicable semiampleness criterion:
for a nef Q-Cartier divisor L there is a closed thickening Z with Z_red=E(L) such that
L is semiample iff L|Z is semiample.

## 1. Total transform of the support hyperplane

The archived incidence-16 section classification is exact.

### Size-48 support type

The singular hyperplane section is reduced:

```text
Sbar cap L = Q1+Q2+Q3+Q4,
```

with four smooth elliptic quartics. Each of the 16 section nodes lies on exactly two quartics.

On the smooth A1 resolution, the strict sum therefore meets each corresponding exceptional curve
with total intersection 2. Since H.E=-0 and E^2=-2, the exceptional coefficient in the total
transform is one:

```text
H ~ Q1+Q2+Q3+Q4 + sum_(j in T16) E_j.
```

For a balanced support Sigma of size 14, the two omitted section nodes are precisely the two
unsupported exceptionals E_a,E_b which connect the quartics into two Q-E-Q trees. Hence

```text
P
 = 7H - 4 sum_(Sigma) E
 = 3H + 4(Q1+Q2+Q3+Q4+E_a+E_b).
```

Since K_S=H,

```text
P = 3K_S + 4(Q1+Q2+Q3+Q4+E_a+E_b).          (Z41-48)
```

### Size-768 support type

The incidence-16 size-24 hyperplane section has scheme structure

```text
Sbar cap L = 2A+2B
```

with disjoint eight-node supports on the two reduced elliptic quartics.

At each of the 16 section nodes the doubled strict component meets the exceptional with total
intersection 2, hence again

```text
H ~ 2A+2B + sum_(j in T16) E_j.
```

The balanced support omits exactly E_A,E_B, one on each quartic. Therefore

```text
P
 = 7H - 4 sum_(Sigma) E
 = 3H + 8A+8B+4E_A+4E_B,
```

or

```text
P = 3K_S + 8A+8B+4E_A+4E_B.                 (Z41-768)
```

## 2. The numerical discrepancies become exact Q-Gorenstein discrepancies

Semiampleness gives an ample Q-Cartier divisor A_Y on Y with

```text
P ~_Q phi^* A_Y.
```

Push forward (Z41-48) or (Z41-768). Exceptional divisors disappear and
`phi_*K_S=K_Y` as a Weil canonical divisor, so

```text
A_Y ~_Q 3K_Y.
```

Thus

```text
K_Y is Q-Cartier,
3K_Y is Q-linearly equivalent to the ample descended P-polarization,
K_Y is ample,
Q-Gorenstein index divides 3.
```

Accordingly the discrepancy vectors previously recorded only conditionally are now unconditional:

Size-48 Q-E-Q tree:

```text
a_Q1=a_E=a_Q2=-4/3.
```

Size-768 connected graph:

```text
a_A=a_B=-8/3,
a_EA=a_EB=-4/3.
```

The 32 isolated A1 contractions are crepant.

Hence the nonrational contraction points are strictly worse than log canonical.

## 3. Canonical square

Because `A_Y~_Q3K_Y` and `phi^*A_Y~_QP`,

```text
K_Y^2=P^2/9=336/9=112/3.
```

This upgrades the earlier discrepancy-square checksum to an exact Q-Gorenstein identity.

## 4. Topological Euler checksum

The smooth cuboid resolution has

```text
e(S)=c2(S)=80.
```

### Size-48

There are 32 isolated A1 exceptional P1s and two connected Q-E-Q fibers.
Each Q-E-Q tree has Euler characteristic

```text
0+2+0-1-1=0.
```

Replacing each isolated P1 by a point changes Euler characteristic by -1, while replacing each
tree of Euler characteristic zero by a point changes it by +1. Thus

```text
e(Y)=80-32+2=50.
```

There are 34 singular points, hence

```text
e(Y_reg)=50-34=16.
```

### Size-768

There are 32 isolated A1 fibers and one connected fiber A+B+E_A+E_B.
Its Euler characteristic is

```text
0+0+2+2 -2 -1 -1 =0,
```

where A and B meet in two points. Hence

```text
e(Y)=80-32+1=49,
#Sing(Y)=33,
e(Y_reg)=16.
```

Therefore all three surviving support types have the same exact smooth-locus Euler invariant

```text
e(Y_reg)=16.
```

## 5. Reformulation of a hypothetical carrier

If an irreducible carrier

```text
C in |lP|
```

exists, then C is disjoint from every P-null curve. Hence it is disjoint from the exceptional
locus of phi and phi is an isomorphism along C.

Its image C_Y therefore satisfies

```text
C_Y subset Y_reg,
C_Y in |3l K_Y|_Q,
normalization genus(C_Y)=1.
```

So the surviving balanced problem can be reformulated as:

```text
Does the index-dividing-3 Q-Gorenstein surface Y with ample K_Y,
K_Y^2=112/3 and e(Y_reg)=16 admit an integral pluricanonical
curve in |3lK_Y|, disjoint from Sing(Y), with normalization genus one?
```

This is a reformulation, not an existence or nonexistence result.

## 6. Next leaf

The contraction local-Euler route can now use the **actual** global contraction rather than a
single-quartic thought experiment:

```text
MB104-Z42-QGORENSTEIN-CONTRACTION-LOCAL-SYMMETRIC-EULER-PREFLIGHT
```

Target: determine whether Wahl/Blache/Langer local Chern / local Euler theory supplies a
source-complete leading cubic correction for the two non-lc Q-Gorenstein graph types above.
Do not substitute quotient-singularity formulas. If the theory requires quotient/log-canonical
singularities or unavailable analytic local data, record the wall.

## Source locks

- Birkar, arXiv:1312.0239, Theorem 1.4.
- archived incidence-16 section note blob
  `593868a09e41ebfd1ad7f0f4c1aa83f6ca5cd923`;
- Z40B complete-null-locus note blob
  `ef72f41f211bc2abf6f6d3cb6dd4c26ea903d4bf`;
- Z3 semiampleness note blob
  `6877f13b66702f5695240c51d56141816b40726b`;
- contraction graph note blob
  `eba722f6a57bacdda81f2a869d8cd83eb405a788`.

## Firewalls

```text
Y_Q_Gorenstein_pre_audit=true
Q_Gorenstein_index_divides_3=true
K_Y_ample_pre_audit=true
K_Y2=112/3
e_Y_reg=16
surviving_orbits_excluded=false
irreducible_carrier_exists=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
