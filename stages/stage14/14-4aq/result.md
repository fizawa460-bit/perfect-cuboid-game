# Stage14-4aq — global-solubility/Sha retainer and weighted averaging target

## Result

For every Stage14 first-face elliptic curve `E_F/Q`, the family has full rational 2-torsion. Hence the standard exact sequence

\[
0\to E_F(\mathbf Q)/2E_F(\mathbf Q)\to \operatorname{Sel}_2(E_F)\to \Sha(E_F)[2]\to0
\]

gives

\[
\dim_{\mathbf F_2}\operatorname{Sel}_2(E_F)
=2+\operatorname{rank}E_F(\mathbf Q)+\dim_{\mathbf F_2}\Sha(E_F)[2].
\]

Write

\[
s(F)=1_{\dim\operatorname{Sel}_2(E_F)>2},\qquad
r(F)=1_{\operatorname{rank}E_F(\mathbf Q)>0}.
\]

Since `r(F)<=s(F)`, define the exact Sha-trap indicator

\[
\tau(F)=s(F)-r(F).
\]

Then `tau(F)=1` exactly when the base has nontrivial 2-Selmer beyond rational 2-torsion but rank zero, equivalently when the excess is carried by nontrivial `Sha(E_F)[2]`. Thus

\[
R(B)=\Sigma(B)-T_{\Sha}(B),\qquad
T_{\Sha}(B)=\sum_{F\in A(B)}\tau(F),
\]

and, whenever `Sigma(B)>0`,

\[
\frac{R(B)}{\Sigma(B)}=1-\frac{T_{\Sha}(B)}{\Sigma(B)}.
\]

This isolates the 4ap middle retainer without mixing it with the s3 first-small-point condition.

## Centered-local compatible weighted identity

Let `W_Q(F)>=0` be any finite local sieve weight constructed from the full local 2-descent system, including the exact local mean subtraction required by s5g. Define

\[
S_Q=\sum_F W_Q(F)s(F),\quad
G_Q=\sum_F W_Q(F)r(F),\quad
T_Q=\sum_F W_Q(F)\tau(F).
\]

Pointwise `r=s-tau`, so for every such weight, without independence assumptions,

\[
G_Q=S_Q-T_Q.
\]

A uniform global-retainer theorem can therefore be targeted in the form

\[
G_Q\le \rho_{\rm glob}(B,Q)S_Q+E_{\rm glob}(B,Q)
\]

uniformly over the dyadic Euclid boxes and centered-local weights used by the local sieve. Equivalently,

\[
T_Q\ge (1-\rho_{\rm glob}(B,Q))S_Q-E_{\rm glob}(B,Q).
\]

This formulation is deliberately agnostic about the existence or value of a global density. If eventually `rho_glob(B,Q) << B^{-delta_glob}` with negligible error, 4ap transfers the exponent `delta_glob`. If only `rho_glob=O(1)`, the global gate contributes no power of `B`; it remains a constant-factor retainer.

## Finite diagnostic

From the complete `H<=20,000` 4am census, the exact `Sigma` counts and unconditional rank intervals imply the following aggregate Sha-trap intervals:

| B | Sigma | R interval | Sha-trap bases `Sigma-R` | R/Sigma | Sha-trap/Sigma |
|---:|---:|---:|---:|---:|---:|
| 2,000 | 476 | 371..385 | 91..105 | 0.7794..0.8088 | 0.1912..0.2206 |
| 5,000 | 1,234 | 916..989 | 245..318 | 0.7423..0.8015 | 0.1985..0.2577 |
| 10,000 | 2,553 | 1,875..2,057 | 496..678 | 0.7344..0.8057 | 0.1943..0.2656 |
| 20,000 | 5,209 | 3,784..4,239 | 970..1,425 | 0.7264..0.8138 | 0.1862..0.2736 |

The finite data show a substantial Sha-trap population but do not show power-law decay of `R/Sigma`. In particular, 14-4aq does **not** assign a positive asymptotic `delta_global`. This reinforces the 4am diagnosis that the observed severe thinning is still concentrated in the later first-small-point gate.

## Boundary

```text
STAGE14_4AQ=GLOBAL_SHA_RETAINER_ISOLATED_AND_WEIGHTED_TARGET_FORMULATED
SEL2_EXACT_SEQUENCE_IMPORTED=true
SHA_TRAP_INDICATOR_EXACT=true
GLOBAL_RETAINER_IDENTITY_R_EQ_SIGMA_MINUS_SHA_TRAP=true
CENTERED_LOCAL_WEIGHTED_GLOBAL_IDENTITY=true
GLOBAL_RETAINER_UNIFORM_AVERAGING_TARGET_FORMULATED=true
GLOBAL_SOLUBILITY_DENSITY_PROVED=false
POSITIVE_GLOBAL_SAVING_EXPONENT_PROVED=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
UNIFORM_FIRST_SMALL_POINT_LOWER_TAIL_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

No independence of local conditions and Sha, no positive-rank density theorem, no power saving, and no `sqrt(B)` asymptotic is claimed.

```text
NEXT=Stage14-4ar isolate the positive-rank-to-first-small-point retainer and formulate a uniform weighted lower-tail target using the s3 height window
```
