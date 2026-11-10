# M3-T11-046 — Singular-x purity and x=-1/8 coprime Gaussian square-factor lattice

CARD_ID: M3-T11-046
CANONICAL_CARD_KEY: M3-T11-046
MIGRATION_MODE: lossless source separation; no new mathematical result.
GLOBAL_OPERATION: HOLD_PENDING_NEW_WHOLE_POPULATION_INPUT.
CURRENT_STATE_RULE: The index metadata below records the migration-time state. Earlier provisional status or NEXT instructions in source text are historical; they do not override the current MAIN or later scoped corrections.
DETAIL_SCOPE: Full original card text is retained below. Proofs located in a ROUTE or audit remain linked dependencies; this migration does not claim to reproduce those external documents.

## Index metadata
ID: M3-T11-046
現行一覧の状態: PROVED_EXACT / COUNTING_GATE_OPEN
種別: EXACT_STRUCTURE / EXCEPTIONAL_CARRIER / SAME_MEASURE_RECEIVER / FIREWALL
要点: Retain M3-T11-045 and, for p^lambda||m_i, v_p(N_u)=2*lambda+c_p, v_p(Den(S))=2*lambda-c_p. A. x=-1/8 is pure full-S-denominator. From x=((1+u^2)S)/(16u), boxed: S=-2u/(1+u^2)=-2ab/
主張の抜粋: Retain M3-T11-045 and, for p^lambda||m_i, v_p(N_u)=2*lambda+c_p, v_p(Den(S))=2*lambda-c_p. A. x=-1/8 is pure full-S-denominator. From x=((1+u^2)S)/(16u), boxed: S=-2u/(1+u^2)=-2ab/N_u. Physical full anti-root splitting requires w^2=u^2+2, hence after clearing the reduced u=a/b, c^2=a^2+2b^2. Primitive parity forces b e
対象・測度: Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet on the two singular fixed-x values from M3-T11-045.
依存関係: M3-T11-020 determinant/Jacobian firewall; M3-T11-035 common-u root line; M3-T11-036 fixed-u B^o(1) multiplicity; M3-T11-040 conductor partition; M3-T11-042/043 exact fresh saturation; M3-T11-045 singu
旧詳細位置: K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 53.
旧詳細リンク: https://docs.google.com/document/d/1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE/edit?usp=drivesdk
旧LEDGERリンク: https://docs.google.com/document/d/1UbCumRibIROxEFPz-ZQHPGlmok_C_R2N1dbYr5mtFAA/edit?usp=drivesdk

## Retained LEDGER source 1
SOURCE_START: 663824
SOURCE_END: 671241
SOURCE_SHA256: 3ad926ff139cb69eece4d4e79963820c5d00cbcc48b59e331173ed8089c9112f

## M3-T11-046
TITLE: Singular-x purity and x=-1/8 coprime Gaussian square-factor lattice
TYPE: EXACT_STRUCTURE / EXCEPTIONAL_CARRIER / SAME_MEASURE_RECEIVER / FIREWALL
STATUS: PROVED_EXACT / COUNTING_GATE_OPEN


CLAIM:
Retain M3-T11-045 and, for p^lambda||m_i,
v_p(N_u)=2*lambda+c_p,
v_p(Den(S))=2*lambda-c_p.


A. x=-1/8 is pure full-S-denominator.


From x=((1+u^2)S)/(16u),
boxed:
S=-2u/(1+u^2)=-2ab/N_u.


Physical full anti-root splitting requires w^2=u^2+2, hence after clearing the reduced u=a/b,
c^2=a^2+2b^2.
Primitive parity forces b even and a,c odd.
Therefore N_u=a^2+b^2 is odd and gcd(N_u,2ab)=1, so
boxed:
Den(S)=N_u.


Comparing the two exact fresh valuations gives
2*lambda-c_p=2*lambda+c_p,
hence
boxed:
c_p=0
for every relative-fresh prime.
Thus on x=-1/8,
boxed:
M_0=M_rel,
Q_S=M_rel^2,
C_u=1
on fresh support.


B. x=27/40 is also pure full-S-denominator.


