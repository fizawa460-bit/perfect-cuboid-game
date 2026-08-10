# Stage14-t39 — critical-strip Friedlander–Iwaniec transfer audit

## Purpose

Stage14-t38 reduced the unresolved super-square-root contribution to the critical strip

\[
\ell=B^{1/2+o(1)},
\]

where the moving canonical Gaussian prime and the descended Gaussian packet have comparable polynomial size.  The natural candidate is the Friedlander–Iwaniec Gaussian Dirichlet-symbol bilinear estimate.

Stage14-t39 tests that transfer exactly.

The conclusion is deliberately two-sided:

1. the Friedlander–Iwaniec bilinear theorem is quantitatively strong enough in a balanced range **if** the Stage14 detector can be converted to a genuine Gaussian Dirichlet symbol;
2. the direct conversion fails for an exact structural reason.  If the modulus is taken from the Stage14 Gaussian coefficient so that the FI symbol is available, the Stage14 coordinate-product character becomes constant (or zero on bad gcd states).  If an external auxiliary split prime is kept so that the Stage14 square detector remains nontrivial, the trace is not multiplicative in the moving Gaussian variable and the auxiliary prime remains an independent third variable.

Thus t39 does not prove the critical-strip power saving.  It proves the precise obstruction to the naive two-variable FI transfer and defines the correct next trilinear object.

No `A_{1,1}` or `T=o(sqrt(B))` conclusion is claimed.

## 1. The exact FI bilinear theorem available over Z[i]

For a primary primitive Gaussian integer `w`, Friedlander–Iwaniec define

\[
\boxed{
\xi_w(z)=\left(\frac{z}{w}\right)
=\left(\frac{\Re(wz)}{N(w)}\right),
}
\tag{39.1}
\]

where the symbol on the right is the rational Jacobi symbol.

For primary primitive `w,z`, they prove reciprocity

\[
\boxed{
\left(\frac zw\right)=\left(\frac wz\right).
}
\tag{39.2}
\]

Their Section 21 studies

\[
Q(M,N)
=\sum_w^*\sum_z \alpha_w\beta_z
\left(\frac zw\right)
\]

with bounded coefficients and obtains Proposition 21.3

\[
\boxed{
Q(M,N)
\ll
(M+N)^{1/12}(MN)^{11/12+\varepsilon}.
}
\tag{39.3}
\]

In the balanced formal scale `M=N=X`, this is

\[
Q(X,X)\ll X^{23/12+\varepsilon},
\]

versus the trivial `X^2`: a power gain `X^{-1/12+\varepsilon}`.

So lack of analytic strength is **not** the obstruction.  The problem is getting the Stage14 detector into the form (39.1).

## 2. Natural-modulus self-factor lemma

Recall

\[
\Psi_w(z)=\Re(wz)\Im(wz),
\qquad
\Phi_w(z)=\Re(wz^2)\Im(wz^2).
\]

Let `w` be primary primitive with odd

\[
q=N(w).
\]

Because

\[
\Re(-iwz)=\Im(wz),
\]

we have directly from (39.1)

\[
\begin{aligned}
\chi_q(\Psi_w(z))
&=\xi_w(z)\xi_w(-iz)\\
&=\xi_w(-i)\xi_w(z)^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\chi_q(\Psi_w(z))
=
\begin{cases}
\xi_w(-i),&(w,\bar z)=1,\\
0,&(w,\bar z)\ne1.
\end{cases}
}
\tag{39.4}
\]

The same calculation with `z^2` gives

\[
\boxed{
\chi_q(\Phi_w(z))
=
\begin{cases}
\xi_w(-i),&(w,\bar z)=1,\\
0,&(w,\bar z)\ne1.
\end{cases}
}
\tag{39.5}
\]

Thus if one chooses the modulus from the Gaussian coefficient `w` in order to create the FI denominator, the moving `z` dependence disappears completely on the good states.

The sign is the harmless unit value

\[
\xi_w(-i)=
\begin{cases}
1,&q\equiv1\pmod8,\\
-1,&q\equiv5\pmod8.
\end{cases}
\]

This is the first obstruction.

## 3. Rational norm factors do not rescue the detector

For a rational nonzero scalar `r`,

