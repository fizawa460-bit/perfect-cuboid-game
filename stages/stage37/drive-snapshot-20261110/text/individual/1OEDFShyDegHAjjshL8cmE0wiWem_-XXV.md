# M3-T11-064 — Exact split-3 delta-parity router on the three-packet survivor locus

CARD_ID: M3-T11-064
CANONICAL_CARD_KEY: M3-T11-064
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-064
現行一覧の状態: PROVED_EXACT_LOCAL_STRUCTURE / GLOBAL CLASSIFICATION OPEN
種別: EXACT_LOCAL_STRUCTURE / THEOREM_GATE REFINEMENT
要点: On the canonical x=27/40 three-packet survivor locus, the M3-T11-062 principal-factor product has local squareclass [-delta] at both primes above 3 because M3-T11-063 makes d a rat
主張の抜粋: On the canonical x=27/40 three-packet survivor locus, the M3-T11-062 principal-factor product has local squareclass [-delta] at both primes above 3 because M3-T11-063 makes d a rational square. Using the Hensel roots s=38,205 modulo 243 of s^2=-14, the exact M3-T11-048 3-adic packet residues give: Packets I/II: [-delta
対象・測度: Exact x=27/40 translated-lift carrier restricted to the canonical M3-T11-048 three-packet survivor locus.
依存関係: M3-T11-048; M3-T11-059; M3-T11-062; M3-T11-063.
再開条件の抜粋: Compute the split-5 local element-squareclass of the principal-factor product on the surviving two delta candidates, preferably resolving the factor-7 bit exactly; then intersect survivors with M3-T11-057.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 71.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 731180
SOURCE_END: 733671
SOURCE_SHA256: c515cb16b4b510705009aae596dfa3b9f2f9e1806ddb88703907f2e26a2dee1a

## M3-T11-064
ID:
M3-T11-064
TYPE:
EXACT_LOCAL_STRUCTURE / THEOREM_GATE REFINEMENT
TITLE:
Exact split-3 delta-parity router on the three-packet survivor locus
STATUS:
PROVED_EXACT_LOCAL_STRUCTURE / GLOBAL CLASSIFICATION OPEN
CLAIM:
On the canonical x=27/40 three-packet survivor locus, the M3-T11-062 principal-factor product has local squareclass [-delta] at both primes above 3 because M3-T11-063 makes d a rational square. Using the Hensel roots s=38,205 modulo 243 of s^2=-14, the exact M3-T11-048 3-adic packet residues give:
Packets I/II: [-delta]=[b] in Q_3^x/Q_3^x2.
Packet III: [-delta]=[2b] in Q_3^x/Q_3^x2.
Therefore the four delta values are halved pointwise:
Packets I/II: b==1 mod3 => delta in {2,14}; b==2 mod3 => delta in {1,7}.
Packet III: b==1 mod3 => delta in {1,7}; b==2 mod3 => delta in {2,14}.
POPULATION:
Exact x=27/40 translated-lift carrier restricted to the canonical M3-T11-048 three-packet survivor locus.
DEPENDS_ON:
M3-T11-048;
M3-T11-059;
M3-T11-062;
M3-T11-063.
IMPLIES:
The active delta-class match no longer has four live packets per survivor. The remaining local bit is whether the allowed parity class contains the factor 7. The next non-duplicative attack is the split-5 element-squareclass discriminator, then intersection with M3-T11-057.
ALIASES:
X27Over40Split3DeltaParityRouter;
X27Over40DeltaCandidatesHalved;
X27Over40Split5DeltaSevenBitRouter.
DUPLICATE_OF:
none found. M3-T11-059 creates four delta packets; M3-T11-063 collapses d to a square but does not separate the four delta classes locally.
DO_NOT_REPEAT:
Do not reopen all four delta values after the b mod3 class is known.
Do not infer rational-point classification, fixed-power saving, or P/M3 credit from the two-candidate reduction.
REOPEN_CONDITION:
Compute the split-5 local element-squareclass of the principal-factor product on the surviving two delta candidates, preferably resolving the factor-7 bit exactly; then intersect survivors with M3-T11-057.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 71.
FLAGS:
M3_T11_X_27_OVER_40_SPLIT3_DELTA_PARITY_ROUTER=true
M3_T11_X_27_OVER_40_DELTA_CANDIDATES_HALVED=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40Split5DeltaSevenBitRouter
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-064
