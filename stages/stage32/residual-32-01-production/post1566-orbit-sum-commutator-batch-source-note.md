# Stage32 post-1566 orbit-sum / correspondence-commutator batch — hostile-audit repair

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, `Q=602`, after hostile-re-audited and merged #1566.

This repair addresses exactly the Route C blocker from hostile audit on #1570. The previous argument passed from a downstairs numerical class to a strict-transform class on the 48-point resolution without controlling exceptional multiplicities. That bridge is withdrawn. No equality of strict transforms and no invariance of an exceptional multiplicity vector is used below.

The replacement works directly on the blow-down numerical Neron-Severi space by quotienting the resolved 64-dimensional numerical Picard space by the exact span of the 48 exceptional classes.

## Route A — current-main reconstruction of the H-orbit-sum class

The retained exact V6 witness supplies the all-140 intersection vector of the resolved box-surface class `C`. The hostile-audited relative-H adapter gives

- `u = g7*g9`,
- `v = g7*g8`,
- `uv = g8*g9`

inside the source-locked nine-generator Stoll action on all 140 classes.

The current-main diagnostic reconstructs the full retained Stoll group of order `1536`, the H subgroup of order `4`, and

`S_B = C + uC + vC + uvC`.

On the resolved numerical Picard space the full stabilizer of `S_B` in Stoll1536 is exactly

`H = {1, g7*g8, g7*g9, g8*g9}`.

Historical unmerged PR #1547 is not used as authority; the calculation is rerun from current retained data.

## Route B — consume #1566

Merged #1566 proves

`Aut(B) = retained_Stoll_1536`

and places the principal-b3 box automorphism `beta_B` in this group but outside H.

This alone proves resolved-class noninvariance. For Route C, however, the hostile audit correctly requires a statement on the blow-down numerical class rather than an uncontrolled strict transform. That is supplied next.

## Route C — hostile-audit repair on blow-down N^1(B)

### C1. Exact exceptional quotient

The retained marked-node source lock identifies the 48 exceptional curves of the box-surface resolution as known classes

`E_93, E_94, ..., E_140`.

The primitive 64-dimensional INDLIST lattice and Gram matrix are reconstructed by the retained Picard helper. The V6 class is recovered from its all-140 pairings, then checked by exact self-square `758` and replay of all 140 pairings.

Every one of the nine retained Stoll generators preserves the set `{93,...,140}`. The exact rational row span of the 48 exceptional classes has rank `48`. Therefore the numerical blow-down quotient used here is

`N^1(resolved B)_Q / <E_93,...,E_140>_Q`

of rank `64-48=16`.

For every `g` in the complete Stoll group of order 1536, the diagnostic tests

`g(S_B)-S_B in <E_93,...,E_140>_Q`.

This is exactly the criterion that `g` fixes the blow-down numerical class of `S_B`.

The complete stabilizer in the quotient again has order four and is exactly

`{1, g7*g8, g7*g9, g8*g9}=H`,

with outside-H stabilizer count zero.

Hence, because #1566 gives `beta_B in Stoll1536` and `beta_B notin H`,

`beta_B^*[S_B] != [S_B] in N^1(B)_Q`.

This is the replacement for the failed strict-transform step. It does not assume that total exceptional multiplicities are beta-invariant and does not use a strict-transform equality.

### C2. Transport from Gamma without strict transforms

The retained quotient square is

- `P = X(8) x X(8)`,
- `X = P/H_diag`,
- `B = P/G_diag`,
- `Q = P/(H x H) = C0 x C0`,
- `pi:X->B`,
- `q:X->Q`.

The retained common-double-cover certificate gives `H` normal of index two in `G` and identifies `X` as the normalization of the degree-two pullback over `B`. Thus `pi:X->B` is finite surjective of generic degree two on the retained normalization level. On numerical divisor classes over Q,

`pi_* pi^* = 2 id`,

so

`pi^*:N^1(B)_Q -> N^1(X)_Q`

is injective.

For a hypothetical actual carrier in the exact V6 class, the retained exact identity is

