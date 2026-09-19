# MB104 — Z32: N=14 support-Hilbert gate and hyperplane no-gain identity

Status: **RESEARCH CHECKPOINT / PRE-AUDIT / NO CREDIT**

## Purpose

The revived-Z work and BTVA now give two different kinds of finite control:

```
explicit Miyaoka/Hodge windows through N<=9,
abstract BTVA finiteness through N<=13.
```

Therefore an unbounded genus-`0/1` multibranch family must have `N>=14`.

The first uncontrolled support size `N=14` is also where the retained balanced
`000707` hostile family lives.  The goal of this checkpoint is to stop treating
`N=14` as merely the next integer and instead exploit the **geometry of the
14-node support**.

The new active object is the space of reflexive symmetric differentials satisfying the
extension conditions at a fixed support.

## 1. Fixed-support extension space

Let `T` be a subset of the 48 box nodes and let `|T|=N`.  Let

```
W_m = H^0(X_pc, (Sym^m Omega^1_Xpc)^^).
```

For a node `s`, BTVA identifies a finite-dimensional local principal-part quotient
`Q_{s,m}`; its dimension is

```
dim Q_{s,m} = chi0(A1,Sym^m Omega)
            = (11/108)m^3 + O(m^2).
```

Define

```
rho_T,m : W_m -> direct_sum_{s in T} Q_{s,m},
V_m(T)  = ker(rho_T,m).
```

Geometrically, `V_m(T)` consists of reflexive differentials that become regular on
the exceptional curves above all nodes in `T`.

A curve whose singular-node support is contained in `T` is complete on the smooth
open surface obtained by deleting the exceptional curves above the complementary
nodes.  Hence, if one proves

```
dim V_m(T) = c_T m^3 + O(m^2),   c_T>0,       (Z32-HILB)
```

then BTVA Lemma 6.1 supplies a section with a fixed hyperplane zero for large `m`,
and Proposition 6.2 implies that only finitely many geometric-genus `0/1` complete
curves can occur with that fixed support.

Thus **an explicit degree cap is not logically necessary** for this support: positive
cubic growth already removes the support from the unbounded tail.

Because there are only finitely many subsets of the 48 nodes (and finitely many
Aut(S)-orbits), proving (Z32-HILB) support-orbit by support-orbit is a valid alternative
to first producing a universal `Dmax`.

This is the formal version of the user's proposed “classify the infinite family before
finite degree enumeration” strategy.

## 2. The BTVA independent-condition estimate misses N=14 by only 5/54

The fixed product presentation

```
X_pc = (X(8) x X(8))/G0,
|G0|=8,
g(X(8))=5
```

gives the exact leading coefficient

```
dim W_m = (4/3)m^3 + O(m^2).
```

If the `N` local extension conditions are charged independently, the cubic coefficient
is bounded below by

```
4/3 - N*(11/108).
```

At `N=14` this is

```
4/3 - 14*(11/108) = -5/54.
```

Therefore a support-specific dependency saving of more than

```
(5/54)m^3 + O(m^2)
```

is sufficient to make the N=14 fixed-support space big.

The target is not “find one low-order form”.  The target is the **asymptotic rank** of
`rho_T,m`.

## 3. Existing order-two balanced computation is a real dependency signal, not a proof

For the retained balanced support

```
T_bal = {0,1,2,3,8,9,10,11,24,25,26,32,33,34},
```

the exact W5 computation gives:

```
dim W_2 = 13,
nominal local rows = 14*3 = 42,
rank rho_Tbal,2 = 12,
dim V_2(T_bal)=1.
```

The unique common-regular form is

```
(z-x1-x2-i*x3)*eta.
```

Thus local extension conditions at different nodes are demonstrably not independent
at order two.

However the surviving line is exactly the known support-hyperplane architecture.
One dimension at `m=2` says nothing by itself about the cubic coefficient `c_T`.
The correct next invariant is a Hilbert/quasi-Hilbert growth law for
`ker(rho_T,m)`, not another isolated finite-order rank advertised as closure.

