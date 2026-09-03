# Stage32 post-1490 — equivariant Beauville deck-cross adapter on the exact V6 class

## Scope

This note is restricted to the fixed recovered V6 class `g1-d186`, `z=(-15,62,-44,26,32)`, with `O=210`, `q'=4`. It uses the already locked conditional carrier interpretation: if an integral genus-one carrier exists in this exact resolved-box class, its connected Beauville pullback gives the X-side divisor `D` used in the V4 defect decomposition.

No arbitrary B-side Picard64 class is promoted to `Pic(X)`. The only B-side class used below is the exact recovered V6 class, reconstructed from its locked all-140 intersection vector.

## Equivariance of the quotient square

Let

- `P = X(8) x X(8)`,
- `H = Gamma'[4]/Gamma[8]`,
- `G = Gamma[4]/Gamma[8]`, with `H` of index two in `G`,
- `X = P/H_diag`,
- `B = P/G_diag`.

The Beauville map `pi:X->B` is the quotient induced by `H_diag subset G_diag`. For `h in H`, the deck transformation used by

`q:X -> P/(H x H) = C0 x C0`

is represented by `(h,1)`. The relevant mod-8 group is elementary abelian, so `(h,1)` normalizes both diagonal quotient groups and induces an automorphism `bar t_h` of `B`. On quotient classes one has identically

`pi(t_h([x,y]_{H_diag})) = [hx,y]_{G_diag} = bar t_h(pi([x,y]_{H_diag}))`.

Thus

`pi o t_h = bar t_h o pi`.

The same square remains equivariant after blowing up the 48 distinguished X points and the corresponding 48 B nodes, because the actions permute these centers. Write the resolved map as `pi_tilde:Xtilde->Btilde`.

The existing relative-H source lock identifies the three nonidentity first-factor elements globally in Stoll's box-surface automorphism generators:

- `u = g7*g9`,
- `v = g7*g8`,
- `uv = g8*g9`.

The theta-transformation/box-coordinate identification is the same one already used to source-lock the 48-node permutations. Here the retained 140-class automorphism interface is additionally used on `Pic(Btilde)`: the primitive INDLIST reconstruction verifies that each composite transports all 140 known classes exactly and preserves the retained intersection Gram matrix.

## Bilinear blow-up / pullback formula

For the hypothetical exact-V6 carrier class `C` on `Btilde`, the already locked Beauville adapter gives

`Dtilde = pi_tilde^* C`.

Equivariance gives

`t(Dtilde) = pi_tilde^*(bar t(C))`.

Projection formula for the finite degree-two map therefore gives

`Dtilde . t(Dtilde) = 2 * C . bar t(C)`.

Let `beta:Xtilde->X` be the blow-down and let `m_j` be the multiplicity of `D` at the j-th blown-up point. The previously locked local adapter identifies these multiplicities with the exact recovered V6 exceptional pairings. Polarizing the standard blow-up intersection identity gives

`D . t(D) = Dtilde . t(Dtilde) + sum_j m_j m_{t(j)}`,

because the three nonidentity actions are involutions. Hence the exact equivariant cross formula is

`D . t(D) = 2 * C . bar t(C) + sum_j m_j m_{t(j)}`.

For `t=1` this specializes to the already certified self formula

`D^2 = 2 C^2 + sum_j m_j^2 = 3874`,

so the cross formula uses exactly the same strict-transform convention and exceptional sign.

## Exact recovered-class arithmetic

The exact V6 all-140 pairing vector determines the class uniquely in the primitive 64-element INDLIST basis. Solving `b = C G` exactly gives an integral coordinate row, replays all 140 pairings, and has self-square `758`.

Applying the three source-locked composite Picard actions gives

| t | `C.bar t(C)` | `sum m_j m_{t(j)}` | `D.t(D)` | `c_t=D.t(D)/2` |
|---|---:|---:|---:|---:|
| `u` | 1266 | 1360 | 3892 | 1946 |
| `v` | 1112 | 1796 | 4020 | 2010 |
| `uv` | 1284 | 1452 | 4020 | 2010 |

Thus

`sum_{t!=1} D.t(D) = 11932`,

or equivalently

`c_u+c_v+c_uv = 5966`.

## Contradiction with the independent X-side defect identity

The independently source-locked V4 deck-translate defect decomposition on the same X-side divisor says

`sum_{t!=1} D.t(D) = 17172 - 2*delta_D`.

The exact Beauville self adapter already fixed `delta_D=2018`, so the required sum is

`17172 - 4036 = 13136`,

or equivalently

`c_u+c_v+c_uv = 6568`.

The two exact values differ by

`13136 - 11932 = 1204`

in the full intersections, i.e. by `602` in the half-intersection sum. Therefore the hypothetical carrier assumptions for `O=210`, `q'=4` in the exact recovered V6 class are inconsistent.

## Decision and firewalls

- `O=210`, `q'=4` is excluded for the exact recovered V6 class, conditional only on the same carrier-to-class binding already used by the certified Beauville self adapter.
- This is not an effectivity proof; it is an exclusion by contradiction of a hypothetical effective integral carrier in that class.
- No post-21bl representative sample is substituted for the exact recovered V6 class.
- No arbitrary B-side class is identified with an X-side class; the transfer is through the explicit equivariant pullback/strict-transform formula above.
- No FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit follows from this fixed-class exclusion alone.
