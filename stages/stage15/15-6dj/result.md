# Stage15-6dj — legal whole-family second moment and collision kernel

Base: Stage15-6di. Keep the graph packet `G(P)`, exact discrepancy
\[
D_{d,e,\omega}(P)=N_{d,e,\omega}(P)-|G(P)|/(de)^2,
\]
and exact weight `lambda(d,e)=phi(d)phi(e)`.

Write `q=de` and `Omega(d,e)` for the legal orientation set.

## 1. Weighted second moment

Define
\[
\mathfrak D_P(Q_0)
:=\sum_{de\le Q_0}\lambda(d,e)
\sum_{\omega\in\Omega(d,e)}
|D_{d,e,\omega}(P)|^2.
\]
Cauchy-Schwarz is applied only after the signed modulus/orientation sum has been formed:
\[
|E_P(Q_0)|^2
\le
\left(\sum_{de\le Q_0}\lambda(d,e)|\Omega(d,e)|\right)
\mathfrak D_P(Q_0).
\]
Since `lambda(d,e)<=de` and the legal orientation multiplicity is divisor-like,
\[
\sum_{de\le Q_0}\lambda(d,e)|\Omega(d,e)|
\ll Q_0^{2+o(1)}.
\]
Therefore
\[
\boxed{|E_P(Q_0)|\ll Q_0^{1+o(1)}\mathfrak D_P(Q_0)^{1/2}.}
\]
This is a legal whole-family dispersion inequality. It does not use a fixed-packet Stage14 exponent.

## 2. Exact pair expansion

For a graph node `x`, put
\[
\psi_{d,e,\omega}(x)
:=1_{x\in C(d,e,\omega)}-(de)^{-2},
\]
where `C(d,e,omega)` is the exact pair of primitive root-line congruences from 6di. Then
\[
D_{d,e,\omega}(P)=\sum_{x\in G(P)}\psi_{d,e,\omega}(x),
\]
and hence
\[
\boxed{
\mathfrak D_P(Q_0)
=\sum_{x,y\in G(P)}K_{Q_0}(x,y),
}
\]
with the signed collision kernel
\[
K_{Q_0}(x,y)
:=\sum_{de\le Q_0}\lambda(d,e)
\sum_{\omega}
\psi_{d,e,\omega}(x)\psi_{d,e,\omega}(y).
\]
Thus the exact missing theorem is a pair-correlation statement on reconstructed graph nodes, not a one-point lattice estimate.

## 3. Same-orientation collision lock

Let
\[
J_1(x,y)=m_xn_y-m_yn_x,
\qquad
J_2(x,y)=r_xs_y-r_ys_x,
\]
and
\[
J(x,y)=\gcd(|J_1(x,y)|,|J_2(x,y)|).
\]
If two nodes lie in the same composite orientation modulo `q=de`, then both toric ratios agree modulo `q`. Therefore
\[
\boxed{q\mid J_1(x,y),\qquad q\mid J_2(x,y),\qquad q\mid J(x,y).}
\]
This implication is exact for every odd switched modulus because `(q,H_xH_y)=1` on the relevant packets; bounded 2-adic conventions remain separate.

Consequently every positive same-orientation off-diagonal collision is supported on a divisor `q` of the explicit pair determinant gcd `J(x,y)`. This is the reconstructed-graph analogue of a large-sieve collision condition.

## 4. Diagonal term

For `x=y`, a fixed `(d,e)` has at most one legal orientation containing `x`. Moreover whenever it contains `x`, necessarily `d|G_S(x), e|G_O(x)`. Truncating at `de<=Q0`,
\[
\sum_{de\le Q_0}\lambda(d,e)
\sum_{\omega}1_{x\in C(d,e,\omega)}
\ll Q_0\,B^{o(1)},
\]
because `lambda(d,e)<=de<=Q0` and the number of divisor pairs of the polynomially bounded channel gcds is `B^{o(1)}`.

The centering terms contribute only smaller divisor-like sums. Hence
\[
\boxed{
\mathfrak D_{P,\mathrm{diag}}(Q_0)
\ll |G(P)|\,Q_0\,B^{o(1)}.
}
\]
This is a genuine improvement over treating all modulus/orientation slots independently.

## 5. Off-diagonal receiver

Define the reconstructed graph collision energy
\[
\mathcal C_P(Q_0)
:=\sum_{\substack{x,y\in G(P)\\x\ne y}}
\sum_{\substack{de\le Q_0\\de\mid J(x,y)}}
\lambda(d,e)\,B^{o(1)}.
\]
The exact signed kernel satisfies the safe majorant
\[
\boxed{
\mathfrak D_P(Q_0)
\ll |G(P)|Q_0B^{o(1)}+\mathcal C_P(Q_0)
+\text{centered main-density terms}.
}
\]
The centered main-density terms are explicit lower-order `q^{-2}`/`q^{-4}` sums and do not create a new polynomial loss. The only possible fixed-power obstruction is therefore the off-diagonal graph collision energy.

No claim is made that `C_P(Q0)` already has square-root size. Taking absolute values pairwise before this stage would destroy the dispersion mechanism; the signed kernel is the primary object.

## 6. Quantitative implication if graph collision is square-root scale

The natural whole-family target is
\[
\boxed{
\mathcal C_P(Q_0)\ll |G(P)|Q_0B^{o(1)}.
}
\]
Under that target,
\[
\mathfrak D_P(Q_0)\ll |G(P)|Q_0B^{o(1)},
\]
so
\[
|E_P(Q_0)|
\ll |G(P)|^{1/2}Q_0^{3/2}B^{o(1)}.
\]
For the physical reconstructed graph, the ambient packet mass sums to at most `B^{1+o(1)}`. Thus, if the packet estimates can be summed with no polynomial packet loss and `Q_0=B^theta`, this becomes
\[
E(Q_0)\ll B^{1/2+3\theta/2+o(1)}.
\]
Relative to the small-range target `B^{1-delta+o(1)}Q_0`, this would permit
\[
\boxed{\delta<\frac12-\frac\theta2}
\]
for every `theta<1`.

This is **conditional only**. The collision-energy estimate has not yet been proved.

```text
STAGE15_6_SUBSTAGE=6dj
STAGE15_6DJ_WHOLE_FAMILY_SECOND_MOMENT_DEFINED=true
STAGE15_6DJ_DISPERSION_INEQUALITY=E<=Q0^(1+o(1))*D^(1/2)
STAGE15_6DJ_PAIR_KERNEL_EXACT=true
STAGE15_6DJ_SAME_ORIENTATION_COLLISION_IMPLIES_Q_DIVIDES_J=true
STAGE15_6DJ_DIAGONAL_BOUND=GRAPH_MASS*Q0*B^o(1)
STAGE15_6DJ_OFFDIAGONAL_COLLISION_ENERGY_DEFINED=true
STAGE15_6DJ_SQRT_COLLISION_TARGET_PROVED=false
STAGE15_6DJ_CONDITIONAL_DELTA=1/2-theta/2
STAGE15_6DJ_NO_STAGE14_EXPONENT_TRANSFER=true
STAGE15_6DJ_EXIT=GRAPH_COLLISION_ENERGY_TEST_READY
```