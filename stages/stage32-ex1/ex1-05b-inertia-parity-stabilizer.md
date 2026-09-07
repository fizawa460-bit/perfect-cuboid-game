# EX1-05B — local inertia parity and component stabilizer refinement

Status: provisional same-PR candidate. No hostile-audit, Stage32 MAIN, endpoint, or merge credit is granted here.

## 1. Inputs retained from EX1-05A

For a hypothetical integral irreducible V6 carrier with normalization `N` of genus `1`, let `D -> N` be the normalized pullback of the Stoll--Testa double cover `Y -> Sbar`.

EX1-05A gives

- `K.V6 = 186`;
- `deg Ram(D/N) >= 186`;
- the 48 exceptional contacts `m_i` have positive support `47` and sum `266`;
- for the strict transform `Gamma` on the minimal resolution, if
  `nu^*E_i = sum_j a_ij q_ij`, then `r_i=#j <= m_i=sum_j a_ij`.

The remaining task is to identify which normalization branches actually ramify in `D -> N`.

## 2. Exact A1 parity adapter

At a box-surface node use the source-locked quotient model

`A1 = Spec C[x,y,z]/(xz-y^2) = C^2/{+-1}`

with

`x=u^2, y=uv, z=v^2`.

On a standard chart of the minimal resolution write

`x=s, y=s t, z=s t^2`,

so `E:{s=0}` is the exceptional curve. Blow up `C^2` at the origin and use the chart `v=u t`. The quotient by `u -> -u` is precisely the resolution chart above with

`s=u^2`.

Thus the normalized pullback of the local double cover to the resolution is the degree-two cover

`u^2=s`,

branched along `E`.

Now let a normalization branch of `Gamma` meet `E` with local contact order

`a = ord_tau(s)`.

After removing a square unit, the induced cover on the branch is

`w^2 = tau^a`.

Therefore:

- `a` odd: one point above the branch parameter, ramification index `2`, ramification contribution `1`;
- `a` even: after normalization the cover is locally split/unramified over `C`.

If

`q_i := #{j : a_ij is odd}`,

then exactly

`deg Ram(D/N) = Q := sum_i q_i`,

and

`q_i == m_i (mod 2)`, `0 <= q_i <= r_i <= m_i`.

Also

`m_i-q_i = 2 sum_j floor(a_ij/2)`.

This is a local-cover invariant. It is not a delta invariant.

## 3. Global parity consequences for the exact V6 contacts

The exact V6 pairing list has:

- 26 positive odd pairings, with total odd-pairing mass `140`;
- 21 positive even pairings, with total even-pairing mass `126`;
- one zero pairing.

Every odd `m_i` forces `q_i>=1`, hence all 26 odd-pairing nodes carry ramification.

But `Q>=186`, while all odd-pairing nodes together can contribute at most `140`. Therefore the even-pairing nodes must contribute at least `46` ramified branches.

The three largest positive even contact masses sum to only `38`; the four largest sum to `48`. Hence ramification must occur at at least **four even-contact nodes**. Since `q_i` is even on an even-contact node, positive ramification there has `q_i>=2`, so such a node is automatically multibranch.

Thus at least

`26+4 = 30`

of the 47 met surface nodes carry ramified normalization branches.

For a sharper multibranch count, start from the unibranch parity baseline `q_i=m_i mod 2`, whose global sum is `26`. Turning a nonunit node multibranch can increase `q_i` by at most

`m_i-(m_i mod 2)`.

To reach `Q>=186` requires extra capacity at least `160`. The 14 largest such capacities sum to `152`, while the 15 largest sum to `160`. Therefore at least **15 nonunit nodes are multibranch**. This improves EX1-05A's lower bound `14 -> 15`.

## 4. Forty-one-state slack compression

Because `Q` is even and `186<=Q<=266`, write

`Q = 186 + 2s`, `0<=s<=40`.

Then

`H_contact := (266-Q)/2 = 40-s = sum_{i,j} floor(a_ij/2)`.

So at most `40-s` normalization branches can have contact order `>=2`. Consequently at least

`Q-(40-s) = 146+3s`

branches are simple contact `a_ij=1`.

This compresses the remaining contact/ramification profiles into 41 integer slack states before the finer per-node partition data are applied.

