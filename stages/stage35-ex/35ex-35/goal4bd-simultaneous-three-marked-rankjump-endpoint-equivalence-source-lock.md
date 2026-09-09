# Stage35-EX Goal4BD source lock — simultaneous three-marked rank-jump receiver collapses to endpoint equivalence

Scope: execute the Goal4BC-selected new view `SIMULTANEOUS_THREE_MARKED_RANKJUMP_FIBER_PRODUCT_RECEIVER`. Audited authority remains V74 / Goal4AK. This leaf materializes the joint receiver of the three cyclic Goal4L marked elliptic points and determines its exact relation to the physical endpoint population. It does not prove E1 or nonexistence.

## 1. Three cyclic Goal4L orientations

Let a positive rational physical endpoint have edges `A,B,C`, face-square radicands

```text
R_AB=A^2+B^2,
R_AC=A^2+C^2,
R_BC=B^2+C^2,
W2=A^2+B^2+C^2.
```

Use the three cyclic orientations

```text
A-orientation: p_A=-B/C, z_A=D_AB/D_AC,
B-orientation: p_B=-C/A, z_B=D_BC/D_AB,
C-orientation: p_C=-A/B, z_C=D_AC/D_BC.                (BD-1)
```

For each `i in {A,B,C}`, Goal4L gives

```text
q_i=(p_i^2-1)/(2*p_i),
c_i=(p_i^2-1)/(2*p_i^2),
E_i: Y_i^2=X_i*(X_i-1)*(X_i+q_i^2),
X_i=c_i*(z_i-p_i)/(z_i+1/p_i),                         (BD-2)
```

with inverse

```text
z_i=-(X_i+(p_i^2-1)/2)/(p_i*(X_i-c_i)).                (BD-3)
```

Equivalently, before the elliptic Möbius adapter, each cyclic marked point lies on the Goal4L quartic

```text
eta_i^2=(p_i^2-z_i^2)*(z_i^2-p_i^(-2)).                (BD-Q_i)
```

The retained physical open excludes zero denominators, `p_i=+-1`, and the Goal4L exceptional/torsion loci.

## 2. Exact cross-face compatibility equations

The three base ratios satisfy

```text
p_A*p_B*p_C=-1.                                         (BD-P)
```

The three face-diagonal ratios satisfy

```text
z_A*z_B*z_C=1                                           (BD-Z)
```

on the positive branch.

More importantly, the same edge triple gives

```text
z_A^2=R_AB/R_AC=(1+p_C^(-2))/(1+p_B^2),
z_B^2=R_BC/R_AB=(1+p_A^(-2))/(1+p_C^2),
z_C^2=R_AC/R_BC=(1+p_B^(-2))/(1+p_A^2).                (BD-FR)
```

A denominator-cleared independent pair is

```text
z_A^2*p_C^2*(1+p_B^2)=1+p_C^2,                         (BD-FR-A)
z_B^2*p_A^2*(1+p_C^2)=1+p_A^2.                         (BD-FR-B)
```

Together with `(BD-P)` and `(BD-Z)`, the third equation in `(BD-FR)` follows automatically.

These four cross equations are generically independent. For the exact rational diagnostic triple

```text
(A,B,C)=(44,117,240),
(p_A,p_B,p_C)=(-39/80,-60/11,-44/117),
(z_A,z_B,z_C)=(125/244,267/125,244/267),
```

the Jacobian of `(BD-P),(BD-Z),(BD-FR-A),(BD-FR-B)` with respect to

```text
(p_A,p_B,p_C,z_A,z_B,z_C)
```

has rank `4`.

Each quartic `(BD-Q_i)` is a two-dimensional surface in `(p_i,z_i,eta_i)`, so their product has generic dimension `6`. Cutting by the four independent cross equations gives a generic dimension-`2` joint receiver, the same dimension as the normalized physical endpoint surface.

## 3. The quartic becomes the space-diagonal square after cross compatibility

Substitute the physical edge reconstruction and `(BD-FR)` into the A-orientation quartic. Exact simplification gives

```text
(p_A^2-z_A^2)*(z_A^2-p_A^(-2))
 = [ A*(B^2-C^2)/(B*C*(A^2+C^2)) ]^2 * W2.             (BD-WA)
```

Cyclically,

```text
eta_B^2
 = [ B*(C^2-A^2)/(C*A*(A^2+B^2)) ]^2 * W2,            (BD-WB)
eta_C^2
 = [ C*(A^2-B^2)/(A*B*(B^2+C^2)) ]^2 * W2.            (BD-WC)
```

