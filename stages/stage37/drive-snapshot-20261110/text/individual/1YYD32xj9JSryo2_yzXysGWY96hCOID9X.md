# M3-T11-033 — For the M3-T11-032 cubic coefficient pair X_sym=T_1-T_3, Y_sym=T_2-D, the joint congruence X_sym+rho_rel Y_sym==0 mod M_rel^2 is primitive at every fresh prime. Primewise, for p^a||m_i, the target anti-root v_i is a p-unit by its oriented root-line congruence. The retained fresh-unit filter makes the relative trace between the other two directions a p-unit. The two remaining unit-argument trace factors in v_i^2 are then also p-units. For j!=i this forces exactly v_p(v_j)=-2a, so their reduced de

CARD_ID: M3-T11-033
CANONICAL_CARD_KEY: M3-T11-033
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-033
現行一覧の状態: PROVED_EXACT_WITH_OPEN_RANGE_ADAPTER
種別: EXACT_LOCAL_VALUATION / PRIMITIVE_JOINT_ROOTLINE
要点: For the M3-T11-032 cubic coefficient pair X_sym=T_1-T_3, Y_sym=T_2-D, the joint congruence X_sym+rho_rel Y_sym==0 mod M_rel^2 is primitive at every fresh prime. Primewise, for p^a||m_i, the target anti-root v_i is a p-unit by its oriented root-line congruence. The retained fresh-unit filter makes the relative trace between the other two directions a p-unit. The two remaining unit-argument trace factors in v_i^2 are then also p-units. For j!=i this forces exactly v_p(v_j)=-2a, so their reduced de
主張の抜粋: For the M3-T11-032 cubic coefficient pair X_sym=T_1-T_3, Y_sym=T_2-D, the joint congruence X_sym+rho_rel Y_sym==0 mod M_rel^2 is primitive at every fresh prime. Primewise, for p^a||m_i, the target anti-root v_i is a p-unit by its oriented root-line congruence. The retained fresh-unit filter makes the relative trace between the other two directions a p-unit. The two remaining unit-argument trace factors in v_i^2 are then also p-units. For j!=i this forces exactly v_p(v_j)=-2a, so their reduced denominators carry p^(2a), while the target A_i,B_i are p-units. For i=1 this gives modulo p^(2a):
再開条件の抜粋: An exact coefficient-pair range/multiplicity adapter strong enough to combine this primitive full M_rel^2 root line with AR-009 without double charging.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 37.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 623878
SOURCE_END: 626553
SOURCE_SHA256: afcdff45f1ed4cc6a5f416e38485147655c3bd1f8fb808da0e3c85f8333cfc55

CARD_ID: M3-T11-033


TYPE: EXACT_LOCAL_VALUATION / PRIMITIVE_JOINT_ROOTLINE
STATUS: PROVED_EXACT_WITH_OPEN_RANGE_ADAPTER


CLAIM:
For the M3-T11-032 cubic coefficient pair
X_sym=T_1-T_3,
Y_sym=T_2-D,
the joint congruence
X_sym+rho_rel Y_sym==0 mod M_rel^2
is primitive at every fresh prime.


Primewise, for p^a||m_i, the target anti-root v_i is a p-unit by its oriented root-line congruence. The retained fresh-unit filter makes the relative trace between the other two directions a p-unit. The two remaining unit-argument trace factors in v_i^2 are then also p-units.


For j!=i this forces exactly
v_p(v_j)=-2a,
so their reduced denominators carry p^(2a), while the target A_i,B_i are p-units.


For i=1 this gives modulo p^(2a):
T_1==D==0,
T_2==A_2*A_3*B_1,
T_3==A_1*A_2*A_3.
Hence both
X_sym==-A_1*A_2*A_3
and
Y_sym==A_2*A_3*B_1
are p-units.


Cyclically,
gcd(X_sym,Y_sym,M_rel)=1.


Therefore the full M_rel^2 modulus survives on one primitive common coefficient pair:
X_sym+rho_rel Y_sym==0 mod M_rel^2,
rho_rel^2==-1 mod M_rel^2,
M_rel^2 | X_sym^2+Y_sym^2.


NOVELTY:
This closes the exact fresh-content blocker of M3-T11-032. It is not the retracted common-v CRT and does not multiply three local density savings.


DOES_NOT_IMPLY:
No global active-M_rel saving until the physical height/range and pushforward multiplicity of (X_sym,Y_sym) are controlled on the same measure.


REOPEN_CONDITION:
An exact coefficient-pair range/multiplicity adapter strong enough to combine this primitive full M_rel^2 root line with AR-009 without double charging.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 37.


M3_T11_CUBIC_COEFFICIENT_PRIMITIVE_AT_FRESH_PRIMES=true
M3_T11_CUBIC_COEFFICIENT_FULL_MREL2_MODULUS_SURVIVES=true
CURRENT_SUPPORTING_ATTACK=ThreeAntiRootCubicCoefficientRootLineRangeAdapter
P_OVER_M3_LIMIT_PROVED=fals


---


e




---
ADDENDUM TO M3-T11-032 / M3-T11-033 — product-factorization no-double-charge correction


Exact identity:
X_sym+i*Y_sym=F_v(i)=product_i(i*B_i-A_i).


Hence
X_sym^2+Y_sym^2=product_i(A_i^2+B_i^2).


Therefore the full M_rel^2 norm divisibility on the cubic coefficient pair is exactly the Gaussian-product packaging of the three previously known one-core norm divisibilities.


M3-T11-032 and M3-T11-033 remain exact algebraic/router results.
However the proposed independent AR-009 range-adapter saving on (X_sym,Y_sym) is frozen: charging it as a new density factor would double-charge the same three one-core root lines.


SEMANTIC_VERDICT=UPDATE_EXISTING_FIREWALL
M3_T11_CUBIC_COEFFICIENT_AR009_INDEPENDENT_SAVING=false
M3_T11_CUBIC_COEFFICIENT_RANGE_ADAPTER_ROUTE_FROZEN=true
P_OVER_M3_LIMIT_PROVED=false


---