## 4. Existing BTVA classification already removes the hyperplane-support genus-zero sector

BTVA Theorem 1.2 proves that any genus-zero curve on the perfect-cuboid surface other
than the 32 van-Luijk plane conics passes through at least seven singularities spanning
`P^6`.

The retained exact adapter
`KNOWN-CONIC-MULTIBRANCH-EXCLUSION.md` proves that all 32 conics are smooth and hence
have `r_i=1` at every box node.  They are not in the MB101 population.

Consequently every genus-zero MB carrier satisfies

```
span(node support) = P^6.
```

Hence every N=14 support contained in a hyperplane is **already excluded from the
genus-zero multibranch population**, without any degree bound.

This is a genuine structural cut:

```
N14 genus 0 -> full-span supports only.
```

For genus one, BTVA gives a different restriction: an unbounded-degree curve cannot be
the bounded hyperplane-section alternative, so its singular support must contain nodes
spanning a hyperplane.  Both span-`P^5` and full-span `P^6` support sectors therefore
remain relevant.

The retained balanced `000707` support lies exactly on

```
z-x1-x2-i*x3=0
```

and belongs to the genus-one span-`P^5` sector.

## 5. Uniform hyperplane vanishing does not repair the N=14 cubic deficit

Because the balanced support lies on one hyperplane, the most obvious higher-order
continuation of W5 is to force proportional vanishing along that hyperplane.

Let symmetric order be `m` and let

```
q = c m + O(1),   0<=c<=1/2.
```

Consider sections twisted by `-qH`, then multiply by the defining equation of the
support hyperplane to order `q`.

### 5.1 Global supply after the twist

On the product cover `P=X(8)xX(8)`, `pi^*H=K_P` and

```
Sym^m Omega_P
 = direct_sum_{i=0}^m K_1^i tensor K_2^(m-i).
```

After twisting by `-qK_P`, only `q<=i<=m-q` contributes at leading order.
Writing `n=m-2q`, the total product dimension has leading term

```
(32/3)n^3.
```

Taking order-eight diagonal invariants divides the leading identity contribution by
eight; all nonidentity character traces are lower order.  Therefore

```
h0(X_pc,(Sym^m Omega)^^(-qH))
 = (4/3)(1-2c)^3 m^3 + O(m^2).               (SUPPLY-c)
```

### 5.2 Residual local extension cost after q-fold hyperplane vanishing

In the BTVA A1 cover coordinates, hyperplane vanishing to order `q` removes all local
terms of coordinate degree below `2q`.

Let `x=n/m` denote normalized local coordinate degree.  From BTVA Proposition 3.3,
the leading dimension of the nonextendable quotient in degree `x` is

```
m^2*x                                           for 0<=x<1/3,

m^2*(1-x)(3x+1)/4                              for 1/3<=x<1.
```

The parity condition `n congruent m mod 2` contributes the density factor `1/2`.
Thus the residual local cubic cost after `q~cm` is

```
C(c) =
  11/108 - c^2,                               0<=c<=1/6,

  c^3 - c^2/2 - c/4 + 1/8,                   1/6<=c<=1/2.
```

This interpolates correctly between

```
C(0)=11/108,
C(1/2)=0.
```

### 5.3 Fourteen-node independent residual subtraction is never positive

If the residual conditions at the 14 met nodes are still charged independently, the
available cubic lower-bound coefficient is

```
L(c)=(4/3)(1-2c)^3 - 14*C(c).
```

For `0<=c<=1/6`,

```
L(c)=-(576c^3-1620c^2+432c+5)/54 < 0.
```

Indeed on that interval
`432c-1620c^2 >=162c>=0`, so the numerator is positive.

For `1/6<=c<=1/2`, an exact factorization gives

```
L(c)=-(2c-1)^2(74c+5)/12 <=0,
```

with equality only at the endpoint `c=1/2`, where the cubic supply itself has
collapsed to zero.