## 5. Component stabilizer in the etale V4 cover

Stoll--Testa gives the even-sign subgroup `G0+` of order four and the smooth quotient

`P: X x X -> Y=(X x X)/diag(G0+)`.

Since `X/G0+` has genus `2`, Riemann--Hurwitz gives

`2g(X)-2 = 8 = 4(2*2-2)`,

so `G0+` acts freely on `X`. Hence `P` is etale.

Pull `P` back to the connected curve `D`. Choose one connected component `Ctilde` and let `H<=G0+` be its stabilizer. Put

`h=|H|=deg(Ctilde->D) in {1,2,4}`.

Let `alpha,beta` be the degrees of the two projections `Ctilde->X`. Since `deg K_X=8` and `K_Y.D=372`, projection formula gives

`8(alpha+beta)=372h`,

or

`2(alpha+beta)=93h`.

The left side is even and `93` is odd, so **h must be even**. Therefore

`h in {2,4}`

and the trivial-stabilizer / four-component branch `h=1` is excluded.

### h=2

A nontrivial subgroup `H<=G0+` acts freely on `X`, and `X/H` has genus `3`. The two projections descend to maps from `D` to genus-3 curves of degrees `alpha,beta`, with

`alpha+beta=93`.

Riemann--Hurwitz gives

`Q=2g(D)-2 >= 4 max(alpha,beta) >= 188`.

Thus `h=2` forces `s>=1`.

### h=4

Here `H=G0+`; the descended targets are the genus-2 quotient `C2=X/G0+`. We recover

`alpha+beta=186`, `Q>=2 max(alpha,beta)>=186`.

The boundary `s=0` (`Q=186`) is therefore extremely rigid: `alpha=beta=93`, and both projections `D->C2` are etale.

In either stabilizer case, if `R1,R2` are the ramification degrees of the two descended projection maps, then

`R1+R2 = 2Q-372 = 4s`.

So the same slack `s` measures how far the product projections are from the extremal unramified boundary, while `40-s` measures the remaining higher-contact budget.

## 6. Three inertia types among the 48 nodes

In the Stoll--Testa model

`X: u^2=2xy, v^2=x^2-y^2, w^2=x^2+y^2`,

`G0=(Z/2)^3` changes signs of `u,v,w`.

Each single-sign involution has exactly 8 fixed points on `X`:

- `u`-sign: `u=0`, hence `xy=0`, giving 4 points with `x=0` and 4 with `y=0`;
- analogously the `v`-sign and `w`-sign each have 8 fixed points.

The triple-sign involution has no projective fixed point. Fixed sets of two different single-sign involutions are disjoint because their product lies in the free even-sign subgroup.

For each single-sign type, the diagonal action on `X x X` fixes `8*8=64` pairs. Their stabilizer has order 2, so each `G0` orbit has size `8/2=4`; hence they produce `64/4=16` quotient nodes. Thus the 48 A1 nodes split exactly into

`16 u-inertia + 16 v-inertia + 16 w-inertia`.

The retained EXC ordering used by the V6 pairing vector is not yet mapped to these three inertia classes. No ordering guess is made here.

## 7. Why the EXC-to-inertia adapter is the next gate

Consider a connected component of the full `G0` pullback. Ramified local inertia elements must lie in its stabilizer subgroup.

If `h=2`, the full component stabilizer has order 4 and intersects `G0+` in `H`; therefore its odd elements contain at most two of the three single-sign inertia types. So the `h=2` branch can be tested by summing the V6 odd-contact capacity on the exact allowed inertia classes and comparing it to the required `Q>=188`.

That test is not legal until the retained 48 EXC labels are mapped exactly to the three 16-node inertia classes. This is the next bounded subroute:

`EX1-05C_EXC_NODE_INERTIA_TYPE_ADAPTER_AND_CAPACITY_TEST`.

## Credit firewall

This leaf establishes only candidate-level branch exclusions/refinements:

- `h=1` is excluded;
- at least 30 met nodes ramify;
- at least 15 nonunit nodes are multibranch;
- the residual profiles are compressed by the integer `s in [0,40]`.

It does **not** identify ramification/contact data with `delta=472`, does not exclude `h=2` without the EXC inertia adapter, does not construct a V6 member, and does not close Stage32EX1.