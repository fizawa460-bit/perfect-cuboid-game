# Stage33-05 source lock — corrected J2 / Creutz--Viray / Hochschild--Serre

## Current authoritative status

The historical Q-defined `ell_J2` / CSA from `j2_arithmetic_descent.py` is **revoked** as a witness for the named nonzero J2. The exact regression is:

```text
stages/stage33/33-12/j2-cv-lclass-zero-regression.json
```

The corrected geometric class is

```text
J2=(f2,1),
f2=(t+1+sqrt(2))/(t-1+sqrt(2)),
```

with R0--R4 and the geometric part of R5 hostile-replayed PASS. The integral geometric receiver is retained:

```text
T(X_J2)=<8> direct_sum <16>
minimum norm=8
marked J2=[1,0]
```

This is `Kgeom=Qbar(t)` credit only.

The attempted post-R5 Q descent was hostile-rejected. `certify_j2_post_r5_q_descent_cocycle.py` had proved only fixedness in the finite 5D CV presentation and then assigned the Pic/2 defect, integral Pic lift and HS d2 to zero constants. That inference is forbidden.

Current failure certificate:

```text
j2-post-r5-hs-descent-datum.json
canonical_sha256=a7c08372b9ef012a1446bd3bf4f40541d77d372dadc73e3780f6ce2529fcc6d8
```

Therefore currently:

```text
CORRECTED_J2_Q_DESCENT_EXACT_EVIDENCE_REESTABLISHED=false
HS_D2_CORRECTED_J2_MATERIALIZED=false
HS_D2_CORRECTED_J2_ZERO_PROVED=false
R5_FULL_REPAIR_EXIT_REACHED=false
Q_DEFINED_DESCENT_CREDIT_RESTORED=false
STAGE33_05_RECLOSED=false
```

## Primary Creutz--Viray sources

### Ruled-surface presentation

Brendan Creutz, Bianca Viray, *On Brauer groups of double covers of ruled surfaces*, arXiv:1306.3251v3, Math. Ann. 362 (2015), 1169--1200.

Load-bearing locators:

- Theorem 2.5: `gamma'` induces an exact sequence of Galois modules for the generic hyperelliptic fiber.
- Proposition 3.1 / Corollary 3.2: residue tests for extending generic-fiber classes.
- Theorem 5.2 / Corollary 5.4: geometric surface Br[2] presentation and NS relations.

This source justifies Galois equivariance of the CV presentation. It does **not** say that a Galois-fixed geometric Brauer class has Hochschild--Serre d2 equal to zero.

### Hyperelliptic cocycle / Brauer-to-WC compatibility

Brendan Creutz, Bianca Viray, *Two torsion in the Brauer group of a hyperelliptic curve*, arXiv:1403.2924v1, Manuscripta Math. 147 (2015), 139--167.

Load-bearing locators:

- Lemma 4.6: explicit `J[2]` 1-cocycle representing `d(ell)`.
- Proposition 5.1 and its proof: `h0 o gamma` and `d` are the same map to `H^1(K,Pic C)`.
- Proposition 3.2 and Lemmas 3.4--3.5: explicit divisor/function cocycles underlying the cohomological construction.

These support the audited geometric chain

```text
J2=(f2,1) -> gamma(J2) -> h0 gamma=d -> xi -> named X_J2.
```

They do not by themselves provide the arithmetic surface `H^2(mu_2)` lift needed for `d2^{0,2}` over Q.

## Hochschild--Serre / Kummer source locks

- Stacks Project, tag `03PK`, Kummer sequence:
  `0 -> mu_2 -> G_m --2--> G_m -> 0`.
- For a geometric K3 with torsion-free Picard group:

```text
0 -> Pic(Kc_bar)/2
  -> H^2_et(Kc_bar,mu_2)
  -> Br(Kc_bar)[2]
  -> 0.
```

For an invariant geometric Brauer class, one must first choose an actual `mu_2` lift. Its Galois defect is a `Pic/2` 1-cocycle. Choosing integral Pic lifts and applying the Bockstein gives the Pic-valued 2-cocycle representing the Hochschild--Serre `d2` obstruction.

- Skorobogatov--Zarhin, JEMS 16 (2014), proof of Theorem B around equation (21): when `H^3(k,kbar^*)=0`,

```text
ker(Br(Xbar)^G -> H^2(k,Pic(Xbar)))
= image(Br(X) -> Br(Xbar)^G).
```

- Neukirch--Schmidt--Wingberg, *Cohomology of Number Fields*, Proposition 8.3.11: the required `H^3` vanishing for number fields.

**Application firewall:** this kernel=image theorem may be applied to corrected J2 only after `d2(J2)=0` is actually proved. It cannot be used to prove its own hypothesis.

## Corrected pre-Kummer descent cochain — exact new MAIN evidence

Current certificate:

```text
j2-corrected-pre-kummer-descent-cochain.json
canonical_sha256=940df53040c6f5245914effbfb7d752a08c61b6d593586952b322e4069415106
```

On the common normalization

```text
z^2=q=(t-r1)(t-r2)(t-r3)(t-r4)
r1=1+sqrt(2)
r2=-(1+sqrt(2))
r3=sqrt(2)-1
r4=1-sqrt(2)
f2=(t-r2)/(t-r4),
```

we have the exact half-divisor

```text
D=P_r2-P_r4
div(f2)=2D.
```

For `ct: sqrt(2)->-sqrt(2)`:

```text
ct: r1<->r4, r2<->r3
h_ct=z/((t-r1)*(t-r2))
u_ct=(t-r3)*(t-r4)/z

div(h_ct)=ct(D)-D
h_ct*ct(h_ct)=1
ct(f2)/f2=u_ct^2
u_ct*ct(u_ct)=1
u_ct=1/ct(h_ct).
```

Thus the line bundle `O(D)` on the normalization has an explicit trivial C2 descent obstruction for this conjugation.

At the full split-pair representative level:

```text
tau(f2,1)=(f2,1)
ct(f2,1)=(f2,1)*(u_ct^2,1)
cc(f2,1)=diag(f2)*(f2,1)*((1/f2)^2,1)
```

These identities are stronger than the old statement that the quotient vector `[0,1,0,0,0]` is Galois-fixed.

### Exact boundary

They are **not** yet a full-surface Kummer lift. In particular none of the following is currently credited:

```text
H^2_et(Kc_bar,mu_2) lift of corrected J2
Pic(Kc_bar)/2 Galois-defect 1-cocycle
integral Pic lift
Bockstein / HS d2 2-cocycle
HS d2(J2)=0
Q-defined arithmetic Brauer preimage
arithmetic unramifiedness of such a preimage
```

The missing functorial adapter is:

```text
corrected CV / normalization half-divisor datum
 -> marked Kc surface H^2(mu_2) lift
 -> Pic/2 defect
 -> integral Pic lift
 -> HS d2.
```

Current machine boundary contract:

```text
stages/stage33/33-12/j2-full-surface-mu2-zero-defect-contract.json
canonical_sha256=c35eec49758734e29cb801ea9a55ed6e739238750f3ff92c14f030ae25e8ff2b
```

The historical `certify_j2_named_kummer_glue_input.py` producer has been tombstoned because it consumed the revoked old `ell_J2` and could regenerate stale zero-defect credit.

## Immutable geometric inputs

- `MichaelStollBayreuth/Verification@51233ed5ef2bf228fac9416c66db9adc0ebcaadd`, `Cuboids/cuboids.magma`.
- Kc marked Picard rank 20 and discriminant 32 are source-locked in Stage33-12.
- `T(Kc)=<4> direct_sum <8>` and the geometric marked class `[1,0]` are retained.

The existence of a complex-lattice B-field/half-dual representative does not by itself determine the arithmetic étale Galois action on a `mu_2` lift. No such transfer may be made without an explicit adapter.

## q1 historical comparison

The separately materialized q1 obstruction used an actual integral Picard lift `D=Cb+E_P0` and computed a nonzero restricted Bockstein. It remains useful as a template for what corrected J2 must now supply: an actual Pic/2 defect and integral lift, not a quotient-fixedness assertion.

## Current source-lock disposition

```text
SOURCE_THEOREM_APPLICABILITY=FROZEN_WITH_POST_R5_HOSTILE_ROLLBACK
LCE_DIMENSION=5
XALPHA_IMAGE_DIMENSION=3
CORRECTED_J2_GEOMETRIC_REPRESENTATIVE=(f2,1)
CORRECTED_J2_MARKED_BRAUER_COORDINATE=[1,0]
CORRECTED_J2_NORMALIZATION_PRE_KUMMER_COCHAIN_MATERIALIZED=true
CORRECTED_J2_SURFACE_MU2_LIFT_MATERIALIZED=false
CORRECTED_J2_HS_D2_MATERIALIZED=false
CORRECTED_J2_HS_D2_ZERO_PROVED=false
CORRECTED_J2_Q_DESCENT_EXACT_EVIDENCE_REESTABLISHED=false
OLD_ELL_Q_J2_WITNESS_REVOKED=true
R5_FULL_REPAIR_EXIT_REACHED=false
STAGE33_05_UNIT_STATUS=BLOCKED_NEW_KERNEL
AUTHORITATIVE_Q_DESCENT_CREDIT_RESTORED=false
NEXT=MATERIALIZE_NORMALIZATION_HALF_DIVISOR_TO_KC_SURFACE_H2_MU2_ADAPTER_THEN_COMPUTE_PIC_MOD2_DEFECT_AND_BOCKSTEIN_HS_D2
```