Therefore:

> proportional vanishing along a single support hyperplane, followed by the same
> independent-node residual accounting, can never produce positive cubic growth at
> N=14.

Since one hyperplane already hits all 14 balanced nodes at unit projective cost, using
several positive-degree hypersurfaces merely to create the same nodewise vanishing
cannot improve this common-divisor mechanism.

This is a quantitative higher-order explanation of the retained W5 statement that the
pure support-hyperplane `1/2` architecture has no intrinsic regularity improvement.

## 6. What remains genuinely new

The support-Hilbert route survives, but only in a narrower form.

A successful N=14 proof now requires a phenomenon not explained by multiplying the
order-two hyperplane form:

1. **primitive higher-order global sections** whose 14-node extension conditions have
   genuine cross-node dependencies;
2. an exact graded-module/Hilbert-series computation proving
   `rank(rho_T,m)` has cubic coefficient strictly below the sum of the 14 local
   coefficients;
3. a support geometry theorem forcing every unbounded N=14 carrier into one of finitely
   many support orbits for which such a positive kernel coefficient is proved;
4. or a different global mechanism entirely.

BTVA Section 5 supplies an exact computational model for this question:
construct `(Sym^m M_X)^^`, represent global sections, expand at each A1 chart, and
impose the finite principal-part equations.  The new research task is to organize
those computations **graded in m** so that the asymptotic kernel coefficient can be
certified, rather than rerunning unrelated fixed values of `m`.

## 7. Proposed execution order

The most informative first test is the retained balanced support, because:

- it is the known hostile equality-shaped N=14 family;
- its exact order-two extension matrix already exists;
- its support is one Aut(S)-meaningful hyperplane packet;
- the common-hyperplane mechanism is now proved insufficient at cubic order.

Execution:

```
Z32-A:
  build/recover the graded extension module for T_bal;
  separate the submodule generated by the known h*omega7 architecture;
  compute the Hilbert growth of the primitive quotient/kernel.

Z32-B:
  if primitive cubic coefficient >0,
  BTVA Lemma 6.1 + Proposition 6.2 give abstract finiteness for the balanced support.

Z32-C:
  materialize the 48-node Aut(S) permutation table from the source-locked action and
  classify the remaining N=14 support orbits by projective span / extension-module type.

Z32-D:
  promote no statement until hostile audit; if balanced primitive cubic coefficient is
  zero, retain the exact Hilbert obstruction and move to full-span support geometry.
```

The old suggestion “just do order four” is retained only as a **module-generation
diagnostic**.  A positive finite-order rank is not itself a finiteness theorem.

## Decision

```
UNBOUNDED_SUPPORT_FRONTIER = N>=14
N14_GENUS0_HYPERPLANE_SUPPORT = EXCLUDED_BY_RETAINED_BTVA_PLUS_CONIC_ADAPTER
N14_GENUS0_REMAINDER = FULL_SPAN_P6_ONLY
N14_GENUS1_BALANCED_SUPPORT = SPAN_P5_LIVE
FIXED_SUPPORT_POSITIVE_CUBIC_GROWTH_IMPLIES_ABSTRACT_FINITENESS = YES_PRE_AUDIT_ROUTE
BALANCED_ORDER2_EXTENSION_DEPENDENCE = REAL_BUT_LOWER_ORDER_EVIDENCE_ONLY
UNIFORM_HYPERPLANE_TWIST_PLUS_INDEPENDENT_RESIDUAL_COST = CUBICALLY_NONPOSITIVE
BALANCED_NEXT_OBJECT = PRIMITIVE_SUPPORT_EXTENSION_HILBERT_GROWTH
EXPLICIT_DMAX_REQUIRED_FOR_THIS_ROUTE = NO
MB104_COMPLETE = false
R29_LG2_MB_DISCHARGED = false
RECEIVER_CREDIT = false
THEOREM_CREDIT = false
ENDPOINT_CREDIT = false
MERGE_AUTHORIZED = false
```
