# M3-T11-011 — Möbius similarity-content factorization and small-direction energy disposal

CARD_ID: M3-T11-011
CANONICAL_CARD_KEY: M3-T11-011
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-011
現行一覧の状態: PROVED_EXACT / NEW LARGE-FACTOR REDUCTION
要点: Möbius similarity-content factorization and small-direction energy disposal
主張の抜粋: For every H-squareclass collision pair rho,sigma, define the unique projective direction [A:B]=[1-rho*sigma : rho+sigma]. After primitive integral scaling, A^2+B^2=N^2. For a primitive ratio vector v=(C0,X0)^T let M=[[-A,B],[B,A]]. Then M v = d v' for the primitive vector v' representing sigma, where d=gcd(BX0-AC0, AX0+BC0). Since M^2=N^2 I, the reverse primitive-reduction content is d'=N^2/d, and exactly d*d'=N^2. Hence max(d,d')>=N. In Gaussian form, when A=u^2-v^2, B=2uv, N=u^2+v^2, the transformation is multiplication by the Gaussian square (u-iv)^2, followed by conjugation and primitive reduction. For each fixed primitive Pythagorean direction, the Möbius map is a bijection on P^1(Q), so by M3-T11-010 and the Stage14 square-root raw-edge bound, I_(A,B)(B)<=B^(1/2+o(1)). There are O(L) primitive Pythagorean directions with N<=L. Therefore Q_H^{N<=L}(B) <= B^(1/2+o(1))*L. For L=B^(1/6-eta), Q_H^{N<=L}(B) <= B^(2/3-eta+o(1)) = o(B^(2/3)). Thus only collision directions with N>B^(1/6-o(1)) remain. Every such collision can be oriented so that its similarity content satisfies d>=N>B^(1/6-o(1)).
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 14.2-14.4.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 261597
SOURCE_END: 263372
SOURCE_SHA256: 6f08b355100b39ce79e10b9c32a1870bb7ce108d46e7555445acd073d98689b8

CARD_ID: M3-T11-011
TITLE: Möbius similarity-content factorization and small-direction energy disposal
STATUS: PROVED_EXACT / NEW LARGE-FACTOR REDUCTION
ROUTE: TrivialPartitionSecondSquareclassEnergy supporting subroute


RESULT:
For every H-squareclass collision pair rho,sigma, define the unique projective direction


[A:B]=[1-rho*sigma : rho+sigma].


After primitive integral scaling,


A^2+B^2=N^2.


For a primitive ratio vector v=(C0,X0)^T let


M=[[-A,B],[B,A]].


Then


M v = d v'


for the primitive vector v' representing sigma, where


d=gcd(BX0-AC0, AX0+BC0).


Since


M^2=N^2 I,


the reverse primitive-reduction content is


d'=N^2/d,


and exactly


d*d'=N^2.


Hence max(d,d')>=N.


In Gaussian form, when


A=u^2-v^2,
B=2uv,
N=u^2+v^2,


the transformation is multiplication by the Gaussian square (u-iv)^2, followed by conjugation and primitive reduction.


For each fixed primitive Pythagorean direction, the Möbius map is a bijection on P^1(Q), so by M3-T11-010 and the Stage14 square-root raw-edge bound,


I_(A,B)(B)<=B^(1/2+o(1)).


There are O(L) primitive Pythagorean directions with N<=L. Therefore


Q_H^{N<=L}(B)
<=
B^(1/2+o(1))*L.


For L=B^(1/6-eta),


Q_H^{N<=L}(B)
<=
B^(2/3-eta+o(1))
=
o(B^(2/3)).


Thus only collision directions with


N>B^(1/6-o(1))


remain. Every such collision can be oriented so that its similarity content satisfies


d>=N>B^(1/6-o(1)).


IMPLIES:
The old global H-energy gate reduces to a same-measure large-similarity-content tail.


NEW_GATE:
PythagoreanMobiusLargeSimilarityContentTail.


DO_NOT_REPEAT:
Do not multiply an ambient root-line density by the Stage14 square-root bound.
Do not return to a fixed-lambda B^o(1) claim.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 14.2-14.4.


---
