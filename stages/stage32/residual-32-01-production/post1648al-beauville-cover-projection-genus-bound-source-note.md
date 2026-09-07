# Stage32 post1648AL — Beauville-cover projection/genus lower bound

Scratch-only proof adapter. It gives necessary conditions for a hypothetical integral geometric-genus-1 V6 carrier; it does not materialize or exclude such a carrier and grants no MAIN theorem/receiver/route/endpoint credit.

## Parent retained leaves

- post1648AJ exact scratch head: `ba2fdb2644938cb398a064449bec27b472e2864d`
- AJ canonical: `499cae84c4f945f38fa75bbb93f4b65c259f56f383c1be2a304b1a3f057fd7f7`
- AJ proves that a hypothetical V6 carrier must have at least `47` FSM-minimal `(4,4)` branches over the box-surface nodes.
- post1648AK bounded-wall head: `66ea87f15abdf4177aee3a778192c489cff2c9fa`
- AK canonical: `242c2702505b0839901b329b3dbed09b8f652f4814a3758a5e1ca00ed5333c30`
- AK dedicated CI: run `34081865302`, job `101618534153`, SUCCESS.

## Primary source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691, DOI `10.1307/mmj/1480734014`.

Author preprint:
`https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`

Exact source locators used here:

- §2, printed p. 8: the compact modular curve `C8 = H*/Gamma[8]` has genus `5`;
- §3, printed p. 10: for a curve in the box variety, projective degree `d` equals canonical intersection on the minimal resolution;
- §4, Lemma 4.1, printed p. 12: `H = Gamma'[4]/Gamma[8] ~= (Z/2)^2` acts freely on `C8`;
- §4, printed pp. 12–13:
  `X=(C8 x C8)/H_diag` is nonsingular, `X -> B` is a two-fold cover, locally at a box node it is `C^2 -> C^2/{+/-1}`, and after blowing up the induced map `Xtilde -> Btilde` is ramified along all 48 exceptional lines.

The following deductions are proof adapters from these source-locked statements, not separately quoted theorems of Freitag–Salvati Manni.

## Genus-two factor quotient

Let `Y=C8/H`. Since `H` has order 4 and acts freely on the genus-5 curve `C8`, Riemann–Hurwitz gives

`2*5-2 = 4*(2*g(Y)-2)`,

hence

`g(Y)=2`.

The diagonal quotient defining `X` has two natural maps

`f1,f2 : X -> Y`

induced by the two factor projections.

Let `rho:C8->Y` and `q:C8 x C8 -> X`. Both are etale. Pulling canonical divisors back by `q` gives the numerical identity

`K_X = f1^* K_Y + f2^* K_Y`.

## Lift of a hypothetical V6 carrier

Assume an integral V6 carrier `C subset B` exists with normalization `Cbar`, geometric genus `1`, and projective degree

`d=186`.

Pull `Cbar -> Btilde` back along the resolved Beauville cover `Xtilde -> Btilde` and normalize. Denote the resulting degree-two cover by

`Dbar -> Cbar`.

Locally the resolved double cover has equation `u^2=s_E` along an exceptional divisor `E`. If a branch of `Cbar` has local intersection multiplicity `m` with `E`, its pulled-back double cover is ramified exactly when `m` is odd.

AJ requires at least 47 minimal `(4,4)` branches, each of exceptional intersection multiplicity `1`. Thus the induced double cover is ramified, hence connected.

Let

`n_i = deg(Dbar -> X -> Y)`.

Because `X -> B` is degree two and quasi-etale in codimension one,

`K_X . pi^*C = 2*(K_B.C)=2d`.

On the other hand `deg(K_Y)=2` and the canonical decomposition above gives

`K_X . pi^*C = 2*n_1 + 2*n_2`.

Therefore

`n_1+n_2=d=186`.

In particular `max(n_1,n_2)>=93`.

## Riemann–Hurwitz lower bound

Let `r` be the number of ramification points of the connected double cover `Dbar -> Cbar`. Since `g(Cbar)=1`,

`2*g(Dbar)-2 = r`.

For every positive-degree projection `Dbar -> Y` of degree `n_i`, Riemann–Hurwitz gives

`2*g(Dbar)-2 >= n_i*(2*g(Y)-2)=2*n_i`.

If one projection were constant, the other would have degree 186 and the same inequality would force `r>=372`; this is already impossible because the total exceptional mass is only 266. Hence both projections are nonconstant.

Using `max(n_i)>=93` gives

`r>=186`.

Every ramification point lies over an exceptional divisor and consumes at least one unit of exceptional intersection. The exact V6 exceptional mass is `266`, so

`186 <= r <= 266`.

Consequently

`94 <= g(Dbar) <= 134`

and, since `r>=2*n_i`,

`53 <= n_1,n_2 <= 133`.

Most importantly, the total number of normalization preimages of the 47 met box nodes is at least `r`, hence at least

`186`.

This is branch excess at least

`186-47=139`.

## Parity-refined multibranch-node bound

At a met node with total exceptional mass `m_i`, if the carrier is unibranch then its contribution to the ramification count is at most `m_i mod 2`: one ramification point when `m_i` is odd, zero when it is even.

If the node is allowed to be multibranch, the maximum possible number of odd local intersection parts is `m_i` (all parts equal to one). Thus changing node `i` from unibranch to multibranch increases ramification capacity by at most

`m_i-(m_i mod 2)`.

For the exact V6 vector there are `26` odd masses. The 14 largest capacity increments sum to `152`, so with at most 14 multibranch nodes

`r <= 26+152=178 < 186`.

The 15 largest increments sum to `160`, reaching capacity `186`.

Therefore any hypothetical integral geometric-genus-1 V6 carrier must be multibranch over at least

`15`

distinct met box-surface nodes.

This is a necessary condition only. It neither asserts that a 15-node pattern exists nor that the ramification lower bound is attainable.

## Exact conclusion and next interface

The Beauville-cover adapter strengthens AJ from

- normalization preimages `>=72` to `>=186`;
- branch excess `>=25` to `>=139`;
- distinct multibranch surface nodes `>=3` to `>=15`.

No V6 carrier is excluded by this leaf. `Q602` and `O210` remain open.

The highest-value next interface is to source-lock the two individual Beauville projection degrees `n1,n2` from retained Picard/fibration data. Since `r<=266` forces both into `[53,133]`, an exact V6 projection degree outside that interval would exclude the carrier.
