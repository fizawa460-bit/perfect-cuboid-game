# Stage30 final — self-contained closure of the modular action/cocycle kernel

```text
STAGE=Stage30
STATUS=AUDITED_FINAL_MERGE_NOT_AUTHORIZED
SOURCE_RECEIVER=R29-KUM5
SOURCE_KERNEL=K16-C2-MODULAR-S4-ACTION
PARENT_ROUTE=Q11-MODULAR
RECEIVER_STATUS=DISCHARGED_ACTION_COCYCLE_ADAPTER_ZERO_DEFECT_ELIMINATION
KERNEL_STATUS=CLOSED_COMPUTATIONAL_KERNEL
PARENT_ROUTE_STATUS=AMBER
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

This file is the Stage30 mathematical closeout surface. Its load-bearing definitions, action comparison, semilinear descent calculation, eight-defect classification, physical-open scope and final implication are written here. Repository paths, hashes, audits and executable checkers near the end are provenance and reproducibility records only; they are not substitutes for omitted mathematical steps.

## 1. Exact theorem and receiver

The perfect-cuboid canonical surface is

\[
\bar S\subset \mathbf P^6_{a_1,a_2,a_3,b_1,b_2,b_3,c}
\]

defined by

\[
a_1^2+a_2^2=b_3^2,\qquad
a_2^2+a_3^2=b_1^2,\qquad
a_1^2+a_3^2=b_2^2,
\]

\[
a_1^2+a_2^2+a_3^2=c^2.
\]

Stage30 consumes one already-defined Stage29 Class-2 receiver:

```text
receiver     R29-KUM5
kernel       K16-C2-MODULAR-S4-ACTION
parent route Q11-MODULAR
```

Its exact unresolved wall is:

```text
action-level arrangement-to-modular S4 identification
compatible with the Q/Q(i) descent cocycles
```

and the exact completion consequence is:

```text
attach the eight marked modular defects to the exact arrangement action.
```

This completion criterion is deliberately non-obstructive. It does **not** require any of the eight defects to be impossible. The kernel is not endpoint-decisive by itself.

Stage30 proves that this requested action/cocycle adapter exists on the full physical endpoint open, that all eight marked defects are attached to it exactly, and that the number of defects eliminated by this adapter is zero. Consequently `R29-KUM5` and `K16-C2-MODULAR-S4-ACTION` close, while `Q11-MODULAR` remains AMBER and the physical endpoint remains unexcluded.

## 2. The arrangement action that must be matched

The sign/Kummer presentation uses the seven branch lines on `P^2_[x:y:z]`

```text
A1 = x
A2 = y
A3 = z
B3 = x+y
B2 = x+z
B1 = y+z
C  = x+y+z.
```

Their projective arrangement automorphism group has order 24 and is isomorphic to `S4`. Over `Q`, only the coordinate-permutation subgroup of order 6 lifts to the cuboid sign cover. Over `K=Q(i)`, all 24 arrangement automorphisms lift because the only extra squareclass multiplier required is `-1=i^2`. Hence the line-orbit split is

```text
Q    : {A1,A2,A3} + {B1,B2,B3} + {C} = 3+3+1
Q(i) : {A1,A2,A3,C} + {B1,B2,B3}     = 4+3.
```

Fix the concrete arrangement generators

```text
s_arr = (A1 A2)(B1 B2)
t_arr = (A1 A2 A3 C)(B1 B3),
```

with dual-line matrix representatives

\[
s_{arr}=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},\qquad
t_{arr}=\begin{pmatrix}0&0&1\\-1&0&1\\0&-1&1\end{pmatrix}.
\]

Direct application to the seven linear forms gives the displayed permutations. Their permutation closure has order 24. On

```text
Omega_arr_4={A1,A2,A3,C}
Omega_arr_3={B1,B2,B3}
```

the action is transitive, with stabilizer orders 6 and 8 respectively.

The full geometric sign deck has order 64, so the geometric automorphism order is `64*24=1536`; this agrees with the Testa--Stoll automorphism exact sequence. Stage30 needs only the concrete 24-element quotient action, not the whole order-1536 group.

## 3. The intrinsic modular action

Independently define

\[
G_{mod}=PSL_2(\mathbf Z/4)
       =SL_2(\mathbf Z/4)/\{\pm I\}.
\]

Exact enumeration of determinant-one `2x2` matrices modulo 4 gives

```text
|SL2(Z/4)|  = 48
|PSL2(Z/4)| = 24.
```

Use

\[
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

modulo projective sign. They generate all 24 projective classes and satisfy, in the concrete enumerated action,

```text
ord(S)=2
ord(T)=4
ord(ST)=3.
```

Let

\[
V_{mod}=\ker\bigl(PSL_2(\mathbf Z/4)\to PSL_2(\mathbf F_2)\bigr).
\]

Exact reduction gives `|V_mod|=4`; direct multiplication makes it a Klein four group. In the frozen canonical matrix enumeration its four elements are

```text
g04 = identity
g06 = [[1,0],[2,1]]
g12 = [[1,2],[0,1]]
g14 = [[1,2],[2,1]]       mod 4, projectively.
```

The intrinsic modular `3+4` action sets are

```text
Omega_mod_3 = V_mod - {1}
Omega_mod_4 = { H <= G_mod : |H|=6, H∩V_mod={1}, H V_mod=G_mod }.
```

There are exactly three points in `Omega_mod_3` and exactly four order-six complements in `Omega_mod_4`. Thus the modular group has a concrete `3+4` action parallel in cardinality to the arrangement `3+4` action.

This coincidence alone is **not** the Stage30 adapter. An abstract `S4 ~= S4` identification carries no arithmetic credit.

## 4. Why the finite 4+3 coincidence is insufficient

All `4!*3!=144` pairs of bijections

```text
Omega_arr_4 -> Omega_mod_4
Omega_arr_3 -> Omega_mod_3
```

were exhaustively tested for simultaneous equivariance under one induced group identification. Exactly 24 survive. They form the expected finite relabelling torsor; each of the four modular complement points receives the arrangement label `C` in six candidates.

One convention-level representative sends

```text
A1,A2,A3,C -> h3,h2,h0,h1
B1,B2,B3   -> v0,v1,v2
s_arr -> S
t_arr -> T.
```

But 24 finite equivariant relabellings do not identify the source geometry. The intrinsic normal Klein four and its `3+4` actions are group-theoretic features of `S4`. Therefore Stage30 must compare the modular and cuboid actions on one common function field rather than promote a finite-action coincidence.

That common-model comparison is the load-bearing step.

## 5. Common `Q(i)` model of the same cuboid surface

The external geometric input is Testa--Stoll, *The surface parametrizing cuboids*, Section 4. Over `K=Q(i)` the same cuboid surface has the modular presentation

\[
\bar S_K\simeq (X(8)\times X(8))/\Delta G_0,
\]

where

\[
X(8):\quad
u^2=2xy,\qquad v^2=x^2-y^2,\qquad w^2=x^2+y^2,
\]

and

\[
G_0=\ker(PSL_2(\mathbf Z/8)\to PSL_2(\mathbf Z/4))\simeq(\mathbf Z/2)^3.
\]

On the diagonal quotient set

```text
U=u1*u2,  V=v1*v2,  W=w1*w2,
X=x1*x2,  Y=y1*y2,  T=x1*y2,  Z=x2*y1,
```

with the Segre relation

\[
XY=TZ.
\]

The explicit cuboid-coordinate identification is

```text
U = 2*b1
V = 2*b2
W = 2*b3
X = a1+c
Y = -a1+c
T = a2+i*a3
Z = a2-i*a3.
```

Consequently the seven cuboid squareclasses are represented on this same quotient by

\[
A_1=(X-Y)^2=4a_1^2,
\]

\[
A_2=(T+Z)^2=4a_2^2,
\]

\[
A_3=-(T-Z)^2=4a_3^2,
\]

\[
B_1=4XY=4b_1^2,
\]

\[
B_2=X^2+Y^2-T^2-Z^2=4b_2^2,
\]

\[
B_3=X^2+Y^2+T^2+Z^2=4b_3^2,
\]

\[
C=(X+Y)^2=4c^2.
\]

Thus the arrangement labels and modular action are now functions on the **same** cuboid surface. No abstract-group identification is being substituted for geometry.

## 6. The `X(4)` gauge and the actual branch projection

Since `X(8)/G0 ~= X(4) ~= P^1`, choose a `Q(i)` Hauptmodul gauge

```text
S:[x:y] -> [-x+y:x+y]
T:[x:y] -> [i*x:y].
```

Equivalently `S(t)=(1-t)/(1+t)` and `T(t)=i t` for `t=x/y`. The six cusp values are

```text
C6={0,infinity,1,-1,i,-i}.
```

The transformation formulas are standard `X(4)` formulas; the literal Testa--Stoll coordinate and any other degree-one Hauptmodul with the same six cusp values may differ by an element of `Aut(P^1,C6)`, the octahedral group of order 24. Hence the displayed generator labels below are a gauge choice, while kernel and image orders are invariant under the resulting conjugation.

Apply the diagonal modular transformations to `X,Y,T,Z`, reduce using `XY=TZ`, and compare the seven displayed quadratic squareclasses. In this chosen gauge:

```text
rho(S) = (A1 A2)(B1 B2)
rho(T) = (A1 C)(B2 B3).
```

Extending through all 24 elements gives

```text
|ker rho|=4
ker rho=V_mod
|im rho|=6
im rho ~= S3.
```

Thus the source-geometric action is not a faithful `S4 -> S4` action on the seven branch squareclasses. Its invariant shape is

\[
1\longrightarrow V_{mod}\simeq V_4
\longrightarrow PSL_2(\mathbf Z/4)\simeq S_4
\stackrel{\rho}{\longrightarrow} S_{3,branch}
\longrightarrow1.
\]

This explains the earlier 24 finite relabellings: they were valid finite-action objects but not 24 geometric adapters. The missing information is precisely how `V_mod` acts below the branch-squareclass quotient and how the whole action descends from `Q(i)` to `Q`.

## 7. Source-derived endpoint lifts

The required lift is derived directly from the `X(8)` equations, not chosen arbitrarily from the branch permutations.

On one `X(8)` factor choose

```text
S:
x' = (-x+y)/sqrt(2)
y' = (x+y)/sqrt(2)
u' = i*v
v' = i*u
w' = w

