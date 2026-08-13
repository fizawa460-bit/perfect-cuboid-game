# Stage15-6dm — exact decorated expansion of the centered occupancy second moment

Base: merged Stage15-6dl after fresh audit PASS. Execute the selected `ORIENTATION_BLIND_PAIR_RESULTANT_OCCUPANCY_ENERGY` route on the **centered occupancy second moment itself**.

Keep one exact reconstructed physical graph packet `G(P)` from Stage15-6di. Thus every node retains

- `R<=B` and the exact consequence `HMNUV<=B`;
- the Stage15-6da `B^o(1)` completion decoration;
- both survivor norm equations;
- `kg^2 | Delta_x`, with `Delta_x=m_x^4-n_x^4`;
- all primitive/canonical/exactly-two masks.

For a legal switched **decorated** pair `(d,e)` put
\[
q=de,\qquad \lambda_{d,e}=\varphi(d)\varphi(e),
\qquad \Omega_{d,e}=|\Omega(d,e)|,
\]
with `(q,H_x)=1` on every occupied node. Do not identify two different decompositions `(d,e)` having the same product `q`.

Define
\[
I_{d,e}(x)=1_{d\mid G_S(x)}1_{e\mid G_O(x)},
\qquad
\alpha_{d,e}=\frac{\Omega_{d,e}}{q^2},
\]
\[
N_{d,e}=\sum_{x\in G(P)}I_{d,e}(x),
\qquad
B_{d,e}=N_{d,e}-\alpha_{d,e}|G(P)|.
\]
Then the exact occupancy second moment is
\[
\boxed{
\mathfrak B_P(Q_0)
=\sum_{de\le Q_0}\frac{\lambda_{d,e}}{\Omega_{d,e}}
|B_{d,e}|^2.
}
\]

## 1. Exact centering expansion

Write `X=|G(P)|`. For every decorated `(d,e)`,
\[
B_{d,e}=\sum_{x\in G(P)}(I_{d,e}(x)-\alpha_{d,e}),
\]
so
\[
\boxed{
B_{d,e}^2
=\sum_{x,y\in G(P)}
(I_{d,e}(x)-\alpha_{d,e})
(I_{d,e}(y)-\alpha_{d,e}).
}
\]
Equivalently,
\[
\boxed{
B_{d,e}^2
=\sum_{x,y}I_{d,e}(x)I_{d,e}(y)
-2\alpha_{d,e}X N_{d,e}
+\alpha_{d,e}^2X^2.
}
\]
Therefore
\[
\mathfrak B_P(Q_0)=\mathcal P_P(Q_0)-2\mathcal C_P(Q_0)+\mathcal M_P(Q_0),
\]
where
\[
\mathcal P_P
=\sum_{de\le Q_0}\frac{\lambda_{d,e}}{\Omega_{d,e}}
\sum_{x,y}I_{d,e}(x)I_{d,e}(y),
\]
\[
\mathcal C_P
=X\sum_{de\le Q_0}\frac{\lambda_{d,e}}{q^2}N_{d,e},
\]
\[
\mathcal M_P
=X^2\sum_{de\le Q_0}\lambda_{d,e}\frac{\Omega_{d,e}}{q^4}.
\]
The cross term and main term are part of the theorem target. They may cancel the quadratic main part of `P`; bounding `P`, `C`, and `M` separately by absolute values cannot prove a centered variance theorem.

## 2. Diagonal is harmless at the target scale

The diagonal contribution is
\[
\sum_x(I_{d,e}(x)-\alpha_{d,e})^2.
\]
For fixed `x`, occupied `(d,e)` are divisor pairs of the polynomially bounded exact channel gcds, hence there are `B^o(1)` of them; moreover `lambda<=q<=Q0`. The pure centering tails have convergent/divisor-like `q^{-2}` weights after the `Omega` normalization. Thus
\[
\boxed{
\mathfrak B_{P,\mathrm{diag}}(Q_0)
\ll XQ_0B^{o(1)}.
}
\]
The obstruction to `kappa<1` is off diagonal.

## 3. Exact decorated occupied-pair support

If `I_{d,e}(x)I_{d,e}(y)=1`, then **with the channel assignment retained**
\[
d\mid G_S(x),\quad d\mid G_S(y),
\qquad
e\mid G_O(x),\quad e\mid G_O(y).
\]
In particular
\[
q\mid \Delta_x,\qquad q\mid\Delta_y,
\]
and likewise `q` divides each inner fourth-power difference `r_x^4-s_x^4` and `r_y^4-s_y^4`.

At every odd prime power in `d`, the two S-channel root/sign choices for `x,y` either agree or are opposite; the same is true at every odd prime power in `e` with the S/O roles interchanged. Therefore, with
\[
A_-(x,y)=m_xn_y-m_yn_x,\qquad A_+(x,y)=m_xn_y+m_yn_x,
\]
\[
B_-(x,y)=r_xs_y-r_ys_x,\qquad B_+(x,y)=r_xs_y+r_ys_x,
\]
we have the orientation-blind support lock
\[
\boxed{
q^2\mid \mathcal R(x,y):=A_-A_+B_-B_+.
}
\]
This is only a consequence of occupancy. The stronger decorated information `d|G_S(x),G_S(y)` and `e|G_O(x),G_O(y)` is retained in `I_{d,e}` and is not replaced by the undecorated condition `q^2|R`.

## 4. Interaction with the reconstructed core lock

For every node,
\[
kg^2\mid\Delta_x,
\qquad \gcd(kg,HMNUV)=1.
\]
For an occupied decorated modulus,
\[
q\mid\Delta_x.
\]
These two statements coexist, but Stage15 has proved neither `q|kg` nor `kg|q`. Thus the core square-divisor lock may restrict the same integer `Delta_x`, but it cannot be charged as an additional independent modulus saving.

Exact divisor switching is legal after `(d,e)` is fixed, but it is a reparameterization of the same divisibility event. It must be inserted inside the centered expansion, not used to replace `B_{d,e}^2` by a positive incidence count.

## 5. Precise quantitative target

The target remains: for some `kappa<1`, uniformly over legal physical packets,
\[
\boxed{
\mathfrak B_P(Q_0)
\ll X^{1+\kappa}Q_0B^{o(1)}.
}
\]
By Stage15-6dl this would imply, for `Q0=B^theta`,
\[
\delta<\frac{1-\kappa}{2}-\frac\theta2.
\]
Stage15-6dm has only fixed the exact decorated kernel and the support available to attack it; no `kappa<1` is claimed yet.

```text
STAGE15_6_SUBSTAGE=6dm
STAGE15_6DM_CENTERED_OCCUPANCY_SECOND_MOMENT_EXACT=true
STAGE15_6DM_DECORATED_DE_ASSIGNMENT_PRESERVED=true
STAGE15_6DM_EXACT_PAIR_CROSS_MAIN_EXPANSION=true
STAGE15_6DM_DIAGONAL_BOUND=GRAPH_MASS*Q0*B^o(1)
STAGE15_6DM_OCCUPIED_PAIR_Q2_DIVIDES_ORIENTATION_BLIND_RESULTANT=true
STAGE15_6DM_Q_DIVIDES_BOTH_NODE_DELTAS=true
STAGE15_6DM_KG2_AND_Q_NO_INCLUSION_PROVED=true
STAGE15_6DM_CENTERING_CROSS_TERMS_RETAINED=true
STAGE15_6DM_KAPPA_LT_1_PROVED=false
STAGE15_6DM_EXIT=CENTERED_PAIR_RESULTANT_ENERGY_TEST_READY
```