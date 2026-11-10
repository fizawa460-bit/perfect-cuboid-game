# M3-XG-008 — 4bn cross-gcd adapter

CARD_ID: M3-XG-008
CANONICAL_CARD_KEY: M3-XG-008
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-XG-008
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE
要点: Under the exact Stage14-4bn bijection, let F2=(S2,X2,H2) and F3=(S3,X3,H3) be the positive cross-square pair, and let F1=(S1,X1,H1) be the reconstructed primitive face of the physical raw edge. Then the first raw cross-gcd factor is exactly c12=gcd(H1,X2) =X2/gcd(X2,X3), and the physical space diagonal is R=c12*H3. The second raw cross-gcd factor satisfies c21=gcd(H2,X1) =gcd(H2,R) =gcd(H2,H3), because c12|X2 and gcd(H2,X2)=1. Therefore boxed: c_raw = [X2/gcd(X2,X3)] * gcd(H2,H3). Equivalently, 
主張の抜粋: Under the exact Stage14-4bn bijection, let F2=(S2,X2,H2) and F3=(S3,X3,H3) be the positive cross-square pair, and let F1=(S1,X1,H1) be the reconstructed primitive face of the physical raw edge. Then the first raw cross-gcd factor is exactly c12=gcd(H1,X2) =X2/gcd(X2,X3), and the physical space diagonal is R=c12*H3. The second raw cross-gcd factor satisfies c21=gcd(H2,X1) =gcd(H2,R) =gcd(H2,H3), because c12|X2 and gcd(H2,X2)=1. Therefore boxed: c_raw = [X2/gcd(X2,X3)] * gcd(H2,H3). Equivalently, boxed: R/c_raw = H3/gcd(H2,H3).
対象・測度: whole Stage14 physical raw two-face graph under the exact 4bn positive-cross-square bijection.
依存関係: M3-XG-005; Stage14-4bn exact bijection; Stage14-s7-03 identity gcd(H1,X2)=X2/gcd(X2,X3).
再開条件の抜粋: none.
旧詳細位置: K16-C3-M3-ROUTE-CROSS-GCD.
旧詳細リンク: https://docs.google.com/document/d/1hRZvWUMvITpvzj8E6AI8hFnOc0PTmB1yO6RvvB6rhUg/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 246888
SOURCE_END: 248546
SOURCE_SHA256: 1f96a5f212b11ad9fef9593e4d2a6d7ab5be163b06316684e4adf496da62c5aa

## M3-XG-008


TYPE: EXACT_STRUCTURE
STATUS: PROVED_EXACT


CLAIM:
Under the exact Stage14-4bn bijection, let F2=(S2,X2,H2) and F3=(S3,X3,H3) be the positive cross-square pair, and let F1=(S1,X1,H1) be the reconstructed primitive face of the physical raw edge.


Then the first raw cross-gcd factor is exactly


c12=gcd(H1,X2)
   =X2/gcd(X2,X3),


and the physical space diagonal is


R=c12*H3.


The second raw cross-gcd factor satisfies


c21=gcd(H2,X1)
   =gcd(H2,R)
   =gcd(H2,H3),


because c12|X2 and gcd(H2,X2)=1.


Therefore


boxed:
c_raw
=
[X2/gcd(X2,X3)] * gcd(H2,H3).


Equivalently,


boxed:
R/c_raw
=
H3/gcd(H2,H3).


POPULATION:
whole Stage14 physical raw two-face graph under the exact 4bn positive-cross-square bijection.


HEIGHT:
exact physical space diagonal R<=B.


DEPENDS_ON:
M3-XG-005;
Stage14-4bn exact bijection;
Stage14-s7-03 identity gcd(H1,X2)=X2/gcd(X2,X3).


IMPLIES:
one cross-gcd factor is exactly the Stage14 true cross-gcd already present in the sharp cutoff;
the residual variable t=R/c_raw is exactly the reduced hypotenuse quotient H3/gcd(H2,H3).


ALIASES:
4bn cross-gcd adapter;
cross-free partner-leg quotient times hypotenuse gcd;
reduced-H3 identity;
R-over-c reduced hypotenuse.


DUPLICATE_OF:
none.


SUPERSEDES:
the need to identify c_raw with Stage14's later internal packet variable called cross-root gcd H.


DO_NOT_REPEAT:
Do not identify gcd(H2,H3) with the final Stage14 common core C without an exact proof.
Do not infer a tail saving only from H3/gcd(H2,H3)<=B/C; the ambient number of reduced quotient values is too large by itself.


REOPEN_CONDITION:
none.


DETAIL_DOC:
K16-C3-M3-ROUTE-CROSS-GCD.