T:
x' = i*x
y' = y
u' = zeta_8*u
v' = i*w
w' = i*v.
```

Direct substitution preserves

```text
u^2=2xy,
v^2=x^2-y^2,
w^2=x^2+y^2.
```

Different square-root sign choices differ by `G0` and disappear after the diagonal `G0` quotient. Applying these transformations diagonally to `X(8)xX(8)` and then using the cuboid-coordinate formulas yields the following `Q(i)`-defined projective endpoint transformations on

```text
(a1,a2,a3,b1,b2,b3,c).
```

For `S0`:

```text
a1 -> -a2
a2 -> -a1
a3 -> -a3
b1 -> -b2
b2 -> -b1
b3 ->  b3
c  ->  c.
```

For `T0`:

```text
a1 -> -c
c  -> -a1
a2 ->  i*a2
a3 ->  i*a3
b1 ->  i*b1
b2 -> -b3
b3 -> -b2.
```

Direct substitution in the four cuboid quadrics verifies that both preserve `Sbar_K`. In `PGL_7(K)` they satisfy

```text
S0^2=1
T0^4=1
(S0*T0)^3=1.
```

They therefore generate a concrete 24-element projective endpoint action corresponding bijectively to `PSL2(Z/4)`.

## 8. Exact lift of the hidden `V_mod` kernel

The kernel elements are obtained from the source-derived generators:

```text
g12 = T0^2
g06 = S0*T0^2*S0^-1
g14 = g12*g06
g04 = 1.
```

Their endpoint actions are pure rational sign-deck transformations:

```text
g04 : identity

