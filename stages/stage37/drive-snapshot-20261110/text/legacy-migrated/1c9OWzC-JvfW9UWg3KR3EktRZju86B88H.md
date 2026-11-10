# M3-T11-160 — Candidate③: physical preselector chart and large H-kernel energy disposal

STATUS=PROVED_GLOBAL_FIRST_COVER_HIGH_KERNEL_ENERGY_SECTOR_FROM_RETAINED_THEOREMS / PRINCIPAL_CLASS_OPEN
PRIMARY_GATE_STATUS=OPEN
GLOBAL_COUNTING_CREDIT=0
NEW_ENDPOINT_COUNT_BOUND=false
NEW_H_ENERGY_TAIL_BOUND=true
CANDIDATE_III_EXHAUSTED=false
AUDIT_MODE=WITHIN_SESSION_WRITTEN_PROOF_AND_DUAL_COMPLETE_FINITE_ENUMERATION_NOT_EXTERNAL_AUDIT
NEXT_CANDIDATE=M3-T11-161: existing TQ-GATE-002 low-kernel first-cover collision estimate, or the still-untested M3-A-001 centered receiver; no new gate

## 1. Current authority and result
Fresh native MAIN / INDEX / RESULT-LEDGER / active ROUTE designate159.159's endpoint-conditioned026 saturation/rank/energy costs remain valid.160 selects its explicitly named alternative: the original TQ-GATE-002 physical first-cover population H_F(B), BEFORE imposing the last H-square condition. We read original ROUTE Sections14.1,15.1,82.1–82.5 and canonical TQ-GATE-002 / T11-010/011/012. No all-history reread or degree enumeration.

Retained whole-population inputs are

 |H_F(B)| ≤ B^(1/2+o(1)),
 m_rho(B):=#{s∈H_F(B):C/X=rho} ≤ B^o(1), uniformly in rho.       (160.1)

These are T11-010 / ROUTE14.1, including all content, physical parents and reconstruction fibers.160 does not reprove the Dujella/Stage14 inputs. Its new energy estimate explicitly depends on them.

For κ the positive squarefree representative of [H], define r_κ and Q_H as in the existing receiver. Then, uniformly for K≥1,

 r_κ(B) ≤ B^(1+o(1))/sqrt(κ),
 Q_H^{κ>K}(B) ≤ B^(3/2+o(1))/sqrt(K).                          (160.2)

In particular

 Q_H^{κ>B^(7/4)}(B) ≤ B^(5/8+o(1)) = o(B^(2/3)).                (160.3)

This is a real fixed-power disposal of one sector of the GLOBAL H-energy problem, not merely a fixed-content estimate. It is NOT a new endpoint-count estimate: κ=1 remains, including every endpoint. No global goal closure or E_bal improvement is claimed.

## 2. Concrete physical population before the last selector
Use the positive integer preselector covering family

 A(B)={(Y,C,X,R):0<C≤X, Y>0, gcd(Y,C,X)=1, R≤B,
                 R²=Y²+C²+X²,
                 C²+Y²=Q², X²+Y²=L² for positive integers Q,L}.  (160.4)

The missing condition is C²+X²=square. Exact space height, positive edges, primitivity and both already-retained faces remain. Equal C=X is included; it is not excluded by an unproved classification. Each first-cover physical state reconstructs such a parent after ordering its missing-face pair, retaining its chart/orientation labels when necessary. Conversely each parent has the explicit t28 chart below. Original H_F may retain a different canonical orientation, chart label or additional exceptional-packet filtering; the finite A census is NOT declared literally equal to canonical H_F. No chart multiplicity is silently used in the energy proof, which works directly on H_F via(160.1).

For A's own normalization, a fully completed primitive geometry contributes exactly three shared-edge states, since all three choices of Y pass. Equal edges cannot occur on a completed geometry because sqrt(2)*C is not an integer. Thus r_A(1;B)=3P(B). This follows from the integer predicates, not finite zero counts. It supplies a concrete original-physical host without substituting a full residue box or dropping another physical square.

### Exact chart and squareclass adapter
Let g=gcd(R,C), D=R/g, c=C/g, ell=L/g. Since g² divides L², ell is integral. Choose coprime positive a>b by a/b=(D+ell)/c. The primitive Pythagorean direction gives

 D=epsilon(a²+b²)/2, c=epsilon ab, epsilon∈{1,2}.

Let p/q=(R+X)/Q in lowest terms, p>q>0, S=p²+q². Then

 X/g=D(p²-q²)/S, Q/g=2Dpq/S, Y/g=epsilon Z/S,
 Z²=(bp-aq)(aq+bp)(bq-ap)(bq+ap).                              (160.5)

The displayed rational Z is integral because its square is an integer. It is positive because Y>0. The Euclid identities give a²+b²≤2R and p²+q²≤2R, so parameters and all chart variables have the correct polynomial physical height; they are not chosen independently in a four-dimensional box.

With A0=a²+b², D0=p²-q², define

 H=(A0 D0)²+(2ab S)²,  H+4Z²=A0² S².

Exactly

 (g epsilon)² H = (2S)²(C²+X²).                              (160.6)

Hence [H]=[C²+X²]. If (C0,X0) is the primitive ratio vector obtained by dividing C,X by their gcd, then

 κ=sf(C0²+X0²),    C0²+X0²≤R²≤B².                           (160.7)

