# M3-T11-130 — Actual cubic unit root excludes strict-interior fresh allocation

Date: 2026-09-30. Current authority: Stage37 Drive, batch129 controls. Status: PROVED_EXACT_PHYSICAL_INTERIOR_EXCLUSION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0. This is an internal rederivation, not an external review.

## Primary result and dependencies

On the canonical finite-u, nondegenerate physical packet branch, every odd split fresh prime p^lambda || m_i has only extreme allocations c_p=0 or c_p=2lambda. No physical packet has 0<c_p<2lambda. This concerns original physical anti-roots, not quartic algebra roots.

Dependencies read from current ROUTE: Section35 gives A=1+u^2, E=4uS/A-4u^2/A, P=4u^2S/A and f(X)=X^3-SX^2+EX-P, whose roots are the actual v_i. Sections36–37 (M3-T11-029/033) give the targeted v_i a p-unit with v_p(v_i^2+1)>=2lambda; the other two have valuation -2lambda. Sections47–48 (M3-T11-040) give Q_S C_u=M_rel^2, c_p=v_p(C_u), k=2lambda-c_p, and min(4lambda,v_p(N_u))=2lambda+c_p for reduced u=a/b. At an interior prime b and a are units, v_p(A)=v_p(N_u)=n=2lambda+c_p=4lambda-k and v_p(S)=-k. Positive k makes this denominator valuation exact, not just capped.

## Exact proof

Suppose 0<c_p<2lambda, hence 0<k<2lambda and n>k. The terms involving S dominate E and P, so v_p(E)=v_p(P)=-(n+k)=-4lambda. Set g(X)=p^(n+k)f(X), an integral p-adic polynomial. Its ascending coefficient valuations are (0,0,n,n+k). Mod p it is a nonzero unit multiple of X-u, because P/E reduces to u. Thus it has exactly one unit root V in Q_p, reducing to u; its derivative there is a unit. Any physical unit anti-root must equal this V.

Direct substitution gives

f(u)=u^2 [u(A-4)/A-S].

Since p is odd and v_p(A)=n>k, A-4 is a unit, and the bracket has valuation -n. Therefore v_p(g(u))=k. Since u and V have the same residue, the factorization g(u)-g(V)=(u-V) times a p-adic unit proves v_p(V-u)=k exactly. Also V+u is a unit, since p is odd. Consequently

v_p(V^2+1)=v_p(A+(V-u)(V+u))=k<2lambda.

This contradicts the original physical condition v_p(v_i^2+1)>=2lambda. The strict-interior branch is empty. The argument needs no N_u square hypothesis, S4 hypothesis, rational discriminant square assumption, residual Selmer computation, or independence model.

## Independent contradiction check

If the physical unit root V existed, V mod p=u and both V^2+1 and u^2+1 would vanish to depth at least 2lambda. The same simple Hensel branch of X^2+1 would force v_p(V-u)>=2lambda, whereas the actual cubic forces the exact smaller depth k. This uses the actual anti-root V only. It does not identify quartic theta with physical z=S/2 and does not revive retracted120.

## Concrete local impostors above the129 S4 family

Take r=932+41250j, j>=0; a=2r, b=r^2-1, c=r^2+1, u=a/b, A=c^2/b^2. This is a subfamily of129's r=8+66k and retains square N and certified S4. Set q=1/625, d=1, S=Aq^2/(8u^2), z=S/2=(cq/(4a))^2. At p=5, lambda=2, c_p=2, k=2: v_5(A)=6 and v_5(S)=-2. The q-scaled cubic reduces to Y(Y^2+1), with three simple roots 0,2,3 mod5, hence splits over Q_5. The residual w^2=-F(z)/N is also locally soluble: its valuation is -12 and its unit reduction a square. The genus3 physical-equation projection103 likewise has a Q_5 lift (T=256u^4 A w). These local algebraic tests do not enforce the physical root-line.

The unique unit root instead satisfies v_5(V^2+1)=2, below the required4. Thus even these split/local-cover impostors fail a necessary original physical equation. For j=0: (a,b,c)=(1864,868623,868625), z=48288601/1389798400. This is an abstract local witness, not a rational physical endpoint, not an all-place global nonpole construction, and not an R<=B counting family.

## Verification and adversarial audit

verify_m3_t11_130.py is standard-library exact rational arithmetic and digit-by-digit unique Hensel lifting. It checks200 abstract allocations: p=5,13,17,29, lambda=1..5, every interior c_p, two S units. All coefficient valuations, f(u), root displacement and norm depth match the proof. It checks26 nested AP packets for the local splitting, residual square and failed physical root-line. PASS; physical endpoints enumerated0. Symbolic replay independently verifies f(u) and its Taylor expansion. Finite checks support, but do not replace, the universal proof.

Audit guards: odd p only; no conclusion at2 or content primes; finite-u nondegenerate branch only; lambda>=1; c_p extremes not included; all denominator reductions retained; targeted physical root is the unique unit root, not either pole root; the Gaussian root-line is an original necessary condition, not a newly charged density. Scalar squareclass choices cannot repair an actual root norm valuation. No extra multiplicity/count estimate is inferred.

## Authority consequence and next legal task

M3-T11-106/107 and ROUTE48 interior residual-unit identities remain correct conditional algebra on projected/local packets, but their strict-interior physical occupancy is now empty. Earlier interior character-dispersion attacks are superseded on this physical branch. Do not claim those abstract packets as realized endpoints. M3-T11-120 remains retracted; its quartic-root lock, extreme phi allocation and fourth-power tails are not reinstated.

Next card M3-T11-131: ExtremeAllocationActualAntiRootPhysicalSupport. Analyze c_p=0 and c_p=2lambda using the actual cubic plus the original coordinate-specific root-lines. In the all-extreme branch Q_S and C_u are squares on fresh support and partition M_rel^2. This is a routing identity, not a counting saving. Retain same physical R<=B, one endpoint one count, all content/exceptional branches and common-packet conditions. Seek a same-measure extreme-support theorem; if root-line compatibility is automatic, record that precisely and advance to genuinely joint physical conditions. Projective u=infinity/degenerate cases are not disposed of here.

GLOBAL_COUNTING_CREDIT=0; GLOBAL_FIXED_POWER_SAVING=false; PRIMARY_GATE_CLOSED=false; P_OVER_M3_LIMIT_PROVED=false; PERFECT_CUBOID_NONEXISTENCE_CREDIT=false. TI remains parked. Retain123 class-group/n factors,128 real signatures and129 scoped residual pole/local persistence results;130 supplies an additional original physical obstruction, not a whole S4 Selmer collapse.
