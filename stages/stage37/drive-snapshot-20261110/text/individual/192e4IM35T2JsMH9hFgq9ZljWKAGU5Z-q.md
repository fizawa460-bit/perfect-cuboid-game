# M3-T11-021 — Six-bilinear selector inherits tH8/tH9 Route-A Hecke infrastructure

CARD_ID: M3-T11-021
CANONICAL_CARD_KEY: M3-T11-021
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-021
現行一覧の状態: PROVED_EXACT_ADAPTER / PRINCIPAL_ENERGY_OPEN
要点: Six-bilinear selector inherits tH8/tH9 Route-A Hecke infrastructure
主張の抜粋: Let P_x = 2*product_{i<j} F_ij^+F_ij^- be the integer six-bilinear detector for one ambient fixed-content relative-core packet x. The raw character chi_l(P_x) does not admit the separated one-variable coefficient structure required by the direct quadratic/Jacobi large-sieve route. However, with an external good split auxiliary prime l=N(varpi), the exact tH8 trilinear form applies: T = sum_varpi sum_x a_varpi d_x chi_{N(varpi)}(P_x). After one Cauchy step, K_L(x,y) = sum_varpi chi_{N(varpi)}(P_xP_y). Writing sigma_x=[P_x], every good auxiliary prime satisfies chi_l(P_xP_y) = chi_{D(sigma_x sigma_y)}(l). Therefore the tH9 Route-A norm-induced quadratic-Hecke certificate is available for every nonprincipal squareclass cross-kernel.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 22.2-22.4.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 389135
SOURCE_END: 390981
SOURCE_SHA256: 77675cb772ed1dbb9b35577905b4b5e0c06372ec93c0f914d606c79f3d37799a

CARD_ID: M3-T11-021
TITLE: Six-bilinear selector inherits tH8/tH9 Route-A Hecke infrastructure
STATUS: PROVED_EXACT_ADAPTER / PRINCIPAL_ENERGY_OPEN
ROUTE: TrivialSplitCyclicDirectionOneThird


RESULT:
Let


P_x
=
2*product_{i<j} F_ij^+F_ij^-


be the integer six-bilinear detector for one ambient fixed-content relative-core packet x.


The raw character


chi_l(P_x)


does not admit the separated one-variable coefficient structure required by the direct quadratic/Jacobi large-sieve route.


However, with an external good split auxiliary prime l=N(varpi), the exact tH8 trilinear form applies:


T
=
sum_varpi sum_x
a_varpi d_x chi_{N(varpi)}(P_x).


After one Cauchy step,


K_L(x,y)
=
sum_varpi
chi_{N(varpi)}(P_xP_y).


Writing sigma_x=[P_x], every good auxiliary prime satisfies


chi_l(P_xP_y)
=
chi_{D(sigma_x sigma_y)}(l).


Therefore the tH9 Route-A norm-induced quadratic-Hecke certificate is available for every nonprincipal squareclass cross-kernel.


BOUNDARY:
Actual endpoint packets have sigma_x=1. Hence the endpoint target is a principal squareclass fiber, on which the Hecke character gives no cancellation.


The remaining problem is the same-measure principal squareclass incidence after summing over moving ordered relative-core pairs.


M3-T11-016 supplies only the fixed-two fiber B^o(1) input.


NEW_GATE:
CyclicSixBilinearPrincipalSquareclassPairIncidenceOneTwelfth.


REQUIRED_OUTPUT:
For each fixed content/coefficient packet, prove enough principal-incidence sparsity to give


# active tau
<<
B^(1/12-delta)


for some fixed delta>0.


DO_NOT_REPEAT:
Do not call the raw selector FI-ready.
Do not count nonprincipal Hecke cancellation as a saving on the principal endpoint class.
Do not treat fixed-two B^o(1) as a moving-pair bound.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 22.2-22.4.


---
