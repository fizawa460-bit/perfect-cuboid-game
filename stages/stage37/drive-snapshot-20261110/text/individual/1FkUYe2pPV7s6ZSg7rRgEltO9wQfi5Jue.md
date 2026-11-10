# M3-CMINUS-002 — four-cross-gcd coordinates

CARD_ID: M3-CMINUS-002
CANONICAL_CARD_KEY: M3-CMINUS-002
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-CMINUS-002
現行一覧の状態: PROVED_EXACT
種別: EXACT_STRUCTURE
要点: With x=a-b, y=a+b, s=m-n, t=m+n, define pairwise-coprime cross gcds alpha=gcd(y,t), beta=gcd(x,s), gamma=gcd(y,s), delta=gcd(x,t). Then g_-=alpha*beta, g_+=gamma*delta, g=g_-*g_+. 
主張の抜粋: With x=a-b, y=a+b, s=m-n, t=m+n, define pairwise-coprime cross gcds alpha=gcd(y,t), beta=gcd(x,s), gamma=gcd(y,s), delta=gcd(x,t). Then g_-=alpha*beta, g_+=gamma*delta, g=g_-*g_+. After peeling these factors, C_-=gamma*delta*x0*y0*s0*t0. Therefore a fixed value C_-=c admits at most tau_6(c)=c^o(1) ordered residual pack
対象・測度: exact one-factor/M3 cross-gcd coordinates.
依存関係: M3-CMINUS-001 and primitive Euclid factorization.
再開条件の抜粋: none.
旧詳細位置: LEGACY-COLD Section98.0-98.3.
旧詳細リンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 296006
SOURCE_END: 297242
SOURCE_SHA256: c2ebb862d7c653fcae302caed645521b145ee90eab276d7e1e285dc3c0db2e97

## M3-CMINUS-002
TYPE: EXACT_STRUCTURE
STATUS: PROVED_EXACT


CLAIM:
With
x=a-b,
y=a+b,
s=m-n,
t=m+n,
define pairwise-coprime cross gcds
alpha=gcd(y,t),
beta=gcd(x,s),
gamma=gcd(y,s),
delta=gcd(x,t).
Then
g_-=alpha*beta,
g_+=gamma*delta,
g=g_-*g_+.
After peeling these factors,
C_-=gamma*delta*x0*y0*s0*t0.
Therefore a fixed value C_-=c admits at most
tau_6(c)=c^o(1)
ordered residual packets.
For each fixed residual packet, the M3 condition is a smooth even genus-one quartic in lambda=alpha/beta whose Jacobian has rational 2-torsion.


POPULATION:
exact one-factor/M3 cross-gcd coordinates.


HEIGHT:
physical height enters the packet multiplicity theorem.


DEPENDS_ON:
M3-CMINUS-001 and primitive Euclid factorization.


IMPLIES:
C_- has divisor-many packet complexity and fixed packets reduce to uniform elliptic-height counting.


ALIASES:
four-cross-gcd coordinates;
MinusCrossGcdLinearFactorization;
ExactMinusModulusPacketProduct;
FixedResidualM3QuarticSmooth.


DUPLICATE_OF:
none.


SUPERSEDES:
coarser C_- strata without residual packet factorization.


DO_NOT_REPEAT:
Do not count C_- as a completely free extra parameter after packetization.


REOPEN_CONDITION:
none.


DETAIL_DOC:
LEGACY-COLD Section98.0-98.3.


---
