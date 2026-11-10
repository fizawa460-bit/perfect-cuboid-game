# M3-T11-205 — Fixed reduced space-edge fibers without an outer content cost

STATUS: PROVED_FIXED_REDUCED_SPACE_EDGE_BO1 / PROVED_SUMMED_SMALL_REDUCED_EDGE_SECTOR / CONTENT_MULTIPLICITY_ABSORBED_IN_FIXED_FIBER / MOVING_REDUCED_EDGE_SUPPORT_OPEN.
PRIMARY_GATE=OPEN; GLOBAL_COUNTING_CREDIT=0. Independent hostile audit NOT RUN. Existing separate-chat audit162–185 scope unchanged;186–205 not independently audited. TI parked;120 retracted;147–149 frozen. Date:2026-10-03 JST.

## 1. Current authority and result

Read current Stage37 MAIN, operational CARD-INDEX through204, short RESULT-LEDGER, latest204, dependencies203/195/194, and174. Active ROUTE17 retains D_i=tau*c_i and the primitive-space-direction interface. Old histories were not reread.174 is essential: it already proves an all-content B^{o(1)} fiber for a fixed labeled primitive space triangle, including unique recovery of the physical scale.

Let E(B) be the original positive primitive canonical physical endpoints R<=B, with all original masks retained. For each direction i set

h_i=gcd(R,e_i), u_i=e_i/h_i, v_i=f_i/h_i, D_i=R/h_i,
u_i²+v_i²=D_i², gcd(u_i,v_i,D_i)=1.

Here f_i is the positive opposite physical face diagonal. Auxiliary signed phases remain derived data; changing this notation does not replace original sign masks.

Uniformly for integer 1<=U<=B,

m_red(U;B):=#E(B; a specified labeled u_i=U) <= B^{o(1)}.       (205.1)

This allows h_i, the other two contents, R, the phase-visible/hidden split and all other labels to MOVE. There is no outer h_i sum.

Put u_min=min_i u_i. For 1<=Z<=B,

#E(B;u_min<=Z) <= Z B^{o(1)}.                                (205.2)

Consequently u_min<=B^{1/3-epsilon_u}, fixed epsilon_u>0, is a scoped o(M3(B)) sector at the retained M3(B)>>B^{1/3} scale. Global closure remains OPEN.

204's fixed-u statement was correctly unproved at that time.205 supplies its missing proof by using the primitive space triangle rather than summing its moving content through the complementary pair triangles.

## 2. A fixed primitive leg has divisor-many space triangles

Fix u_i=U>0 and use positivity v_i>0. Exactly

(D_i-v_i)(D_i+v_i)=U².                                     (205.3)

Write A=D_i-v_i and C=D_i+v_i. Then A,C are positive integers with A<C, AC=U² and A,C of the same parity. Conversely each such divisor pair determines

D_i=(A+C)/2, v_i=(C-A)/2.                                  (205.4)

Post-filter gcd(U,v_i,D_i)=1, D_i<=B and the retained masks. Thus there are at most d(U²)=B^{o(1)} admissible labeled primitive space triangles. No content has been fixed or summed. For odd U, A,C are odd; for even U, compatible pairs are even. U=1 has no positive v. Boundary v=0 is excluded.

Also D_i<=(U²+1)/2. This inequality alone would only convert174's small-D threshold into a roughly B^{1/6} reduced-leg threshold. It is NOT the counting proof of(205.2): the divisor-many packet argument improves the counted reduced-leg threshold to B^{1/3-epsilon_u}.

## 3. Fixed packet absorbs the entire content multiplicity

174 Sections2–3 prove that each fixed labeled primitive space triangle (U,v,D) has B^{o(1)} endpoint extensions uniformly at R<=B. Its smooth opposite-face elliptic receiver has polynomial coefficient/point heights and finite reconstruction of all normalized edges. Primitive scale is then unique:

R=lcm(Den(e_1/R),Den(e_2/R),Den(e_3/R)).                       (205.5)

The right side equals R because the edges are primitive; primewise at least one edge is a unit at every prime of R. Thus h_i=R/D is reconstructed, not a multiplier of the count. The other contents and tau are reconstructed too. Applying this theorem once for each packet in Section2 proves(205.1). A sum over U<=Z, followed by a finite union over the three direction labels, proves(205.2).

This proof uses174's FIXED LABELED TRIANGLE result, not just its stated D_min fiber. No hypothesis that the chosen i minimizes D_i is required.

## 4. Explicit elliptic cross-check and uniformity

For an independently readable receiver, fix(U,v,D) and let j,k be the other directions. Set t=e_j/h_i, a=e_k/h_i, c=f_k/h_i. Then

t²+a²=v², c²=U²+t².

The rational point

X=-t², Y=t*a*c

lies on

E_(U,v): Y²=X(X+v²)(X-U²).                                  (205.6)

