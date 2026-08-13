# Stage15-6do — exact character/Ramanujan occupancy-dispersion promotion

Base: Stage15-6dn negative certificate. The positive orientation-blind pair-resultant route does not prove `kappa<1` from the currently certified support data. Promote the preserved analytic backup
\[
\boxed{\text{CHARACTER / RAMANUJAN OCCUPANCY DISPERSION ON THE RECONSTRUCTED GRAPH}.}
\]
without importing any Stage14 fixed-packet exponent.

Keep the exact decorated `(d,e)` data, `q=de`, legal orientation set `Omega(d,e)`, physical graph packet `G(P)`, exact weight `lambda=phi(d)phi(e)`, and occupancy residual
\[
B_{d,e}=\sum_{x\in G(P)}\left(I_{d,e}(x)-\frac{\Omega(d,e)}{q^2}\right).
\]

## 1. Exact Fourier expansion of one legal orientation

For one composite legal orientation `omega`, the two primitive root-line conditions can be written
\[
L_{\omega,1}(x)\equiv0\pmod q,
\qquad
L_{\omega,2}(x)\equiv0\pmod q,
\]
where, after the CRT orientation is fixed,
\[
L_{\omega,1}=m-\rho_\omega n,
\qquad
L_{\omega,2}=r-\sigma_\omega s
\]
with unit root/sign coefficients modulo the relevant odd switched modulus. Bounded 2-adic conventions remain separately charged as before.

Additive orthogonality gives exactly
\[
1_{C_\omega}(x)
=\frac1{q^2}\sum_{u,v\bmod q}
 e_q\!\left(uL_{\omega,1}(x)+vL_{\omega,2}(x)\right),
\]
where `e_q(t)=exp(2 pi i t/q)`.

Since the legal orientation cells are disjoint on the primitive occupied population,
\[
I_{d,e}(x)=\sum_{\omega\in\Omega(d,e)}1_{C_\omega}(x).
\]
The joint zero frequency `(u,v)=(0,0)` contributes exactly
\[
\frac{\Omega(d,e)}{q^2}.
\]
Therefore the centered indicator has the exact nonzero-frequency expansion
\[
\boxed{
I_{d,e}(x)-\frac{\Omega(d,e)}{q^2}
=\frac1{q^2}
\sum_{\omega\in\Omega(d,e)}
\sum_{\substack{u,v\bmod q\\(u,v)\ne(0,0)}}
 e_q\!\left(uL_{\omega,1}(x)+vL_{\omega,2}(x)\right).
}
\]
This removes the centering problem algebraically rather than estimating the positive occupancy term first.

## 2. Exact graph exponential sums

Define
\[
S_P(q,\omega;u,v)
:=\sum_{x\in G(P)}
 e_q\!\left(uL_{\omega,1}(x)+vL_{\omega,2}(x)\right).
\]
Then
\[
\boxed{
B_{d,e}
=\frac1{q^2}
\sum_{\omega\in\Omega(d,e)}
\sum_{(u,v)\ne(0,0)}
S_P(q,\omega;u,v).
}
\]
Consequently the exact centered occupancy second moment becomes
\[
\boxed{
\mathfrak B_P(Q_0)
=\sum_{de\le Q_0}
\frac{\lambda(d,e)}{\Omega(d,e)q^4}
\left|
\sum_{\omega\in\Omega(d,e)}
\sum_{(u,v)\ne(0,0)}
S_P(q,\omega;u,v)
\right|^2.
}
\]
The decorated channel assignment is still explicit through `(d,e)` and through the orientation set. Distinct decompositions with the same `q` are not merged.

## 3. Ramanujan-style frequency grouping

The nonzero frequency pairs may be partitioned by
\[
t=\gcd(u,v,q).
\]
After writing `u=t u_1`, `v=t v_1`, the phase descends to modulus `q/t` with primitive frequency pair relative to that quotient. Grouping by `t` is an exact divisor decomposition of the character expansion. Summing primitive frequency classes over root/sign orientations produces the natural Ramanujan/Gauss-type local coefficients for this receiver.

No cancellation bound for those coefficients is assumed here. In particular, the word `Ramanujan` denotes the exact primitive-frequency/divisor organization of the centered indicator, not an imported Ramanujan or Weil estimate.

## 4. New precise theorem gate

