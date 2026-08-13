# Stage14-e11 — explicit thin-cover exponent and growing-prime local sieve

> STATUS: `STAGE14_E11_COMPLETE_EXPLICIT_THIN_COVER_EXPONENT_AND_GROWING_PRIME_SIEVE`
>
> INPUT: Stage14-e10 adelic six-state law and Euler-brick degree-two K3 cover.
>
> PURPOSE: replace e10's unnamed positive logarithmic saving by an explicit admissible exponent, and upgrade the e10 residue blocker from a fixed-prime/two-limit argument to a genuinely growing-prime uniform sieve.

## 1. Frozen geometry and height

The ambient base is

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1),
\qquad \rho(Y)=6,
\qquad \dim Y=2,
\]

with globally generated anticanonical bundle.  The Euler-brick third-face-square locus resolves to a smooth proper geometrically integral K3 surface `Z` with a dominant proper generically finite map

\[
f:Z\to Y
\]

of generic degree `2`.

As in e10, the physical Euclidean height and Huang's canonical toric anticanonical height are fixed multiplicatively comparable, so any logarithmic saving for one transfers to the other.

## 2. Extracting an explicit exponent from Huang v3

Huang v3 Theorem 1.6(1) states, for a generically finite map of degree greater than one,

\[
\mathcal N_{\rm loc}(f;B)
=O\bigl(B(\log B)^{r-1-\iota_f}\bigr)
\]

for some `0<iota_f<1`.  The theorem statement leaves `iota_f` unnamed, but its proof is quantitative enough to extract an admissible range.

In the proof, after applying the uniform Selberg sieve, one obtains for every small `epsilon>0`

\[
\mathcal N_{\rm loc}(f;B)
\ll_\varepsilon
\frac{B(\log B)^{r-1}}{N^{1-\varepsilon}}
+
N^{2(r+2\dim Y+1)+\varepsilon}
B(\log B)^{r-3/2+\varepsilon}.
\]

For the Stage14-e surface,

\[
r=6,\qquad \dim Y=2,
\]

hence

\[
\boxed{2(r+2\dim Y+1)=22.}
\]

Put

\[
N=(\log B)^\lambda.
\]

The two logarithmic savings relative to `B(log B)^5` are, up to the arbitrarily small epsilon loss,

\[
\lambda
\qquad\text{and}\qquad
\frac12-22\lambda.
\]

Balancing them gives

\[
\lambda=\frac1{46},
\qquad
\lambda=\frac12-22\lambda.
\]

This value satisfies Huang's proof restriction

\[
\lambda<\frac{1}{4(r+2\dim Y+1)}=\frac1{44}.
\]

Because the proof carries epsilon losses, the endpoint `1/46` itself is not claimed.  For every

\[
\boxed{0<\eta<\frac1{46}}
\]

choose epsilon sufficiently small; then both proof terms are

\[
O_\eta\bigl(B(\log B)^{5-\eta}\bigr).
\]

Therefore

\[
\boxed{
R_{\rm EB}(B)
\ll_\eta
B(\log B)^{5-\eta}
\qquad
\text{for every }\eta<\frac1{46}.
}
\]

This is an explicit downstream form of e10's unnamed `eta_EB>0`.

### 2.1 Concrete exponent

For a no-endpoint statement with a fixed number, take

\[
\boxed{\eta=\frac1{50}}.
\]

Thus unconditionally

\[
\boxed{
R_{\rm EB}(B)
\ll
B(\log B)^{5-1/50}.
}
\]

The deterministic audit uses the explicit witnesses

\[
\lambda=\frac1{46},\qquad \varepsilon=\frac1{1000}.
\]

Then the first proof term saves

\[
\frac{999}{46000}>\frac1{50},
\]

and the second saves

\[
\frac{953}{46000}>\frac1{50}.
\]

So the concrete `1/50` statement does not rely on a limiting epsilon argument.

This does **not** claim that `1/46` is an optimal exponent for the Euler-brick cover.  It is only the supremum obtained by balancing the two error terms in Huang's present general proof.

## 3. e10 blockers are uniform mod-p toric conditions

E10 defines, for every odd prime `p`, a local blocker `B_p` inside state `G` with mass

\[
\delta_p
=
\frac{2(p-\chi_4(p))}{p^2+6p+1}
=
\frac2p+O(p^{-2}).
\]

To use a growing-prime Selberg sieve we must verify that these are uniformly bounded-level congruence conditions, not merely fixed-prime measurable sets.

On the torus write

\[
(n_1,n_2)=(v_p(q_1),v_p(q_2)).
\]

The fan of `Y` contains the four exceptional rays

\[
(1,1),\quad(1,-1),\quad(-1,1),\quad(-1,-1),
\]

created by blowing up the four torus-fixed corners of `P1 x P1`.

The e9/e10 state `G` is exactly

\[
|n_1|=|n_2|>0.
\]

Thus a state-G point specializes to the open stratum of one of those four exceptional toric divisors.  After factoring the common valuation, the leading unit ratio `x/y mod p` is precisely a residue coordinate on that exceptional divisor.

Consequently the condition

\[
\chi_p(x^2+y^2)=-1
\]

