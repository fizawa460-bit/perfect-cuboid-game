# Stage14-4ce addendum — merged s7-19 and the dual primitive-Pythagorean switch

Merged Stage14-s7-19 arrived while 4ce was being prepared. It is complementary, not conflicting.

The original 4ce result proves that every endpoint off-diagonal same-`(xi,k)` pair has

```text
Xi_switch >= B^(1/4-o(1)),
K_switch  >= B^(3/8-o(1)),
```

and retains the exact primewise residue graph.

Merged s7-19 applies hyperbolic composition to the `k=k_-k_+` split and produces a primitive Pythagorean triple in which

```text
K_switch | hypotenuse,
xi_0     | a transverse leg,
xi_0 >= B^(1/4-o(1))
```

at the 4cd endpoint.

This addendum applies the same composition to the `xi=a*b` split and obtains the exact dual theorem.

## 1. xi-split composition

For two same-`(xi,k)` states write

```text
P_i=a_i*x_i^2,
Q_i=b_i*y_i^2,
Q_i^2-P_i^2=k*h_i^2.
```

Use the 4ce four-cell split

```text
a_1=A*B,
b_1=C*D,
a_2=A*C,
b_2=B*D,
Xi_agree=A*D,
Xi_switch=B*C.
```

Define

```text
H_xi = Q_1*Q_2 + P_1*P_2,
L_xi = Q_1*P_2 + P_1*Q_2,
W_xi = k*h_1*h_2.
```

The identity

```text
(Q_1^2-P_1^2)(Q_2^2-P_2^2)
 =(Q_1Q_2+P_1P_2)^2-(Q_1P_2+P_1Q_2)^2
```

gives

```text
H_xi^2=L_xi^2+W_xi^2.
```

Expanding through the four cells gives

```text
H_xi
 = B*C*(D^2*y_1^2*y_2^2 + A^2*x_1^2*x_2^2),

L_xi
 = A*D*(C^2*y_1^2*x_2^2 + B^2*x_1^2*y_2^2).
```

Hence

```text
Xi_switch | H_xi,
Xi_agree  | L_xi.
```

## 2. Primitive reduction

Let

```text
d_xi=gcd(H_xi,L_xi,W_xi),
H_xi,0=H_xi/d_xi,
L_xi,0=L_xi/d_xi,
W_xi,0=W_xi/d_xi.
```

Since every prime of `xi` divides `P_i Q_i` while

```text
gcd(P_i Q_i,Q_i^2-P_i^2)=1,
```

we have

```text
gcd(xi,W_xi)=1.
```

Therefore

```text
gcd(d_xi,xi)=1,
```

so the full xi divisibility survives primitive reduction:

```text
boxed:
Xi_switch | H_xi,0,
Xi_agree  | L_xi,0.
```

The primitive triple

```text
H_xi,0^2=L_xi,0^2+W_xi,0^2
```

is pairwise coprime.

Define the surviving squarefree k-part

```text
k_0 = k/gcd(k,d_xi).
```

Then

```text
boxed:
k_0 | W_xi,0.
```

## 3. A large part of k survives on the transverse leg

Because

```text
xi=Xi_switch*Xi_agree | H_xi,0*L_xi,0
```

and `0<L_xi,0<H_xi,0`,

```text
xi < H_xi,0^2=(H_xi/d_xi)^2.
```

Also `P_i,Q_i<=X` gives

```text
H_xi=Q_1Q_2+P_1P_2 <= 2X^2.
```

Hence

```text
boxed:
d_xi <= 2X^2/sqrt(xi).
```

Therefore

```text
boxed:
k_0
 >= k/d_xi
 >= k*sqrt(xi)/(2X^2).
```

At the 4cd endpoint

```text
xi=B^(3/4+o(1)),
k=B^(1-o(1)),
X=B^(1/2+o(1)),
```

so

```text
boxed:
k_0 >= B^(3/8-o(1)).
```

## 4. Dual primitive-Pythagorean hard core

The merged s7-19 triple and the new dual triple give simultaneously:

```text
k-split triple:
  K_switch >= B^(3/8-o(1)) divides the primitive hypotenuse,
  xi_0     >= B^(1/4-o(1)) divides a primitive leg;

xi-split triple:
  Xi_switch >= B^(1/4-o(1)) divides the primitive hypotenuse,
  k_0       >= B^(3/8-o(1)) divides a primitive leg.
```

Thus the endpoint collision is constrained by two transverse primitive Pythagorean incidences with exchanged squarefree scales.

As an independent check, every odd divisor of a primitive Pythagorean hypotenuse is `1 mod 4`; this re-proves the 4ce statement that every odd prime of `K_switch` and `Xi_switch` is `1 mod 4`. The stronger 4cd primewise residue conditions are still retained.

## 5. Canonical receiver after s7-19

The canonical post-4ce receiver is the intersection

```text
DualPrimitivePythagoreanSwitchIncidence
+
PrimewiseResidueLock.
```

Required data:

```text
same xi,
same k,
Xi_switch >= B^(1/4-o(1)),
K_switch  >= B^(3/8-o(1)),
primitive k-split Pythagorean triple,
primitive xi-split Pythagorean triple,
large transverse xi_0 and k_0 leg divisors,
primewise Legendre signatures,
physical interval/reconstruction selectors.
```

No power saving is claimed merely from the existence of the two triples. A future theorem must count this *simultaneous* dual incidence; counting each triple separately and multiplying densities is not justified.

```text
MERGED_S7_19_IMPORTED=true
DUAL_PRIMITIVE_PYTHAGOREAN_COMPOSITION_PROVED=true
XI_SWITCH_DIVIDES_DUAL_PRIMITIVE_HYPOTENUSE=true
DUAL_TRANSVERSE_K0_LOWER_EXPONENT=3/8
CANONICAL_POST_4CE_RECEIVER=DualPrimitivePythagoreanSwitchIncidence+PrimewiseResidueLock
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=false
NEXT=Stage14-4cf
```