g12 : negate {a2,a3,b1}

g06 : negate {a1,a3,b2}

g14 : negate {a1,a2,b1,b2}.
```

Modulo common projective sign these four patterns are distinct and form a Klein four subgroup of the endpoint sign deck. Thus

\[
j:V_{mod}\hookrightarrow G_{sign}
\]

is an explicit injective lift. This is the information lost by the branch-squareclass projection `rho`.

## 9. The `Q(i)/Q` coordinate cocycle

Let `sigma` be complex conjugation in `Gal(Q(i)/Q)`. From

```text
T = a2+i*a3
Z = a2-i*a3
```

we have

\[
a_3=\frac{T-Z}{2i}.
\]

Conjugating the common-model isomorphism therefore changes only the sign of `a3`. Hence

```text
Phi^sigma = delta_a3 o Phi
```

and the coordinate descent cocycle is

\[
c_\sigma=\delta_{a_3}.
\]

It is `Q`-defined and has order two, so

\[
c_\sigma\,\sigma(c_\sigma)=1.
\]

This coordinate cocycle must not be confused with the arithmetic eight-torsion defect `kappa` introduced later.

## 10. Residual Galois automorphism and semilinear identity

The retained level-4 sign condition uses

\[
D_4=\operatorname{diag}(1,-1)\pmod4.
\]

Although `D4` is not itself an element of `PSL2(Z/4)`, it defines an automorphism

\[
\theta(g)=D_4gD_4^{-1}.
\]

On the modular generators,

```text
theta(S)=S
theta(T)=T^-1,
```

and direct reduction shows that `theta` fixes every element of `V_mod` pointwise.

Coefficient conjugation of the source-derived endpoint generators gives

\[
\sigma(S_0)=c_\sigma S_0 c_\sigma^{-1},
\]

\[
\sigma(T_0)=c_\sigma T_0^{-1}c_\sigma^{-1}.
\]

Let

\[
\widehat\alpha:G_{mod}\to Aut_K(\bar S_K)
\]

be the projective representation generated by `S0,T0`. The exact semilinear compatibility condition is

\[
\boxed{
\sigma(\widehat\alpha(g))
=c_\sigma\widehat\alpha(\theta(g))c_\sigma^{-1}
\quad\text{for every }g\in PSL_2(\mathbf Z/4).
}
\]

This was not accepted merely from the two generator formulas. An independent exact enumeration reconstructed all 24 modular classes and all 24 projective endpoint representatives, checked that every representative preserves the cuboid quadratic ideal, checked the correspondence on all `24*24=576` multiplication pairs, reconstructed `theta` on all 24 elements, and evaluated the boxed semilinear identity for all 24 elements. The result is

```text
modular classes                         24
endpoint projective representatives     24
multiplication pairs checked            576
semilinear elements checked              24
failed semilinear elements                0
V_mod/sign-deck intersection             exactly V_mod.
```

The computation uses exact integers, rationals and Gaussian rationals only; no floating-point comparison enters the certificate.

Thus the common-model modular action and its `Q(i)/Q` descent are exact on the endpoint surface, rather than inferred from an abstract `S4` isomorphism.

## 11. The arithmetic eight-torsion defect

For a rational endpoint point on the noncuspidal fine-moduli locus, the external Testa--Stoll modular interpretation supplies

```text
E/Q(i),
(P1,P2) a symplectic basis of E[4],
psi:E[8] -> E^sigma[8],
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

