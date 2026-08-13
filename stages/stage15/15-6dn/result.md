# Stage15-6dn — centered pair-resultant energy test and rigorous negative certificate

Base: Stage15-6dm. This substage tests whether the currently available **deterministic support information** can prove
\[
\mathfrak B_P(Q_0)\ll X^{1+\kappa}Q_0B^{o(1)}
\qquad (X=|G(P)|)
\]
with some `kappa<1`.

The permitted inputs are the exact reconstructed graph, decorated `(d,e)` occupancy, `q^2|R(x,y)` for occupied pairs, `q|Delta_x`, `kg^2|Delta_x`, legal divisor switching, Stage15-6da Pell reconstruction, local valuations and previously preserved internal routes. No external equidistribution theorem is inserted.

## 1. What the pair-resultant support gives after decoration is retained

For one off-diagonal pair `(x,y)`, any occupied decorated pair satisfies
\[
d\mid\gcd(G_S(x),G_S(y)),
\qquad
e\mid\gcd(G_O(x),G_O(y)),
\qquad de\le Q_0,
\]
and also
\[
(de)^2\mid\mathcal R(x,y).
\]
Because all relevant integers are polynomially bounded, the number of legal decorated divisor pairs for fixed `(x,y)` is `B^{o(1)}`. With
\[
\lambda(d,e)\le de\le Q_0,
\]
the safe positive-incidence estimate is therefore only
\[
\sum_{\substack{de\le Q_0\\I_{d,e}(x)I_{d,e}(y)=1}}
\frac{\lambda(d,e)}{\Omega(d,e)}
\ll Q_0B^{o(1)}.
\]
Summing pairs gives
\[
\boxed{
\mathcal P_{P,\mathrm{off}}(Q_0)
\ll X^2Q_0B^{o(1)}.
}
\]
The square-divisor resultant improves the **description** of the support, but without a distribution theorem it does not improve the exponent of `X`.

## 2. Why centering cannot be recovered from that positive bound

Stage15-6dm gives exactly
\[
\mathfrak B_P=\mathcal P_P-2\mathcal C_P+\mathcal M_P.
\]
The desired gain is precisely the cancellation between the quadratic main portion of `P` and the cross/main terms. Replacing any of these three terms by a positive majorant loses that cancellation and returns the quadratic `X^2` scale.

Equivalently, for a fixed decorated modulus
\[
B_{d,e}=N_{d,e}-\alpha_{d,e}X,
\qquad \alpha_{d,e}=\Omega(d,e)/(de)^2.
\]
A theorem with `kappa<1` requires a genuine statement that `N_{d,e}` is close to `alpha_{d,e}X` on average. The divisibility implications `q|Delta` and `q^2|R` are support statements; they do not compare the actual occupancy mass with its local main density.

## 3. Fixed-small-modulus obstruction to a purely deterministic sparsity proof

Fix one legal odd decorated pair `(d_0,e_0)` with constant `q_0=d_0e_0`. Locally modulo `q_0`, occupancy is a union of exactly `Omega(d_0,e_0)` primitive root-line pairs. This is a positive-density residue set of density
\[
\alpha_0=\Omega(d_0,e_0)/q_0^2.
\]
For any two points inside this occupied residue union, the pair-resultant divisibility
\[
q_0^2\mid\mathcal R(x,y)
\]
is automatic from the local root/sign alternatives. Thus the resultant condition does not make pairs in one occupied residue packet rare.

The current deterministic inputs do not rule out a reconstructed graph packet having a fixed positive proportion `c` of its nodes in that occupied residue union with `c` separated from `alpha_0`. If that occurs,
\[
|B_{d_0,e_0}|\asymp X,
\]
so the single fixed-modulus contribution to `mathfrak B_P` is already `asymp X^2` up to a constant weight.

This is a **logical obstruction certificate for the present route inputs**, not a construction of an actual biased Stage15 packet and not a proof that equidistribution is false. It shows that support/divisibility alone cannot imply `kappa<1`; an input controlling residue distribution is mathematically necessary.

## 4. Tests of the preserved structural routes

### 4.1 `q|Delta_x` and `kg^2|Delta_x`
Both constrain the same fourth-power difference, but no inclusion `q|kg` or `kg|q` is proved. For fixed small `q`, `q|Delta_x` is itself a positive-density congruence condition. The divisor-many list of `kg` for a fixed outer pair does not center the frequency of `q` across graph nodes.