inside `G` is a union of residue classes on the reduction of these four exceptional divisors.  Equivalently, for every good odd prime,

\[
\boxed{B_p\text{ is detected modulo }p}
\]

on the canonical smooth toric integral model.  In Huang's notation this gives the uniform covering-level exponent

\[
\boxed{n_0=1.}
\]

The finitely many excluded/bad primes are absorbed into the fixed set `S` and do not affect the asymptotic sieve dimension.

## 4. The e10 blocker has sieve dimension two

Let

\[
\Omega_p=Y(\mathbf Q_p)\setminus B_p.
\]

In Huang's Selberg sieve the relevant multiplicative weight is

\[
w_p=
\frac{\omega_p(B_p)}{\omega_p(\Omega_p)}
=
\frac{\delta_p}{1-\delta_p}.
\]

Since

\[
\delta_p=\frac2p+O(p^{-2}),
\]

we have

\[
\boxed{w_p=\frac2p+O(p^{-2}).}
\]

Hence

\[
\sum_{p<N}w_p\log p
=2\log N+O(1).
\]

The same multiplicative-function lemma used in Huang's proof of Theorem 1.6(2a) and Theorem 1.8 then gives

\[
\boxed{
G(N)=C_G(\log N)^2+O(\log N)
}
\]

for some `C_G>0`.  In sieve language the explicit e10 blocker has dimension

\[
\boxed{\kappa=2.}
\]

The committed finite values of `G(N)` are diagnostics only; the logarithmic exponent two comes from the prime-sum calculation above, not from numerical fitting.

## 5. Growing-prime uniformity

Huang's uniform Selberg sieve (Theorem 3.11 / Corollary 3.13) together with the toric effective equidistribution error gives, in this `r=6`, `dim Y=2`, `n0=1` setting,

\[
\#\{\text{ambient points avoiding every }B_p\}
\ll_\varepsilon
B(\log B)^5
\left(
\frac1{G(N)}
+
\frac{N^{22+\varepsilon}}{(\log B)^{1/2-\varepsilon}}
\right).
\]

Every Euler brick avoids every `B_p`.  Choose for example

\[
N=(\log B)^{1/100}.
\]

Then

\[
\frac12-\frac{22}{100}=\frac7{25}>0,
\]

so the error term has a fixed positive log-power gap and is negligible relative to `(log log B)^-2`.  Since

\[
G(N)\asymp(\log N)^2\asymp(\log\log B)^2,
\]

we obtain the one-limit growing-prime estimate

\[
\boxed{
R_{\rm EB}(B)
\ll
\frac{B(\log B)^5}{(\log\log B)^2}.
}
\]

This is weaker than the explicit thin-cover log-power estimate in §2, but it closes an independent boundary left open in e10:

```text
ELEMENTARY_GROWING_PRIME_UNIFORMITY_PROVED=true
```

Here "elementary" means that the local obstruction itself is the explicit e10 residue blocker; the uniform counting mechanism is Huang's toric Selberg-sieve theorem.

## 6. Comparison of the control bounds

The e-track now has three logically independent quantitative views of the third-face-square/Euler-brick subpopulation:

\[
\begin{array}{c|c}
\text{route}&\text{bound}\\ \hline
\text{e8 divisor projection}&B^{1+o(1)}\\
\text{e11 explicit local blockers}&B(\log B)^5/(\log\log B)^2\\
\text{e11 degree-two thin cover}&B(\log B)^{5-\eta},\ \forall\eta<1/46
\end{array}
\]

These bounds are not directly ordered for every finite `B`; they arise from different structures and have different asymptotic forms.  In particular the e8 `B^(1+o(1))` envelope is much stronger at the polynomial-power level, while the thin-cover result gives a genuine saving relative to the ambient `B(log B)^5` scale within the toric counting framework.

No route proves the finite `sqrt(B)` signal to be asymptotic.

## 7. Literature boundary

The general effective equidistribution, uniform Selberg sieve, and generically finite thin-image estimate are theorem-level inputs from Huang v3.  The e11 contribution is the Stage14-specific substitution

\[
(r,\dim Y,n_0)=(6,2,1),
\]

the explicit balancing to `eta<1/46`, and the identification of the e10 residue blockers as mod-p conditions on the four exceptional toric divisors with sieve dimension two.

No novelty claim is inferred merely from not finding the exact Stage14 formulas elsewhere.

## 8. Locked result

```text
STAGE14_E11=COMPLETE_EXPLICIT_THIN_COVER_EXPONENT_AND_GROWING_PRIME_SIEVE
HUANG_PROOF_EXPLICIT_ETA_RANGE_PROVED=true
ETA_EB_ANY_LT_1_OVER_46=true
CONCRETE_ETA_1_OVER_50_PROVED=true
ENDPOINT_ETA_1_OVER_46_PROVED=false
ELEMENTARY_GROWING_PRIME_UNIFORMITY_PROVED=true
LOCAL_BLOCKER_LOGLOG_SAVING_PROVED=true
LOCAL_BLOCKER_SIEVE_DIMENSION=2
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT_E_SUPPLEMENT=NONE_DEFINED_AFTER_E11
```