Here
boxed:
S=54ab/(5N_u).
For every relative-fresh p!=5, p does not divide ab and therefore
v_p(Den(S))=v_p(N_u), forcing c_p=0.
If p=5 were relative-fresh, then
v_5(Den(S))=v_5(N_u)+1,
which would force
2*lambda-c_5=2*lambda+c_5+1,
impossible.
Therefore p=5 is absent from M_rel and
boxed:
c_p=0
for every relative-fresh prime on x=27/40 as well.
Hence
M_0=M_rel,
Q_S=M_rel^2,
C_u=1
on fresh support.


C. x=-1/8 has an exact coprime Gaussian factorization.


Every primitive conic solution c^2=a^2+2b^2 has, up to signs,
a=(r^2-2s^2)/epsilon,
b=2rs/epsilon,
c=(r^2+2s^2)/epsilon,
with gcd(r,s)=1 and epsilon in {1,2} the frozen 2-primary primitive-content factor.


Then
boxed:
N_u=(r^4+4s^4)/epsilon^2=A_-*A_+,
where
A_-=[(r-s)^2+s^2]/epsilon,
A_+=[(r+s)^2+s^2]/epsilon,
and
boxed:
gcd(A_-,A_+)=1.


After the fixed (1+i)-normalization when epsilon=2, A_-,A_+ are primitive Gaussian norms
N(H_-),N(H_+)
with
boxed:
H_-*H_+=unit*(a+ib).


The common-u oriented fresh square conductor therefore splits uniquely:
boxed:
mathfrak M=mathfrak M_-*mathfrak M_+,
N(mathfrak M)=M_rel,
mathfrak M_-^2|H_-,
mathfrak M_+^2|H_+,
N(mathfrak M_-)*N(mathfrak M_+)=M_rel.


Because all fresh c_p vanish on this carrier, the quotient after removing each assigned square conductor is fresh-primitive at those primes.


D. Primitive-parameter lattice receiver.


After freezing epsilon and one oriented prime allocation, the two Gaussian square-divisibility conditions place primitive (r,s) in a rank-two lattice whose fresh index is
boxed:
M_rel^2
(up to the frozen 2-primary packet normalization).


For fixed M_rel, allocation/orientation multiplicity is M_rel^o(1).
Together with the already-audited fixed-u B^o(1) endpoint multiplicity, the exceptional carrier is reduced to
boxed:
B^o(1) unions of primitive determinant-M_rel^2 parameter lattices.


This is not itself a fixed-power count.


POPULATION:
Exact fixed-content/coefficient nondegenerate relative-fresh endpoint packet on the two singular fixed-x values from M3-T11-045.


HEIGHT:
Physical R<=B retained.
No ambient (r,s)-box estimate is promoted without a same-physical-measure range adapter.


DEPENDS_ON:
M3-T11-020 determinant/Jacobian firewall;
M3-T11-035 common-u root line;
M3-T11-036 fixed-u B^o(1) multiplicity;
M3-T11-040 conductor partition;
M3-T11-042/043 exact fresh saturation;
M3-T11-045 singular fixed-x identification.


IMPLIES:
Both singular fixed-x carriers lie entirely in the full-S-denominator fresh allocation.
The x=-1/8 carrier has an exact two-factor Gaussian square-conductor decomposition and a determinant-M_rel^2 primitive-parameter receiver.


DOES_NOT_IMPLY:
No M_rel^-2 endpoint saving without a physical range theorem.
No closure of x=-1/8.
No closure of x=27/40.
No global one-twelfth support theorem.


ALIASES:
SingularXFullSDenominatorPurity;
XMinusOneEighthGaussianSquareFactorLattice;
SophieGermainExceptionalCarrier;
XMinusOneEighthDetMrel2;
X27Over40FullSDenominatorPurity.


DUPLICATE_OF:
NONE.
Not M3-T11-020: the determinant here comes from a genuine fresh square-divisibility condition on an exceptional conic parameter, not from a coordinate-change Jacobian. The M3-T11-020 warning still applies against charging the index before a same-measure range adapter is proved.


DO_NOT_REPEAT:
Do not reopen mixed c_p allocations on either singular x value.
Do not put fresh p=5 on x=27/40.
Do not charge M_rel^-2 merely from the parameter-lattice determinant.
Do not forget the epsilon=2 fixed 2-primary normalization in the primitive conic parameterization.


FIRST_MISSING_LEMMA:
XMinusOneEighthPhysicalGaussianSquareLatticeRangeOneTwelfth.


