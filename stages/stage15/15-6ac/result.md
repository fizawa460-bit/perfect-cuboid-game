# Stage15-6ac — high-core spacing and low-core Gaussian-square receiver

Base: merged Stage15-6ab (`PR #834`, merge commit `6dad73d`). Stage15-6ab legally charged the moving odd core `q=k_S k_O` on each physical outer-pair fiber and made the mixed CRT root-line estimate available without changing the Stage15 `R<=B` measure. Its only remaining obstruction was that the estimate

\[
1+\frac{R_0S_0}{q}
\]

is strong only when the charged modulus is large compared with the actual inner support.

Stage15-6ac makes that dichotomy exact. It proves a square-root collapse on the high-core part of every dyadic physical fiber and replaces the low-core part by an exact coupled Gaussian-square receiver. It does **not** yet count that low-core receiver globally and therefore does not claim a new Stage15 thinning exponent.

## 1. Frozen verdict

Fix a physical outer pair `(m,n)`, an actual charged channel core `(k_S,k_O)`, one CRT orientation, and one dyadic inner box

\[
R_0\le r<2R_0,\qquad S_0\le s<2S_0,
\]

inside the exact physical fiber. Put

\[
q=k_Sk_O,\qquad V=R_0S_0.
\]

Split the box by

\[
\boxed{\text{HIGH CORE}:q^2\ge V,}
\qquad
\boxed{\text{LOW CORE}:q^2<V.}
\]

Then:

1. on the high-core branch, the legalized AR-009 root-line estimate gives
   \[
   \#\{(r,s)\}\ll 1+\sqrt V;
   \]
   hence the two-dimensional inner support `O(V)` collapses to square-root support on every charged high-core fiber;
2. on the low-core branch, after charging two cross-gcd decorations of divisor-many multiplicity, both norm conditions become exact Gaussian-core times Gaussian-square identities.

The low-core exact receiver is

\[
\boxed{
\alpha_0=\varepsilon_\alpha\Pi_\alpha z^2,
\qquad
\beta_0=\varepsilon_\beta\Pi_\beta w^2,
}
\]

where

\[
\alpha_0=\frac{mr+i\,ns}{h_\alpha},
\qquad
\beta_0=\frac{ms+i\,nr}{h_\beta},
\]

are primitive Gaussian integers,

\[
h_\alpha=\gcd(mr,ns),\qquad h_\beta=\gcd(ms,nr),
\]

and `N(Pi_alpha)=N(Pi_beta)=k=2^eta q` with the Stage15-6aa same/opposite prime orientations.

```text
STAGE15_6_SUBSTAGE=6ac
STAGE15_6AC_HIGH_LOW_SPLIT=q^2_vs_R0*S0
STAGE15_6AC_HIGH_CORE_FIBERWISE_SQRT_COLLAPSE=true
STAGE15_6AC_LOW_CORE_CROSS_GCD_CHARGE=true
STAGE15_6AC_LOW_CORE_GAUSSIAN_SQUARE_RECEIVER=true
STAGE15_6AC_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AC_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AC_EXIT=HIGH_CORE_SQRT_COLLAPSE_LOW_CORE_SQUARE_RECEIVER_READY
```

## 2. High-core branch

Stage15-6ab proved that after fixing `(m,n)`, `(k_S,k_O)` and one root orientation, the inner primitive pair lies on one line

\[
r\equiv \rho s\pmod q,
\]

with

\[
\rho^2\equiv1\pmod{k_S},
\qquad
\rho^2\equiv-1\pmod{k_O}.
\]

On a dyadic box of area scale `V=R_0S_0`, AR-009 gives

\[
\#\{(r,s)\text{ on the line}\}
\ll 1+\frac{V}{q}.
\]

If `q^2>=V`, then `V/q<=sqrt(V)`, so

\[
\boxed{
\#\{(r,s)\text{ on a charged high-core line}\}
\ll 1+\sqrt V.
}
\]

The core labels, root orientations, 2-primary flag and dyadic boxes cost only `B^o(1)` after the outer pair has been fixed, by Stage15-6ab and AR-016. Thus the high-core part of each physical outer fiber has a genuine square-root collapse relative to the crude `O(V)` rectangle support.

This is a **fiberwise causal statement**. It does not say that the complete Stage15 survivor count is `B^(1/2+o(1))`, because the relation between the collection of outer fibers and the global height measure is not replaced by a raw toric box count.

## 3. Why the low-core branch cannot be discarded

If `q^2<V`, the root-line estimate alone gives no uniform square-root collapse. In particular `q=1` occurs on genuine primitive exactly-two survivors. Two concrete low-core witnesses are

```text
(m,n,r,s)=(5,3,7,4),   k=1, q=1
(m,n,r,s)=(31,7,31,23), k=2, q=1
```