\[
\Psi_{rw}(z)=r^2\Psi_w(z),
\qquad
\Phi_{rw}(z)=r^2\Phi_w(z).
\tag{39.6}
\]

Hence rational norm factors appearing in the t37 common-core decomposition are invisible in squareclass.

After removing those rational factors, the natural primitive Gaussian core is exactly the coefficient to which (39.4)–(39.5) applies.  Therefore the t37 square-orientation structure does not create a hidden nontrivial FI self-symbol; it makes the natural self-symbol even more degenerate.

## 4. Application to the t38 visible packet

For example, the visible same-orientation packet is

\[
F=-\ell^2 C\,\Phi_c(\pi),
\tag{39.7}
\]

with fixed descended Gaussian coefficient `c=UV` after unit normalization.

Suppose the rational content of `c` is removed and its primitive Gaussian core is denoted `w`.  Up to a rational square, the moving factor has the shape `Phi_w(pi)` after the square-orientation factors are allocated.

Trying to use `N(w)` as the FI modulus gives, by (39.5),

\[
\chi_{N(w)}(\Phi_w(\pi))=\xi_w(-i)
\]

on every good state.  The prime variable `pi` has vanished.

So the natural internal modulus produces **resonance, not cancellation**.

The same phenomenon occurs for every self-coordinate factor `Psi_w(pi)` in the invisible branch by (39.4).

## 5. External auxiliary prime keeps the detector nontrivial

The Stage14 square sieve instead uses a good split auxiliary rational prime `lambda`, independent of the canonical prime and descended coefficient norms.

For instance a visible local trace is

\[
A_{\lambda,c}(z)
=\chi_\lambda(\Phi_c(z)).
\tag{39.8}
\]

This is genuinely nonconstant.  But it is not a multiplicative character of the Gaussian variable `z`.

The frozen finite audit gives explicit nonzero counterexamples already for the valid local model `c=1`:

```text
lambda=13: z1=1+5i, z2=1+5i
A(z1)=-1, A(z2)=-1, A(z1*z2)=-1

lambda=17: z1=1+2i, z2=1+4i
A(z1)=-1, A(z2)=+1, A(z1*z2)=+1

lambda=29: z1=1+2i, z2=1+6i
A(z1)=-1, A(z2)=-1, A(z1*z2)=-1

lambda=37: z1=1+2i, z2=1+2i
A(z1)=+1, A(z2)=+1, A(z1*z2)=-1

lambda=41: z1=1+2i, z2=1+4i
A(z1)=-1, A(z2)=-1, A(z1*z2)=-1
```

Thus

\[
\boxed{
A_{\lambda,c}(z_1z_2)
\ne
A_{\lambda,c}(z_1)A_{\lambda,c}(z_2)
}
\tag{39.9}
\]

in general.

The analogous external trace

\[
\chi_\lambda(\Psi_c(z))
\]

is also nonmultiplicative in `z`; the audit freezes a counterexample for every tested split prime `13,17,29,37,41`.

A genuine FI numerator character `z -> (z/w)` is completely multiplicative.  Hence neither external trace is a single FI Dirichlet symbol in the moving variable.

This is the second obstruction.

## 6. The root-of-minus-one rotation mismatch

There is another way to see the same issue.

If an auxiliary split prime is represented by a primary Gaussian prime

\[
\varpi=u+iv,
\qquad N(\varpi)=\lambda,
\]

then FI evaluates

\[
\left(\frac z\varpi\right)
=\chi_\lambda(ux-vy),
\qquad z=x+iy.
\tag{39.10}
\]

The Stage14 auxiliary trace, however, contains fixed coordinate linear forms such as `x`, `y`, or fixed packet-dependent forms `ax+by` whose coefficients do not depend on the auxiliary representation `u+iv`.

For a split odd prime both `u` and `v` are nonzero modulo `lambda`, so the FI form `ux-vy` is not proportional to either coordinate form.  Converting a Stage14 coordinate factor to (39.10) requires a rotation depending on `varpi`.  That makes the would-be numerator coefficient depend on the denominator variable and destroys the separated bilinear form

\[
\alpha_w\beta_z\left(\frac zw\right).
\]

The finite audit checks this mismatch on the primary Gaussian primes above `5,13,17,29,37,41`.

## 7. Exact two-variable dilemma