REQUIRED_OUTPUT:
A uniform same-physical-measure count of primitive (r,s) on the determinant-M_rel^2 lattices, with the true R<=B region, packet masks, moving conductor/orientation summation and boundary terms, strong enough after B^o(1) losses to give B^(1/12-delta).


DETAIL_DOC:
K16-C3-M3-ROUTE-TRIVIAL-SPLIT-CYCLE section 53.


FLAGS:
M3_T11_SINGULAR_X_ALL_FRESH_CP_ZERO=true
M3_T11_SINGULAR_X_M0_EQUALS_MREL=true
M3_T11_X_MINUS_ONE_EIGHTH_DEN_S_EQUALS_NU=true
M3_T11_X_MINUS_ONE_EIGHTH_GAUSSIAN_COPRIME_SPLIT=true
M3_T11_X_MINUS_ONE_EIGHTH_FRESH_SQUARE_CONDUCTOR_SPLIT=true
M3_T11_X_MINUS_ONE_EIGHTH_PARAMETER_LATTICE_DET_MREL2=true
M3_T11_X_MINUS_ONE_EIGHTH_POWER_SAVING_PROVED=false
M3_T11_X_27_OVER_40_ALL_FRESH_CP_ZERO=true
M3_T11_X_27_OVER_40_FRESH_FIVE_EXCLUDED=true
M3_T11_X_27_OVER_40_POWER_SAVING_PROVED=false
P_OVER_M3_LIMIT_PROVED=false
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|XMinusOneEighthGaussianSquareFactorLattice|InteriorCharacterGlobalDispersion
NEXT_ATTACK=XMinusOneEighthPhysicalGaussianSquareLatticeRangeOneTwelfth|X27Over40SplitCubicSameMeasureCarrier|GenericXMovingSupportDispersion|InteriorCharacterGlobalDispersion


ADDENDUM_TO_M3-T11-046:


On x=-1/8, write c^2=a^2+2b^2.
The three distinct rational anti-roots are
z_0=2ab/N_u,
z_+=2a/(c+b),
z_-=-2a/(c-b),
all in lowest terms.


Their root-line norm forms satisfy
boxed:
N_0=(2ab)^2+N_u^2,
boxed:
N_+=(c-b)*(5c+7b),
boxed:
N_-=(c+b)*(5c-7b).


For every relative-fresh p, M3-T11-046 gives c_p=0 and p divides exactly one of c-b,c+b.


If p|c+b, then N_0 and N_+ are p-units while p|N_-.
If p|c-b, then N_0 and N_- are p-units while p|N_+.


Therefore the anti-root destination of every fresh prime is forced:
p|c-b -> core attached to z_+;
p|c+b -> core attached to z_-;
no fresh prime -> core attached to z_0.


Hence, up to the physical permutation of the three corrected anti-roots,
boxed:
one of m_1,m_2,m_3 equals 1,
and the other two multiply to M_rel and are exactly the fresh square-conductor parts of c-b and c+b.


This is a carrier-specific support-dimension reduction, not a generic pointwise two-core CRT and not a reopening of the retracted common-v statement.


NEW_ALIAS:
XMinusOneEighthTwoFreshCoreGaussianSquarePair.


NEW_FIRST_MISSING_LEMMA:
XMinusOneEighthTwoCorePhysicalRangeDeficit.


ADDITIONAL_FLAGS:
M3_T11_X_MINUS_ONE_EIGHTH_ONE_RELATIVE_FRESH_CORE_EMPTY=true
M3_T11_X_MINUS_ONE_EIGHTH_FRESH_PRIME_ROOT_DESTINATION_FORCED=true
M3_T11_X_MINUS_ONE_EIGHTH_TWO_FRESH_CORE_GAUSSIAN_PAIR=true
M3_T11_X_MINUS_ONE_EIGHTH_TWO_CORE_POWER_SAVING_PROVED=false
CURRENT_SUPPORTING_ATTACK=FullSDenominatorLegendreXSupportOneTwelfth|XMinusOneEighthTwoFreshCoreGaussianSquarePair|InteriorCharacterGlobalDispersion
NEXT_ATTACK=XMinusOneEighthTwoCorePhysicalRangeDeficit|X27Over40SplitCubicSameMeasureCarrier|GenericXMovingSupportDispersion|InteriorCharacterGlobalDispersion