The promoted route asks for a whole reconstructed-graph large-sieve/dispersion estimate on the nonzero modes above. Quantitatively, it suffices to prove for some `kappa<1`
\[
\boxed{
\sum_{de\le Q_0}
\frac{\lambda(d,e)}{\Omega(d,e)q^4}
\left|
\sum_{\omega}
\sum_{(u,v)\ne(0,0)}
S_P(q,\omega;u,v)
\right|^2
\ll X^{1+\kappa}Q_0B^{o(1)}.
}
\]
This is exactly the `mathfrak B_P` target, now in a form where the local main density has been removed by orthogonality before absolute values.

A dual formulation may instead bound correlations between two reconstructed graph nodes across nonzero frequencies. Orthogonality then returns the orientation-blind pair-resultant conditions from 6dm, so the character and pair-resultant receivers are analytically equivalent views of the same centered gate. The gain must come from cancellation, not from re-counting the same positive support.

## 5. Existing input test and cross-promotion firewall

- `kg^2|Delta`, `q|Delta` and the Pell completion remain inside every graph sum but give no nonzero-frequency cancellation theorem by themselves.
- AR-009/t76 supplies fixed-modulus root-line geometry, not a whole-family centered large sieve on this reconstructed graph.
- tH21/tH22 and Stage14 Type-II/spectral inputs use different fixed-U/fixed-tag packet measures. No adapter identifying their averaging measure, coefficients and local main term with the present `S_P(q,omega;u,v)` family has been proved.
- Stage15-6ah pair energy is recovered only as structural guidance; its common-support modulus is not the present decorated occupancy modulus.

Hence no Stage14 exponent is promoted in this substage.

## 6. Delta/sigma ledger and split eligibility

No `kappa<1` is proved in Stage15-6do, so
\[
\boxed{\delta>0\text{ remains unproved}.}
\]
Conditionally, if the new character gate proves `kappa<1`, then for `Q0=B^theta`
\[
\boxed{
\delta<\frac{1-\kappa}{2}-\frac\theta2,
\qquad 0<\theta<1-\kappa
}
\]
is the polynomial small-side window condition.

The large receiver still has no certified `D_0^{-sigma}` gain, so
\[
\boxed{\sigma>0\text{ remains unproved}.}
\]
There is still one selected quantitative obstruction rather than two independently quantified branches; `SPLIT_TRIGGER=false`.

## 7. Controller exit

```text
STAGE15_6_SUBSTAGE=6do
STAGE15_6DO_PAIR_RESULTANT_NEGATIVE_CERTIFICATE_ACCEPTED=true
STAGE15_6DO_SELECTED_ROUTE=CHARACTER_RAMANUJAN_OCCUPANCY_DISPERSION
STAGE15_6DO_CENTERED_INDICATOR_NONZERO_FOURIER_EXPANSION_EXACT=true
STAGE15_6DO_DECORATED_DE_ASSIGNMENT_PRESERVED=true
STAGE15_6DO_ZERO_MODE_EQUALS_LOCAL_MAIN_DENSITY=true
STAGE15_6DO_RAMANUJAN_GROUPING_IS_EXACT_REORGANIZATION=true
STAGE15_6DO_CHARACTER_LARGE_SIEVE_ADAPTER_PROVED=false
STAGE15_6DO_KAPPA_LT_1_PROVED=false
STAGE15_6DO_DELTA_PROVED=false
STAGE15_6DO_SIGMA_PROVED=false
STAGE15_6DO_EXECUTABLE_OVERLAP_WINDOW=false
STAGE15_6DO_STAGE14_EXPONENT_TRANSFER=false
STAGE15_6DO_SPLIT_TRIGGER=false
STAGE15_6DO_AUDIT_REQUIRED=true
STAGE15_6DO_CODEX_REQUIRED=false
STAGE15_6DO_MERGE_ALLOWED=false
```

Controller output:
```text
CURRENT_SUBSTAGE=Stage15-6do
NEXT_GATE=FRESH_AUDIT_OF_PAIR_RESULTANT_NEGATIVE_CERTIFICATE_AND_CHARACTER_OCCUPANCY_PROMOTION
ALL_PRIOR_CHECKS_PASS=true
AUDIT_REQUIRED=true
CODEX_REQUIRED=false
MERGE_ALLOWED=false
SPLIT_TRIGGER=false
```

The next main task after audit is to test a **whole-family reconstructed-graph character large-sieve adapter** for these exact nonzero modes, with the physical packet and decorated `(d,e)` measure preserved.