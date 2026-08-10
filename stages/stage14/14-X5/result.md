# Stage14-X5 — charged-once four-sign factor cycle to a ratio biquadratic

## Status

`COMPLETE_FOUR_SIGN_DIFFERENCE_SQUARE_AND_RATIO_BIQUADRATIC_REDUCTION`

Merged Stage14-X4 preserves the X1 charged-once coefficient space.  Since X4 merged, parallel merged Stage14-s7-26 and Stage14-4cm have already proved that the formal quadratic cyclotomic branches are empty and that only four signed linear branch types survive on the current top-theta edge.

X5 therefore does **not** re-claim the `9 -> 4` reduction.  It starts from that merged boundary and reduces each of the four signed linear classes to two exact coupled difference-of-squares equations, then eliminates the absolute scales to one fixed-coefficient bidegree `(2,2)` ratio curve.

No whole-family power saving is claimed.  The current unconditional bound remains

```text
V(B) << B^(7/8+o(1)).
```

No canonical index or exponent ledger is modified.

---

## 1. Imported merged boundary

Keep the X1 -> X4 charged-once outer data, including the common-core residual triple, primitive root-line data, endpoint-small roots, orientations and reconstruction masks.

Merged s7-26 / 4cm leave four signed linear allocation classes.  Write the odd agreement branch moduli as

```text
m_- m_+ = oddpart(R*J),
n_- n_+ = oddpart(alpha*delta),                    (1.1)

gcd(m_-,m_+)=1,
gcd(n_-,n_+)=1.                                    (1.2)
```

They divide

```text
m_- | D-A,
m_+ | D+A,

n_- | V-U,
n_+ | V+U,                                     (1.3)
```

where

```text
A=alpha*r,
D=delta*s,
U=R*X,
V=J*Y,                                            (1.4)
```

with `D>A>0`, `V>U>0`.

The complementary quotients are fixed-residual factor-pair data.  Define the **full** positive integral quotients

```text
a_- := (D-A)/m_-,
a_+ := (D+A)/m_+,

b_- := (V-U)/n_-,
b_+ := (V+U)/n_+.                                (1.5)
```

For fixed charged-once residual data their odd parts have only `B^o(1)` allocations; the finite 2-primary choices are also `B^o(1)`.  X5 may therefore condition on `(a_-,a_+,b_-,b_+)` without fixed-power cost.

---

## 2. Exact reconstruction from the linear factors

Equations (1.5) give

```text
D-A=a_- m_-,
D+A=a_+ m_+,

V-U=b_- n_-,
V+U=b_+ n_+.                                     (2.1)
```

Hence

```text
2D=a_+m_+ + a_-m_-,
2A=a_+m_+ - a_-m_-,

2V=b_+n_+ + b_-n_-,
2U=b_+n_+ - b_-n_-.                              (2.2)
```

Thus the four branch moduli determine the four host variables once the quotient decoration is fixed.

---

## 3. Reciprocal coupled difference-of-squares system

Taking the difference of the squares in (2.1),

```text
(a_+m_+)^2-(a_-m_-)^2
 = (D+A)^2-(D-A)^2
 = 4AD
 = 4*r*s*(alpha*delta).                           (3.1)
```

Let

```text
epsilon_k := (alpha*delta)/oddpart(alpha*delta),  (3.2)
```

a power of two fixed by the 2-primary refinement.  Using (1.1),

```text
boxed:
(a_+m_+)^2-(a_-m_-)^2
 = 4*epsilon_k*r*s*n_-n_+.                        (3.3)
```

Likewise define

```text
epsilon_xi := (R*J)/oddpart(R*J).                 (3.4)
```

Then

```text
boxed:
(b_+n_+)^2-(b_-n_-)^2
 = 4*epsilon_xi*X*Y*m_-m_+.                       (3.5)
```

This pair is exact on every physical packet.  It retains the reciprocal generation of the moduli: the `m`-variables generate the right side of the `n`-equation and conversely.

Define

```text
c := 4*epsilon_k*r*s,
d := 4*epsilon_xi*X*Y.                              (3.6)
```

Then the receiver is

```text
a_+^2 m_+^2-a_-^2 m_-^2 = c n_-n_+,
b_+^2 n_+^2-b_-^2 n_-^2 = d m_-m_+.               (3.7)
```

This is strictly narrower than a generic binary-quartic equal-value problem.

---

## 4. Exact ratio elimination

Because all four branch moduli are positive, put

```text
x := m_+/m_-,
y := n_+/n_-                                      (4.1)
```

as positive reduced rational ratios.

Divide the first equation of (3.7) by `m_-^2` and the second by `n_-^2`:

```text
a_+^2 x^2-a_-^2 = c*(n_-^2/m_-^2)*y,             (4.2)

b_+^2 y^2-b_-^2 = d*(m_-^2/n_-^2)*x.             (4.3)
```

Multiplying cancels the unknown absolute scale ratio `m_-^2/n_-^2` exactly.  Therefore every physical packet satisfies

```text
boxed:
(a_+^2 x^2-a_-^2)
(b_+^2 y^2-b_-^2)
 = c*d*x*y.                                       (4.4)
```

Equivalently,

```text
F(x,y)
 := (a_+^2 x^2-a_-^2)(b_+^2 y^2-b_-^2)
    - kappa*x*y
 =0,                                              (4.5)

kappa := 16*epsilon_k*epsilon_xi*r*s*X*Y.         (4.6)
```