The minus sign is required because complex conjugation changes the Weil pairing `i` to `-i`; the sign on `P2^sigma` restores the symplectic convention.

Define

\[
\kappa=\psi^\sigma\circ\psi:E[8]\to E[8].
\]

The level-4 identities imply that `kappa` fixes the chosen `E[4]` basis. Hence, in a symplectic level-8 basis,

\[
\kappa\in K_8:=\ker(SL_2(\mathbf Z/8)\to SL_2(\mathbf Z/4)).
\]

Every element of `K8` has a unique form

\[
\kappa(A)=I+4A\pmod8,
\qquad
A=\begin{pmatrix}a&b\\c&a\end{pmatrix}\in\mathfrak{sl}_2(\mathbf F_2).
\]

There are exactly eight such matrices, so

\[
K_8\simeq(\mathbf Z/2)^3,
\qquad |K_8|=8.
\]

The ordinary unmarked conjugation action factors through `SL2(F2) ~= S3`. It has four orbits of sizes

```text
1,3,3,1,
```

corresponding to `A=0`, nonzero determinant-zero `A`, determinant-one nonidentity `A`, and `A=I`.

These four ordinary orbits are **not** the marked arithmetic quotient.

## 12. Why the marked arithmetic classes are eight singletons

The retained level-4 sign datum makes the `sigma` transport on `K8` trivial. Indeed, any mod-8 lift `M` of the retained level-4 correspondence satisfies `M mod 2=I`. For

\[
k=I+4A\in K_8,
\]

we have modulo 8

\[
MkM^{-1}=I+4(MAM^{-1})=I+4A,
\]

because the conjugation of `A` depends only on `M mod 2`. Thus

