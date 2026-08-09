# Stage13-13fj — R06 repair plan

> STATUS: `R06_REQUIRED_BY_R05_EXTERNAL_REVIEW`
>
> SOURCE_REVIEW_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R05`
>
> R05_IMMUTABLE: `true`

R05 remains byte-for-byte immutable. This plan records the minimum work required before a new R06 review bundle may be created.

## Gate R06-A — analytic chamber normalization

**Mandatory / theorem-level proof completeness.**

Prove analytically

```text
I_ab + I_ac + I_bc = pi^2/8
```

from the chamber integrals. Acceptable routes include:

1. direct chamber partition and symmetry; or
2. the existing `J_q=2 I_q/pi` bridge plus an analytic proof that `sum_q J_q=pi/4`.

The Simpson quadrature remains validation only. R06 must not cite a numerical audit as the proof of this identity.

Required lock:

```text
SUM_IQ_ANALYTIC_PROOF_COMPLETE=true
NUMERICAL_QUADRATURE_USED_AS_PROOF=false
```

## Gate R06-B — Gaussian-Hecke primary-source closure

**Mandatory / theorem-level external boundary.**

Verify directly from primary sources that the exact proof-facing family used by R05 has the required properties:

```text
k=8 ell, ell>=1
fixed finite residue twists only
analytic continuation
functional equation
nonzero angular family holomorphic at s=1
no pole at s=1
fixed-strip polynomial conductor/angular growth sufficient for the Riesz/Perron argument
```

If the cited theorems do not imply this exact contract, replace the contract or proof route before R06.

Required lock:

```text
HECKE_PRIMARY_SOURCE_CONTRACT_VERIFIED=true
UNMAPPED_HECKE_ASSUMPTIONS=0
```

## Gate R06-C — proof-facing explicitness hardening

Include the non-theorem-changing improvements requested by Claude and Qwen:

- define the Wiener mixed term `M` explicitly before the `32/9` estimate;
- state `lambda_3=1` and therefore inert contraction begins at `p>=7`;
- state that finite `100k -> 5m` data are neither contradiction nor positive convergence evidence;
- expand the Gelfand–Leray radial normalization from the Jacobian to `1/(P/d)`;
- enumerate or otherwise expose OE/EE 2-adic face-independence;
- identify the unbounded pole-producing multiplicative channels and character-twist pole loss;
- decompose the `4*C_H+D_H+6` harmonic exponent ledger;
- add the minor factor-two sorting, Riesz/Perron transition-majorant and mixed-log-shift details where useful.

## Bundle rule

After A and B are closed and C is integrated:

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