No approximation, completion or averaging is used.

---

## 5. Geometry of the new receiver

For fixed outer data and quotient decoration, `F(x,y)` has bidegree `(2,2)` on `P^1 x P^1`.

Therefore its arithmetic genus is

```text
(2-1)(2-1)=1.                                     (5.1)
```

X5 does **not** assert that every physical coefficient specialization is nonsingular.  Singular and reducible specializations must be classified separately before invoking any elliptic-curve theorem.

The exact new receiver is

```text
ChargedOnceReciprocalRatioBiquadraticIncidence.    (5.2)
```

It consists of positive rational points `(x,y)` on (4.5) satisfying:

```text
- x=m_+/m_- and y=n_+/n_- with coprime positive numerator/denominator;
- the original four signed branch choices;
- the quotient-factor provenance from fixed residuals;
- cell balance and squarefree/coprime masks;
- the 4x4 prime-allocation compatibility retained from X4;
- integrality of the absolute scales recovered from either equation in (4.2)-(4.3);
- all original interval/orientation/reconstruction masks.
```

A generic rational-point bound on the ambient `(2,2)` curve is not automatically a bound for the physical family unless these height and lift conditions are preserved.

---

## 6. Relation to the current `1/8` short-cofactor ledger

Merged s7-26 / 4cm prove on the only unsaved top-theta edge

```text
theta=5/16,
3/16<=phi<=1/4,                                   (6.1)
```

that the two dominant linear cofactors have total exponent at most `1/8`.

X5 does not multiply that support count by a separate curve saving.  Instead it uses the short cofactors as coefficient data in (4.5).  For fixed residual/2-primary decoration, only `B^o(1)` factor-pair choices of their odd parts occur.

Thus the live fixed-power freedom is now transferred to rational ratio points and their admissible absolute-scale lifts, not to an independent cofactor box.

---

## 7. Finite diagnostic and quantifier guard

The deterministic X5 audit reuses the frozen physical dual-cross family and verifies:

```text
- all four linear dominant sign classes occur;
- both coupled difference-square equations hold exactly;
- the ratio identity (4.4) holds as an exact Fraction identity;
- the branch ratios are reduced because m_-/m_+ and n_-/n_+ are coprime;
- no `i` branch is reintroduced.
```

The finite family is diagnostic only.

In particular, X5 does **not** infer from finite uniqueness that a fixed ratio curve has `B^o(1)` physical lifts asymptotically.

The remaining obligations are:

```text
1. classify singular/reducible coefficient specializations of F(x,y);
2. prove that physically allowed singular specializations are empty or subcritical, or count them directly;
3. for nonsingular fibers, translate the original branch-modulus height box into a curve height;
4. control average rational-point/lift multiplicity without reversing the charged-once quantifiers.
```

---

## 8. H / tH decision

No X5-specific H line is needed yet.

The next obstruction is now an explicit low-degree algebraic curve family.  Before any external elliptic/large-sieve theorem audit, X6 should classify the singular locus of (4.5) and determine the exact physical height map.  Only after that theorem shape is frozen would an H-line applicability audit be useful.

```text
X5_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false.
```

---

## Boundary

```text
STAGE14_X5=COMPLETE_FOUR_SIGN_DIFFERENCE_SQUARE_AND_RATIO_BIQUADRATIC_REDUCTION
MERGED_X4_IMPORTED=true
MERGED_S7_26_IMPORTED=true
MERGED_4CM_IMPORTED=true
X1_CHARGED_ONCE_QUANTIFIER_ORDER_PRESERVED=true
FOUR_SIGN_LINEAR_BRANCH_REDUCTION_IMPORTED=true
FIXED_RESIDUAL_LINEAR_QUOTIENT_DECORATION_COST=Bo1
RECIPROCAL_COUPLED_DIFFERENCE_SQUARE_SYSTEM_PROVED=true
FIRST_DIFFERENCE_SQUARE_EQUATION=(a_+m_+)^2-(a_-m_-)^2=c*n_-*n_+
SECOND_DIFFERENCE_SQUARE_EQUATION=(b_+n_+)^2-(b_-n_-)^2=d*m_-*m_+
BRANCH_RATIO_X=m_+/m_-
BRANCH_RATIO_Y=n_+/n_-
RATIO_BIQUADRATIC_EQUATION=(a_+^2*x^2-a_-^2)*(b_+^2*y^2-b_-^2)=kappa*x*y
RATIO_BIQUADRATIC_BIDEGREE=(2,2)
RATIO_BIQUADRATIC_ARITHMETIC_GENUS=1
RATIO_BIQUADRATIC_NONSINGULAR_UNIFORMLY_PROVED=false
SINGULAR_SPECIALIZATIONS_CLASSIFIED=false
PHYSICAL_RATIO_CURVE_HEIGHT_TRANSFER_PROVED=false
CHARGED_ONCE_RECIPROCAL_RATIO_BIQUADRATIC_INCIDENCE_PROVED=false
REMAINING_RECEIVER=ChargedOnceReciprocalRatioBiquadraticIncidence
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
X5_AUXILIARY_H_NEEDED=false
X_ROUTE_BLOCKED_BY_H=false
NEXT_RECOMMENDED=Stage14-X6 classify singular/reducible ratio-biquadratic fibers and derive the physical height/lift map before any external elliptic theorem audit
```