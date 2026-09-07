# Stage32EX1 EX1-01 — two-model normalization/defect decomposition

Status: provisional `stage32ex1-mainbatch` candidate on PR #1688. This note proves the location partition used by EX1-01. It does not grant hostile-audited credit.

## 1. Keep the two ambient models distinct

Let `X` be the singular canonical cuboid surface over `C`, with its 48 isolated `A1` nodes, and let

`pi : S -> X`

be the minimal resolution. Let `E_i` be the exceptional component over node `x_i`.

A hypothetical Stage32EX1 target carrier is an integral irreducible curve `Gamma` on `S` with Picard class `V6` and geometric genus `1`. Its canonical-model image is `B = pi(Gamma)`. The V6 carrier is not an exceptional component (`K.Gamma=186`), so `Gamma` and `B` are birational integral curves and have the same normalization `N`.

This distinction is load-bearing:

- the adjunction defect `472 = p_a(Gamma)-g(N)` is the total delta of the strict-transform curve `Gamma` on the smooth surface `S`;
- nonbijectivity of `N -> B` can also be created by contraction of distinct points of `Gamma cap E_i` to one surface node `x_i`;
- therefore canonical-model fibre multiplicity at a node is not automatically strict-transform delta.

## 2. Replay of the bounded globally-bijective exclusion

The retained FSM/AH source lock gives, under the hypothesis that `N -> B` is globally bijective:

- degree `d=186`, genus `g=1`;
- 47 met surface nodes;
- zero order at least `372 k`;
- pole order at most `376 k` if all met-node branches are minimal;
- pole order at most `368 k` if at least one met-node branch is nonminimal.

For genus `1`, the tensor divisor identity has equal total zero and pole orders. Hence `372 > 368` rules out any nonminimal met-node branch under the global-bijectivity hypothesis. Every one of the 47 met-node branches would therefore have the minimal FSM cusp type.

The local `A1` resolution calculation in the retained source note shows that a minimal FSM cusp has exceptional intersection multiplicity exactly `1`. Thus global bijectivity would force total exceptional mass `47`. The exact V6 class has exceptional mass `266`. Contradiction.

Candidate consequence:

`if a V6 genus-1 carrier exists, N -> B is nonbijective somewhere`.

This consequence is retained only at the Stage32EX1 candidate ceiling until hostile audit.

## 3. Exact node-fibre bound from exceptional contacts

Write

`m_i = Gamma.E_i`

for the exact V6 exceptional pairing, and let

`r_i = # { q in N : q maps to x_i in B }`.

For every normalization branch over `x_i`, the lifted branch on `S` meets `E_i`. Because `Gamma` does not contain `E_i`, the pullback of a local equation of `E_i` to that normalization branch has strictly positive order. Summing those branch orders gives the intersection number `m_i`. Hence

`r_i <= m_i`.

Consequences:

- `m_i=0` implies `r_i=0`;
- `m_i=1` implies `r_i=1`, so that node cannot be a nonbijective normalization fibre;
- `r_i>=2` is possible only for `m_i>=2`.

The exact V6 vector has:

- zero label: `[6]`;
- unit-positive labels: `[1,2,3,7,15,20,22,24,36]`;
- nonunit-positive labels: `[4,5,8,9,10,11,12,13,14,16,17,18,19,21,23,25,26,27,28,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48]`.

Therefore the surface-node multibranch branch is narrowed from 47 met nodes to exactly 38 candidate node labels.

A further exact bookkeeping bound is

`sum_i max(r_i-1,0) <= sum_{m_i>0}(m_i-1) = 266-47 = 219`.

This `219` is node-fibre excess capacity. It is **not** delta.

## 4. Exhaustive normalization-nonbijectivity location split

Every point of `X` is either one of its 48 singular nodes or lies in `X_reg`. Therefore any point where `N -> B` is nonbijective lies in exactly one of:

1. `SURFACE_NODE_FIBRE`: over some `x_i in Sing(X)`. By the preceding lemma only the 38 labels with `m_i>=2` are possible.
2. `SMOOTH_AMBIENT_LOCUS_CURVE_MULTIBRANCH_SINGULARITY`: over `x in X_reg`. Since `pi` is an isomorphism over `X_reg`, this is precisely multibranch noninjectivity of `Gamma` away from the exceptional divisor.

There is no third ambient location in this source-locked model.

This is only a location/type partition. Neither branch is closed by EX1-01.

## 5. Independent strict-transform delta ledger

Let `E = union_i E_i`. Since `S` is smooth and `Gamma` is integral,

`delta_total(Gamma) = p_a(Gamma)-g(N) = 473-1 = 472`.

Partition the singular points of `Gamma` by whether they lie on `E`:

`delta_E = sum_{p in Sing(Gamma) cap E} delta_p`,
`delta_U = sum_{p in Sing(Gamma) cap (S\E)} delta_p`.

Then exactly

`delta_E + delta_U = 472`.

This delta partition must remain separate from the canonical-model normalization-fibre ledger:

- surface-node nonbijectivity does not by itself imply `delta_E>0`; distinct smooth points of `Gamma` on the same `E_i` may be contracted to one node;
- smooth-ambient nonbijectivity does imply a multibranch singularity of `Gamma` off `E`, hence `delta_U>=1`;
- unibranch singularities may contribute positive delta while their normalization fibre has one point, so the AH nonbijectivity witness never accounts for all `472` by itself.

## 6. EX1-01 exit

Established at candidate level:

- exhaustive two-model normalization-nonbijectivity location partition;
- exact separation of canonical-model fibre excess from strict-transform delta;
- exact reduction of possible node-multibranch sites from 47 to 38;
- exact node-fibre excess upper bound `219`.

Not established:

- closure of the 38 node-multibranch candidates;
- closure of smooth-ambient singularities;
- any identification `266=472` or `219=472`;
- existence of an actual V6 genus-1 carrier;
- Stage32 MAIN / receiver / theorem / endpoint / Perfect Cuboid credit.

Next leaf: `EX1-02_SURFACE_NODE_MULTIBRANCH_CLOSURE`.
