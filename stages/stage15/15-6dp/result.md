# Stage15-6dp — exact whole-family character large-sieve / dual receiver

Base: merged Stage15-6do after fresh audit PASS. Execute the selected `CHARACTER_RAMANUJAN_OCCUPANCY_DISPERSION` route on the reconstructed physical graph. No Stage14 exponent is imported.

Keep one exact physical packet `G(P)` with

- `R<=B` as the population cutoff;
- cross-gcd cells and `HMNUV<=B` retained only as the proved height consequence;
- the Stage15-6da `B^o(1)` completion decoration charged once;
- both exact survivor norm equations;
- `kg^2|Delta`, `Delta=(abM)^4-(cdN)^4`;
- all primitivity, positivity, canonical, exactly-two and direction masks.

For a decorated switched pair `(d,e)`, put
\[
q=de,
\qquad
\lambda(d,e)=\varphi(d)\varphi(e),
\qquad
\Omega_{d,e}=|\Omega(d,e)|,
\]
with `(q,H)=1`. Distinct channel assignments `(d,e)` are never collapsed merely because they have the same product `q`.

For one legal orientation `omega`, Stage15-6do gives primitive root-line forms
\[
L_{\omega,1}(x)=m-\rho_\omega n,
\qquad
L_{\omega,2}(x)=r-\sigma_\omega s,
\]
and the exact graph exponential sum
\[
S_P(q,\omega;u,v)
=\sum_{x\in G(P)}
 e_q\bigl(uL_{\omega,1}(x)+vL_{\omega,2}(x)\bigr).
\]
The zero mode was already removed before absolute values:
\[
B_{d,e}
=\frac1{q^2}
\sum_{\omega\in\Omega(d,e)}
\sum_{(u,v)\ne(0,0)}
S_P(q,\omega;u,v).
\]
Hence
\[
\mathfrak B_P(Q_0)
=\sum_{de\le Q_0}
\frac{\lambda(d,e)}{\Omega_{d,e}q^4}
\left|
\sum_\omega\sum_{(u,v)\ne(0,0)}S_P(q,\omega;u,v)
\right|^2.
\]
This is the quantity that must satisfy a same-measure bound with `kappa<1`.

## 1. Exact AR-025-style valuation reduction of the frequency family

For one nonzero frequency pair `(u,v) mod q`, define
\[
t=(u,v,q),\qquad Q=q/t>1,
\qquad u=tu_1,\quad v=tv_1.
\]
Then
\[
(u_1,v_1,Q)=1
\]
and exactly
\[
e_q\bigl(uL_1+vL_2\bigr)
=e_Q\bigl(u_1L_1+v_1L_2\bigr).
\]
Because the odd S/O channel divisors are coprime prime by prime, `Q|q` inherits a decorated pair
\[
d_Q=(d,Q),\qquad e_Q=(e,Q),\qquad Q=d_Qe_Q,
\]
and every legal orientation modulo `q` projects to a legal orientation modulo `Q`. Forgetting prime-power factors and omitted primes has at most divisor/root multiplicity
\[
B^{o(1)}.
\]
Thus the nonzero family can be reorganized exactly into primitive reduced-frequency packets
\[
(Q,d_Q,e_Q,\bar\omega;u_1,v_1),
\qquad
Q|q,\ Q>1,\ (u_1,v_1,Q)=1,
\]
with only `B^o(1)` valuation/orientation-lift multiplicity.

This is a legal Stage15 adapter of the **recombination mechanism** in AR-025. It consumes the superficial unit/nonunit frequency split. It does **not** consume the polynomial primitive-character family and supplies no exponent by itself.

## 2. Exact operator formulation

Set
\[
F_{d,e}(x)
:=I_{d,e}(x)-\mu_{d,e},
\qquad
\mu_{d,e}=\frac{\Omega_{d,e}}{q^2}.
\]
Define the linear operator
\[
(T_P a)_{d,e}
:=\sqrt{\frac{\lambda(d,e)}{\Omega_{d,e}}}
\sum_{x\in G(P)}a_xF_{d,e}(x),
\qquad de\le Q_0.
\]
Then, with `1_G` the constant vector on the graph,
\[
\boxed{
\mathfrak B_P(Q_0)=\|T_P1_G\|_2^2.
}
\]
Since
\[
\|1_G\|_2^2=|G(P)|=:X,
\]
a whole-family large-sieve theorem strong enough for Stage15 would be
\[
\boxed{
\|T_P\|_{2\to2}^2
\ll X^\kappa Q_0B^{o(1)}
\quad\text{for some }\kappa<1,
}
\]
uniformly over every retained physical packet. It would imply
\[
\mathfrak B_P(Q_0)
\ll X^{1+\kappa}Q_0B^{o(1)}.
\]

The exact dual form is
\[
\boxed{
\sum_{x\in G(P)}
\left|
\sum_{de\le Q_0}
 b_{d,e}
 \sqrt{\frac{\lambda(d,e)}{\Omega_{d,e}}}
 F_{d,e}(x)
\right|^2
\ll
X^\kappa Q_0B^{o(1)}
\sum_{de\le Q_0}|b_{d,e}|^2.
}
\]
This formulation preserves the decorated `(d,e)` measure and centers every modulus before any absolute value.