so the odd-core-free branch is not empty and cannot be removed by a local congruence argument.

The correct next operation is therefore not to demand more spacing from `q`, but to use the **square part** of the exact Stage15-4 norm equations.

## 4. Cross-gcd decomposition is divisor-many outer data

Define

\[
h_\alpha=\gcd(mr,ns),
\qquad
h_\beta=\gcd(ms,nr).
\]

Because `(m,n)=1` and `(r,s)=1`, primewise valuation separation gives the exact identities

\[
\boxed{
h_\alpha=\gcd(m,s)\gcd(n,r),
}
\]

and

\[
\boxed{
h_\beta=\gcd(m,r)\gcd(n,s).
}
\]

The two factors in each product are coprime. In particular every factor on the right divides one of the already fixed outer integers `m` or `n`.

Hence after `(m,n)` is fixed, the possible quadruple

\[
(\gcd(m,s),\gcd(n,r),\gcd(m,r),\gcd(n,s))
\]

has at most

\[
\tau(m)^2\tau(n)^2=B^{o(1)}
\]

possibilities. By AR-016 these cross-gcd decorations can be charged before the low-core receiver is counted without changing the outer physical measure.

This is not AR-014: no nonprimitive root-pair square-divisor loss is being repaired. It is an ordinary divisor/finite-decoration charge from fixed outer data.

## 5. Primitive Gaussian reduction preserves the squarefree core

Set

\[
\alpha=mr+i\,ns,
\qquad
\beta=ms+i\,nr,
\]

and divide by the charged rational gcds:

\[
\alpha_0=\alpha/h_\alpha,
\qquad
\beta_0=\beta/h_\beta.
\]

By construction the real and imaginary parts of each of `alpha_0,beta_0` are coprime, so both are primitive Gaussian integers.

Stage15-4 gives

\[
N(\alpha)=kP^2,
\qquad
N(\beta)=kQ^2,
\]

with squarefree

\[
k=2^\eta q,\qquad \eta\in\{0,1\}.
\]

Division by the rational squares `h_alpha^2,h_beta^2` does not change prime-valuation parity. Therefore

\[
\boxed{
\operatorname{sf}(N\alpha_0)
=
\operatorname{sf}(N\beta_0)
=k.
}
\]

Equivalently there are positive integers `T_alpha,T_beta` with

\[
N(\alpha_0)=kT_\alpha^2,
\qquad
N(\beta_0)=kT_\beta^2.
\]

## 6. Exact Gaussian-square lift

Use unique factorization in `Z[i]`. Since `alpha_0` is primitive, no odd rational prime can divide both `alpha_0` and its conjugate. Thus:

- each odd split prime `p|q` occurs in exactly one Gaussian orientation in `alpha_0`, with odd exponent;
- after one copy of that oriented Gaussian prime is removed, the remaining exponent is even;
- every split prime not in `q` occurs with even exponent;
- the only ramified issue is `1+i`, encoded by the fixed flag `eta`;
- inert primes cannot occur to odd norm valuation.

Let `Pi_alpha` be the product of one selected Gaussian prime over each `p|q`, together with `(1+i)^eta`, and absorb units into `epsilon_alpha`. Then

\[
N(\Pi_\alpha)=k
\]

and every Gaussian prime exponent in `alpha_0/Pi_alpha` is even. Therefore

\[
\boxed{
\alpha_0=\varepsilon_\alpha\Pi_\alpha z^2
}
\]

for some `z in Z[i]`.

The same argument gives

\[
\boxed{
\beta_0=\varepsilon_\beta\Pi_\beta w^2.
}
\]

Stage15-6aa already determined the relation between the two Gaussian cores: on S-channel primes `Pi_beta` uses the same orientation as `Pi_alpha`, while on O-channel primes it uses the conjugate orientation. Therefore, after the Stage15-6ab core/orientation charge, `Pi_alpha` and `Pi_beta` are fixed decorations of the same charged core rather than new independent moduli.

This is the exact low-core receiver.

## 7. Expanded coupled receiver

Write

\[
\Pi_\alpha=A_0+iB_0,
\qquad z=a+ib.
\]

Then, after absorbing the finite unit choice into signs / coordinate swaps,

\[
\frac{mr}{h_\alpha}
=A_0(a^2-b^2)-2B_0ab,
\]

\[
\frac{ns}{h_\alpha}
=B_0(a^2-b^2)+2A_0ab.
\]

Similarly, for `Pi_beta=C_0+iD_0` and `w=c+id`,

\[
\frac{ms}{h_\beta}
=C_0(c^2-d^2)-2D_0cd,
\]

\[
\frac{nr}{h_\beta}
=D_0(c^2-d^2)+2C_0cd.
\]

The same physical `r,s` occur in both lifts, so the four displayed equations are coupled. This is strictly stronger than the low-modulus root-line condition.

