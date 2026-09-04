# Stage32 post-1566 orbit-sum / correspondence-commutator batch — hostile-audit repair

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, `Q=602`, after hostile-re-audited and merged #1566.

This repair addresses exactly the Route C blocker from hostile audit on #1570. The previous argument passed from a downstairs numerical class to a strict-transform class on the 48-point resolution without controlling exceptional multiplicities. That bridge is withdrawn. No equality of beta-transformed strict transforms and no invariance of an exceptional multiplicity vector is used below.

The replacement computes the relevant stabilizer directly after quotienting the resolved numerical Picard space by the exact exceptional span, i.e. on the blow-down numerical Neron-Severi space.

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

For hostile-audit repair we do not stop at resolved-class noninvariance. We pass to the blow-down numerical class exactly.

## Route C — hostile-audit repair on blow-down N^1(B)

### C1. Exact exceptional quotient and complete stabilizer

The retained marked-node source lock identifies the 48 exceptional curves of the box-surface resolution as known classes

`E_93, E_94, ..., E_140`.

The primitive 64-dimensional INDLIST lattice and Gram matrix are reconstructed by the retained Picard helper. The V6 class is recovered from its all-140 pairings, then checked by exact self-square `758` and replay of all 140 pairings.

Every one of the nine retained Stoll generators preserves the set `{93,...,140}`. The exact rational row span of the 48 exceptional classes has rank `48`. Hence the numerical blow-down quotient used here is

`N^1(Btilde)_Q / <E_93,...,E_140>_Q`,

of rank `64-48=16`. This is the standard numerical blow-up decomposition: the kernel of numerical push-forward to the blow-down is the Q-span of the exceptional divisor classes.

For every `g` in the complete Stoll group of order 1536, the diagnostic tests

`g(S_B)-S_B in <E_93,...,E_140>_Q`.

Equivalently, it tests whether `g` fixes the image `[S_B]_B` of `S_B` in the blow-down `N^1(B)_Q`.

The complete stabilizer after quotienting again has order four and is exactly

`{1, g7*g8, g7*g9, g8*g9}=H`,

with outside-H stabilizer count zero. Since #1566 gives `beta_B in Stoll1536` and `beta_B notin H`,

`beta_B^*[S_B]_B != [S_B]_B in N^1(B)_Q`.

This is the repaired noninvariance statement. It does not assume any beta-invariance of exceptional multiplicities.

### C2. Descend the retained pullback identity through the exceptional quotients

The retained quotient square is

- `P = X(8) x X(8)`,
- `X = P/H_diag`,
- `B = P/G_diag`,
- `Q = P/(H x H) = C0 x C0`,
- `pi:X->B`,
- `q:X->Q`.

The retained #1490 source note states that the same square remains equivariant after blowing up the 48 distinguished X points and the corresponding 48 B nodes, because the actions permute the centers. Write the resolved map as

`pi_tilde:Xtilde->Btilde`.

For the hypothetical exact-V6 carrier it source-locks the resolved pullback identity

`Dtilde = pi_tilde^* C`.

Now quotient both numerical Neron-Severi spaces by their exceptional spans. Because `pi_tilde` covers `pi` and maps the exceptional locus over the blown-up centers into the exceptional locus, pullback descends to the quotient. Thus the displayed resolved identity induces, without choosing or comparing any exceptional multiplicity vector,

`[D]_X = pi^*[C]_B`.

The H-actions preserve the exceptional spans and the square is H-equivariant, so summing the four translates gives

`[D+uD+vD+uvD]_X = pi^*[S_B]_B`.

The independently retained correspondence identity is

`q^*Gamma = D + uD + vD + uvD`.

Therefore, on the blow-down numerical spaces,

`[q^*Gamma] = pi^*[S_B]_B in N^1(X)_Q`.

This is obtained by quotienting the source-locked resolved pullback identity; it is not an assertion that strict transforms are unchanged by beta.

The retained common-double-cover certificate gives H normal of index two in G and identifies X as the normalization of the degree-two pullback over B. Thus `pi:X->B` is finite surjective of generic degree two on the retained normalization level. The projection formula gives

`pi_* pi^* = 2 id`

on numerical divisor classes over Q, so

`pi^*:N^1(B)_Q -> N^1(X)_Q`

is injective.

Merged #1556 supplies compatible automorphisms `beta_X` and `beta_B` with

`pi o beta_X = beta_B o pi`,

and the same principal-b3 lift gives

`q o beta_X = (b3 x b3) o q`.

Assume for contradiction

`(b3 x b3)^*[Gamma]=[Gamma] in NS(Q)`.

Pulling back by q and using q-equivariance gives beta_X-invariance of `[q^*Gamma]`. Using the quotient-descended identity and pi-equivariance gives

`pi^*(beta_B^*[S_B]_B-[S_B]_B)=0`.

Injectivity of `pi^*` forces

`beta_B^*[S_B]_B=[S_B]_B`,

contradicting C1. Therefore, conditional on existence of the exact carrier/correspondence,

`(b3 x b3)^*[Gamma] != [Gamma]`.

No injectivity of q-pullback is used. The only reverse pullback step is the source-bound degree-two injectivity of `pi^*`.

## Route D — correspondence class to Jacobian commutator

External source lock: Igor Dolgachev and Yuri G. Zarhin, *Endomorphisms of Complex Abelian Varieties*, April 8, 2025, Chapter 10 §10.1.

The exact facts used are `Corr(C)=NS(C x C)/(two fibral classes) ~= End(J(C))`, compatibility with composition, factor switch/Rosati, and the criterion that valence nu induces `[-nu]`.

For an automorphism `a` of C, diagonal transport `(a x a)^*Gamma` induces conjugation of the associated Jacobian endomorphism, up to the harmless inverse convention from pull/push orientation.

Gamma and its diagonal-b3 transform have the same bidegree `(105,81)`, so their difference has bidegree `(0,0)`. A nonzero fibral combination cannot have bidegree `(0,0)`. Hence the nonzero Neron-Severi difference from repaired Route C survives in `Corr(C0)`, and under the same exact-carrier/correspondence conditionality

`[T,b3] != 0`.

## Route E — valence/scalarity lane

A valence-nu correspondence induces `T=[-nu]`, hence is scalar and commutes with b3. Route D proves the opposite for any hypothetical exact-V6 O210 correspondence. Therefore such a correspondence, if it exists, is neither of valence nor scalar.

The former #1522 conditional route cannot be promoted to Q602 exclusion: its valence premise is refuted for this hypothetical exact correspondence.

## Route F — Q602 firewall

The hostile-audited post1532 certificate leaves exactly residues `73,97,235` at Q602, and all three have nonzero principal-b3 commutator modulo 2. Actual noncommutation is therefore compatible with every retained Q602 residue.

## Hostile-audit repair invariants

The repaired certificate/certifier must enforce:

- exceptional labels exactly `93..140`;
- exceptional curve count `48`;
- exceptional span rank over Q `48`;
- blow-down quotient rank `16`;
- resolved stabilizer exactly H;
- blow-down stabilizer exactly H;
- outside-H blow-down stabilizer count `0`;
- `beta_B` in Stoll1536 and outside H;
- strict-transform beta bridge not used;
- exceptional multiplicity invariance not assumed;
- blow-down N^1 quotient route used.

## Firewalls

Do not infer carrier existence/nonexistence, unconditional Gamma existence, `Q(T)!=602`, O210 exclusion, O212+ authorization, or any effectivity/FULL178/receiver/route/theorem/endpoint/perfect-cuboid credit.

The Stage32 controller remains unchanged.