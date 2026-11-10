# M3-T11-131 — Extreme actual anti-root orientation and coupled linear congruence

Authority: Stage37 Drive current130, MAIN/INDEX/ROUTE/RESULT-LEDGER and130 card freshly read. Status: PROVED_EXACT_EXTREME_LOCAL_CLASSIFICATION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0. Audit is internal, not independent external review. TI remains parked.

## Result

For an odd split relative-fresh p^lambda || m_i on the nondegenerate physical branch, put L=2lambda, A=1+u^2, u=a/b reduced, S=s/t reduced with t>0. Retain130: strict interior allocation is empty. The two remaining cases have the following actual targeted anti-root V:

| Allocation | Exact valuations | Actual unit root-line |
| --- | --- | --- |
| c_p=0, denominator extreme | v_p(A)=L, v_p(S)=-L | V congruent u mod p^L; V^2+1 divisible by p^L automatically |
| c_p=L, Gaussian extreme | v_p(A)=2L, S and S-u units | V^2+1 divisible by p^L iff 2S congruent u mod p^L; then V congruent -u mod p^L |

The Gaussian case additionally has both pole roots in Q_p iff chi_p(-2/A_0)=+1, with A_0=A/p^(2L) a unit. Under the displayed root-line congruence this character is sufficient for all three cubic roots over Q_p with valuations (0,-L,-L); there is no additional higher-precision cubic-splitting obstruction. This only classifies the actual cubic plus its targeted root-line, not the entire Gaussian-core/physical lift.

In particular, if N_u=a^2+b^2 is a rational integer square, A is a rational square and A_0 is a local square. A Gaussian-extreme fresh prime must then satisfy p=1 mod8. Fresh primes p=5 mod8 must be denominator extreme. This is not a fixed-power density or a global endpoint theorem.

## Exact proof: denominator extreme

ROUTE35 gives f(X)=X^3-SX^2+EX-P, E=4u(S-u)/A, P=4u^2S/A. Its roots are the actual physical v_i; ROUTE36–37 give one targeted unit root with norm depth >=L and two pole roots of valuation -L. At c_p=0, g=p^(2L)f is integral with ascending coefficient valuations (0,0,L,2L). Its reduction is a nonzero multiple of X-u; there is a unique unit root V, with unit derivative. The identity

f(u)=u^2[u(A-4)/A-S]

has valuation at least -L, because both bracket terms have valuation -L. Consequently v_p(g(u))>=L and, by the unit-derivative factorization, v_p(V-u)>=L. Since v_p(A)=L, the norm V^2+1=A+(V-u)(V+u) has valuation >=L. This required root-line imposes no extra condition on S in this branch. Pole-root splitting is still a separate condition; no denominator-extreme support count is proved.

For a simple pole reduction, writing s_0=p^L S and a_0=A/p^L, the scaled cubic p^(3L)f(Y/p^L) reduces to

Y [Y^2-s_0Y+4u s_0/a_0].

Its quadratic discriminant s_0^2-16u s_0/a_0 must be a square modulo p. A nonzero square is sufficient by Hensel; the zero-discriminant case is not disposed of here. This is the existing045 Legendre receiver in pole-root coordinates, not a newly chargeable density.

## Exact proof: Gaussian extreme

Here v_p(A)=2L and v_p(S)>=0 from allocation. The actual roots give v_p(E)=v_p(P)=-2L: the product of the two pole roots uniquely dominates E and all three root valuations determine P. Since P=4u^2S/A, S is a unit, and E=4u(S-u)/A forces S-u a unit. The exact norm saturation is already retained042, not a new theorem; independently, if the capped branch had v_p(A)>2L, the P valuation would force v_p(S)>0, and E would then have the wrong valuation.

Now g=p^(2L)f has unit constant and linear coefficients; its remaining coefficients vanish modulo p. Its unique unit root reduces to uS/(S-u). Because u^2=-1 mod p, the norm of this residue vanishes iff 2S=u mod p. In that case its residue is -u, not +u.

Direct evaluation gives

f(-u)=u^2 [u(4-A)-S(A+8)]/A.

For a root V reducing to -u, the same unit-derivative factorization gives

v_p(V+u)=v_p(g(-u))=v_p(u(4-A)-S(A+8)).

As v_p(A)=2L, this valuation is >=L iff 2S-u vanishes modulo p^L (p is odd, so8 is a unit). Since V-u is a unit, V^2+1=A+(V+u)(V-u) vanishes modulo p^L iff V+u does. This proves the exact equivalence, including the case where the bracket is zero. When the congruence fails already modulo p, the norm root-line fails already modulo p.

Under 2S=u mod p^L, the pole-scaled cubic reduces to