Stage15-6ac does not count this receiver yet. In particular, it does not freeze one of its moving quadratic coefficients and declare a genus-one theorem. AR-010 remains a reconstruction firewall for the next substage.

## 8. Arsenal accounting

### AR-009 — high-core mechanism completed

Status:

```text
AR-009=HIGH_CORE_FIBERWISE_SQRT_COLLAPSE_PROVED
```

The modulus is charged legally by 6ab and the adaptive condition `q^2>=R0*S0` makes its spacing quantitatively effective.

### AR-017 — low-core square quotient sharpened

Status:

```text
AR-017=EXACT_GAUSSIAN_SQUARE_QUOTIENT_RECEIVER_PROVED
```

After the cross-gcd and common-core charges, the quotient is not merely an arbitrary Gaussian integer: it is a Gaussian square up to a unit. No additional modulus is charged.

### AR-018 — orientation data consumed once

The S/O orientation dictionary determines `Pi_beta` from the same charged primewise data. It supplies bookkeeping for the square lift, not an independent saving.

### AR-016 — direct reuse

The cross-gcd decorations are divisors of the fixed outer `m,n` and therefore have `B^o(1)` multiplicity.

### AR-023 / AR-024 / AR-028 — firewall pass

The high/low split occurs inside each exact physical outer fiber. Neither `q` nor the Gaussian square parameters replace the physical outer measure, and core/orientation data are charged only once.

### AR-010 — next-stage reconstruction firewall

The coupled square-lift equations now make AR-010 relevant as a **watch** item: before opening a genus-one or character route, determine which products/ratios are reconstructed by the original four equations.

### AR-012 / AR-013 — still not triggered

The receiver has coupled binary quadratic equations, but not yet two fixed reciprocal difference-of-squares right-hand sides in the AR-012 sense. No CRT lift variable has appeared after exact reconstruction.

### AR-014 — not needed

No new nonprimitive common-gcd multiplicity remains after the cross-gcd charge.

## 9. What Stage15-6ac proves causally

The Stage15-4 squareclass condition has now separated into two exact mechanisms.

```text
charged core q
   |
   +-- q^2 >= R0*S0
   |      -> one CRT root line modulo q
   |      -> AR-009
   |      -> O(1+sqrt(R0*S0)) inner support
   |
   +-- q^2 < R0*S0
          -> charge cross gcds h_alpha,h_beta
          -> primitive Gaussian norms of squareclass k
          -> alpha0 = unit * Pi_alpha * z^2
          -> beta0  = unit * Pi_beta  * w^2
          -> coupled Gaussian-square receiver
```

Thus the failure of spacing at small `q` is no longer an unstructured residual branch. It has an exact algebraic receiver that exposes the square condition directly.

What is still missing is a uniform count of that low-core receiver in the original physical measure.

## 10. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ac
STAGE15_6AC_STARTING_GATE=CORE_SIZE_VS_PHYSICAL_INNER_SUPPORT
STAGE15_6AC_HIGH_LOW_SPLIT=q^2_vs_R0*S0
STAGE15_6AC_HIGH_CORE_ROOT_SPACING_EFFECTIVE=true
STAGE15_6AC_HIGH_CORE_FIBERWISE_SQRT_COLLAPSE=true
STAGE15_6AC_LOW_CORE_NONEMPTY=true
STAGE15_6AC_CROSS_GCD_IDENTITIES_PROVED=true
STAGE15_6AC_LOW_CORE_CROSS_GCD_CHARGE=B^o(1)_PER_OUTER_PAIR
STAGE15_6AC_LOW_CORE_PRIMITIVE_GAUSSIAN_REDUCTION=true
STAGE15_6AC_LOW_CORE_GAUSSIAN_SQUARE_RECEIVER=true
STAGE15_6AC_AR009_HIGH_CORE_STATUS=SQRT_COLLAPSE_PROVED
STAGE15_6AC_AR017_LOW_CORE_STATUS=EXACT_SQUARE_QUOTIENT_RECEIVER
STAGE15_6AC_AR010=WATCH_RECONSTRUCTION_BEFORE_GENUS_ONE
STAGE15_6AC_AR012_TRIGGERED=false
STAGE15_6AC_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AC_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AC_STAGE15_5_REPROVED=false
STAGE15_6AC_EXIT=HIGH_CORE_SQRT_COLLAPSE_LOW_CORE_SQUARE_RECEIVER_READY
```

## 11. Next narrow gate

Stage15-6ad should count or further reconstruct the **low-core coupled Gaussian-square receiver** while preserving the same physical outer-pair measure. The first operation should be AR-010 style reconstruction audit on the four exact lifted equations, not a generic genus-one or character estimate.

No Stage14 route should be restarted unless that audit produces an exact trigger signature.