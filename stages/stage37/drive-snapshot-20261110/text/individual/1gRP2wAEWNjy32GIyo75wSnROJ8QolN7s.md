# M3-T11-029 — principal anti-root correction

CARD_ID: M3-T11-029
CANONICAL_CARD_KEY: M3-T11-029
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-029
現行一覧の状態: PROVED_EXACT_WITH_OPEN_COUNTING_GATE
種別: EXACT_STRUCTURE / CORRECTION / THEOREM_GATE
要点: The M3-T11-028 distinguished root z=1+D*t/(C*s) is anti-rational under Gaussian conjugation: conj(z)=-z. Hence z=i*v with v in Q, not z in Q. Consequently K=-Lambda(C)*Lambda(s)*Lambda(C*s)=z^2=-v^2, so the principal trace product satisfies Lambda(C)*Lambda(s)*Lambda(C*s)=v^2. On the relative-fresh G_3 branch, with m=tau_3^sharp and mathfrak_M_3=(G_3^sharp)^2, the correct fresh condition is i*v==1 mod mathfrak_M_3. Writing v=A/B reduced gives the orientation-dependent primitive root line A==rho_
主張の抜粋: The M3-T11-028 distinguished root z=1+D*t/(C*s) is anti-rational under Gaussian conjugation: conj(z)=-z. Hence z=i*v with v in Q, not z in Q. Consequently K=-Lambda(C)*Lambda(s)*Lambda(C*s)=z^2=-v^2, so the principal trace product satisfies Lambda(C)*Lambda(s)*Lambda(C*s)=v^2. On the relative-fresh G_3 branch, with m=tau_3^sharp and mathfrak_M_3=(G_3^sharp)^2, the correct fresh condition is i*v==1 mod mathfrak_M_3. Writing v=A/B reduced gives the orientation-dependent primitive root line A==rho_m*B mod m^2, rho_m^2==-1 mod m^2, and therefore m^2 | A^2+B^2. The prior M3-T11-028 claims m^2 | Num(z-1) and H(z)>=m^2/2 are retracted. Fixed v still gives a smooth genus-one cubic X*Y*(X+Y-v^2-4)+v^4=0 with rational 3-torsion and B^o(1) physical endpoint multiplicity. For T=tau_0*tau_1*tau_2 there is a fixed packet denominator carrier L_pkt such that the reduced denominator B of v divides L_pkt*T^2 and gcd(m,L_pkt*T)=1. Thus for fixed (T,m,packet), # compatible rational v <= B^o(1)*(1+L_pkt*T^2/m^2).
対象・測度: Exact fixed-content/coefficient relative-fresh endpoint packets on the TrivialSplitCyclicDirectionOneThird route.
依存関係: M3-T11-024 paired Gaussian adapter; M3-T11-026 fresh squared modulus; the full double-lift equation retained in M3-T11-028; AR-009 only as local primitive root-line counting infrastructure.
再開条件の抜粋: A same-physical-measure theorem controlling moving (T,m) occupancy/root-line support strongly enough to give # active tau << B^(1/12-delta) per fixed content/coefficient packet.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 30.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 609158
SOURCE_END: 612191
SOURCE_SHA256: 8083fb048fcd634bef850cd4b24ebf064571e59a785f0ee36d7cefad2fae1f7d

CARD_ID: M3-T11-029


TYPE: EXACT_STRUCTURE / CORRECTION / THEOREM_GATE
STATUS: PROVED_EXACT_WITH_OPEN_COUNTING_GATE


CLAIM:
The M3-T11-028 distinguished root
z=1+D*t/(C*s)
is anti-rational under Gaussian conjugation:
conj(z)=-z.
Hence z=i*v with v in Q, not z in Q.


Consequently
K=-Lambda(C)*Lambda(s)*Lambda(C*s)=z^2=-v^2,
so the principal trace product satisfies
Lambda(C)*Lambda(s)*Lambda(C*s)=v^2.


On the relative-fresh G_3 branch, with m=tau_3^sharp and mathfrak_M_3=(G_3^sharp)^2,
the correct fresh condition is
i*v==1 mod mathfrak_M_3.
Writing v=A/B reduced gives the orientation-dependent primitive root line
A==rho_m*B mod m^2,
rho_m^2==-1 mod m^2,
and therefore
m^2 | A^2+B^2.


The prior M3-T11-028 claims
m^2 | Num(z-1)
and
H(z)>=m^2/2
are retracted.


Fixed v still gives a smooth genus-one cubic
X*Y*(X+Y-v^2-4)+v^4=0
with rational 3-torsion and B^o(1) physical endpoint multiplicity.


For T=tau_0*tau_1*tau_2 there is a fixed packet denominator carrier L_pkt such that the reduced denominator B of v divides L_pkt*T^2 and gcd(m,L_pkt*T)=1.
Thus for fixed (T,m,packet),
# compatible rational v
<= B^o(1)*(1+L_pkt*T^2/m^2).


POPULATION:
Exact fixed-content/coefficient relative-fresh endpoint packets on the TrivialSplitCyclicDirectionOneThird route.


HEIGHT:
Exact physical R<=B. The fixed-(T,m) root-line bound uses only packet-derived denominator carriers and the bounded real range |v|<=2*sqrt(2).


DEPENDS_ON:
M3-T11-024 paired Gaussian adapter;
M3-T11-026 fresh squared modulus;
the full double-lift equation retained in M3-T11-028;
AR-009 only as local primitive root-line counting infrastructure.


IMPLIES:
The relative-fresh branch remains one-dimensional at power scale, but its correct arithmetic receiver is moving oriented Gaussian root-line occupancy, not a rational square-divisor threshold on z-1.


ALIASES:
principal anti-root correction;
relative-fresh v-root-line;
anti-rational torus root;
Gaussian root-line principal compression.


DUPLICATE_OF:
none.
AR-009 is the local lattice engine, not the same M3 same-measure moving-modulus theorem.


SUPERSEDES:
The relative-fresh counting gate and rational-root/square-divisor portion of M3-T11-028.
It does not supersede M3-T11-028's exact conic adapter or fixed-root/fixed-v elliptic compression.


DO_NOT_REPEAT:
Do not assert z in Q.
Do not use m^2|Num(z-1).
Do not use H(z)>=m^2/2.
Do not convert m^2|A^2+B^2 into an independent square-divisor probability.
Do not infer a global active-tau saving from fixed-(T,m) AR-009 spacing alone.
Do not ignore moving modulus occupancy/core-size distribution.


REOPEN_CONDITION:
A same-physical-measure theorem controlling moving (T,m) occupancy/root-line support strongly enough to give
# active tau << B^(1/12-delta)
per fixed content/coefficient packet.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 30.


CURRENT_RELATIVE_FRESH_GATE=FreshRelativePrincipalAntiRootGaussianRootLineOneTwelfth
M3_T11_MOVING_ROOTLINE_OCCUPANCY_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


---