Y [Y^2+2/A_0].

Thus two pole roots require chi_p(-2/A_0)=+1. Conversely this gives two simple nonzero roots and one simple zero root modulo p, hence all lift uniquely; the nonzero roots give poles of valuation -L, and the zero root corresponds to the already-certified unit V. For square N_u, chi_p(A_0)=1 and p=1 mod4, so chi_p(-2/A_0)=chi_p(2); the elementary supplementary law gives p=1 mod8. This character also restates the discriminant-square equation: Q(S,u)=2 mod p under u^2=-1 and S=u/2. It is not an independent second saving.

## Global integer receiver and nonzero firewall

Let M_D be the product p^lambda over denominator-extreme fresh primes and M_G over Gaussian-extreme primes. Then M_D M_G=M_rel, the factors are coprime, Q_S=M_D^2, C_u=M_G^2, and the exact fresh norm is M_D^2 M_G^4. These are retained130/042 routing identities.

The new Gaussian root-line equivalence gives the integral coupled receiver

H_G=2 b s-a t,
M_G^2 divides H_G,
gcd(a b t,M_G)=1.

This links the same physical S and u; it does not identify distinct anti-roots. The targeted anti-root has orientation +u at D primes and -u at G primes. No product of three root-line densities is taken.

Moreover H_G cannot vanish on a physical packet: H_G=0 implies S=u/2, whereas the original split-discriminant quartic satisfies exactly

Q(u/2,u)=u^2(112+145u^2+u^4)/16>0 for real u!=0.

This contradicts Y^2=-(1+u^2)Q(S,u). Hence |H_G|>=M_G^2. It is a legitimate nonzero integer divisor lock on the original packet, not yet a height/counting theorem. Do not replace physical R<=B by arbitrary heights of a,b,s,t, or assume uniform residues of H_G.

If N_u=c^2 and e=v_p(c)>0 at a fresh prime: denominator allocation requires lambda=e; Gaussian allocation requires e even, lambda=e/2 and p=1 mod8. This is an exact assignment restriction, not an endpoint population estimate.

## Replay, audit and novelty boundary

verify_m3_t11_131.py uses standard-library exact rational arithmetic and digit-by-digit Hensel lifting. PASS:800 denominator packets,272 Gaussian congruence perturbations,40 Gaussian pole packets, p=5,13,17,29,41 and lambda=1..4, both square/nonsquare norm units. It verifies the root-line equivalence and the pole-splitting character, including lifting admitted pole roots. Symbolic replay verifies both f(±u) identities and the positive-real Q(u/2,u) identity. Physical endpoints enumerated0; the synthetic local packets are NOT rational physical endpoints. In particular S=u/2 test packets are globally impossible over R, yet can be locally admissible at a fresh p; they do not prove a global impostor family.

Targeted anti-duplication: retained042 exact norm saturation and043 absence of Gaussian Phi_* residual valuation remain unchanged; neither is claimed new. Retained045/046 and their later audited successors retain the denominator-extreme Legendre/singular-carrier scope. Sections39/40's corrected inverse remains u=SP/(SE+P), not the retracted missing-S inverse. New here are the actual unit-root orientation/equivalence, H_G nonzero coupled integer receiver, and its square-N Gaussian-prime consequence. M3-T11-120 stays retracted: no quartic theta is substituted for physical z or anti-root V, no extreme phi allocation or fourth-power tail is reinstated.

Scope: odd split fresh primes outside content, u finite and nonzero, original nondegenerate packet. Projective infinity on M_rel>1 is already excluded by retained035; no new statement for M_rel=1, content or2-primary/degenerate loci. The zero-discriminant denominator pole case remains a boundary requiring its existing receiver. Other Gaussian-core square/lifting, common-global-point and exact-height conditions are not discarded.

## Next legal continuation

Reserve M3-T11-132: GaussianExtremeCoupledNonzeroIntegerReceiverSamePhysicalHeight. On exact R<=B, determine the actual joint height/range/multiplicity of (a,b,s,t,H_G) and frozen content data, especially the large-M_G branch, and whether the new nonzero divisor lock supplies a legal same-measure tail. If H_G is already consumed by the original root-line product, record the exact no-double-charge identity and move to a genuinely joint lift. The denominator branch must retain045's Legendre receiver and all singular shells; no new higher-p-adic unit-root sieve there. Preserve130 interior exclusion and123/128/129 scoped S4 data. Do not infer a deficit merely from one congruence class per p^L at fixed ambient coordinates.

GLOBAL_COUNTING_CREDIT=0; GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; PERFECT_CUBOID_NONEXISTENCE_CREDIT=false.