This is an exact preselector population/height adapter. It does NOT endow it with026's all-endpoint equal-tau four-core fresh modulus: such an extension is not proved. TQ-005's existing two-Gaussian-spin adapter is a possible receiver on this first-cover population; its analytic global estimate remains open.

## 3. Proof of the large-kernel energy estimate
Fix κ. Every ratio rho=C/X has a unique primitive positive pair (C0,X0) and satisfies

 C0²+X0²=κ z², 1≤z≤B/sqrt(κ).

For each z the number of integer representations of κz² as two squares is at most 4d(κz²)=B^o(1), uniformly because κz²≤B². This divisor bound follows from Gaussian unique factorization; restricting to positive primitive pairs only reduces the count. Multiplying by the RETAINED uniform m_rho≤B^o(1), not by an assumed independent density, yields

 r_κ≤B^o(1) floor(B/sqrt(κ)).                                 (160.8)

All constants are uniform in κ on this physical range; no coefficient/content family is resummed afterward. Let N_>(B;K)=sum_{κ>K}r_κ. Then

 Q_H^{κ>K}=sum_{κ>K}r_κ²
             ≤ [B^(1+o(1))/sqrt(K)] N_>(B;K)
             ≤ B^(3/2+o(1))/sqrt(K),                          (160.9)

using the complete host bound(160.1). More generally K=B^(5/3+η), fixed η>0, gives B^(2/3-η/2+o(1)). The choice η=1/12 gives(160.3). At η=0 there is no certified little-o margin; do not promote the boundary exponent without further log control.

## 4. What remains and what has NOT been improved
Split Q_H into κ≤B^(7/4) and κ>B^(7/4). The second term now satisfies the receiver. The first includes κ=1 and remains OPEN. Since κ=1 contains all endpoints,160 does not remove any endpoint directly. The low-kernel support grows with B; a fixed-twist/Faltings result or a finite list of kernels does not control it.

The retained same-ratio and reciprocal-ratio collision energies are already B^(1/2+o(1)) by010. The retained small Möbius-direction sector is already negligible by011.012's correction is essential: large similarity content d is norm over bilinear gcd and cannot be charged as another independent root density. These are retained, not rediscovered credits.

The unresolved substantive target is still the original TQ-GATE-002 off-ratio collision incidence on κ≤B^(7/4), with complete physical masks and all moving kernels/parents/content counted. This is not a new gate. Directly bounding its principal κ=1 class would also reach the goal without proving small energy in every other class; do not insist on the stronger full-energy statement if a principal-class argument becomes available.

159's one-variable product rank obstruction is about coefficients already on the endpoint congruence shell. The present first-cover host does not impose the last H-square condition, and so does not suffer that specific self-conditioning by definition. Its coefficients are still arithmetically dependent; no inverse-fraction or large-sieve applicability is inferred merely from constructing the host.158 terminal energy and this H-energy remain different populations.

## 5. Complete finite physical replay
verify160.cpp enumerates ALL A(10^6) in two ways:
1. Every primitive Euclid Pythagorean face, every positive scale with face hypotenuse≤B, both choices of shared leg; then pair partners with C≤X and apply primitive/space-square/space-height predicates.
2. For each shared Y≤B, enumerate d<Y dividing Y², write partner X=(Y²/d-d)/2 and face hypotenuse (Y²/d+d)/2, impose parity and height, then the same final predicates.
These lists coincide. Completeness follows from Euclid's theorem and the exact difference-of-squares factorization. Positive space height guarantees each constituent face hypotenuse≤B. Ordering C≤X prevents duplicate missing-face pairs; Y remains distinguished. Raw predicates do not impose the last face square.

Python separately replays every integer predicate, primitive ratio, factorization/squareclass, t28 coordinate identity and height reconstruction. The C++ quartic calculations use128-bit integers; B≤10^6 keeps the largest checked expressions below that range. Python uses unbounded integers. The finite kernel cutoff is tested exactly by κ^4>B^7, not floating-point thresholds.

| Exact R cutoff |A states|Squareclasses|A energy|High-kernel energy κ>B^(7/4)|
|---|---:|---:|---:|---:|
|1000|2|2|2|0|
|10000|25|25|25|6|
|100000|89|89|89|19|
|1000000|255|255|255|70|

All255 missing-face squareclasses are distinct ONLY in this finite census. This does not prove injectivity, asymptotic near-linear energy, or global endpoint scarcity. The literal original H_F chart population may differ by canonical labels/exceptional filters; its numerical counts are not substituted by A's without a separate exact multiplicity convention. The asymptotic proof(160.9) does not use any census number.

## 6. Continuation and retained state
Next161 candidate should stay on an existing③ receiver: test TQ-005/tH collision machinery against the now-explicit physical low-kernel host, preserving the moving κ range and distinguishing residue collisions from global rational squareclass collisions. Reopen only with an actual admissible coefficient/range/energy estimate; mere Fourier algebra, fixed-fiber counts or more finite data do not suffice. M3-A-001 centered directional correlation remains an untested separate③ receiver. Candidate③ is not exhausted; other routes are not declared defeated.

Retain152/153 sectors;E_bal unresolved;155 witnesses;156 uniform raw-tail obstruction and restricted variants OPEN;157 certificate;158 theorem-match failures;159 coefficient costs;TI parked;120 retracted;147–149 frozen curves. This card adds a proved GLOBAL H-energy SECTOR bound dependent on retained010, but no total H-energy bound and no endpoint-count saving. P(B)/M3(B)->0 remains OPEN.
