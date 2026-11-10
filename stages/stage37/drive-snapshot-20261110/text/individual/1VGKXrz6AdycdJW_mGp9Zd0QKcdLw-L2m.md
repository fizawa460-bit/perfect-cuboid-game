# M3-T11-076 — X27Over40HKFourNeighborDenominatorRouter

CARD_ID: M3-T11-076
CANONICAL_CARD_KEY: M3-T11-076
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-076
現行一覧の状態: PROVED_EXACT / HOSTILE_AUDIT_PASS
種別: EXACT_STRUCTURE / MORDELL-WEIL_HK_ROUTER / SAME_COSET_DENOMINATOR_BRIDGE
要点: Fresh H/K source factors equal four neighboring Mordell-Weil root-denominator fresh parts.
主張の抜粋: For S={2,3,5,7}, (H^sharp)^2=(C_{n-2,epsilon} C_{n+2,epsilon})^sharp and K^sharp=(C_{n-1,epsilon} C_{n+1,epsilon})^sharp. Primewise H valuations double on exactly one n±2 neighbor; K valuations occur unchanged on exactly one n±1 neighbor. On epsilon=0 / Packet III every fresh K-side prime has (2|p)=+1.
対象・測度: Exact canonical x=27/40 translated-lift three-packet survivor locus; operationally the four live Mordell-Weil progressions.
依存関係: M3-T11-058; M3-T11-060; M3-T11-063; M3-T11-066; current frontier M3-T11-075.
再開条件の抜粋: Reopen only if the H/K normalization, U=2500+35000(a/b)^2, or canonical root-denominator dictionary changes. Remaining u/v split allocation is still open.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 84.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 794564
SOURCE_END: 799156
SOURCE_SHA256: 5eae87c967da8524ad1406946b9d932596277824bca0e17005c18877a83b7140

## M3-T11-076 — exact H/K neighboring Mordell–Weil denominator router


ID:
M3-T11-076


TYPE:
EXACT_STRUCTURE / MORDELL-WEIL_HK_ROUTER / SAME_COSET_DENOMINATOR_BRIDGE


STATUS:
PROVISIONAL_EXACT / AUDIT_PENDING


CLAIM:
On the exact x=27/40 translated-lift carrier, let P_{n,epsilon}=nQ+epsilon*T on E2, and let C_{m,epsilon} be the positive canonical root denominator of U(P_{m,epsilon}). For N^sharp denoting the part supported outside S={2,3,5,7}, the M3-T11-060 source factors satisfy exactly
(H^sharp)^2=(C_{n-2,epsilon}*C_{n+2,epsilon})^sharp,
K^sharp=(C_{n-1,epsilon}*C_{n+1,epsilon})^sharp.
Primewise: p^e||H iff exactly one n±2 neighbor denominator has p-valuation 2e; p^e||K iff exactly one n±1 neighbor denominator has p-valuation e. The sign is unique at fresh p.


POPULATION:
Exact canonical x=27/40 translated-lift three-packet survivor locus; operationally restricted to the four M3-T11-067 live Mordell-Weil progressions when used in the current frontier. The identity itself is primewise on the translated-lift carrier away from S={2,3,5,7}.


HEIGHT:
Exact inherited physical height; no ambient-box replacement and no multiplicity change.


DEPENDS_ON:
M3-T11-058 translated-lift parameter U=2500+35000(a/b)^2;
M3-T11-060 exact H/K normalization from a and J=100a^2+7b^2;
M3-T11-063/M3-T11-066 packet and canonical root-denominator dictionaries;
U=2500 at +/-2Q, U=50 at +/-Q;
C_2=1 and C_4=18 for uniqueness of the neighboring sign;
M3-T11-075 only for the live-frontier intersection target.


PROOF_CORE:
The exact algebra gives U-2500=35000*a^2/b^2 and U-50=350*J/b^2. At every p outside {2,3,5,7}, the target points +/-2Q and +/-Q are good p-integral points with unit y-coordinate. Thus x-x(R) is a local uniformizer at R, and translation to O identifies its valuation with the formal-parameter valuation, which equals v_p of the canonical root denominator. The a^2 identity doubles H-side valuation; the J identity preserves K-side valuation. Since H and K differ from a and J only by fixed-S factors, the displayed fresh-part identities follow. Simultaneous +/- signs would force a fresh denominator prime of 4Q or 2Q, excluded by C_4=18 and C_2=1.


PACKET_COROLLARY:
On Packet III (hence the epsilon=0 live progressions), the canonical root formulas give
K=(A^2-50*C^2)/350 for d=9,
K=(A^2-50*C^2)/14 for d=225.
Therefore every fresh K-side prime satisfies (2|p)=+1. The generic K-side inert/deterministic case of M3-T11-061 is absent on the live Packet-III locus.


IMPLIES:
The residual H/K fresh source data after M3-T11-075 are not independent rational factor data: they are exactly encoded by four neighboring canonical root denominators on the same Mordell-Weil coset. The current first attack can therefore be rewritten as a Sturmian-principal-product / four-neighbor-denominator allocation intersection.


ALIASES:
X27Over40HKFourNeighborDenominatorRouter;
X27Over40MWHKNeighborSupport;
X27Over40SturmianPrincipalProductFourNeighborDenominatorAllocationIntersection.


DUPLICATE_OF:
none found under semantic rematch. M3-T11-060/061 give the rational source-factor allocation laws; M3-T11-066 gives the root-coordinate dictionary; no prior card identifies the complete fresh H/K valuation data with n±1,n±2 same-coset root denominators.


SUPERSEDES:
the treatment of fresh H and K as unrelated source factors in the current M3-T11-075 continuation. It does not supersede the u/v allocation tests of M3-T11-060/061.


DO_NOT_REPEAT:
Do not return to H and K as unrelated fresh-prime sources.
Do not infer independence or density from the four neighboring denominator factors.
Do not reopen local p=3/p=5/p=7 character routing or [P_pr]=[-delta].
Do not claim the u/v split allocation is solved.


REOPEN_CONDITION:
Only if the M3-T11-060 H/K normalization, the translated-lift identity U=2500+35000(a/b)^2, or the M3-T11-066 canonical root-denominator dictionary is retracted or changed.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 84.


FLAGS:
M3_T11_X_27_OVER_40_HK_FRESH_TO_FOUR_NEIGHBOR_DENOMINATORS_EXACT=true
M3_T11_X_27_OVER_40_EPSILON0_K_FRESH_TWO_SPLIT_ONLY=true
M3_T11_X_27_OVER_40_HK_SPLIT_ALLOCATION_GLOBAL_COUPLING_PROVED=false
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40SturmianPrincipalProductFourNeighborDenominatorAllocationIntersection
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-076
