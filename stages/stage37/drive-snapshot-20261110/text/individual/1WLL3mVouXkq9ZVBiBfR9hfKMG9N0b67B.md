# M3-T11-028 — Principal square-root coordinate and fixed-root elliptic compression

CARD_ID: M3-T11-028
CANONICAL_CARD_KEY: M3-T11-028
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-028
現行一覧の状態: PARTIALLY_RETRACTED / FIXED-v BO1 RETAINED
種別: EXACT_STRUCTURE / CORRECTED_BY_M3-T11-029
要点: Principal-root compression retained; rational-square-divisor claim retracted
主張の抜粋: M3-T11-029 proves the distinguished root is anti-rational: z=i*v with v in Q. The earlier M3-T11-028 claims m^2|Num(z-1) and H(z)>=m^2/2 are retracted. The fixed-v genus-one compression and B^o(1) physical multiplicity are retained.
対象・測度: Exact fixed-content/coefficient relative-fresh endpoint packets.
依存関係: M3-T11-024; M3-T11-026; corrected by M3-T11-029.
再開条件の抜粋: Use the corrected moving Gaussian root-line/support receiver of M3-T11-029 and later cards.
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 30.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 601227
SOURCE_END: 609158
SOURCE_SHA256: d473b34b8c1f7c8cc813b856d4df9375679e77589d2d558331c24feade141838

CARD_ID: M3-T11-028
TITLE: Principal square-root coordinate and fixed-root elliptic compression
TYPE: EXACT_STRUCTURE / ANALYTIC_ADAPTER / THEOREM_GATE
STATUS: PROVED_EXACT_ADAPTER / REALIZED_ROOT_SUPPORT_DEFICIT_OPEN
ROUTE: TrivialSplitCyclicDirectionOneThird


CLAIM:
On the relative-fresh branch, choose the fresh core G_3 and write the exact full double-lift equation as


D*t^2+2*C*s*t+P=0,


where


D=1+C^2+C^2*s^2,
P=1+s^2+C^2*s^2.


Because t is divisible by the squared fresh Gaussian ideal


mathfrak_M_3=(G_3^sharp)^2,


the full principal-incidence equation itself gives


P==0 mod mathfrak_M_3.


Thus the squared-modulus restriction is a two-variable conic incidence on the same (C,s) variables as the principal torus-trace selector.


Define


K=-Lambda(C)*Lambda(s)*Lambda(C*s).


The exact identities imply


K=((D*t+C*s)/(C*s))^2.


Hence the distinguished principal root


z=1+D*t/(C*s)


is rational and satisfies z^2=K.


Moreover


z-1=D*t/(C*s),


so, writing z=A/B in lowest terms,


boxed:
(tau_3^sharp)^2 | (A-B)
=
Num(z-1).


The value z=1 is impossible on the rational norm-one endpoint torus: z=1 would force D=0, hence N(1+s^2)=1 and Lambda(s)=+/-1, which requires sqrt(-3) in Q(i).


Therefore every nontrivial relative-fresh endpoint satisfies


H(z)>= (tau_3^sharp)^2/2.


For fixed z, put


x=Lambda(C),
y=Lambda(s),
w=Lambda(C*s),
X=x^2,
Y=y^2.


Using the Fricke identity and x*y*w=-z^2 gives the plane cubic


X*Y*(X+Y+z^2-4)+z^4=0.


Its singular parameters are exactly z^2 in {0,1,-8}. The physical nontrivial relative-fresh branch excludes all of these. The smooth cubic has rational flexes at infinity, hence rational 3-torsion.


The repo-retained uniform bounded-height elliptic theorem with rational prime-order torsion therefore gives, uniformly for fixed content/coefficient packet and fixed z,


# physical endpoint states <= B^o(1).


Thus the relative-fresh branch reduces at power scale to support of realized principal-root labels z carrying an actual fresh square-divisor witness.


POPULATION:
Exact fixed-content/coefficient Step-A-complement relative-fresh endpoint packets.


HEIGHT:
Exact physical R<=B. The principal-root height and cubic point heights are polynomial in B.


DEPENDS_ON:
M3-T11-022,
M3-T11-024,
M3-T11-026,
M3-T11-027,
the Fricke torus identity,
the repo-retained Stage14-t22/t36/t37 bounded-height elliptic theorem with rational prime-order torsion.


IMPLIES:
The algebraic principal-incidence-preserving adapter is closed on the relative-fresh branch.
The minimal remaining relative-fresh receiver is one-dimensional realized-z support with a square-divisor witness in Num(z-1).


ALIASES:
PrincipalRootNearOneSquareModulus;
FreshRelativePrincipalRootSquareDivisorSupportOneTwelfth;
M3PrincipalRootSquareDivisorSupport.


SUPERSEDES:
M3PrincipalIncidencePreservingSquaredModulusInverseFrequencyAdapter as the narrowest algebraic receiver on the relative-fresh branch.
The inverse-frequency representation remains available as an alternate analytic form but is no longer the unique next gate.


DO_NOT_REPEAT:
Do not multiply conic-modulus density by principal-squareclass density.
Do not count K==1 mod mathfrak_M as an independent local saving.
Do not charge inverse-frequency and square-divisor-root savings independently.
Do not replace the realized-z physical measure by all rational z of comparable height.
Do not infer fixed-power sparsity merely from B^o(1) square-divisor witness multiplicity.


