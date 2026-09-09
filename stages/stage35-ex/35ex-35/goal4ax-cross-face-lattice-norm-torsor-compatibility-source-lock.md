# Stage35-EX Goal4AX source lock — cross-face six-norm torus compatibility

Scope: execute the `CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY` lens retained by Goal4AS. Audited Stage35-EX authority remains V74 / Goal4AK (hostile review `5142248509`). Goal4AX is provisional and may only consume the exact-green Goal4AW parent after its repaired exact-head aggregate succeeds. No E1, Stage35, endpoint, or Perfect Cuboid credit is granted here.

## 1. Six exact Pythagorean norm equations

For a positive rational endpoint write

```text
D_AB^2=A^2+B^2,
D_AC^2=A^2+C^2,
D_BC^2=B^2+C^2,
W^2=D_AB^2+C^2=D_AC^2+B^2=D_BC^2+A^2.
```

Equivalently, with `N(z)=z*conj(z)` on `Q(i)`,

```text
N(A+iB)=D_AB^2,
N(A+iC)=D_AC^2,
N(B+iC)=D_BC^2,                                  (AX-N1)

N(D_AB+iC)=W^2,
N(D_AC+iB)=W^2,
N(D_BC+iA)=W^2.                                   (AX-N2)
```

Thus the three face circles and the three space-diagonal circles form one six-incidence norm package.

The primitive pair-gcd decomposition does not change the face ratios. For example

```text
A=x*y*a, B=x*z*b, D_AB=x*r_AB
```

gives

```text
B/(D_AB+A)=z*b/(r_AB+y*a).
```

Hence the rational torus coordinate below is already compatible with the primitive reduced face dictionary. The gcd/parity information remains an additional *integral representative* condition; it is not a new rational norm equation.

## 2. Universal half-angle chart for one positive norm equation

For a positive rational Pythagorean triple

```text
U^2+V^2=H^2
```

put

```text
t=V/(H+U).
```

Then `0<t<1`, and with

```text
R(t)=2*t/(1-t^2),
H0(t)=(1+t^2)/(1-t^2),
```

one has

```text
V/U=R(t),
H/U=H0(t),
H0(t)^2-R(t)^2=1.                                 (AX-H1)
```

On the norm-one torus `T=Res^1_{Q(i)/Q} G_m`,

```text
(U+iV)/H = (1+i*t)/(1-i*t).                       (AX-H2)
```

Therefore every one of the six positive endpoint norm equations has an explicit Hilbert--90 lift `1+i*t` in `Q(i)^*`. No local or global norm-solvability obstruction is left at this level.

## 3. Six source-marked torus coordinates

Define the three face coordinates

```text
f_AB = B/(D_AB+A),
f_AC = C/(D_AC+A),
f_BC = C/(D_BC+B),
```

and the three space coordinates

```text
s_AB = C/(W+D_AB),
s_AC = B/(W+D_AC),
s_BC = A/(W+D_BC).                                (AX-COORD)
```

All lie in `(0,1) cap Q` on the positive endpoint open.

Their leg ratios are

```text
B/A       = R(f_AB),       D_AB/A = H0(f_AB),
C/A       = R(f_AC),       D_AC/A = H0(f_AC),
C/B       = R(f_BC),       D_BC/B = H0(f_BC),

C/D_AB    = R(s_AB),       W/D_AB = H0(s_AB),
B/D_AC    = R(s_AC),       W/D_AC = H0(s_AC),
A/D_BC    = R(s_BC),       W/D_BC = H0(s_BC).
```

Because the same edges and diagonals occur in several circles, the six torus coordinates satisfy exactly four rational compatibility relations:

```text
R(f_AC) = R(f_AB)*R(f_BC),                         (AX-C1)

R(s_AB) = R(f_AC)/H0(f_AB),                        (AX-C2)

R(s_AC) = R(f_AB)/H0(f_AC),                        (AX-C3)

R(s_BC) = 1/(R(f_AB)*H0(f_BC)).                    (AX-C4)
```

These relations are source identities: `(AX-C1)` is `C/A=(B/A)(C/B)`, while `(AX-C2)`--`(AX-C4)` are the three space-leg ratios.

## 4. Exact inverse reconstruction

