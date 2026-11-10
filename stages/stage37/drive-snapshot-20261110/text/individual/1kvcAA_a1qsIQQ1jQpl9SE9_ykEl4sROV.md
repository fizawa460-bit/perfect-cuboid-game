# M3-XG-007 — double-space-triangle content theorem

CARD_ID: M3-XG-007
CANONICAL_CARD_KEY: M3-XG-007
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-XG-007
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE
要点: For a Stage14 physical raw two-face edge with primitive oriented face data F1=(S1,X1,H1), F2=(S2,X2,H2), g=gcd(S1,S2), define the physical face diagonals p=(S2/g)*H1, q=(S1/g)*H2, 
主張の抜粋: For a Stage14 physical raw two-face edge with primitive oriented face data F1=(S1,X1,H1), F2=(S2,X2,H2), g=gcd(S1,S2), define the physical face diagonals p=(S2/g)*H1, q=(S1/g)*H2, and nonshared edges x=(S2/g)*X1, y=(S1/g)*X2. Then p^2+y^2=R^2, q^2+x^2=R^2, and exactly c12=gcd(H1,X2)=gcd(p,y), c21=gcd(H2,X1)=gcd(q,x). T
対象・測度: whole Stage14 physical raw two-face graph with integral space diagonal.
依存関係: M3-XG-005 and exact Stage14 gluing.
再開条件の抜粋: none.
旧詳細位置: K16-C3-M3-ROUTE-CROSS-GCD.
旧詳細リンク: https://docs.google.com/document/d/1hRZvWUMvITpvzj8E6AI8hFnOc0PTmB1yO6RvvB6rhUg/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 245274
SOURCE_END: 246888
SOURCE_SHA256: 237080a7f20f94c9004b878896ca2d3743ee4515431d6aca7a53817a24f574cb

## M3-XG-007


TYPE: EXACT_STRUCTURE
STATUS: PROVED_EXACT


CLAIM:
For a Stage14 physical raw two-face edge with primitive oriented face data
F1=(S1,X1,H1), F2=(S2,X2,H2), g=gcd(S1,S2), define the physical face diagonals


p=(S2/g)*H1,
q=(S1/g)*H2,


and nonshared edges


x=(S2/g)*X1,
y=(S1/g)*X2.


Then


p^2+y^2=R^2,
q^2+x^2=R^2,


and exactly


c12=gcd(H1,X2)=gcd(p,y),
c21=gcd(H2,X1)=gcd(q,x).


Therefore c12 and c21 are precisely the contents of the two physical Pythagorean triples


(p,y,R),
(q,x,R)


sharing the same space diagonal R.


Since gcd(c12,c21)=1,


c_raw=c12*c21


is the product of the two coprime space-triangle contents.


Writing R=c12*c21*t, the normalized triples are primitive:


(p/c12, y/c12, c21*t),
(q/c21, x/c21, c12*t).


POPULATION:
whole Stage14 physical raw two-face graph with integral space diagonal.


HEIGHT:
exact R<=B.


DEPENDS_ON:
M3-XG-005 and exact Stage14 gluing.


IMPLIES:
the raw cross-gcd has a direct physical interpretation independent of endpoint/M3;
large c means the two auxiliary space Pythagorean triangles carry large coprime contents.


ALIASES:
double-space-triangle content theorem;
space-Pythagorean content factorization;
physical interpretation of c_raw.


DUPLICATE_OF:
none.


SUPERSEDES:
the view of c_raw as only an abstract cross-gcd of primitive-face coordinates.


DO_NOT_REPEAT:
Do not infer a B/C count merely by summing hypotenuse contents; the residual hypotenuse t still has O(B/c) ambient range and the two triples must reconstruct one physical raw edge.


REOPEN_CONDITION:
none.


DETAIL_DOC:
K16-C3-M3-ROUTE-CROSS-GCD.


---
