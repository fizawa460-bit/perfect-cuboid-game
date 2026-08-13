# Stage15-6dj — repaired orientation-mean decomposition and occupancy gate

Base: Stage15-6di. Fresh audit returned FIX_REQUIRED because the prior second-moment discussion treated same-orientation collision energy as if it were the only obstruction. The exact orientation mean must be separated first.

Keep one legal graph packet `G(P)`, switched modulus `q=de`, exact weight
\[
\lambda(d,e)=\varphi(d)\varphi(e),
\]
legal orientation set `Omega_q` of size `\Omega=|Omega_q|`, and
\[
N_\omega:=N_{d,e,\omega}(P),\qquad
N_{\rm tot}:=\sum_{\omega\in\Omega_q}N_\omega,
\qquad A_q:=\frac{|G(P)|}{q^2}.
\]
Put
\[
\bar N_q:=\frac{N_{\rm tot}}{\Omega}.
\]

## 1. Exact orientation-mean decomposition

For every fixed switched modulus,
\[
\boxed{
\sum_{\omega\in\Omega_q}(N_\omega-A_q)^2
=
\sum_{\omega\in\Omega_q}(N_\omega-\bar N_q)^2
+\Omega(\bar N_q-A_q)^2.
}
\]
Equivalently,
\[
\boxed{
\sum_{\omega}(N_\omega-A_q)^2
=V_q+\frac{B_q^2}{\Omega},
}
\]
where
\[
V_q:=\sum_{\omega}(N_\omega-\bar N_q)^2,
\qquad
B_q:=N_{\rm tot}-\Omega\frac{|G(P)|}{q^2}.
\]
The first term is **orientation variance**. The second is **modulus occupancy bias**.

Thus the weighted second moment decomposes exactly as
\[
\mathfrak D_P(Q_0)
=\mathfrak V_P(Q_0)+\mathfrak B_P(Q_0),
\]
with
\[
\mathfrak V_P(Q_0)
:=\sum_{de\le Q_0}\lambda(d,e)V_{de},
\]
\[
\boxed{
\mathfrak B_P(Q_0)
:=\sum_{de\le Q_0}
\frac{\lambda(d,e)}{\Omega(d,e)}
\left|N_{d,e}(P)-\frac{\Omega(d,e)}{(de)^2}|G(P)|\right|^2.
}
\]
No term is discarded.

## 2. The signed small-range error depends directly on occupancy, not orientation variance

The exact discrepancy sum from 6di is
\[
E_P(Q_0)
=\sum_{de\le Q_0}\lambda(d,e)
\sum_{\omega}(N_\omega-A_q).
\]
But
\[
\sum_{\omega}(N_\omega-A_q)
=N_{\rm tot}-\Omega A_q=B_q.
\]
Therefore
\[
\boxed{
E_P(Q_0)=\sum_{de\le Q_0}\lambda(d,e)B_{de}.
}
\]
In particular orientation fluctuations around their own mean cancel from the signed orientation sum. This is the correction to the previous 6dj implication.

Cauchy-Schwarz now gives the exact occupancy-based dispersion inequality
\[
|E_P(Q_0)|^2
\le
\left(\sum_{de\le Q_0}\lambda(d,e)\Omega(d,e)\right)
\mathfrak B_P(Q_0).
\]
Since the first factor is `Q0^{2+o(1)}`,
\[
\boxed{
|E_P(Q_0)|\ll Q_0^{1+o(1)}\mathfrak B_P(Q_0)^{1/2}.
}
\]
Thus a positive small-side exponent requires control of **occupancy bias**. A square-root orientation-collision theorem alone is insufficient.

## 3. Pair-collision energy belongs only to the orientation-variance term

For fixed `q`,
\[
V_q
=\sum_{\omega}N_\omega^2-\frac{N_{\rm tot}^2}{\Omega}.
\]
Expanding `N_omega^2` gives pairs lying in the same legal orientation. For
\[
J_1(x,y)=m_xn_y-m_yn_x,
\qquad
J_2(x,y)=r_xs_y-r_ys_x,
\]
same orientation still implies
\[
q\mid J_1(x,y),\qquad q\mid J_2(x,y).
\]
Hence the reconstructed-graph pair-collision energy from the previous draft is a legal receiver for `mathfrak V_P(Q0)` only.

This collision theorem may remain useful for finer orientation distribution, but it cannot by itself bound `E_P(Q0)` because `E_P` is the occupancy residual.

## 4. Exact occupancy indicator

Define
\[
I_{d,e}(x)
:=1_{d\mid G_S(x)}1_{e\mid G_O(x)}.
\]
Every occupied node has exactly one legal orientation, so
\[
N_{d,e}(P)=\sum_{x\in G(P)}I_{d,e}(x).
\]
The expected occupancy attached to the ambient root-line density is
\[
\mu_{d,e}:=\frac{\Omega(d,e)}{(de)^2}.
\]
Therefore
\[
\boxed{
B_{d,e}=\sum_{x\in G(P)}(I_{d,e}(x)-\mu_{d,e}).
}
\]
The occupancy second moment has its own exact pair kernel:
\[
\boxed{
\mathfrak B_P(Q_0)
=\sum_{x,y\in G(P)}
\sum_{de\le Q_0}
\frac{\lambda(d,e)}{\Omega(d,e)}
(I_{d,e}(x)-\mu_{d,e})(I_{d,e}(y)-\mu_{d,e}).
}
\]
This is the actual whole-family theorem gate after the audit repair.

## 5. Corrected conditional implication

If, and only if, one proves the occupancy target
\[
\boxed{
\mathfrak B_P(Q_0)
\ll |G(P)|Q_0B^{o(1)},
}
\]
then
\[
|E_P(Q_0)|
\ll |G(P)|^{1/2}Q_0^{3/2}B^{o(1)}.
\]
After packet summation with no polynomial loss and `Q0=B^theta`, this conditionally yields
\[
E(Q_0)\ll B^{1/2+3\theta/2+o(1)},
\]
so the previous numerical window
\[
0<\delta<\frac12-\frac\theta2
\]
remains valid **only under the occupancy second-moment target**, not under the orientation-collision target alone.

```text
STAGE15_6_SUBSTAGE=6dj
STAGE15_6DJ_ORIENTATION_MEAN_DECOMPOSITION_EXACT=true
STAGE15_6DJ_ORIENTATION_VARIANCE_TERM_DEFINED=true
STAGE15_6DJ_MODULUS_OCCUPANCY_BIAS_TERM_DEFINED=true
STAGE15_6DJ_SIGNED_ERROR_EQUALS_OCCUPANCY_RESIDUAL=true
STAGE15_6DJ_COLLISION_ENERGY_CONTROLS_ORIENTATION_VARIANCE_ONLY=true
STAGE15_6DJ_SQRT_COLLISION_ALONE_IMPLIES_DELTA=false
STAGE15_6DJ_OCCUPANCY_PAIR_KERNEL_EXACT=true
STAGE15_6DJ_OCCUPANCY_SQRT_TARGET_PROVED=false
STAGE15_6DJ_CONDITIONAL_DELTA_UNDER_OCCUPANCY_TARGET=1/2-theta/2
STAGE15_6DJ_NO_STAGE14_EXPONENT_TRANSFER=true
STAGE15_6DJ_EXIT=MODULUS_OCCUPANCY_BIAS_GATE_READY
```