# M3-T11-075 — The live principal-factor product squareclass is an exact Sturmian two-state law

CARD_ID: M3-T11-075
CANONICAL_CARD_KEY: M3-T11-075
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-075
現行一覧の状態: PROVED_EXACT / PRINCIPAL_PRODUCT_INTERSECTION_CLOSED / HK_SPLIT_ALLOCATION_OPEN
種別: EXACT_STRUCTURE / MORDELL-WEIL_TO_GLOBAL_SQUARECLASS_BRIDGE / THEOREM_GATE_REFINEMENT
要点: On the four live x=27/40 Mordell-Weil progressions, the canonical principal-factor product squareclass is the exact base/shifted Sturmian two-state law; the remaining first attack is H/K split-prime allocation/global coupling.
主張の抜粋: Let P_pr=alpha0*alpha-*alpha+ in Q(sqrt(-14)). On actual canonical translated-lift survivors, [P_pr]=[-chi_n] for epsilon=0 (n even) and [P_pr]=[2*chi_n] for epsilon=1 (n odd), where chi_n is the actual positive canonical p=3 denominator character from M3-T11-072/074. Equivalently [P_pr]=[(-1)^(n+1)*2^(n mod 2)*chi_n]. This closes the principal-product/global-squareclass insertion but gives no counting saving by itself.
対象・測度: Exact x=27/40 translated-lift carrier restricted to the four M3-T11-067 live Mordell-Weil progressions and canonical M3-T11-048 three-packet survivor locus.
依存関係: M3-T11-062; M3-T11-063; M3-T11-066; M3-T11-071; M3-T11-072; M3-T11-074.
再開条件の抜粋: Only if one of M3-T11-062/063/066/071/072/074 is retracted or its population adapter changes. Otherwise continue with residual H/K split-prime allocation/global coupling.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 83.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit

## Retained LEDGER source 1
SOURCE_START: 790107
SOURCE_END: 794564
SOURCE_SHA256: 69ca0d96352264fce6926932022df5f74b76d04bed69b1ca8bf104ba6f245588

## M3-T11-075
ID:
M3-T11-075
TYPE:
EXACT_STRUCTURE / MORDELL-WEIL_TO_GLOBAL_SQUARECLASS_BRIDGE / THEOREM_GATE_REFINEMENT
TITLE:
The live principal-factor product squareclass is an exact Sturmian two-state law
STATUS:
PROVED_EXACT / PRINCIPAL_PRODUCT_INTERSECTION_CLOSED / HK_SPLIT_ALLOCATION_OPEN
CLAIM:
Retain M3-T11-062, M3-T11-063, M3-T11-066, M3-T11-071, M3-T11-072, and M3-T11-074. In K=Q(sqrt(-14)), let P_pr=alpha0*alpha-*alpha+ be the M3-T11-062 principal-factor product. M3-T11-063 gives [P_pr]=[-delta] on the canonical three-packet translated-lift survivor locus.


Let chi_n be the actual positive canonical root-denominator p=3 character of the translated point: chi_n=(C_n|3) on epsilon=0 and chi_n=(C_n^T|3)=(A_n/5|3) on epsilon=1. M3-T11-071 gives kappa5=+1 on all four live progressions, so M3-T11-066 gives
(-1)^e2=chi_n,
(-1)^e7=(-1)^n*chi_n,
delta=2^e2*7^e7.


Therefore exactly:
- epsilon=0, n even: [P_pr]=[-chi_n];
- epsilon=1, n odd: [P_pr]=[2*chi_n].
Equivalently,
[P_pr]=[(-1)^(n+1)*2^(n mod 2)*chi_n].


With the retained Sturmian laws:
- epsilon=0, n==n0 mod 2656080, n0 in {+2,-2}:
  [P_pr]=[-rho(n0)*sigma^(n-1)*(-1)^floor(n*beta)];
- epsilon=1, n==n0 mod 2656080, n0 in {+1,-1}:
  [P_pr]=[2*rho_T(n0)*sigma_T^(n-1)*(-1)^floor(n*beta_T)].


Thus the principal-factor/global-squareclass insertion requested after M3-T11-074 is exact and closed. The unresolved first attack is the residual coupling of this forced Sturmian class with u*v=H*K, gcd(H,K)|7 and the M3-T11-060/061 fresh split-prime allocation laws.
POPULATION:
Exact x=27/40 translated-lift carrier restricted to the four M3-T11-067 live Mordell-Weil progressions and the canonical M3-T11-048 three-packet survivor locus. The formula is a law on actual translated-lift survivor states, not a claim that every ambient Mordell-Weil index is a survivor.
HEIGHT:
Inherited exact physical Stage37 height and reconstruction conditions. No height measure changes and no counting exponent is obtained by this card alone.
DEPENDS_ON:
M3-T11-062;
M3-T11-063;
M3-T11-066;
M3-T11-071;
M3-T11-072;
M3-T11-074.
IMPLIES:
The moving principal-product element squareclass is no longer an unresolved delta label. It is the exact base/shifted Sturmian two-state class above. The next legal first attack is the H/K split-allocation/global coupling, not another local-character or principal-product-squareclass calculation.
ALIASES:
X27Over40SturmianPrincipalProductSquareclass;
X27Over40TwoSturmianGlobalElementClass;
X27Over40PrincipalSquareclassMWBridge;
X27Over40SturmianPrincipalProductHKSplitAllocationIntersection.
DUPLICATE_OF:
none found under semantic rematch. M3-T11-063 proves [P_pr]=[-delta], M3-T11-066 transports delta to Mordell-Weil root characters, and M3-T11-072/074 prove the two Sturmian character laws, but no prior canonical card composes these into the exact live principal-product squareclass law.
SUPERSEDES:
the unresolved principal-squareclass insertion component of CURRENT_X27_FIRST_ATTACK=X27Over40TwoSturmianDeltaHKGlobalPacketIntersection. It does not supersede M3-T11-060/061 factor-allocation work.
DO_NOT_REPEAT:
Do not reopen either p=3 character law, p=5, ramified-7, or the global identity [P_pr]=[-delta].
Do not infer half-density or fixed-power pruning from Sturmian sign alternation on the ambient Mordell-Weil progression: P_pr is attached only after the translated-lift survivor condition is present.
Do not claim rational-point classification, a fixed-power saving, primary theorem-gate closure, or P(B)/M3(B) credit.
REOPEN_CONDITION:
Only if one of M3-T11-062/063/066/071/072/074 is retracted or its population adapter is changed. Otherwise continue with the residual H/K split-prime allocation/global coupling or one of the retained independent global closure routes.
DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 83.
FLAGS:
M3_T11_X_27_OVER_40_STURMIAN_PRINCIPAL_PRODUCT_SQUARECLASS_EXACT=true
M3_T11_X_27_OVER_40_PRINCIPAL_PRODUCT_GLOBAL_SQUARECLASS_INTERSECTION_CLOSED=true
M3_T11_X_27_OVER_40_HK_SPLIT_ALLOCATION_GLOBAL_COUPLING_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40SturmianPrincipalProductHKSplitAllocationIntersection
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-07
