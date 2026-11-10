# M3-T11-012 — Möbius similarity content is norm over bilinear gcd

CARD_ID: M3-T11-012
CANONICAL_CARD_KEY: M3-T11-012
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-012
現行一覧の状態: EXACT_CORRECTION / PREVIOUS_GATE_RETRACTED
要点: Möbius similarity content is norm over bilinear gcd
主張の抜粋: For primitive collision ratio vectors v=(C,X), v'=(C',X'), put S=C^2+X^2, S'=C'^2+X'^2, L=XX'-CC', K=CX'+C'X, g=gcd(L,K). If the H-squareclasses collide then L^2+K^2=S*S'=Q^2. The primitive Möbius/Pythagorean direction is A=L/g, B=K/g, N=Q/g. With M=[[-A,B],[B,A]], one has exactly M v=(S/g)v', M v'=(S'/g)v. Hence the two similarity contents are d=S/g, d'=S'/g, and N=sqrt(S*S')/g. Therefore d*d'=N^2 is automatic. After orienting S>=S', the inequality d>=N is equivalent simply to S>=S'. Thus large d is not an independent arithmetic restriction, and the root-line congruence Mv==0 mod d cannot be charged as a new saving after the collision partner has already been fixed. Also, with z=X+iC and z'=X'+iC', z*z'=g*(unit)*eta^2, where N(eta)=N. This gives an exact same/opposite Gaussian-orientation decomposition, but no global saving is transferred from a different measure.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 15.1-15.2.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 263372
SOURCE_END: 264893
SOURCE_SHA256: f550b9c348855d1fe55c1fb7414c230d2f17b51962b7a361e9ae097b40dca5a8

CARD_ID: M3-T11-012
TITLE: Möbius similarity content is norm over bilinear gcd
STATUS: EXACT_CORRECTION / PREVIOUS_GATE_RETRACTED
ROUTE: TrivialPartitionSecondSquareclassEnergy supporting subroute


RESULT:
For primitive collision ratio vectors


v=(C,X), v'=(C',X'),


put


S=C^2+X^2,
S'=C'^2+X'^2,
L=XX'-CC',
K=CX'+C'X,
g=gcd(L,K).


If the H-squareclasses collide then


L^2+K^2=S*S'=Q^2.


The primitive Möbius/Pythagorean direction is


A=L/g,
B=K/g,
N=Q/g.


With


M=[[-A,B],[B,A]],


one has exactly


M v=(S/g)v',
M v'=(S'/g)v.


Hence the two similarity contents are


d=S/g,
d'=S'/g,


and


N=sqrt(S*S')/g.


Therefore d*d'=N^2 is automatic.


After orienting S>=S', the inequality d>=N is equivalent simply to S>=S'. Thus large d is not an independent arithmetic restriction, and the root-line congruence Mv==0 mod d cannot be charged as a new saving after the collision partner has already been fixed.


Also, with z=X+iC and z'=X'+iC',


z*z'=g*(unit)*eta^2,


where N(eta)=N.


This gives an exact same/opposite Gaussian-orientation decomposition, but no global saving is transferred from a different measure.


RETRACTS:
PythagoreanMobiusLargeSimilarityContentTail as a new theorem gate.


RETAINS:
The small-direction estimate
Q_H^{N<=B^(1/6-eta)}=o(B^(2/3))
from M3-T11-011 remains valid.


DO_NOT_REPEAT:
Do not treat large similarity content d as an additional root-line density after conditioning on the collision pair.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE sections 15.1-15.2.


---