On the retained open the displayed prefactors are nonzero. Therefore a rational joint receiver point forces

```text
W2 in Q^(times 2).                                      (BD-W)
```

Thus the simultaneous elliptic/quartic condition is not merely three unrelated rank jumps: once the cross-face ratios are imposed, it forces a rational space diagonal.

## 4. The three face radicands have one common squareclass

Because `z_A,z_B,z_C` are rational and `(BD-FR)` holds,

```text
[R_AB]=[R_AC]=[R_BC]=:delta in Q*/Q*^2.                 (BD-DELTA)
```

At this stage the joint receiver appears to be a common quadratic twist of the three face-square conditions, together with the exact space-square condition `(BD-W)`.

The remaining question is whether `delta` can be nontrivial on a primitive rational edge triple.

## 5. Primitive common-squareclass collapse lemma

Clear denominators and divide the common gcd, obtaining primitive positive integers

```text
gcd(A,B,C)=1,
W^2=A^2+B^2+C^2,
[R_AB]=[R_AC]=[R_BC]=delta.                             (BD-PRIM)
```

Choose the positive squarefree integer representative `d` of `delta`.

### Odd primes

If an odd prime `ell` divides `d`, then its valuation in each of `R_AB,R_AC,R_BC` is odd, hence `ell` divides all three. But

```text
2*A^2=R_AB+R_AC-R_BC,
2*B^2=R_AB+R_BC-R_AC,
2*C^2=R_AC+R_BC-R_AB.                                  (BD-ODD)
```

Therefore `ell` divides `A,B,C`, contradicting primitivity. So `d` has no odd prime divisor.

### The prime 2

Hence `d` is `1` or `2`. If `d=2`, every one of `R_AB,R_AC,R_BC` has odd 2-adic valuation, in particular every face sum is even. Thus every pair among `A,B,C` has the same parity, so primitivity forces all three edges odd. Then

```text
W^2=A^2+B^2+C^2 = 3 (mod 8),                            (BD-2)
```

impossible for a square.

Therefore

```text
d=1,
delta=1 in Q*/Q*^2.                                    (BD-COLLAPSE)
```

Every face radicand is a rational square.

This lemma uses the **common** squareclass supplied by the simultaneous receiver. It is not available from one Goal4L orientation alone.

## 6. Exact receiver equivalence

Forward direction is source-locked: every positive rational perfect cuboid produces all three cyclic Goal4L marked points and satisfies `(BD-P)`, `(BD-Z)`, `(BD-FR)`.

Conversely, a rational point of the joint receiver on the retained positive open reconstructs the edge ratios from

```text
A=1,
B=-1/p_C,
C=-p_B,                                                 (BD-REC)
```

with `(BD-P)` recovering `p_A=-B/C`. The cross equations give `(BD-FR)`, the quartic gives `(BD-W)`, and the primitive collapse lemma gives `(BD-COLLAPSE)`. Hence all three face diagonals and the space diagonal are rational.

Therefore, modulo positive scaling, cyclic relabeling/sign choices already covered by the source convention, and the explicitly excluded exceptional loci,

```text
joint three-marked Goal4L receiver Q-points
<=> positive rational perfect-cuboid endpoints.         (BD-EQUIV)
```

This is an exact endpoint-equivalence blocker, not an exclusion theorem.

The common receiver does **not** furnish a smaller rational-point problem to which `S34-W03` can presently be applied. No new local-empty intersection has been produced.

## 7. Route decision

Certified provisionally:

- all three cyclic Goal4L maps in one convention;
- four exact independent cross-face equations;
- generic joint receiver dimension `2`;
- exact quartic-to-space-square identities `(BD-WA)`–`(BD-WC)`;
- primitive common-squareclass collapse `delta=1`;
- exact endpoint equivalence `(BD-EQUIV)`.

Not certified:

- emptiness or nonemptiness of the joint receiver;
- a Selmer/Cassels obstruction;
- a local obstruction;
- E1, Stage35, or Perfect Cuboid existence/nonexistence.

The B1 route is therefore fail-closed as an endpoint-equivalent reformulation.

Next priority from Goal4BC:

```text
35EX-35_GOAL4BE_GCD_RESERVOIR_QUADRATIC_RECIPROCITY_CYCLE_PREFLIGHT
```

Question: can the exact AU reservoirs `h_a,h_b,h_c` and the primitive Pythagorean face structure produce a non-tautological quadratic-reciprocity/Jacobi-symbol cycle beyond the already-known product-one Kummer relation?

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