`q^*Gamma = D + uD + vD + uvD`.

At the blow-down numerical level, the four H-translates are the pullbacks of the four B-side translates of the exact V6 class, hence

`[q^*Gamma] = pi^*[S_B] in N^1(X)_Q`.

This statement is made before any 48-point resolution; no `Dtilde` or exceptional correction is used.

Merged #1556 supplies compatible automorphisms `beta_X` and `beta_B` with

`pi o beta_X = beta_B o pi`,

and the same principal-b3 lift gives

`q o beta_X = (b3 x b3) o q`.

Assume for contradiction

`(b3 x b3)^*[Gamma]=[Gamma] in NS(Q)`.

Pulling back by q and using q-equivariance gives beta_X-invariance of `[q^*Gamma]`. Using the blow-down identity above and pi-equivariance gives

`pi^*(beta_B^*[S_B]-[S_B])=0`.

Injectivity of `pi^*` forces

`beta_B^*[S_B]=[S_B] in N^1(B)_Q`,

contradicting C1. Therefore, conditional on existence of the exact carrier/correspondence,

`(b3 x b3)^*[Gamma] != [Gamma]`.

No injectivity of q-pullback is used. The only reverse pullback step is the source-bound degree-two injectivity of `pi^*`.

## Route D — correspondence class to Jacobian commutator

External source lock:

Igor Dolgachev and Yuri G. Zarhin, *Endomorphisms of Complex Abelian Varieties*, April 8, 2025, Chapter 10 §10.1, official University of Michigan lecture notes.

Exact facts used:

1. Equation (10.2) identifies `Corr(C)=NS(C x C)/T`, with T generated by the two fibral classes, with `End(J(C))`.
2. Composition gives the ring structure.
3. Factor switch corresponds to Rosati.
4. A correspondence has valence nu exactly when its induced Jacobian endomorphism is `[-nu]`.

For an automorphism `a` of C, diagonal transport `(a x a)^*Gamma` induces conjugation of the associated Jacobian endomorphism, up to the harmless inverse convention from pull/push orientation.

The two fibral classes are fixed by `(b3 x b3)`. Also Gamma and its diagonal-b3 transform have the same bidegree `(105,81)`, so their difference has bidegree `(0,0)`. A nonzero fibral combination cannot have bidegree `(0,0)`. Thus the nonzero Neron-Severi difference from repaired Route C remains nonzero in `Corr(C0)`.

Therefore, under the same exact-carrier/correspondence conditionality,

`[T,b3] != 0`.

This is not an existence statement.

## Route E — valence/scalarity lane

A valence-nu correspondence induces `T=[-nu]`, hence is scalar and commutes with b3. Repaired Route C plus Route D proves the opposite for any hypothetical exact-V6 O210 correspondence. Therefore such a correspondence, if it exists, is neither of valence nor scalar.

The former #1522 conditional route cannot be promoted to Q602 exclusion: its valence premise is refuted for the exact hypothetical correspondence.

## Route F — Q602 firewall

The hostile-audited post1532 certificate leaves exactly residues `73,97,235` at Q602, and all three have nonzero principal-b3 commutator modulo 2. Therefore actual noncommutation is compatible with every retained Q602 residue.

Do not infer Q602 or O210 exclusion.

## Hostile-audit repair invariants

The repaired certificate/certifier must enforce all of the following:

- exceptional labels exactly `93..140`;
- exceptional curve count `48`;
- exceptional span rank over Q `48`;
- blow-down quotient rank `16`;
- resolved stabilizer exactly H;
- blow-down stabilizer exactly H;
- outside-H blow-down stabilizer count `0`;
- `beta_B` is in Stoll1536 and outside H;
- strict-transform bridge is not used;
- exceptional multiplicity invariance is not assumed;
- the blow-down N^1 route is used.

## Firewalls

Do not infer:

- existence or nonexistence of the exact carrier;
- unconditional existence of Gamma;
- `Q(T)!=602` from `[T,b3]!=0`;
- O210 exclusion;
- O212+ authorization;
- effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit.

The Stage32 controller remains unchanged.