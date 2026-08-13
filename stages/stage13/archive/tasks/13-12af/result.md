# Stage13-12af — R03 external-review resynthesis

> STATUS: `STAGE13_12AF_COMPLETE_R03_REVIEW_RESYNTHESIS`
>
> MATHEMATICS CHANGED HERE: no new asymptotic theorem; this stage synthesizes the repaired proof and makes Qwen's R02 minor objections explicit in the current proof map
>
> REVIEW STATUS: `PENDING_EXTERNAL_R03`

Stage13-12af packages the post-R02 repairs into a new immutable single-file
Stage13-only review target.  R01 and R02 are not modified.

The authoritative proof entrypoint is

```text
stages/stage13/13-12af/current-proof.md
```

and the physical review target is

```text
review/STAGE13-FINAL-SELF-CONTAINED-20260809-R03.html
```

The R03 source precedence is

```text
13-12af/current-proof.md
13-12ad/result.md
13-12ae/result.md
13-12aa/result.md
13-12ab/result.md
13-12ac/current-proof.md
historical Stage13 material
```

## Review history carried into R03

```text
R01: OPEN
R02 Grok: OPEN
R02 Claude: REPAIRABLE
R02 Qwen: REPAIRABLE
```

These verdicts are evidence about what was previously challenged, but are not
binding on the R03 verdict.

## Repairs included

R03 includes the complete Stage13-12ad quantitative `j=0` closure:

```text
||C_{ell,p}-1||_{5/8} <= 529 p^(-5/4)
H0=U=exp((log B)^(1/4))
eta=(log B)^(-8)
L=(log B)^4
finite-order A=48
```

with the explicit curved-region and harmonic error ledger.

R03 also includes the complete Stage13-12ae inert local factor:

```text
v_p(h)=0 for primitive inert states
L_p,0(1,1,1)=(p+1)/(p-1)
positive valuation fraction=2/(p+1)<=2/p
C0=2
lambda_p=(p+5)/(2(p+1))
lambda_p<=3/4 for inert p>=7
```

## Qwen minor clarifications promoted into the R03 proof

The R03 current proof explicitly records:

1. the tagged factor `2` as a safe upper multiplicity, not an exact mapping;
2. Stage12 total mass is used for Vaaler excess only as an error majorant and
   is used for `Theta` calibration only after commonness is proved;
3. OE/EE are finite 2-adic branch variants handled branchwise before summing;
4. the analytic change of variables proving
   `J_q = 2 I_q / pi`, rather than relying on numerical quadrature.

## Neutrality

R03 preserves the neutral review protocol:

```text
PREVIOUS_R01_R02_VERDICTS_BINDING=false
INTERNAL_PASS_FLAGS_ARE_EVIDENCE=false
INTERNAL_COMPLETE_FLAGS_ARE_EVIDENCE=false
GIT_HASHES_ARE_MATHEMATICAL_EVIDENCE=false
CI_SUCCESS_IS_MATHEMATICAL_EVIDENCE=false
NEGATIVE_VERDICT_REQUIRES_EXTRA_BURDEN=false
R03_SELF_DECLARED_CLOSED=false
```

The allowed external classifications remain

```text
CLOSED
REPAIRABLE
OPEN
UNREADABLE_SOURCE
```

with no preferred result.

Stage12 R09 remains a frozen declared theorem-level input; Stage12 source is not
embedded and Stage12 itself is not re-audited by this bundle.
