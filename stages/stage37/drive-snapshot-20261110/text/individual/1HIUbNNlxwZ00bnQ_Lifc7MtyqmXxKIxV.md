# M3-T11-025 — Principal torus-trace K3 barrier and cross-gcd trivial-split escape

CARD_ID: M3-T11-025
CANONICAL_CARD_KEY: M3-T11-025
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-025
現行一覧の状態: PROVED_EXACT_STRUCTURE / DIRECT_COUNT_OPEN
種別: EXACT_STRUCTURE / FIREWALL / THEOREM_GATE
要点: Principal torus-trace K3 barrier and cross-gcd trivial-split escape
主張の抜粋: For x=Lambda(C), y=Lambda(s), z=Lambda(Cs), the torus traces satisfy x^2+y^2+z^2-x*y*z=4. The principal selector -x*y*z=w^2 therefore gives x^2+y^2+z^2+w^2=4. In half-angle coordinates c=a/b, u=m/n, the principal square cover is a double cover of P1xP1 branched in class (4,4)=-2K, with only ordinary branch crossings generically; its canonical resolution is K3. Hence fixed genus-one fibers do not by themselves globalize the principal count. This matches the Stage14-t41/t42 Kummer theorem species structurally.
対象・測度: Fixed-content/coefficient Step-A-complement active-tau packets under the exact M3 paired-Gaussian physical measure.
依存関係: M3-T11-023, M3-T11-024, Stage14-t41/t42 only as theorem-species ancestry.
再開条件の抜粋: A same-measure count for the large-d cross-gcd/root-line branch or the small-d simultaneous post-gcd square branch strong enough to beat B^(1/12) per fixed content packet.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 26.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 590226
SOURCE_END: 593485
SOURCE_SHA256: a172b7645948648ef1f1a3d2c9f4b17a5c2a88fcaf4baf49c04607fa6505586a

CARD_ID: M3-T11-025
TITLE: Principal torus-trace K3 barrier and cross-gcd trivial-split escape
TYPE: EXACT_STRUCTURE / FIREWALL / THEOREM_GATE
STATUS: PROVED_EXACT_STRUCTURE / DIRECT_COUNT_OPEN
ROUTE: TrivialSplitCyclicDirectionOneThird


CLAIM:
For x=Lambda(C), y=Lambda(s), z=Lambda(Cs), the torus traces satisfy


x^2+y^2+z^2-x*y*z=4.


The principal selector -x*y*z=w^2 therefore gives


x^2+y^2+z^2+w^2=4.


In half-angle coordinates c=a/b, u=m/n, the principal square cover is a double cover of P1xP1 branched in class (4,4)=-2K, with only ordinary branch crossings generically; its canonical resolution is K3. Hence fixed genus-one fibers do not by themselves globalize the principal count. This matches the Stage14-t41/t42 Kummer theorem species structurally.


EXPONENT FIREWALL:
If r(kappa) are squareclass multiplicities and A1=sum r(kappa)^2, then


# active tau <= r(1) <= sqrt(A1).


Thus an energy route must prove


A1 << B^(1/6-2*delta)


to obtain the fixed-content target B^(1/12-delta).
The generic Stage14 target A1<<H*B^o(1) is not sufficient unless H itself is separately proved below B^(1/6-2*delta+o(1)) on this exact M3 packet.


DIRECT ARITHMETIC COLLAPSE:
Put


A0=a^2-b^2,
M0=m^2-n^2,
X=A0*M0,
Y=4*a*b*m*n.


For


L5=am-an-bm-bn,
L6=am+an+bm-bn,


one has exactly


L5*L6=X-Y,


so the six-factor selector becomes


W^2=-8*X*(X-Y).


For primitive (a,b),(m,n), define


d1=gcd_odd(A0,m*n),
d2=gcd_odd(M0,a*b),
d=d1*d2.


Then gcd(d1,d2)=1 and


gcd_odd(X,Y)=gcd_odd(X,X-Y)=d.


Moreover d splits into four pairwise-coprime cross cells


gcd_odd(A0,m),
gcd_odd(A0,n),
gcd_odd(M0,a),
gcd_odd(M0,b).


After dividing by d, the odd parts of X/d and (X-Y)/d are coprime; since -8X(X-Y) is square, each odd cofactor is separately a square. Only a finite sign/2-adic state remains.


POPULATION:
Fixed-content/coefficient Step-A-complement active-tau packets under the exact M3 paired-Gaussian physical measure.


HEIGHT:
Exact physical R<=B retained.


DEPENDS_ON:
M3-T11-023,
M3-T11-024,
Stage14-t41/t42 only as theorem-species ancestry.


IMPLIES:
The K3/Kummer formulation is structural but not yet exponent-sufficient.
A more arithmetic direct route exists through the charged-once cross-gcd d and two post-gcd square cofactors.


ALIASES:
CyclicTorusTracePrincipalK3Barrier;
CyclicTorusTracePrincipalCrossGcdTrivialSplit.


DO_NOT_REPEAT:
Do not claim K3 geometry alone gives a quantitative rational-point saving.
Do not import Stage14 near-linear principal energy as if it met the M3 1/12 exponent.
Do not multiply a cross-gcd lattice density by an independently proved endpoint ceiling.
Do not treat the two post-gcd square cofactors as independent probabilities.
Do not recharge determinant/Jacobian savings already paid by the same coordinate map.


REOPEN_CONDITION:
A same-measure count for the large-d cross-gcd/root-line branch or the small-d simultaneous post-gcd square branch strong enough to beat B^(1/12) per fixed content packet.


NEW_GATE:
CyclicTorusTracePrincipalCrossGcdTrivialSplit.


REQUIRED_OUTPUT:
Uniformly for fixed content/coefficient packet,


# active tau << B^(1/12-delta)


for some fixed delta>0.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 26.


P_OVER_M3_LIMIT_PROVED=false


---
