# M3-T11-185 — Content-supported full-S cofactor and fresh joint denominator conservation

STATUS=PROVED_FULL_S_CONTENT_SUPPORTED_COFACTOR / PROVED_FRESH_JOINT_DENOMINATOR_CONSERVATION / CORRECTED_184_COEFFICIENT_SCOPE / NO_NEW_GLOBAL_COUNT
PRIMARY_GATE=M3-T11-GATE-001 OPEN
GLOBAL_COUNTING_CREDIT=0
AUDIT_MODE=WITHIN_SESSION_DEDUCTIVE_REVIEW; INDEPENDENT_HOSTILE_AUDIT=NOT_RUN
TI=PARKED;120=RETRACTED;147–149=FROZEN

## Current authority and scope

Continuation from current MAIN, CARD-INDEX row413/latest184, current short RESULT-LEDGER, active ROUTE §17 and targeted134/181. MAIN is authoritative over stale historical NEXT blocks. No whole-history restart. Keep primitive positive endpoints R<=B, canonical ordering/signed witness, finite nonzero corrected common-u, all original content/coefficient/orientation/cyclic masks, four-square lift and intrinsic R. The fresh identities below hold for all retained content packets; the counting discussion is restricted to K=1, (h1,h2,h3)=(1,1,h), h<=C.

Use H=h1*h2*h3, M=M_rel, T0=tau0^sharp. Let R_H be the product of FULL prime powers p^lambda||R with p|H. Thus R=T0*M*R_H, gcd(R_H,T0*M)=1, rad(R_H)|H. R_H is not R/H: remaining powers at content primes must stay in R_H.

## 1. Correction to184: coefficients are norm-one, not globally Gaussian units

ROUTE17.2 has beta_i=B_i/conjugate(B_i), N(B_i)=c_i, and r_i=conjugate(epsilon_i)*conjugate(beta_i)*q_i^2. Therefore kappa_i=conjugate(epsilon_i)*conjugate(beta_i) is a rational Gaussian norm-one coefficient. It need not belong to the finite group of Gaussian integer units. Its numerator/denominator support is confined to content primes, so it IS a unit at both split primes over every fresh p outside H.

The statement 'the kappas are Gaussian units' in184 §2 is incorrect as a global statement and has been corrected in place. The product-phase formula Z_ph=q0^3*q1*q2*q3/(kappa1*kappa2*kappa3) and its fresh valuation proof are retained. At content primes the kappas cannot be discarded. No content-free global phase formula is inferred from the fresh calculation.

## 2. The full-S cofactor has only content-supported primes

Write Z_ph=X+iY, c=c_u=den(Z_ph), T=sum x_i*y_i, S=2T, and t=Den(S). From184, T*Y=2e1*e2*e3/R^3. On the retained finite nonzero-u locus Y=±a/c with gcd(a,c)=1. At every odd p|c, v_p(Y)=-v_p(c). R is odd by the primitive space-triangle interface, so multiplication by2 does not change denominator depths at primes dividing R. Also t|R^2 by134.

Fix p^lambda||R with p not dividing H. All three e_i are p-units. Consequently

v_p(T)+v_p(Y)=-3lambda.

The four fresh cores exhaust these primes. If p belongs to T0,184 gives v_p(c)=3lambda, hence v_p(T)=0 and v_p(t)=0. If p belongs to M,184 gives v_p(c)=lambda, hence v_p(T)=-2lambda and v_p(t)=2lambda. This also independently recovers134's relative D-only allocation; it does not reopen fresh G/interior branches.

Thus the fresh part of the FULL reduced S denominator is exactly M^2, with NO all-same fresh denominator contribution:

t=M^2*t_H,
rad(t_H)|H,
gcd(t_H,T0*M)=1,
t_H|R_H^2.

Here t_H is precisely the former t_*; the new content-support assertion replaces the formerly unresolved possibility that t_* contains all-same fresh primes. No conclusion about v_p(t_H) at content primes follows from the fresh unit argument.

Together with184:

c=M*T0^3*w_H,
rad(w_H)|H,
gcd(w_H,T0*M)=1,
w_H | R_H^3/H.

The last divisibility follows from c|R^3/H and disjoint fresh/content support. H|R_H, so the quotient is an integer.

## 3. Joint conservation and the content-free specialization

At every fresh prime, the sum of the c and t denominator depths is exactly3lambda. Therefore

(c*t)^sharp=(T0*M)^3=(R^sharp)^3,
c*t/R^3=w_H*t_H/R_H^3.

The right side is a positive rational number supported only at content primes. This is a pointwise conservation identity on the SAME physical endpoint, not two independent density factors. In particular H=1 forces R_H=w_H=t_H=1, so

c=M*T0^3, t=M^2, R=M*T0, c*t=R^3.

For H>1, do not promote c*t=R^3, t_H square, or w_H*t_H=R_H^3. Content numerator cancellation may affect both denominators. No uniform content-prime depth classification was proved here.

## 4. Count preflight: support compression does not remove the outer content cost

