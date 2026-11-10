# M3-T11-092 — Homogeneous Legendre-defect normal form and full-S residual character lock

CARD_ID: M3-T11-092
CANONICAL_CARD_KEY: M3-T11-092
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-092
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS / FULL_MODULUS_NORMALIZED_COLLISION / FRESH_CHARACTER_LOCK / NO_POWER_SAVING
種別: EXACT_STRUCTURE / SAME_MEASURE_COMPATIBILITY / GLOBAL_DISPERSION_RECEIVER
要点: On the generic full-S-denominator branch, the Legendre defect has an exact homogeneous quadratic-form model whose endpoint-quartic division identity yields a full-modulus normalized collision and a residual fresh character lock.
主張の抜粋: Define P_ell=4a^2t^2-12abst+(b^2-11a^2)s^2. Then ell=N_u*P_ell/(8abs)^2 and Phi=-4t^2*P_ell+s^3(N_u*s-16abt). After dividing the forced M_rel^2, Phi_0=s^3(N_0s-16ab t_0)-4M_rel^2 t_0^2 P_ell. Remove the even fresh square support from Phi_0 to Phi_flat and put L=ell/M_rel^2. Then -L*Phi_flat=P_ell*(square), while P_ell==3(2bs)^2 mod every fresh p and p==1 mod4. Hence 3L*Phi_flat is a unit square modulo M_rel^2. This is an exact same-measure character receiver, not a fixed-power saving: the unit-square condition has only index 2 per distinct fresh prime.
対象・測度: Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with R<=B, all relative-fresh primes in c_p=0; hard branch M_rel>B^(1/12-eta).
依存関係: M3-T11-091; M3-T11-045 / Section 52; Sections 48-50 homogeneous normalization and W_*^2=-N_*Phi_*; exact fresh p==1 mod4 Gaussian splitting.
再開条件の抜粋: Reopen if the exact polynomial identities fail, the full-S M_rel^2 divisibilities fail, the fresh p-unit assumptions fail, or hostile audit finds a normalization/cancellation error.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 102.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit

## Retained LEDGER source 1
SOURCE_START: 869309
SOURCE_END: 873973
SOURCE_SHA256: 99f20a0b810ed3b3abb73e97a106089d65d1a64aaf841c23108cb04bc8438ade

RESEARCH_CARD=M3-T11-092
---
CARD_ID=M3-T11-092
TITLE=Homogeneous Legendre-defect normal form and full-S residual character lock
STATUS=PROVISIONAL EXACT_SAME_MEASURE_ADAPTER / FULL_MODULUS_NORMALIZED_COLLISION / FRESH_CHARACTER_LOCK / HOSTILE_AUDIT_REQUIRED / NO_POWER_SAVING
TYPE=EXACT_STRUCTURE / SAME_MEASURE_COMPATIBILITY / GLOBAL_DISPERSION_RECEIVER
CLAIM:
On the exact nondegenerate generic full-S-denominator branch write
S=s/t,
u=a/b,
N_u=a^2+b^2,
and define
P_ell=4*a^2*t^2-12*a*b*s*t+(b^2-11*a^2)*s^2.
Then the M3-T11-091 Legendre defect has the exact homogeneous form
ell=N_u*P_ell/(8*a*b*s)^2.
The endpoint quartic satisfies the exact polynomial identity
Phi=-4*t^2*P_ell+s^3*(N_u*s-16*a*b*t).
Moreover
Res_t(Phi,P_ell)=256*a^8*s^8*(a^4-750*a^2*b^2+17*b^4).
For rational u=a/b the last factor has no zero because its roots in u^2 are 375+/-104*sqrt(13). At every fresh p|M_rel it is 768*b^4 mod p and hence a p-unit, so Phi and P_ell are fresh-transverse.


On the full-S branch set
N_0=N_u/M_rel^2,
t_0=t/M_rel^2,
Phi_0=Phi/M_rel^2,
W_0=W/M_rel^2.
Then
W_0^2=-N_0*Phi_0
and exactly
Phi_0=s^3*(N_0*s-16*a*b*t_0)-4*M_rel^2*t_0^2*P_ell.
Hence
Phi_0==s^3*(N_0*s-16*a*b*t_0) mod M_rel^2,
which packages the Section-52 valuation collision into one full-modulus identity.


