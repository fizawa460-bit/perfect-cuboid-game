# M3-T11-066 — Kummer-parity packet router and canonical E2 root-character bridge

CARD_ID: M3-T11-066
CANONICAL_CARD_KEY: M3-T11-066
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-066
現行一覧の状態: PROVED_EXACT_STRUCTURE / MORDELL-WEIL CHARACTER INTERSECTION OPEN
種別: EXACT_STRUCTURE / MORDELL-WEIL INTERSECTION BRIDGE
要点: Retain M3-T11-049, M3-T11-050, M3-T11-056, M3-T11-057, and M3-T11-063 through M3-T11-065. Write every rational E2 point as R=nQ+epsilon*T, Q=(50,5600), T=(0,0), and every finite tr
主張の抜粋: Retain M3-T11-049, M3-T11-050, M3-T11-056, M3-T11-057, and M3-T11-063 through M3-T11-065. Write every rational E2 point as R=nQ+epsilon*T, Q=(50,5600), T=(0,0), and every finite translated-lift x-coordinate canonically as U=d0*(A/C)^2, d0 in {1,2}, A,C>0, gcd(A,C)=1. 1. The standard 2-isogeny Kummer map satisfies alpha
対象・測度: Exact x=27/40 translated-lift carrier restricted to the canonical M3-T11-048 three-packet survivor locus and the saturated E2 Mordell-Weil decomposition of M3-T11-056/057.
依存関係: M3-T11-049; M3-T11-050; M3-T11-056; M3-T11-057; M3-T11-059; M3-T11-063; M3-T11-064; M3-T11-065; the standard 2-isogeny Kummer homomorphism on y^2=x(x^2+1244x+562500).
再開条件の抜粋: For the five M3-T11-057 residue classes n=n0+k*2656080, prove the exact 3-,5-,7-adic character laws of the canonical root denominator C(nQ+epsilon*T), and of A only on the 5|C branch, preferably via division polynomials / elliptic divisibil
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 73.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 737478
SOURCE_END: 743585
SOURCE_SHA256: e8e4d7eecf22ea8048a285f13b27a2cddaaa3d2a3c50bcf598b216bf85fd841b

## M3-T11-066
ID:
M3-T11-066
TYPE:
EXACT_STRUCTURE / MORDELL-WEIL INTERSECTION BRIDGE
TITLE:
Kummer-parity packet router and canonical E2 root-character bridge
STATUS:
PROVED_EXACT_STRUCTURE / MORDELL-WEIL CHARACTER INTERSECTION OPEN


CLAIM:
Retain M3-T11-049, M3-T11-050, M3-T11-056, M3-T11-057, and M3-T11-063 through M3-T11-065. Write every rational E2 point as
R=nQ+epsilon*T,
Q=(50,5600), T=(0,0),
and every finite translated-lift x-coordinate canonically as
U=d0*(A/C)^2,
d0 in {1,2}, A,C>0, gcd(A,C)=1.


1. The standard 2-isogeny Kummer map satisfies alpha(Q)=[2] and alpha(T)=[562500]=1. Hence
alpha(nQ+epsilon*T)=[2]^n.
Using M3-T11-049,
n odd iff Packets I/II,
n even iff Packet III
on every finite canonical three-packet survivor.
Since M=2656080 is even, the M3-T11-057 survivor cosets therefore split exactly:
epsilon=0, n==0,+/-2 mod M -> Packet III for finite affine survivors;
epsilon=1, n==+/-1 mod M -> Packets I/II.


2. The M3-T11-063/065 packet data give the exact canonical root dictionary. If F0=b^2+14a^2:
- Packets I/II: write b=2C and F0=2w^2. Then U=2*(25w/C)^2, so d0=2, A=25w, C=b/2.
- Packet III,d=9: write F0=w^2. Then U=(50w/b)^2, so d0=1, A=50w, C=b.
- Packet III,d=225: M3-T11-065 gives v_5(b)>=3. Put C=b/25 and F0=w^2. Then U=(2w/C)^2, so d0=1, A=2w, C=b/25, and (A|5)=(a|5).
The displayed pairs are reduced; the proofs use primitiveness together with the retained 7∤b exclusion and the exact 5-adic packet data.


Thus the common content is determined directly by the Mordell-Weil root coordinates:
n odd => d=64;
n even and 5∤C => d=9;
n even and 5|C => d=225.
In particular 5|C occurs exactly on Packet III,d=225.


3. Define
kappa5(R)=(C|5) if 5∤C,
kappa5(R)=(A|5) if 5|C.
Write delta=2^e2*7^e7. Then M3-T11-064/065 become the uniform exact identities
(-1)^e2=(C|3),
(-1)^e7=(-1)^n*(C|3)*kappa5(R).
Equivalently,
e2=(1-(C|3))/2,
e7=(1-(-1)^n*(C|3)*kappa5(R))/2,
delta=2^e2*7^e7.
Therefore delta is pointwise reconstructible from the Mordell-Weil coefficient parity and the canonical root numerator/denominator characters.