For fixed h<=C and R<=B, the177 uniform supported-integer lemma gives B^o choices for R_H,w_H,t_H, since their supports lie in h and their sizes are bounded by fixed powers of B. Treat these as correlated choices; multiplying their subpolynomial bounds is safe for an upper bound but yields no fixed power.

For Den(S)<=L, t=M^2*t_H implies M<=sqrt(L). Retained178 bounds the fiber for fixed h/coefficient packet/M by B^o, and the coefficient multiplicity is B^o. Hence

#E_K1(h<=C, Den(S)<=L) <= C*sqrt(L)*B^o.

This is exactly an application of178's existing small-M sector. It is not an additional independent sector saving. At L=B^(1/3-2xi-2epsilon), it is <=B^(1/3-epsilon+o), but this population already lies in the previously disposed M<=B^(1/6-xi-epsilon) sector. On the current large-M residual this maneuver gives no new closure.

Nor does fixing the fresh parts of c,t recover h: content primes have been deliberately removed. The supported-integer lemma is uniform only after h is fixed. It does not turn the C possible contents into B^o possibilities across all h. Conversely182's global fixed-S fiber fixes the entire rational value S, including its numerator; it does not give a B^o fiber for fixed Den(S). Do not substitute denominator fibers for rational-value fibers.

The new full-S support theorem narrows the unresolved joint correlation to R_H,w_H,t_H and the physical lift/numerators. It does NOT provide a fixed-power bound for their moving physical occupancy.184's tail-budget obstruction,183 fixed-c fiber/small-c sector,180/181 sectors and firewalls all remain intact. No actual endpoint lower bound or physical nonexistence result is claimed.

## 5. Verification and limits

verify_m3_t11_185.py deterministically constructs synthetic p-adic sphere/space-triangle witnesses at p=13,17,29,37 and lambda=1,2,3, with modulus p^(6lambda+3),80 unit-edge witnesses per stratum and all8 face signs. All7680 cases PASS the product identity and the only fresh depth pairs (v_p(c),v_p(t))=(3lambda,0) or (lambda,2lambda), and depth(c)+depth(t)=3lambda. Output: M3-T11-185-verification.json. These modular witnesses are not positive rational physical endpoints. Physical endpoints enumerated=0.

An initial test at p=5 did not produce unit-edge sphere witnesses: three nonzero squares cannot sum to0 mod5. That test stratum was replaced by37; no failed theorem case was hidden or reclassified as PASS. The final script requires80 accepted witnesses at every reported stratum.

The proof is the exact184 product identity plus primitive norm-conic valuations and exhaustive fresh support. Finite tests support replay but do not prove an asymptotic endpoint count. Review is within-session, not independent hostile auditing.

## Drive-only handoff / NEXT186

Attack K=1 large-c/large-M physical joint occupancy with t=M^2*t_H, c=M*T0^3*w_H and R=T0*M*R_H from the outset. The remaining cofactors have only h-supported primes. Seek a quantitative CONTENT-PRIME cancellation/numerator compatibility theorem preserving134's four-square/intrinsic-R lift and181's face-space gcd/lcm conditions, or a same-endpoint global count that genuinely reduces the outer h cost. The exact relation T*Y=2e1e2e3/R^3 is available, but at content primes the edge valuations and reduced numerators must be retained; no fresh-unit formula may be reused there.

Do not repeat supported-integer compression alone,178 small-M via a renamed Den(S) threshold,184 cubic divisor sums, cube-image density, denominator-only versions of182's fixed-S theorem, or independent products of fresh/core/modulus savings. If no counted content-prime correlation emerges, record the specific obstruction rather than crediting the support identity as closure.

Large-c threshold tail and K>1 low-median averaging remain separately OPEN. TI parked;120 retracted;147–149 frozen. Latest substantive result185; next candidate186. Gate OPEN and global credit0.

## Dependencies and durable locations

THIS_CARD_FILE_ID=1WoBtJLeBILL9XXGruJVE0sNYvvUOVnWb.
VERIFICATION_SCRIPT_FILE_ID=1rm27FqmygFuFvjRyLaXtSEh-ny3yJFsi.
VERIFICATION_JSON_FILE_ID=1Nl1mycgVASzytYhD-Rh0Iir16oHKl2t6.
184 product-phase and fresh valuations: CARD_DOC_ID=1jvdtwROi4MPSmaRha7XX1Q8SXv-OUrwgQNmKRNQLoBM (coefficient sentence corrected in place).
134 exact triangle denominators/D-only: CARD_FILE_ID=1Uxm_NWVBDZJj4dGZNSZkI8nMP2XFoJzs.
181 face-space filters: CARD_DOC_ID=1oHsUtVShm0IfGrmdxzpTcYgQgtjSGU9n6xguGG5KVHY.
177 support lemma,178 fixed-content/M count,182/183 fibers: locate by ID in CARD-INDEX.
Active ROUTE §17: DOC_ID=1_O0DDPJxK1DT6wV2cXm3UqaMcZc7YLFZgKpfQ7dXlaE. Its latest184 header is historical after this writeback; MAIN and CARD-INDEX supply current185/NEXT186. Proofs are not duplicated into ROUTE.