### 4.2 Reconstructed Pell graph
Stage15-6da removes the independent fourth residual support: a fixed base triple has only `B^{o(1)}` completions. This is vertical multiplicity control. Modulo a fixed `q`, the base triples and Pell/unit-orbit completions may occupy periodic residue classes; no uniform statement that those classes are sampled with density `alpha_{d,e}` has been proved. Therefore the Pell reconstruction does not supply centered occupancy cancellation by itself.

### 4.3 Exact divisor switching
Switching `(d,e)` to complementary cofactors is multiplicity-one bookkeeping after the state is fixed. Applied to the positive pair term it can reorganize large divisors, but it does not manufacture the negative cross term `-2 alpha X N`. Hence it cannot prove the centered second moment without an additional average theorem.

### 4.4 Large-resultant thresholding
For large `q`, `q^2|R(x,y)` can reduce the available pair support. But a uniform `kappa<1` theorem for `mathfrak B_P(Q0)` also contains every fixed small legal modulus. The small-modulus sector cannot be removed by large-resultant thresholding and remains capable of quadratic centered bias unless its residue distribution is controlled.

### 4.5 Existing pair-energy / Stage14 routes
Stage15-6ah and the Stage14 fixed-tag Type-II/spectral/projective-spacing results control different packet measures or different common-support variables. No exact adapter to the centered decorated occupancy residual has been proved. Their exponents remain firewalled.

## 5. Negative certificate

From the currently certified deterministic inputs, the best safe centered estimate remains
\[
\boxed{
\mathfrak B_P(Q_0)
\ll X^2Q_0B^{o(1)},
}
\]
corresponding to
\[
\boxed{\kappa=1.}
\]
No `kappa<1` follows from the orientation-blind pair-resultant support plus the existing reconstruction/divisor structure.

The blocked claim is intentionally narrow:

> `ORIENTATION_BLIND_PAIR_RESULTANT_OCCUPANCY_ENERGY`, when used only through positive support/divisor sparsity and the currently certified reconstructed-graph identities, does not prove a subquadratic centered occupancy second moment.

It does **not** rule out a future arithmetic theorem exploiting cancellation on exactly the same resultant.

## 6. Delta, overlap, sigma, and split

With `kappa=1`, the corrected formula
\[
\delta<\frac{1-\kappa}{2}-\frac\theta2
\]
gives no positive `delta` for any polynomial `theta>0`. Hence there is no executable polynomial small-side overlap window.

No new inverse-`D_0` estimate for the large receiver is obtained, so `sigma>0` remains unproved. There are not two independently quantified live obstructions; the split trigger remains false.

## 7. Required stop audits

- **EXHAUSTIVE_VIEW_AUDIT**: pair-resultant, one-point Delta/core support, Pell modular correlation, divisor switching, local valuations, character/Ramanujan expansion and preserved Stage14 adapters all checked.
- **BLIND_REDISCOVERY status**: Stage15-6dl already rediscovered the character/Ramanujan form as the next analytic backup; the present negative certificate does not expose a new deterministic route.
- **Arsenal trigger search**: no exact current-measure exponent adapter found.
- **Exact reconstruction search**: no second deterministic dimension collapse beyond Stage15-6da.
- **Measure/quantifier audit**: physical graph first, decorated `(d,e)` second, centering retained before absolute values.

```text
STAGE15_6_SUBSTAGE=6dn
STAGE15_6DN_DECORATED_PAIR_RESULTANT_TESTED=true
STAGE15_6DN_CENTERING_REQUIRED_FOR_GAIN=true
STAGE15_6DN_FIXED_SMALL_MODULUS_OBSTRUCTION=true
STAGE15_6DN_PELL_RECONSTRUCTION_CENTERS_OCCUPANCY=false
STAGE15_6DN_DIVISOR_SWITCHING_CENTERS_OCCUPANCY=false
STAGE15_6DN_RESULTANT_SUPPORT_KAPPA=1
STAGE15_6DN_KAPPA_LT_1_PROVED=false
STAGE15_6DN_NEGATIVE_CERTIFICATE=true
STAGE15_6DN_DELTA_PROVED=false
STAGE15_6DN_SIGMA_PROVED=false
STAGE15_6DN_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6DN_SPLIT_TRIGGER=false
STAGE15_6DN_EXIT=CHARACTER_RAMANUJAN_OCCUPANCY_DISPERSION_PROMOTION_READY
```