The direct FI transfer therefore has an exact dichotomy:

### Internal/natural modulus

Choose the denominator from the Stage14 Gaussian packet so that FI reciprocity and Proposition 21.3 apply.

Then the relevant self-coordinate character satisfies (39.4) or (39.5), and the moving prime dependence collapses to a constant/zero.

### External square-sieve modulus

Keep an independent auxiliary split prime so that the quartic Stage14 trace is nontrivial.

Then the trace is nonmultiplicative in the moving Gaussian variable and the auxiliary prime remains an independent third variable.

Symbolically the surviving analytic object has the form

\[
\boxed{
\mathcal T
=
\sum_{\varpi\in\mathcal L}
\sum_{\pi\in\mathcal P}
\sum_{\gamma\in\mathcal C}
 a_\varpi b_\pi c_\gamma
 \chi_{N\varpi}\!\bigl(P_\gamma(\pi)\bigr),
}
\tag{39.11}
\]

where `gamma` denotes the descended packet and `P_gamma` is the t38 quartic/coordinate-product polynomial.

This is a **three-variable external-modulus Kummer/Dirichlet hybrid**, not the two-variable FI form `Q(M,N)`.

## 8. Why the FI theorem is still relevant

The failure above does not make FI technology irrelevant.

Friedlander–Iwaniec Section 21 proves that once a genuine Gaussian Dirichlet symbol is exposed, arbitrary bounded coefficients can be handled with a balanced power saving.  Their Jacobi–Kubota multiplier similarly shows how a nonmultiplicative spin can produce a Dirichlet-symbol coupling after a suitable product decomposition.

The lesson for Stage14 is therefore precise:

> one more differencing / dispersion step must eliminate the external auxiliary variable or convert the surviving cross-correlation into a genuine `(z/w)` symbol.  Applying Proposition 21.3 before that step cannot work.

Modern quadratic Hecke mean-value results over `Q(i)` likewise require a genuine quadratic residue-symbol family; they do not bypass the transfer obstruction in (39.8)–(39.11).

## 9. Frozen audit

The standard-library audit verifies:

```text
primary Gaussian prime moduli                 6
Psi natural-modulus identities             1008
Phi natural-modulus identities             1008
unit-sign checks                               6
external Phi nonmultiplicativity witnesses    5
external Psi nonmultiplicativity witnesses    5
FI coordinate-rotation mismatch checks         6
```

The external witnesses use split primes `13,17,29,37,41`.  All values are nonzero, so the failure is not caused by a bad-prime zero.

The audit also locks the formal balanced FI exponent:

```text
trivial bilinear exponent in X        2
FI Proposition 21.3 exponent         23/12
formal saving                         1/12
```

This exponent bookkeeping is diagnostic only; t39 does not claim that the Stage14 trilinear form has already been reduced to FI Proposition 21.3.

## Locked boundary

```text
STAGE14_T39=COMPLETE_FI_TRANSFER_AUDIT_AND_EXTERNAL_AUXILIARY_TRILINEAR_BOUNDARY
FI_DIRICHLET_SYMBOL_DEFINITION_MATCHED=true
FI_PROPOSITION_21_3_BALANCED_POWER_SAVING_AVAILABLE=true
NATURAL_MODULUS_PSI_TRACE=CONSTANT_OR_ZERO
NATURAL_MODULUS_PHI_TRACE=CONSTANT_OR_ZERO
EXTERNAL_AUXILIARY_PSI_TRACE_MULTIPLICATIVE=false
EXTERNAL_AUXILIARY_PHI_TRACE_MULTIPLICATIVE=false
AUXILIARY_ROOT_ROTATION_PRESERVES_SEPARATED_COEFFICIENTS=false
DIRECT_TWO_VARIABLE_FI_TRANSFER_VALID=false
EXTERNAL_AUXILIARY_THIRD_VARIABLE_ESSENTIAL=true
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t40 build an external-auxiliary trilinear dispersion inequality for T=sum_varpi,sum_pi,sum_gamma chi_{N(varpi)}(P_gamma(pi)); after one Cauchy/differencing step, test whether the surviving cross-kernel becomes a genuine Gaussian Dirichlet symbol to which FI Proposition 21.3 or a quadratic-Hecke large sieve applies
```