```text
sigma action on K8 = identity.
```

Since `K8` is abelian, the marked twisted relation

\[
k\sim g^{-1}k\,\sigma(g)
\]

reduces to equality on the retained marked defect datum. Therefore there are exactly eight marked `Q`-descent classes, each a singleton.

This is why the ordinary `1,3,3,1` orbit compression cannot be used to collapse the arithmetic defect population.

## 13. Exact `K8 ->` endpoint sign-deck adapter

The source `X(8)` action determines the adapter explicitly. Write

\[
A=\begin{pmatrix}a&b\\c&a\end{pmatrix}\in\mathfrak{sl}_2(\mathbf F_2).
\]

For the basis element `E12`, the standard level-8 translation satisfies

```text
T^4 = I+4E12 mod 8,
```

and the source action gives `T^4:u -> -u`, with `v,w` fixed. Thus `E12` flips `u`.

Residual `S` conjugation exchanges `E12` and `E21`, while the source action exchanges the `u,v` sign coordinates, so `E21` flips `v`.

The matrix `I` is the unique nonzero element of `sl2(F2)` fixed by all residual `S3` conjugation. The unique nonzero vector fixed by all permutations of the three sign coordinates is `(1,1,1)`, so `I` flips all of `u,v,w`.

By linearity,

\[
\boxed{
\phi\!\left(\begin{pmatrix}a&b\\c&a\end{pmatrix}\right)
=(a+b,\ a+c,\ a)\in\mathbf F_2^3.
}
\]

The three bits act on `(u,v,w)`. Since

```text
U=u1u2=2b1
V=v1v2=2b2
W=w1w2=2b3,
```

the same bits give the endpoint sign action on `(b1,b2,b3)`.

The residual `PSL2(Z/4)` action on `K8` factors through `S3` and, under `phi`, is exactly permutation of these three bits. Consequently the ordinary orbits are precisely the Hamming-weight layers of sizes `1,3,3,1`.

## 14. Complete eight-defect table

The complete marked population is therefore:

| defect | `A in sl2(F2)` | `kappa=I+4A mod 8` | endpoint sign image | ordinary weight/orbit | marked class |
|---|---|---|---|---|---|
| K8-000 | `[[0,0],[0,0]]` | `[[1,0],[0,1]]` | identity | W0 / 1 | singleton |
| K8-001 | `[[0,0],[1,0]]` | `[[1,0],[4,1]]` | `delta_{b2}` | W1 / 3 | singleton |
| K8-010 | `[[0,1],[0,0]]` | `[[1,4],[0,1]]` | `delta_{b1}` | W1 / 3 | singleton |
| K8-011 | `[[0,1],[1,0]]` | `[[1,4],[4,1]]` | `delta_{b1,b2}` | W2 / 3 | singleton |
| K8-100 | `[[1,0],[0,1]]` | `[[5,0],[0,5]]` | `delta_{b1,b2,b3}` | W3 / 1 | singleton |
| K8-101 | `[[1,0],[1,1]]` | `[[5,0],[4,5]]` | `delta_{b1,b3}` | W2 / 3 | singleton |
| K8-110 | `[[1,1],[0,1]]` | `[[5,4],[0,5]]` | `delta_{b2,b3}` | W2 / 3 | singleton |
| K8-111 | `[[1,1],[1,1]]` | `[[5,4],[4,5]]` | `delta_{b3}` | W1 / 3 | singleton |

The label `K8-100` corresponds to `A=I`, so its actual defect is `5I mod 8`; it is not the group identity.

Every row is fixed by `sigma`. Exact finite verification checks the adapter equivariance for every one of the `24*8=192` pairs `(g,kappa)` and reproduces all eight rows and their stabilizers. No row is eliminated:

```text
K8_DEFECT_COUNT=8
ALL_24x8_DEFECT_EQUIVARIANCE_VERIFIED=true
MARKED_Q_DESCENT_CLASS_COUNT=8
MARKED_CLASSES_ARE_SINGLETONS=true
DEFECT_ELIMINATION_COUNT=0.
```

## 15. Physical endpoint coverage and boundary firewall

It remains to show that the adapter applies to every physical endpoint, not only to a generic modular point.

On one `X(8)` factor the cusp locus is

\[
uvw=0.
\]