Its three rational2-torsion roots are0,-v²,U². Since U,v>0 they are distinct, and

discriminant=16 U^4 v^4 (U²+v²)² !=0.

The coefficients in monic form are v²-U²,-U²v²,0, of polynomial height in B. X has rational height<=B² because both e_j and h_i are<=B. Given X, t is recovered with at most two signs, a from a²=v²+X with at most two signs, and the normalized vector is(U/D,t/D,a/D). Its primitive scale is unique by(205.5). c and the remaining diagonal/sign/original masks only post-filter this finite fiber. Thus even this larger two-face receiver has bounded physical reconstruction multiplicity. It is not asserted that every receiver point is an endpoint.

External counting input was rechecked in the primary source: Marta Dujella, arXiv:2312.03655v1, Theorem1.1 and the height comparison in the proof of Corollary1.3, PDF pp2–3, https://arxiv.org/pdf/2312.03655. Take k=Q and ell=2. h(E)=O(log B) and h(X)=O(log B). The stated canonical-height comparison gives hat h(P)=O(log B) with absolute constants. Choose T_*=B^A, one sufficiently large absolute A, so BOTH the coefficient-height threshold and point-height ceiling hold. Theorem1.1 then gives B^{O(1/log log B)}, uniformly in(U,v). The finite divisor packet has the same subpower scale. Use Theorem1.1 directly with enlarged height; do not assume a curve-dependent constant is uniform merely because a curve is fixed.

This is the same retained counting input as174/194, not a newly stronger external theorem.

## 5. Relation to204 and the low-median residual

On the median direction h_i=b,204 has

q_+=b_Q²r_+, q_-=b_S²r_-, b_Qb_S=b,
r_+r_-=-u_i².                                               (205.7)

Fixed u_i now has a B^{o(1)} physical fiber including ALL moving b_Q,b_S. This does not follow from treating the two square divisibilities as independent: it follows from reconstructing the endpoint through its space triangle and elliptic point.

After removal of(205.2), every direction satisfies

u_i>Z=B^{1/3-epsilon_u}, hence e_i=h_i u_i>Z h_i.              (205.8)

For the low-median branch b<=K this replaces204's lower bound u_i>B^{1/3-epsilon_e}/K by a threshold independent of K. No strict comparison of arbitrary epsilon choices is asserted.

The small physical-edge sector in204 at the SAME threshold is contained in(205.2): u_i<=e_i. It therefore must not receive a second disposal charge.174's small-D sector at the same threshold is also contained, because u_i<D_i. This is a valid deterministic inclusion, not a multiplicative gain. Other small-W/Sigma/Phi sectors may be removed by union only; no independence is asserted.

For the median direction,174 gives D_i=R/b=a_content*d_content*tau, while D_min=q_min*b. These are DIFFERENT direction labels in general.205 does not prove a subpower fixed-q_min fiber and does not close176's low-median average. Do not substitute D_min for R/b in(205.3).

## 6. What remains open and NEXT206

The new theorem pays the moving content ONLY WITHIN ONE fixed reduced-edge fiber. Summing all occupied U up to B still costs B^{1+o(1)} and does not beat the primary scale. No sparsity of the large-U occupied support follows from(205.1).

NEXT206: on u_i>B^{1/3-epsilon_u} for all i, low-median b<=K and the retained large-Sigma/large-D_min conditions, seek an actual support bound for occupied median U, or a same-physical joint bound for U and the complementary pair coordinates in(205.7), with the original N_T/full-S/phase masks. The primitive-space factor pair A=D_i-v_i,C=D_i+v_i, AC=U² is an exact receiver; its divisor count for fixed U has already been used. A new theorem must save on the moving U support rather than repeat fixed-fiber counting.

If this branch yields only another scalar relabeling, record the scope and switch to the distinct large-c threshold tail. Large-W, large-c_u/full-S and unshared conductor remain OPEN. Do not reopen K1-only177–181,134-superseded fresh-C_u, or201/202's normalization-scale coupling.

## 7. Verification and authority limits

verify_m3_t11_205.py and M3-T11-205-verification.json: PASS. Exhaustive divisor-packet comparison for160 primitive-leg labels gives203 packets; two exact positive primitive TWO-face partial examples test the elliptic map and scale recovery, including nonunit content17;90240 finite-field map checks PASS. The example edges(672,153,104), R697 has only two integral face diagonals and is NOT a physical endpoint. Finite-field points are NOT rational endpoints. Physical endpoints checked=0. These checks verify algebra/reconstruction, not the asymptotic theorem or independent audit.

Novelty is relative to the inspected Drive portfolio:174 supplies fixed-triangle and fixed-D results;204 explicitly left fixed reduced edge open.205 adds the fixed-leg divisor packet, the all-content fixed-U count and the summed small-reduced-edge sector. No literature-wide novelty claim. Within-session deductive review PASS; independent hostile audit NOT RUN. No retraction or global closure/credit change.