Let
R_M=product_{p|M_rel} p^(v_p(Phi_0)/2),
Phi_flat=Phi_0/R_M^2,
W_flat=W_0/R_M,
and
L=ell/M_rel^2.
The normalized square equation makes the fresh valuations v_p(Phi_0) even, so
gcd(Phi_flat,M_rel)=1,
W_flat^2=-N_0*Phi_flat,
and
-L*Phi_flat=P_ell*(W_flat/(8*a*b*s))^2.
For every fresh p|M_rel,
P_ell==12*b^2*s^2=3*(2*b*s)^2 mod p.
Since fresh p==1 mod4, -1 is a p-adic square. Therefore for every p^lambda||M_rel,
3*L*Phi_flat is a unit square modulo p^(2*lambda),
and by CRT it is a unit square modulo M_rel^2.
Equivalently chi_p(L*Phi_flat)=chi_p(3) for every p|M_rel.


POPULATION:
Exact fixed-content/coefficient nondegenerate generic full-S-denominator physical branch with R<=B, all relative-fresh primes in c_p=0, and hard branch M_rel>B^(1/12-eta).


DEPENDENCIES:
M3-T11-091; M3-T11-045 / Section 52; Sections 48-50 homogeneous normalization and W_*^2=-N_*Phi_*; exact fresh p==1 mod4 Gaussian splitting.


REQUIRED_OUTPUT:
Prove a same-physical-measure fixed-power dispersion/support bound for realized normalized defects L, or the exact realized pairs (L,Phi_flat), strong enough to give <<B^(1/12-delta) uniformly per fixed packet on the hard branch.


DOES_NOT_IMPLY:
The full-modulus square lock gives only one quadratic-character condition per distinct fresh prime. It does not prove a fixed-power saving, denominator-extreme closure, primary-gate closure, endpoint theorem, P(B)/M3(B), or Perfect Cuboid nonexistence.


NO_DOUBLE_CHARGE:
Do not charge M_rel^-1 or M_rel^-2 from the square lock. The unit-square subgroup modulo p^(2*lambda) has index 2, so naive tensorization is only 2^(-omega(M_rel))=M_rel^(-o(1)). Do not multiply this lock with the M3-T11-091 square-numerator condition, P_ell transversality, or fixed-ell/fixed-x/fixed-u B^o(1) fibers as independent savings.


ALIASES:
FullSDefectResidualCharacterDispersionOneTwelfth;
FullSHomogeneousLegendreDefectNormalForm;
FullSNormalizedCollisionModMrel2.


DUPLICATE_OF:
Not a duplicate. Section 50.3 had only the first mod-p normalized collision; Section 52.2 recorded the truncated valuation identity; M3-T11-091 recorded exact defect valuation and fixed-ell compression. M3-T11-092 supplies the global polynomial division identity, homogeneous defect form, fresh transversality, square-supported residual normalization, and the resulting full-conductor residual character lock.


REOPEN_CONDITION:
Failure of the exact polynomial identities; failure of the full-S exact divisibilities N_u,t,Phi,W by M_rel^2; failure of fresh p==1 mod4 or the p-unit assumptions; or hostile audit finding a normalization/cancellation error.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 102.


FLAGS:
M3_T11_FULL_S_HOMOGENEOUS_LEGENDRE_DEFECT_FORM=PROVISIONAL
M3_T11_FULL_S_PHI_DEFECT_EXACT_DIVISION=PROVISIONAL
M3_T11_FULL_S_DEFECT_PHI_FRESH_TRANSVERSALITY=PROVISIONAL
M3_T11_FULL_S_NORMALIZED_COLLISION_MOD_MREL2=PROVISIONAL
M3_T11_FULL_S_RESIDUAL_CHARACTER_LOCK=PROVISIONAL
M3_T11_FULL_S_RESIDUAL_CHARACTER_FIXED_POWER=false
M3_T11_DENOMINATOR_EXTREME_SUPPORT_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
NEXT_LEGAL_ACTION=Hostile-audit M3-T11-090 through M3-T11-092. Mainbatch may attack FullSDefectResidualCharacterDispersionOneTwelfth or the existing realized-ell support receiver; no local squareclass or fixed-fiber factor may be charged independently.
NEXT_RESEARCH_CARD_ID=M3-T11-093.




0
