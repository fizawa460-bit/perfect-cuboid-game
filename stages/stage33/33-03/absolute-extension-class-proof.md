# Stage33-03 absolute hypercohomology extension class

This note resolves the hostile-audit residual

```text
R33-BR0B-ABSOLUTE-HYPERCOHOMOLOGY-EXTENSION-CLASS
L33-03-COMPUTE-ABSOLUTE-H2-UPIC-EXTENSION-CLASS-AND-PRIMARY-ORDERS
```

without asserting that the filtration splits.

## 1. Audited input

Write

```text
U = U_D = Z^14
T = Pic(Ubar)_tors = (Z/2)^2
F = Pic(Ubar)_free = Z^6
X_Q = Hom_cont(G_Q,Q/Z)
A = X_Q^14 / <KAPPA_1,KAPPA_2>.
```

The absolute actions on `U` and `T` are trivial.  The hostile audit accepted

```text
H^3(G_Q,U)=0,
H^1(G_Q,Pic(Ubar)) = Hom_cont(G_Q,T) direct-sum (Z/2)^5,
0 -> A -> H^2(G_Q,UPic(Ubar)) -> H^1(G_Q,Pic(Ubar)) -> 0.
```

It also accepted the exact rank-two `d2_01` image `KAPPA_1,KAPPA_2`.

## 2. Recover the torsion Postnikov classes

For one trivial `Z/2` summand of `T` and the Z-free trivial lattice `U`, the
change-of-rings spectral sequence has only the `Ext_Z^1(Z/2,U)=U/2U` row in
total degree two.  Hence

```text
Ext^2_{Z[G_Q]}(Z/2,U) = H^1(G_Q,U/2U).
```

Moreover `H^1(G_Q,U)=Hom_cont(G_Q,Z^14)=0`, so the integral Bockstein

```text
H^1(G_Q,U/2U) -> H^2(G_Q,U)[2]
```

is injective.  Therefore the two exact `KAPPA` images determine the torsion
Postnikov classes uniquely.

The materialized `d2-01-image.json` shows that both are supported only on the
complex-conjugation character `chi_-1`:

```text
lambda_1 = v_1 * chi_-1,
lambda_2 = v_2 * chi_-1,
```

where `v_1,v_2 in (F2)^14` are the two exact independent unit-coordinate
vectors written in `absolute-h2-extension-class.json`.

## 3. Hidden extension / doubling map

For `alpha=(alpha_1,alpha_2) in H^1(G_Q,T)`, the hidden extension class is the
Yoneda product with the Postnikov class.  Its doubling obstruction is

```text
delta(alpha)
 = [alpha_1 cup lambda_1 + alpha_2 cup lambda_2]
 in H^2(G_Q,U/2U) / <red(KAPPA_1),red(KAPPA_2)>.
```

Because `H^3(G_Q,U)=0`, multiplication by two gives

```text
H^2(G_Q,U/2U) = H^2(G_Q,U)/2H^2(G_Q,U),
```

so the target is exactly `A/2A`.

For a quadratic character `alpha`, the connecting map for

```text
0 -> Z/2 -> Z/4 -> Z/2 -> 0
```

is the Bockstein `alpha -> alpha cup alpha`.  Serre, *Topics in Galois
Theory*, Chapter 1, sec. 1.2, Theorem 1.2.4 and the following cohomological
proof (printed pp. 4-5) identifies this cup square with the quaternion class
`(alpha,alpha)=(-1,alpha)`.  Thus

```text
alpha cup chi_-1 = alpha cup alpha,
```

and, using the accepted Milne vanishing, this is precisely the class of
`alpha` in `X_Q/2X_Q`.

Therefore the absolute extension is represented exactly by

```text
delta(alpha_1,alpha_2)
 = [v_1*alpha_1 + v_2*alpha_2] in A/2A.
```

This determines the extension class even though the filtration is not split.

## 4. Primary orders

The representative `v_1*alpha_1+v_2*alpha_2` is 2-torsion in `A`.
Consequently a right-filtration class has minimal lift order

```text
2  if delta(alpha_1,alpha_2)=0,
4  if delta(alpha_1,alpha_2) is nonzero.
```

No right-filtration class requires minimal order above four.  Because
`v_1,v_2` are independent, `delta=0` is equivalent to the two independent
conditions

```text
[alpha_j] in span_F2([chi_-1]) inside X_Q/2X_Q,  j=1,2.
```

For `alpha_j=chi_d`, Serre's cyclic-quartic criterion gives the equivalent
adapter

```text
(d,-1) is 0 or (-1,-1) in Br(Q)[2],
```

or equivalently one of `d` and `-d` is a norm from `Q(i)`.

## 5. The five finite free classes

The exact normalized V4 bar calculation in
`compute_absolute_h2_extension_class.py` gives

```text
beta_Z(chi_-1 cup chi_-1) = 0,
beta_Z(chi_2  cup chi_-1) != 0.
```

Thus each torsion generator contributes rank one to finite `d2_11`.
Independence of `v_1,v_2` gives rank two already, equal to the audited total
finite `rank(d2_11)=2`.  Hence the restriction of finite `d2_11` to the five
`H^1(V4,F)` classes is zero.  Their lifts occur in the exact finite group

```text
H^2(V4,UPic) = (Z/2)^33,
```

so all five inflate to absolute lifts of order two.

## 6. Closure state

The exact extension class, not a split assertion, is now the closure datum:

```text
FILTRATION_EXTENSION_SPLIT_CLAIMED=false
FILTRATION_EXTENSION_CLASS_EXACT=true
KERNELS_COKERNELS_TORSION_EXACT=true
OPEN_ALGEBRAIC_Q_DEFINED_CLASS_INVENTORY_COMPLETE=true
BR0B_ALL_PRIMARY_CLASSES_ACCOUNTED=true
BR0B=DISCHARGED
UNRESOLVED_UNKNOWN_IN_SCOPE=0
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
```

A new hostile audit is still required before Stage33-03 can close or release
33-06.