Indeed the six base values are `0,infinity,±1,±i`, the branch values of the three equations for `u,v,w`. Off `uvw=0`, the sign group `G0 ~= (Z/2)^3` acts freely: a nontrivial independent sign change cannot fix a point with all three coordinates nonzero.

On the diagonal quotient,

```text
U=u1u2=2b1
V=v1v2=2b2
W=w1w2=2b3.
```

A physical perfect-cuboid endpoint has positive, hence nonzero, face diagonals

\[
b_1b_2b_3\ne0.
\]

Therefore `U,V,W` are all nonzero, which forces

\[
u_1u_2v_1v_2w_1w_2\ne0.
\]

Both `X(8)` factors are noncuspidal, and the diagonal `G0` action is stabilizer-free on every physical endpoint preimage. Hence the fine-moduli action/cocycle construction of Sections 5--14 covers the **entire physical endpoint open**.

No extension to a compactified boundary is required for this receiver. In particular, Stage30 does not claim that the generic degree-24 modular map is everywhere finite on a compactification.

## 16. Exact receiver implication

Assume a physical endpoint point exists and consider its Stage29 modular datum.

1. By Section 15 it lies in the noncuspidal, stabilizer-free fine-moduli locus.
2. By Section 11 it supplies a conjugate-self level-8 correspondence with defect `kappa in K8`.
3. Sections 12--14 show that `kappa` is one of exactly eight distinct marked singleton classes and attach each class explicitly to an endpoint sign-deck action.
4. Sections 5--10 identify the residual modular action with the actual action on the same cuboid surface and verify the exact `Q(i)/Q` semilinear cocycle on all 24 residual elements.
5. Therefore every possible marked defect is attached to the exact arrangement/endpoint action with the required descent compatibility.

That is exactly the completion consequence of `R29-KUM5` / `K16-C2-MODULAR-S4-ACTION`. Hence

```text
R29_KUM5=DISCHARGED_ACTION_COCYCLE_ADAPTER_ZERO_DEFECT_ELIMINATION
K16_C2_MODULAR_S4_ACTION=CLOSED_COMPUTATIONAL_KERNEL
SMALLER_RESIDUAL_CLASS2_LEAF=NONE
NEW_CLASS3_THEOREM_GATE=NONE.
```

The argument is not a contradiction to the assumed endpoint. It is a complete classification/adapter theorem. All eight states survive this kernel:

```text
DEFECT_ELIMINATION_COUNT=0
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false.
```

Thus the parent route remains

```text
Q11_MODULAR=AMBER
ROUTE_COLOR_CHANGED=false.
```

## 17. Research-OS consequence

The frozen post-Stage29 frontier had

```text
active kernels = 13
Class 2        = 4
Class 3        = 9.
```

Stage30 closes exactly one Class-2 kernel and creates neither a smaller Class-2 leaf nor a Class-3 theorem gate. Therefore the live frontier becomes

```text
active kernels = 12
Class 2        = 3
Class 3        = 9.
```

Historical Stage29 closeout artifacts remain historical snapshots; this downstream consequence does not rewrite them.

## 18. Explicit non-claims

The following implications are not asserted:

```text
abstract S4 ~= S4
  => source-geometric cuboid/modular adapter                  FALSE

ordinary 8-congruence
  => physical endpoint                                        FALSE

E[8] ~= E^sigma[8]
  => E descends to Q                                          FALSE IN GENERAL

c_sigma = delta_a3
  => c_sigma equals arithmetic defect kappa                   FALSE

V_mod
  => K8                                                       FALSE

ordinary S4 orbit
  => marked arithmetic equivalence                            FALSE

marked defect survives
  => physical endpoint exists                                 FALSE

zero defects eliminated
  => physical endpoint exists                                 FALSE

Stage30 kernel closure
  => Q11-MODULAR is GREEN                                     FALSE

Stage30 kernel closure
  => perfect cuboid exists or does not exist                  FALSE.
```

Accordingly:

```text
ELLIPTIC_CURVE_Q_DESCENT_INFERRED=false
GENERIC_DEGREE_24_COMPACTIFICATION_CLAIM=false
ORDINARY_S4_ORBIT_EQUALS_MARKED_ARITHMETIC_CLASS=false
ORDINARY_8_CONGRUENCE_IMPLIES_ENDPOINT=false
DEFECT_ORBIT_MEMBERSHIP_IMPLIES_IMPOSSIBILITY=false
PRIMITIVE_CANONICAL_POPULATION_THEOREM_PROVED=false
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false.
```