Conversely, suppose six rational parameters in `(0,1)` satisfy `(AX-C1)`--`(AX-C4)`. Up to positive scaling choose

```text
A=1,
B=R(f_AB),
C=R(f_AC),

D_AB=H0(f_AB),
D_AC=H0(f_AC),
D_BC=R(f_AB)*H0(f_BC),

W=H0(f_AB)*H0(s_AB).                               (AX-INV)
```

Using `H0(t)^2=1+R(t)^2` and `(AX-C1)`,

```text
D_AB^2 = A^2+B^2,
D_AC^2 = A^2+C^2,
D_BC^2 = B^2+C^2.
```

Using `(AX-C2)`,

```text
W^2
 = H0(f_AB)^2*(1+R(s_AB)^2)
 = H0(f_AB)^2+R(f_AC)^2
 = 1+R(f_AB)^2+R(f_AC)^2
 = A^2+B^2+C^2.                                    (AX-W)
```

The same value is recovered from `(f_AC,s_AC)` and `(f_BC,s_BC)` because `(AX-C3)` and `(AX-C4)` give

```text
D_AC^2*H0(s_AC)^2 = A^2+B^2+C^2,
D_BC^2*H0(s_BC)^2 = A^2+B^2+C^2.
```

Thus the positive endpoint open modulo scaling and the positive rational six-torus compatibility chart are mutually reconstructible. Goal4AX has produced an exact reparameterization, not a stricter receiver.

## 5. Why this does not produce a new torsor obstruction

The six norm-one phases live in `T(Q)^6`, but each phase already has the explicit source lift

```text
lambda_t=1+i*t,
lambda_t/conj(lambda_t)=(U+iV)/H.
```

So the product Hilbert--90 torsor is split pointwise by the endpoint.

The four cross-face equations are also not independent arithmetic conditions: `(AX-INV)` proves they are precisely the incidence equations needed to reconstruct the same endpoint. Consequently:

```text
NEW_NONTRIVIAL_H1_TORSOR_CLASS=false
NEW_LOCAL_NORM_OBSTRUCTION=false
NEW_SPINOR_REPRESENTATION_OBSTRUCTION=false
NEW_BRANCH_PRUNING=false
```

This also explains the Goal4O boundary. A single represented ternary form was tautological there; assembling all six circle norms does create a useful common chart, but its rational compatibility variety is still endpoint-equivalent.

A genuine future lattice/spinor attack would need an additional arithmetic lift condition that is *necessary* for every endpoint yet not automatically split by `(AX-COORD)`. Merely requiring a rational Spin lift of an auxiliary rotation would not be valid unless such necessity were separately proved.

## 6. Relation to Goal4AU

Goal4AU's exact relation

```text
d_A*d_B*d_C=1
```

is retained. Goal4AX does not force any individual `d_i=1`, does not recover the three source reservoirs, and does not turn the six norm phases into a common Selmer complex. The six-torus chart is therefore not a hidden repair of the blocked common-cover route.

## 7. Decision

```text
CROSS_FACE_LATTICE_NORM_TORSOR_COMPATIBILITY
  -> PASS_EXACT_SPLIT_SIX_NORM_TORUS_CHART
  -> BLOCKED_AS_POSITIVE_ENDPOINT_BIRATIONAL_REPARAMETRIZATION

SIX_NORM_PACKAGE_CONSTRUCTED=true
SIX_HILBERT90_LIFTS_EXPLICIT=true
FOUR_CROSS_FACE_COMPATIBILITIES_EXACT=true
POSITIVE_ENDPOINT_OPEN_RECONSTRUCTED=true
NEW_TORSOR_OBSTRUCTION=false
NEW_BRANCH_PRUNING=false
```

The next genuinely distinct untested Goal4AS lens is the nonlinear full-endpoint descent route:

```text
NEXT=35EX-35_GOAL4AY_GENUINE_NONLINEAR_FULL_ENDPOINT_SELF_MAP_DESCENT_PREFLIGHT
```

It must seek a total source-locked self-map of the full endpoint population that preserves all four square equations and strict positivity/primitivity while strictly decreasing a well-founded height. It must not reuse the already-closed common scalar `v2` division from Goal4I.

No merge. No hostile-audit credit. `MAIN-STATE.json` remains at V74 / Goal4AK.
