# Stage13-13fj — R06 repair plan

> STATUS: `R06_REQUIRED_BY_R05_EXTERNAL_REVIEW`
>
> SOURCE_REVIEW_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R05`
>
> R05_IMMUTABLE: `true`

R05 remains byte-for-byte immutable. This plan records the minimum work required before a new R06 review bundle may be created.

## Gate R06-A — analytic chamber normalization

**Mandatory / theorem-level proof completeness.** Prove analytically

```text
I_ab + I_ac + I_bc = pi^2/8
```

by chamber partition/symmetry or via `J_q=2I_q/pi` plus an analytic proof of `sum_q J_q=pi/4`. Numerical quadrature remains validation only.

```text
SUM_IQ_ANALYTIC_PROOF_COMPLETE=true
NUMERICAL_QUADRATURE_USED_AS_PROOF=false
```

## Gate R06-B — Gaussian-Hecke primary-source closure and exact normalization

**Mandatory / theorem-level external boundary.** Verify directly from primary sources the exact proof-facing family:

```text
k=8 ell, ell>=1
fixed finite residue twists only
exact Xi_k definition and completed functional equation/gamma factor
analytic continuation
nonzero angular family holomorphic/no pole at s=1
fixed-strip polynomial conductor/angular growth sufficient for Riesz/Perron
```

The R06 statement must match the cited source normalization exactly. If a harmless reindexing changes `|k|` versus `2|k|` in the gamma factor, state that map explicitly and derive the proof-facing polynomial-growth consequence from the correctly normalized equation.

```text
HECKE_PRIMARY_SOURCE_CONTRACT_VERIFIED=true
HECKE_FUNCTIONAL_EQUATION_NORMALIZATION_VERIFIED=true
UNMAPPED_HECKE_ASSUMPTIONS=0
```

## Gate R06-C — fixed-S principal pole sector and pole-loss closure

**Mandatory / theorem-level overlap transfer.** Replace the intensional §14 description by a proof-facing characterization:

1. define each unbounded pole-producing multiplicative channel and its untwisted pole order;
2. write the fixed-`S` finite character expansion on the actual algebraically constrained local state space, allowing auxiliary-character aliasing;
3. characterize the full principal pole sector as the tuples whose induced characters are principal on every unbounded pole-producing channel;
4. prove that the sum of this full sector reproduces the local principal multiplier `product_{p in S} lambda_p`;
5. prove the tagged factor `2` covers every true pair-overlap state and therefore gives an upper bound, never an undercount;
6. prove that every tuple outside the principal sector leaves at least one induced unbounded channel genuinely nonprincipal after all aliasing/cancellation, so the total pole order drops by at least one and its fixed-`S` contribution is `o_S(B(log B)^3)`.

```text
PRINCIPAL_POLE_SECTOR_EXPLICITLY_CHARACTERIZED=true
AUXILIARY_CHARACTER_ALIASING_PROOF_COMPLETE=true
TAGGED_FACTOR_TWO_UPPER_BOUND_PROVED=true
NONPRINCIPAL_POLE_LOSS_PROVED=true
```

## Gate R06-D — proof-facing explicitness hardening

Include the non-theorem-changing improvements requested across Claude, Qwen and DeepSeek:

- define Wiener mixed term `M` explicitly before the `32/9` estimate;
- expose the separate `p=5` Wiener bound `<432` calculation (`rho=5^-5/8>1/4`);
- state `ell>=1` when defining `C_{ell,p}`;
- state `lambda_3=1`, hence inert contraction begins at `p>=7`;
- state finite `100k -> 5m` data are neither contradiction nor positive convergence evidence;
- expand Gelfand–Leray radial normalization to `1/(P/d)`;
- expose OE/EE 2-adic face-independence branchwise;
- display the mesh count `O(log(2B)/eta)=O((log B)^9)` per coordinate and `O((log B)^27)` in three coordinates;
- decompose `4*C_H+D_H+6`;
- state Vaaler endpoint convention or measure-zero handling;
- retain `theta` / `vartheta` separation and audit it;
- add factor-two sorting, Riesz/Perron transition-majorant and mixed-log-shift details where useful;
- optionally show the elementary `1+O(p^-2)` expansion for absolute convergence of the explicit `kappa` Euler product.

## Bundle rule

After A-C are closed and D is integrated:

1. create a new canonical repaired proof snapshot;
2. generate immutable `R06` with a new source snapshot and SHA-256;
3. reset external review counts to zero for R06;
4. obtain at least two independent `CLOSED` verdicts on R06 with zero unresolved theorem-level objections;
5. only then promote to `13-13g`.

```text
R05_IMMUTABLE=true
R05_PROMOTION_ALLOWED=false
R06_REQUIRED=true
R06_FRESH_EXTERNAL_REVIEW_REQUIRED=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
```
