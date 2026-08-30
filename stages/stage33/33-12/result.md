# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_WAITING_ON_STAGE33_05_SUPER_HOSTILE_AUDIT_AFTER_R5_REPAIR_EXIT`

Stage33-12 remains open. Stage33-13 is not released. Class-3 promotion is **not** authorized. Stage33 progress remains `5/11`.

## Historical regression and geometric repair

The historical Stage33-05 Q-defined `ell_Q`/CSA formerly used as the named geometric `J2` representative was hostile-proved geometrically trivial in the exact Creutz--Viray quotient:

```text
stages/stage33/33-12/j2-cv-lclass-zero-regression.json
```

That revoked witness is not reused.

The Stage33-05 repair then independently reconstructed the named class:

```text
R1 abstract J2 nonzero                         PASS
R2 corrected full-L pair (f2,1) nonzero       PASS
R3 explicit CV E[2] cocycle xi(rho)=Tr        PASS
R4 correct attempt-2 torsor / lattice marking PASS
R5 hostile replay R1--R4                      PASS
```

R4 hostile verification fixes the integral statement

```text
T(X_J2) ~= ker(J2:T(Kc)->Q/Z)
```

with inherited integral pairing, and the independent degree-two quotient comparison gives

```text
T(X_J2)=<8> direct_sum <16>,
minimum norm=8,
marked J2=[1,0].
```

Attempt 1 remains revoked as the named torsor.

## Post-R5 corrected J2 arithmetic descent

The previous residual

```text
CORRECTED_J2_Q_DEFINED_DESCENT_OR_EXPLICIT_ARITHMETIC_REPRESENTATIVE
```

now has **pre-audit exact evidence of resolution** without reusing the old `ell_Q`.

New certificate/verifier:

```text
../33-05/j2-post-r5-hs-descent-datum.json
../33-05/certify_j2_post_r5_q_descent_cocycle.py
```

The exact full-pair presentation has basis `[J1,J2,q1,q2,q3]` and source-locked Galois generators `tau`, `cc`, `ct`.  Direct replay gives

```text
tau(J2)-J2 = 0
cc(J2)-J2  = 0
ct(J2)-J2  = 0.
```

Creutz--Viray's Galois-equivariant presentation/cocycle comparison identifies this with the Kummer `Pic/2` defect.  Hence corrected J2 has the explicit normalized descent cochains

```text
Pic/2 defect 1-cocycle = 0,
integral Pic lift       = 0,
Bockstein / HS d2       = 0.
```

For `k=Q`, `H^3(Q,Qbar^*)=0`.  Standard Hochschild--Serre exactness therefore gives

```text
ker(Br(Kc_bar)^G_Q -> H^2(Q,Pic(Kc_bar)))
 = image(Br(Kc_Q) -> Br(Kc_bar)^G_Q).
```

Thus there is an arithmetic class

```text
beta_J2_Q in Br(Kc_Q)
```

with

```text
res_Qbar(beta_J2_Q)=corrected nonzero J2=(f2,1).
```

Because the class is obtained in `Br(Kc_Q)` of the smooth projective Q-K3 itself, rather than only in the function-field Brauer group, arithmetic unramifiedness is built into this conclusion.  This repair records an explicit **Hochschild--Serre/Kummer descent datum**; it does **not** claim a new closed-form Q quaternion/CSA formula.

External source locks are frozen in `../33-05/source-lock.md`, including:

- Creutz--Viray, arXiv:1306.3251, Theorem I / Theorem 2.5;
- Creutz--Viray, arXiv:1403.2924, Remark 3.1 / Proposition 3.2 / Lemmas 3.4--3.5;
- Skorobogatov--Zarhin, JEMS 16 (2014), Hochschild--Serre equation (21) application;
- Neukirch--Schmidt--Wingberg, *Cohomology of Number Fields*, Proposition 8.3.11.

## R5 repair exit and mandatory audit gate

The R5 repair line has now reached its full mathematical exit **as pre-audit evidence**:

```text
R5_FULL_REPAIR_EXIT_REACHED=true
CORRECTED_J2_Q_DESCENT_EXACT_EVIDENCE_REESTABLISHED=true
EQUIVALENT_ARITHMETIC_DESCENT_DATUM_MATERIALIZED=true
UNRESOLVED_UNKNOWN_IN_R5_REPAIR_SCOPE=0
```

However the repository-wide promotion firewall and the user's explicit workflow require a separate **super-hostile audit** before any authoritative closure credit.

Current Stage33-05 state is therefore

```text
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
Q_DEFINED_DESCENT_CREDIT_AUTHORITATIVELY_RESTORED=false
```

The next exact leaf is

```text
SUPER_HOSTILE_AUDIT_STAGE33_05_CORRECTED_J2_REPAIR
```

and the audit must be performed on a new PR/work line.  It must independently challenge at least:

```text
1. R0--R5 replay without trusting promoted booleans;
2. zero full-pair presentation defect -> zero Kummer/Pic defect;
3. zero Bockstein -> HS d2=0;
4. H^3(Q,Qbar^*)=0 and ker(d2)=image Br(Kc_Q);
5. whether this explicit cohomological descent datum satisfies the Stage33-05
   explicit arithmetic representative closure contract;
6. corrected geometric restriction is nonzero (f2,1), never the revoked ell_Q.
```

Only a super-hostile `PASS` may reclose Stage33-05 or allow Stage33-12 / downstream release to be reconsidered.

## Firewalls

```text
R4 minimum norm 8 / marked J2=[1,0] = RETAINED GEOMETRIC CREDIT
post-R5 corrected J2 Q-descent evidence = EXACT PRE-AUDIT
old ell_Q J2 witness = REVOKED / FORBIDDEN
Stage33-05 reclosed = false
Stage33-12 exact closure = false
Stage33-13 released = false
Stage33 progress = 5/11
class3 promoted = false
theorem credit = false
receiver credit = false
endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