4. Because M3-T11-059 gives 7∤b and
U-2500=14*(50a/b)^2,
one has
v_7(U-2500)=1+2v_7(a).
Hence
7|a iff v_7(U-2500)>=3.
On this branch the M3-T11-065 ramified-7 condition becomes
(C|7)=(-1)^n*(C|3)*kappa5(R),
because b/C is 2,1,25 in the three root cases and each is a square modulo 7.


5. Adding T acts by
U(P+T)=562500/U(P).
For canonical U(P)=d0*(A/C)^2:
- d0=1: with g=gcd(A,750), root pair maps to (750C/g, A/g);
- d0=2: with g=gcd(A,375), root pair maps to (375C/g, A/g).
Thus the epsilon=1 denominator-character problem is reducible to numerator/denominator data of nQ after removing only fixed {2,3,5}-support.


POPULATION:
Exact x=27/40 translated-lift carrier restricted to the canonical M3-T11-048 three-packet survivor locus and the saturated E2 Mordell-Weil decomposition of M3-T11-056/057.


DEPENDS_ON:
M3-T11-049;
M3-T11-050;
M3-T11-056;
M3-T11-057;
M3-T11-059;
M3-T11-063;
M3-T11-064;
M3-T11-065;
the standard 2-isogeny Kummer homomorphism on y^2=x(x^2+1244x+562500).


IMPLIES:
The requested M3-T11-065 numerator/denominator-character bridge to nQ+epsilon*T is now exact. Packet species, d, and delta no longer require returning to generic a/b packet enumeration. The remaining infinite-progressions problem can be attacked directly through division-polynomial, elliptic-divisibility, or formal-group laws for the canonical root numerator/denominator of nQ+epsilon*T at 3,5,7.


NEW_RECEIVERS:
X27Over40KummerParityPacketRouter;
X27Over40CanonicalEllipticRootCharacterBridge;
X27Over40DeltaOnMWRootCoordinates;
X27Over40Ramified7MWCoordinateCompatibility;
X27Over40TorsionRootReciprocity;
X27Over40DivisionPolynomialCharacterSequencesOnMWSurvivorProgressions.


ALIASES:
X27Over40KummerParityPacketRouter;
X27Over40CanonicalEllipticDenominatorCharacterBridge;
X27Over40MWRootDeltaFormula.


DUPLICATE_OF:
none found. M3-T11-049/050 identify the two U-squareclasses and the Kummer image but do not identify packet species with n parity. M3-T11-065 requests, but does not provide, the exact transfer of b/a characters to canonical Mordell-Weil root coordinates.


DO_NOT_REPEAT:
Do not reopen packet species after n parity is known.
Do not reopen generic d profiles: d is 64,9,225 according to the exact root-coordinate rule above.
Do not return to a/b merely to recover delta; use the canonical root characters.
Do not infer that the denominator/root characters are globally periodic in k on n=n0+k*M until a division-polynomial, EDS, or formal-group proof is supplied.
Do not infer rational-point classification, fixed-power saving, primary theorem-gate closure, or P/M3 credit from this bridge alone.


REOPEN_CONDITION:
For the five M3-T11-057 residue classes n=n0+k*2656080, prove the exact 3-,5-,7-adic character laws of the canonical root denominator C(nQ+epsilon*T), and of A only on the 5|C branch, preferably via division polynomials / elliptic divisibility sequences / formal groups. Intersect those laws with
(-1)^e2=(C|3),
(-1)^e7=(-1)^n*(C|3)*kappa5,
and, when v_7(U-2500)>=3,
(C|7)=(-1)^n*(C|3)*kappa5.
A lower-genus global reduction of the same delta-resolved H*K packet is also acceptable. Another unconstrained auxiliary-prime sieve is not sufficient.


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE, Section 73.


FLAGS:
M3_T11_X_27_OVER_40_KUMMER_PACKET_PARITY_ROUTER=true
M3_T11_X_27_OVER_40_MW_SIEVE_COSETS_PACKET_SEPARATED=true
M3_T11_X_27_OVER_40_CANONICAL_ROOT_DENOMINATOR_BRIDGE=true
M3_T11_X_27_OVER_40_COMMON_CONTENT_FROM_MW_ROOT=true
M3_T11_X_27_OVER_40_DELTA_BITS_ON_MW_ROOT_COORDINATES=true
M3_T11_X_27_OVER_40_RAMIFIED7_MW_COORDINATE_COMPATIBILITY=true
M3_T11_X_27_OVER_40_TORSION_ROOT_RECIPROCITY=true
M3_T11_X_27_OVER_40_RATIONAL_POINTS_CLASSIFIED=false
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_X27_FIRST_ATTACK=X27Over40DivisionPolynomialCharacterSequencesOnMWSurvivorProgressions
CURRENT_X27_SECOND_ATTACK=X27Over40EllipticLogHeightReductionBelow1328040
CURRENT_X27_THIRD_ATTACK=X27Over40SplitJacobianQuadraticChabauty
RESEARCH_CARD=M3-T11-06
