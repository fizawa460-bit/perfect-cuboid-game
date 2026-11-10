# M3-HIST21-INTERACTION-001 — Stage21 interaction theorem

CARD_ID: M3-HIST21-INTERACTION-001
CANONICAL_CARD_KEY: M3-HIST21-INTERACTION-001
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-HIST21-INTERACTION-001
現行一覧の状態: PROVED_AUDITED
種別: THEOREM_RESULT / INTERACTION_CLASSIFICATION
要点: Stage21 compares the integral-space-diagonal survival inside the primitive canonical exactly-one-face population against the ambient primitive canonical space-diagonal survival. Us
主張の抜粋: Stage21 compares the integral-space-diagonal survival inside the primitive canonical exactly-one-face population against the ambient primitive canonical space-diagonal survival. Using the exact leading source and target asymptotics M_1(B) ~ [3/(4*pi^2)] B^2 log B and N_1(B) ~ [kappa/(24*pi)] B(log B)^3, Stage21 proves 
対象・測度: source = primitive canonical exactly-one-face cuboids under R<=B with no space requirement; target = same population with integral space diagonal; control = unrestricted primitive 
依存関係: Stage21 final R02; M3-HIST16S-SPACE-001; M3-HIST17-N1-ASYMPTOTIC-001; E-1e exact M_1 source asymptotic frozen into Stage21.
再開条件の抜粋: a finer theorem canonically decomposing the log-squared enhancement into named pole/local-factor contributions, or a changed population.
旧詳細位置: Stage21 final self-contained bundle R02; Stage21 reusable Arsenal.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 534302
SOURCE_END: 537027
SOURCE_SHA256: 70c17e3be8e276060e197620ca1953fd64fd411551d746d56ad8b91e25919387

## M3-HIST21-INTERACTION-001
TYPE: THEOREM_RESULT / INTERACTION_CLASSIFICATION
STATUS: PROVED_AUDITED
CLAIM:
Stage21 compares the integral-space-diagonal survival inside the primitive canonical exactly-one-face population against the ambient primitive canonical space-diagonal survival.
Using the exact leading source and target asymptotics
M_1(B) ~ [3/(4*pi^2)] B^2 log B
and
N_1(B) ~ [kappa/(24*pi)] B(log B)^3,
Stage21 proves the transition law
N_1(B)/M_1(B)
~ [kappa*pi/18] * (log B)^2/B.
Directionwise, for q=ab,ac,bc,
N_{1,q}(B)/M_{1,q}(B)
~ [kappa*pi/18] * (log B)^2/B,
because the common positive chamber factor cancels.
Against the Stage16S ambient control
N_S^all(B)/U(B)
~ [9*zeta(3)/(8*pi*G)]/B,
the interaction quotient satisfies
[(N_1/M_1)/(N_S^all/U)]
~ [4*kappa*pi^2*G/(81*zeta(3))] * (log B)^2
-> infinity.
Hence the intrinsic polynomial cost of imposing an integral space diagonal is one power B^-1, while conditioning first on one integral face gives a positive logarithmic enhancement of order (log B)^2.
Ratio-level asymptotic independence is therefore false.
There is no new leading direction-specific interaction.
POPULATION:
source = primitive canonical exactly-one-face cuboids under R<=B with no space requirement;
target = same population with integral space diagonal;
control = unrestricted primitive canonical ambient population versus its integral-space-diagonal subpopulation.
HEIGHT:
common exact R<=B cutoff; on target objects d=R.
DEPENDS_ON:
Stage21 final R02;
M3-HIST16S-SPACE-001;
M3-HIST17-N1-ASYMPTOTIC-001;
E-1e exact M_1 source asymptotic frozen into Stage21.
IMPLIES:
one-face conditioning enhances space-diagonal survival by a factor asymptotic to a positive constant times (log B)^2 without changing the polynomial B^-1 cost.
ALIASES:
Stage21 interaction theorem;
one-face space survival constant;
positive log-squared enhancement;
ambient-control comparison.
DUPLICATE_OF:
S21-W01 and S21-W02 are the reusable Arsenal forms; this card records the Stage21 historical theorem/classification surface.
SUPERSEDES:
the Stage16S/17-era state where the interaction sign was deferred to Stage21.
DO_NOT_REPEAT:
Do not call the result stochastic independence.
Do not split the two logarithms into independent local or pole probabilities without a further theorem.
Do not multiply the ambient B^-1 control as an additional cost after already using the one-face transition ratio.
Do not infer the same interaction law for two-face or Euler populations.
REOPEN_CONDITION:
a finer theorem canonically decomposing the log-squared enhancement into named pole/local-factor contributions, or a changed population.
DETAIL_DOC:
Stage21 final self-contained bundle R02; Stage21 reusable Arsenal.
---