REOPEN_CONDITION:
A same-physical-measure fixed-power support theorem for realized z carrying an actual fresh witness m with


m^2 | Num(z-1),


or an exact further adapter to a certified square-divisor/divisor-window theorem with the realized-z measure and physical masks retained.


NEW_GATE:
FreshRelativePrincipalRootSquareDivisorSupportOneTwelfth.


REQUIRED_OUTPUT:
Uniformly per fixed content/coefficient packet,


# realized relative-fresh z << B^(1/12-delta)


for some fixed delta>0, with fixed-z endpoint multiplicity absorbed into B^o(1).


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 29.


M3_T11_PRINCIPAL_INCIDENCE_PRESERVING_CONIC_ADAPTER=true
M3_T11_FIXED_Z_PHYSICAL_MULTIPLICITY=BO1
M3_T11_REALIZED_Z_SQUARE_DIVISOR_DEFICIT_PROVED=false
P_OVER_M3_LIMIT_PROVED=false


---


## SEMANTIC DUPLICATION AUDIT — M3-T11-023 through M3-T11-028


AUDIT_SCOPE:
Recent TrivialSplitCyclicDirectionOneThird cards M3-T11-023..028 were compared against RESULT-LEDGER, NEGATIVE-REGISTER, relevant M3 route cards, and adjacent Stage14 / StructureRadar theorem species by:
CLAIM, POPULATION/MEASURE, load-bearing equation, saving mechanism, theorem species, and required exponent.


VERDICT:


M3-T11-023:
KEEP_CANONICAL.
Novel retained content is the exact torus-trace multiplicative Fourier separation and bounded spectral L2 energy on the M3 three-core packet.
Its former three-core theorem gate was later superseded by M3-T11-024, but the exact transform result itself is not duplicated.


M3-T11-024:
KEEP_CANONICAL.
Novel retained content is the exact O(1)-multiplicity paired-Gaussian reduction of the M3 three-core packet to the existing tH shared-common-core packet.
This is a genuine same-measure adapter, not a renaming of M3-T11-023.


M3-T11-025:
KEEP_CANONICAL.
Novel retained content is the M3 principal torus-trace K3 identification plus the exact cross-gcd / two-post-gcd-square arithmetic collapse and exponent firewall.
Stage14 has adjacent Kummer theorem species, but not this M3 exact packet and arithmetic reduction.


M3-T11-026:
KEEP_CANONICAL_AS_INTERMEDIATE_ADAPTER.
Novel retained content is the fresh relative-core squared-ideal CRT incidence and exact same-measure Fourier/Gauss inverse-frequency reduction.
SR-STR-169 contains the generic Fourier/Gauss theorem species, but M3-T11-026 supplies the M3-specific endpoint-derived modulus and same-measure dictionary.
Its active gate is superseded on the relative-fresh branch by M3-T11-028.


M3-T11-027:
ROUTER_ONLY / NOT_AN_INDEPENDENT_ACTIVE_THEOREM_GATE.
This card mostly assembles M3-T11-026, the retained all-same valuation square-divisor branch, and Stage14-t27 ancestry into a fresh-part trichotomy.
It should be retained as an anti-loop routing junction, but should not be counted as a separate analytic breakthrough or reopened as an independent route.
Its relative-fresh active gate is superseded by M3-T11-028.


M3-T11-028:
KEEP_CANONICAL.
The exact distinguished principal root
z=1+D*t/(C*s),
the rational square-divisor consequence
(tau_i^sharp)^2 | Num(z-1),
and the fixed-z Fricke cubic reduction with B^o(1) endpoint multiplicity were not found as an existing M3 canonical card or exact Stage14 receiver.
Stage14 contains adjacent fixed-squareclass genus-one / cross-ratio theorem species, but the CLAIM + POPULATION + square-divisor witness + one-twelfth receiver are different.
Therefore this is a genuine new same-measure adapter / receiver, not merely a variable rename.


CURRENT_CANONICAL_CHAIN:
M3-T11-023 exact spectral transform
-> M3-T11-024 paired-Gaussian adapter
-> M3-T11-025 principal K3 / cross-gcd firewall
-> M3-T11-026 fresh squared-modulus adapter
-> M3-T11-028 principal-root square-divisor compression.


M3-T11-027 is a ROUTING JUNCTION between 026 and branch-specific successors, not a new independent gate.


ANTI_LOOP_DECISION:
Do not create a new card for any future reformulation of M3-T11-028 unless it changes the exact physical measure, introduces a genuinely new load-bearing arithmetic condition, proves a new same-measure adapter, or improves the exponent.
Coordinate changes among torus / Gaussian / rational / Fourier descriptions should default to ADDENDUM_TO_M3-T11-028.


RECENT_CARD_COMPLETE_DUPLICATE_FOUND=false
RECENT_CARD_OVERGRANULAR_ROUTER=M3-T11-027
M3_T11_027_INDEPENDENT_ACTIVE_GATE=false
CURRENT_RELATIVE_FRESH_CANONICAL_GATE=FreshRelativePrincipalRootSquareDivisorSupportOneTwelfth


---
