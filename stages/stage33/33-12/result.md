# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_BLOCKED_BY_STAGE33_05_POST_R5_SURFACE_MU2_AND_HS_D2`

Stage33-12 remains open. Stage33-13 is not released. Stage33 progress remains `5/11`.

## Retained geometric repair

The historical Q-defined `ell_Q`/CSA is revoked as the named nonzero J2 witness: its geometric Creutz--Viray class is zero. It must not be reused.

The corrected geometric repair remains authoritative:

```text
R0 old ell_J2 zero regression                  PASS
R1 abstract J2 nonzero                         PASS
R2 corrected full-L pair (f2,1) nonzero       PASS
R3 explicit CV cocycle xi(rho)=Tr              PASS
R4 named geometric torsor / integral kernel    PASS
R5 hostile replay of R1--R4 geometric content  PASS
```

R4 retains

```text
T(X_J2) ~= ker(J2:T(Kc)->Q/Z)
T(X_J2)=<8> direct_sum <16>
minimum norm=8
marked J2=[1,0]
```

This is geometric `Kgeom=Qbar(t)` credit only.

## Hostile failure of the attempted post-R5 Q descent

The previous post-R5 verifier proved only that J2 is fixed in the finite 5D F2 Creutz--Viray presentation. It then assigned

```text
Pic/2 defect = 0
integral Pic lift = 0
HS d2 cocycle = 0
```

without deriving them. This inference is invalid. Galois invariance of a geometric Brauer class does not imply its Hochschild--Serre obstruction vanishes.

Current failure certificate:

```text
../33-05/j2-post-r5-hs-descent-datum.json
canonical_sha256=a7c08372b9ef012a1446bd3bf4f40541d77d372dadc73e3780f6ce2529fcc6d8
```

Therefore:

```text
corrected_J2_Q_descent_exact_evidence_reestablished=false
Q_defined_descent_credit_restored=false
R5_full_repair_exit_reached=false
Stage33-05 reclosed=false
```

## New exact MAIN progress: corrected pre-Kummer descent cochain

MAIN now materializes explicit representative-level descent data for the corrected pair without promoting it to a surface Kummer lift.

Certificate/verifier:

```text
../33-05/j2-corrected-pre-kummer-descent-cochain.json
../33-05/certify_j2_corrected_pre_kummer_descent_cochain.py
canonical_sha256=940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106
```

On the normalization

```text
z^2=q=(t-r1)(t-r2)(t-r3)(t-r4)
f2=(t-r2)/(t-r4)
```

the corrected half-divisor is

```text
D=P_r2-P_r4
div(f2)=2D.
```

For sqrt(2)-conjugation `ct`, with `r1<->r4` and `r2<->r3`, define

```text
h_ct = z/((t-r1)(t-r2))
u_ct = (t-r3)(t-r4)/z.
```

Exact identities give

```text
div(h_ct)=ct(D)-D
h_ct*ct(h_ct)=1
ct(f2)/f2=u_ct^2
u_ct*ct(u_ct)=1
u_ct=1/ct(h_ct).
```

The full split pair also has explicit representative witnesses:

```text
tau(f2,1)=(f2,1)
ct(f2,1)=(f2,1)*(u_ct^2,1)
cc(f2,1)=diag(f2)*(f2,1)*((1/f2)^2,1)
```

This is strictly stronger than merely observing that the 5D quotient vector J2 is fixed.

## Exact boundary after this batch

The new datum is still only a normalization/full-L pre-Kummer descent cochain. It is **not yet** a class in `H^2_et(Kc_bar,mu_2)`.

Current machine contract:

```text
j2-full-surface-mu2-zero-defect-contract.json
status=OPEN_CORRECTED_REPRESENTATIVE_PRE_KUMMER_COCHAIN_MATERIALIZED_SURFACE_MU2_AND_HS_D2_UNPROVEN
canonical_sha256=c35eec49758734e29cb801ea9a55ed6e739238750f3ff92c14f030ae25e8ff2b
```

The historical `j2-named-kummer-glue-input` producer was also tombstoned because it could regenerate revoked old-ell zero-defect credit.

Still missing:

```text
1. an explicit functorial adapter from the corrected CV/normalization datum
   to a genuine H^2_et(Kc_bar,mu_2) lift of J2;
2. sigma(lift)-lift in Pic(Kc_bar)/2;
3. integral Pic lifts of that 1-cocycle;
4. the resulting Bockstein / Hochschild-Serre d2 2-cocycle;
5. determination of its class, without assuming it is zero.
```

Only if the actual d2 class is zero may Hochschild--Serre kernel=image be used to restore Q-defined Brauer credit.

## Next exact leaf

```text
MATERIALIZE_NORMALIZATION_HALF_DIVISOR_TO_KC_SURFACE_H2_MU2_ADAPTER
THEN_COMPUTE_PIC_MOD2_DEFECT_AND_BOCKSTEIN_HS_D2
```

## Firewalls

```text
R4 minimum norm 8 / marked J2=[1,0] = RETAINED GEOMETRIC CREDIT
post-R5 Q descent = FAIL / UNPROVEN
surface mu2 lift = OPEN
HS d2 = OPEN
Q-defined descent credit = false
Stage33-05 reclosed = false
Stage33-12 exact closure = false
Stage33-13 released = false
Stage33 progress = 5/11
theorem/receiver/endpoint credit = false
perfect cuboid existence/nonexistence claim = false
```