Equivalently, the Gram kernel is
\[
K_P(x,y;Q_0)
=\sum_{de\le Q_0}
\frac{\lambda(d,e)}{\Omega_{d,e}}
F_{d,e}(x)F_{d,e}(y).
\]
The desired theorem is a spectral cancellation statement for this **centered** kernel. Replacing it by its positive support reproduces the blocked 6dm/6dn receiver.

## 3. A legal but stronger frequency-separated inequality

Cauchy--Schwarz inside one decorated modulus gives
\[
|B_{d,e}|^2
\le
\frac{\Omega_{d,e}(q^2-1)}{q^4}
\sum_{\omega}\sum_{(u,v)\ne(0,0)}
|S_P(q,\omega;u,v)|^2.
\]
Therefore
\[
\boxed{
\mathfrak B_P(Q_0)
\le
\mathfrak L_P(Q_0)
:=
\sum_{de\le Q_0}
\frac{\lambda(d,e)}{q^2}
\sum_\omega\sum_{(u,v)\ne(0,0)}
|S_P(q,\omega;u,v)|^2.
}
\]
This inequality is same-measure and legal, but stronger than necessary because it destroys cancellation between different nonzero frequencies and orientations.

For one fixed `(q,omega)`, full frequency orthogonality gives
\[
\sum_{u,v\bmod q}|S_P(q,\omega;u,v)|^2
=q^2 C_{q,\omega},
\]
where
\[
C_{q,\omega}
=\#\{(x,y)\in G(P)^2:
L_{\omega,1}(x)\equiv L_{\omega,1}(y),
L_{\omega,2}(x)\equiv L_{\omega,2}(y)\pmod q\}.
\]
Removing the zero frequency yields exactly
\[
\boxed{
\sum_{(u,v)\ne(0,0)}|S_P|^2
=q^2C_{q,\omega}-X^2.
}
\]
Hence a frequency-separated large sieve is equivalent to quantitative equidistribution of the reconstructed graph under the two-value map
\[
x\mapsto(L_{\omega,1}(x),L_{\omega,2}(x))\pmod q,
\]
not merely to the already-known root-line occupancy support.

## 4. Why the exact structural locks do not yet bound the operator norm

The facts
\[
q\mid\Delta_x,
\qquad
kg^2\mid\Delta_x,
\]
apply to nodes that are actually occupied at the root target. They do not imply that the full graph values of `(L_1,L_2) mod q` are equidistributed, nor do they control the nonzero Fourier modes of the centered indicator.

Likewise the Stage15-6da Pell completion theorem is a finite-fiber statement after three residuals are fixed. It does not give cancellation when those three residuals vary through a whole packet.

One-dimensional slicing also does not produce an off-the-shelf large-sieve adapter: if `(M,N,U)` are used as the reconstructed base and the `M` phase is isolated, the completion `V` occurring in the second root-line phase varies with `M` and with the survivor branch. Treating the `V` phase as an arbitrary coefficient makes the coefficient sequence depend on `(q,omega,u,v)`, outside the standard fixed-coefficient large-sieve hypothesis. The symmetric slices have the same problem.

Thus the exact operator/dual receiver is now exposed, but no `kappa<1` follows from reconstruction, `kg^2|Delta`, or root-line support alone.

## 5. Measure and quantifier audit

- The graph is formed from exact physical survivors under `R<=B` before characters are introduced.
- `HMNUV<=B` remains only a proved height majorant.
- `(d,e)` and the exact `phi(d)phi(e)` weight are retained throughout.
- The joint zero mode equals the local main density and is removed before any absolute value.
- AR-025 valuation reduction reorganizes nonzero modes only; it does not change the outer graph measure.
- No average over physical packets has been substituted for an every-packet statement.
- `kg`, `q`, cells and completion labels are each charged once.

```text
STAGE15_6_SUBSTAGE=6dp
STAGE15_6DP_CHARACTER_OPERATOR_EXACT=true
STAGE15_6DP_DUAL_INEQUALITY_EXACT=true
STAGE15_6DP_ZERO_MODE_SUBTRACTED_BEFORE_ABSOLUTE=true
STAGE15_6DP_DECORATED_DE_MEASURE_PRESERVED=true
STAGE15_6DP_AR025_VALUATION_REDUCTION_ADAPTER=EXACT_RECOMBINATION_ONLY
STAGE15_6DP_PRIMITIVE_REDUCED_FREQUENCIES=true
STAGE15_6DP_FREQUENCY_SEPARATED_BOUND_IS_STRONGER_THAN_TARGET=true
STAGE15_6DP_FULL_FREQUENCY_ORTHOGONALITY_EXACT=true
STAGE15_6DP_KAPPA_LT_1_PROVED=false
STAGE15_6DP_EXIT=UPDATED_ARSENAL_ADAPTER_AUDIT_READY
```