## 19. External references

The external mathematical inputs used above are:

- Damiano Testa and Michael Stoll, *The surface parametrizing cuboids*, arXiv:1009.0388, especially Section 4 for the `X(8)` model, diagonal quotient, cuboid coordinates, modular interpretation and the `Q(i)` geometry.
- Ching-Li Chai, Chang-Shou Lin and Chin-Lung Wang, *Mean field equations, hyperelliptic curves and modular forms: I*, Cambridge J. Math. 3 (2015), Proposition 4.3 and Corollary 4.4, for the standard `X(4)` Hauptmodul transformation law. The Stage30 argument uses only the gauge-invariant consequence after accounting for the Möbius ambiguity preserving the six cusp values.

The Stage-specific hypotheses and the exact finite consequences of these inputs are stated in Sections 5--15, so these references do not conceal a repository-internal proof step.

## 20. Reproducibility provenance

The principal frozen repository artifacts used to reproduce the finite calculations are:

```text
concrete action tables
  stages/stage30/30-02C/action-tables.json
  blob d2ae114d859283b30ecfe3bf84448c8b3f6170ec

common Q(i) model / branch projection
  stages/stage30/30-05/common-anchor.json
  blob 8dabd493ba107142898ada88f9e8c0a2371fadf0

source-derived endpoint lifts / semilinear specification
  stages/stage30/30-06/semilinear-spec.json
  blob c699105666cd07ff9eded5dd60cf1896c25eaf4f

all-24 exact semilinear certificate
  stages/stage30/30-06C/semilinear-certificate.json
  blob 23338d990bc337f456967a5ab8d3b6d81a1b1769

all-eight defect classification
  stages/stage30/30-07/defect-classification.json
  blob 0a42601ec958f0e914b7e6be5f3461560657e644

physical-open adapter
  stages/stage30/30-08/physical-adapter.json
  blob 1c1e1f9297ded4305fde9e20ca0cb7fb4aa873a2

final certificate
  stages/stage30/30-09/final-certificate.json
  blob f1e8b8b823b3f7cce32cf78ec6bec76b875e63e1

final hostile audit
  stages/stage30/30-10/audit.md
  blob 9ed229c7078728d21c8152882f1182332682b1af
```

The independent all-24 semilinear verifier reconstructs `SL2(Z/4)`, `PSL2(Z/4)`, the source-derived projective endpoint group, all 576 multiplication pairs, `V_mod`, `theta`, `c_sigma` and all 24 semilinear identities using exact arithmetic. The final Stage30 checker independently reconstructs `PSL2(Z/4)`, `V_mod`, all eight `K8` endpoint images, the Hamming multiplicities `1,3,3,1`, the eight singleton marked classes, zero eliminations and the physical-open/firewall state; it binds rather than silently re-runs the separately audited all-24 semilinear certificate.

These records permit byte-for-byte reproduction. They are not required to determine the mathematical meaning of the Stage30 closeout, because that meaning and the load-bearing formulas are stated above.

## 21. Final handoff

The terminal hostile audit verdict is

```text
PASS_STAGE30_CLOSED_NONOBSTRUCTIVE_MODULAR_KERNEL.
```

The final Stage30 state is

```text
STAGE30_CLOSED=true
R29_KUM5_DISCHARGED=true
K16_C2_MODULAR_S4_ACTION_CLOSED=true
DEFECT_ELIMINATION_COUNT=0
SMALLER_RESIDUAL_CLASS2_LEAF=NONE
NEW_CLASS3_THEOREM_GATE=NONE
Q11_MODULAR_COLOR=AMBER
ROUTE_COLOR_CHANGED=false
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false
POST_STAGE30_ACTIVE_KERNELS=12
POST_STAGE30_CLASS2_KERNELS=3
POST_STAGE30_CLASS3_KERNELS=9
AUDIT_STATUS=PASS
ADVANCE_ALLOWED=false
AUTOMATIC_NEXT_STAGE=NONE
PERFECT_CUBOID_CONCLUSION=NONE
```

Stage30 is therefore closed as a complete action/cocycle/marked-defect adapter computation. It does not close the modular parent route and does not decide the perfect-cuboid problem.