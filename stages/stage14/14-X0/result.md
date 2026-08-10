# Stage14-X0 — three-receiver exact-transfer audit

## Status and source snapshot

`COMPLETE_THREE_RECEIVER_EXACT_TRANSFER_AND_FIBER_AUDIT`

This is an independent read-only audit of the Stage14 barrier receivers.  It
does not edit a canonical index, an exponent ledger, or any predecessor Stage.

```text
main snapshot                         e7b8675d434a62c00df3ae94c4220247dcda6cf0
merged sources                        14-4cg, 14-s7-21, 14-t58
toolbox-av reviewed PR head            a6b49caf4c94ac03826b38921a8077cc26fa4902
tH16 reviewed PR head                  ad7fae945e604cee1a03bfe6e49e14549d5b6c32
```

The last two heads were reviewed as related成果; neither is silently treated
as merged main input.  Every promotion boundary in them remains false.

The three audited receivers are

1. `CoupledCommonCoreGaussianResidualIncidence` (CCGRI);
2. `BalancedDualCRTShortVectorEnergy` (BDCSVE);
3. `SharedUCanonicalPrimeDeltaToroidalSecondMoment` (SCPTSM).

The whole-family bound remains `B^(7/8+o(1))`.

## 1. Complete correspondence table

| Field | CCGRI | BDCSVE | SCPTSM |
|---|---|---|---|
| physical object | ordered off-diagonal pair of reduced states | same ordered off-diagonal pair | one fixed-`U` physical state inside a coefficient sum |
| outer fixed data | same squarefree `(xi,k)`, eight cells and balanced block | orientation packet `Pi`, same `(xi,k)` and eight cells | primitive `U`, finite `epsilon`, divisor-fan `k`, invisible branch |
| moving variables | pair roots, four Gaussian hosts, `(C,u_res,v_res)` | `(x1,y1,x2,y2)`, `(z1,z2)`, primewise root orientations | canonical `pi`, `ell=N(pi)`, primitive `V`, `delta=N(V)/k`, angular lift |
| exact labels | `q_beta=q_gamma=C*u_res`, `q_S=q_T=C*v_res` | `Lambda_xi subset Z^4`, `Lambda_k subset Z^2`, primitive `z` ratio | `t=a/b`, `x=p/q`, `u_tor=x/t`, `v_tor=t*x` |
| selector | all primitive, coprimality, canonical interval and reconstruction masks | the identical physical masks plus a legal primewise orientation branch | centered physical coefficient, canonical/primitive/interval/reconstruction/bad-prime masks |
| arithmetic support | `C<=B^(3/8+o(1))`, `u_res*v_res<=B^(1/4+o(1))` | root boxes `B^(1/16)` and `z` box `B^(1/8)`; determinants `xi^2,k^2` | sharp radial hyperbola `ell*delta<=Y_U`; `B^o(1)` angular cell fibers |
| average range | balanced `(xi,k)` physical collision packets | same balanced packets; sum `#C(Pi)` with each pair charged once | distinct auxiliary split primes `p,q~L`, then physical hyperbola sum |
| quantifier order | sum packets/pairs, then expose common-core datum | fix orientation packet/lattices, count compatible short roots, then average packets | fix `U,epsilon,k`; sum `p!=q` of squared physical-state sums |
| kernel/sign | positive Gaussian square-divisor incidence | positive homogeneous CRT short-vector incidence | signed `K_p(t,x)K_q(t,x)` toroidal Kummer kernel |
| required gain | some fixed `eta>0` below `B^(7/8)` | `<<B^(7/8-eta+o(1))` | zero fixed-power loss: `P^2 B^o(1) sum|w_s|^2` |
| proved so far | exact equal shells/common core/hyperbolic residual range | exact orientations/determinants/rank caps/product ratio | exact toroidal kernel, masks and radial-cell energy; tH16 no-import boundary |
| still open | uniform physical reconstruction fiber or centered common-core incidence | average simultaneous short-vector scarcity | SMTKLS or THJB; squareclass row coherence must be broken |

Notation guard: CCGRI's `u_res,v_res` are positive residual norm quotients.
They are not t58's toroidal `u_tor=x/t,v_tor=tx`.  Reusing the letters does not
define a variable transformation.

## 2. Exact common coefficient space for receivers 1 and 2

CCGRI and BDCSVE are two deterministic projections of one decorated physical
pair.  Define

```text
JointBalancedCollisionPacket J =
  (physical state pair;
   xi,k; R,S,T,J; alpha,beta,gamma,delta;
   x1,y1,x2,y2,z1,z2,r1,s1,r2,s2,omega1,omega2;
   legal primewise orientations;
   four Gaussian square descents;
   canonical/primitive/reconstruction masks).
```

On `J`, the s7-21 CRT data are obtained directly from the cell-square
congruences.  The 4cg data are obtained from the same roots by

```text
q_k  = N(Z_beta)/beta^2 = N(Z_gamma)/gamma^2,
q_xi = N(Z_S)/S^2       = N(Z_T)/T^2,

C = oddpart(H_k^+/oddpart(S*T))
  = oddpart(H_xi^+/oddpart(beta*gamma)),

u_res=q_k/C,  v_res=q_xi/C.
```

Also the rank-one `Lambda_k` direction is exact:

```text
(z1,z2)=d*(a_z,b_z), gcd(a_z,b_z)=1,
b_z*g2*x1*y1=a_z*g1*x2*y2.
```

Therefore

```text
J -> CCGRI data     exact
J -> BDCSVE data    exact
```

and both maps preserve the same physical pair and masks.  This is the
previously unrecorded common coefficient space.  It is a **joint refinement**,
not an estimate.

No inverse or estimate transfer follows yet.  A CCGRI datum forgets the
primewise CRT orientations and short-span geometry.  A BDCSVE datum, when
stated only as lattices/short vectors, forgets the four Gaussian host choices
and common residual core.  To transfer a bound in either direction one must
prove that the relevant projection fibers are `B^o(1)` uniformly and that each
physical pair is charged once.  Neither predecessor proves this.

## 3. Receiver classification

| Direction | Verdict | Reason |
|---|---|---|
| CCGRI vs BDCSVE | `SAME_PHYSICAL_PROBLEM_DIFFERENT_EXACT_PROJECTIONS` | identical pair, labels, cells and masks; common joint packet exists |
| CCGRI -> BDCSVE estimate | `ADAPTER_NEEDED` | common-core datum does not control orientation/short-span fiber |
| BDCSVE -> CCGRI estimate | `ADAPTER_NEEDED` | lattice datum does not control Gaussian-host/common-core fiber |
| either s receiver -> SCPTSM | `ESSENTIALLY_DIFFERENT_PROBLEM` | pair-positive collision average versus fixed-`U` signed one-state auxiliary-prime second moment |
| SCPTSM -> either s receiver | `ESSENTIALLY_DIFFERENT_PROBLEM` | fixed `U`, `(ell,delta)` and toroidal characters have no exact identification with moving `(xi,k)` eight-cell collision packets |
| SCPTSM -> quadratic product-row frame | `ONE_WAY_EXACT_PROJECTION_BUT_CIRCULAR_ENERGY` | tH16 gives `K_r(s)=chi_{D_s}(r)`, but the collapsed coefficient norm is the unresolved squareclass-fiber energy |

In particular, the shared occurrence of Gaussian integers, squareclasses,
hyperbolas, or the exponent `1/4` does not make receiver 3 a specialization of
receiver 1 or 2.

## 4. Proof obligations closed by combining existing results

The following obligations can now be marked closed without a new analytic
claim.

1. **Same-pair compatibility of 4cg and s7-21.**  Both reductions can be
   attached simultaneously to `J`; there is no coefficient-space mismatch.
2. **No independent-savings multiplication.**  Since both are projections of
   the same positive pair, hypothetical gains cannot be multiplied unless a
   joint counting theorem explicitly charges each `J` once.
3. **SCPTSM mask adapter.**  t58 already makes every radial cell `B^o(1)` in
   coefficient energy; X0 does not reopen this gate.
4. **SCPTSM reciprocity adapter.**  tH16's
   `Delta_s=(B^2P^2-A^2Q^2)(B^2Q^2-A^2P^2)` gives an exact one-way quadratic
   character projection and legally imports the tH14-R2 product-row frame.
5. **Reason that this reciprocity route does not finish.**  States with the
   same `D_s` give identical auxiliary-prime rows, so the new coefficient
   energy `sum_D |sum_{D_s=D}w_s|^2` is exactly the missing fiber energy.

The following remain open: either s-side projection-fiber theorem, average
short-vector scarcity, common-core centered incidence, SMTKLS, THJB, and the
fixed-`U` mixed branch.

## 5. Finite computation and falsification plan

`receiver_transfer_audit.py` enumerates reduced states with `Q<=300`, selects
same-`(xi,k)` dual-cross pairs, reruns every s7-21 divisibility/orientation
check, derives the 4cg common core from the same pair, and measures projection
fibers.

Observed diagnostic:

```text
dual-cross physical pairs                 24
(xi,k,C,u_res,v_res) fiber histogram      {1: 24}
(xi,k,primitive z ratio) histogram        {1: 24}
joint projection histogram                {1: 24}
```

This finite injectivity is evidence for the next lemma, not proof of a uniform
`B^o(1)` bound.  The audit deliberately prints that the asymptotic fiber claim
is unproved.

Three required counterexample/stress families are retained:

- **projection collision search:** increase `Q` and record the first repeated
  `(xi,k,C,u_res,v_res)` or joint key, together with differing cells and roots;
- **non-Cartesian fixed-`U` support:** t58's `3-of-4` toroidal rectangle shows
  that `pi/V` tensorization is false even with radial multiplicity two;
- **equal-squareclass row coherence:** tH16's `r` distinct same-`D` states give
  second moment `P(P-1)r^2`, while source `L2` energy is only `r`; coefficient
  energy roadworks alone cannot prove SCPTSM.

Useful finite correlations to log in the next run are

```text
fiber multiplicity versus C,
fiber multiplicity versus gcd(u_res,v_res),
fiber multiplicity versus primitive z ratio,
CRT short-span rank versus C and u_res*v_res,
same-D multiplicity versus radial (ell,delta) multiplicity.
```

None of these finite statistics may be promoted to an asymptotic saving.

## 6. Highest-probability next move

The best next move is not another generic large-sieve import.  It is the
charge-preserving s-side lemma

```text
JointCommonCoreCRTPhysicalFiberLemma:
for fixed legal (xi,k), cells, primewise orientations,
(C,u_res,v_res), and primitive z ratio,
the number of physical JointBalancedCollisionPackets is B^o(1),
uniformly over the balanced endpoint.
```

Why this ranks first:

- it attacks the only missing arrow between the two strongest exact s-side
  reductions;
- all its variables are integral and already present in merged audits;
- the finite sample is injective rather than merely low-multiplicity;
- success lets one count on the small common-core hyperbola while retaining
  the CRT determinant/rank restrictions, with no double charging;
- failure should yield an explicit parametric high-fiber family, which is
  itself decisive and will prevent more false reconstruction arguments.

The lemma must be proved algebraically (or refuted by a growing family), not
inferred from the finite scan.  Only after it is proved should one test whether
the resulting joint datum count gives `B^(7/8-eta+o(1))` for a fixed `eta>0`.

SCPTSM should continue independently through t/tH via SMTKLS or THJB.  It is
not the preferred X0 bridge because tH16 already identifies a genuine
same-squareclass coherence obstruction and no s-side exact variable map
removes it.

## Locked boundary

```text
STAGE14_X0=COMPLETE_THREE_RECEIVER_EXACT_TRANSFER_AND_FIBER_AUDIT
MAIN_SNAPSHOT=e7b8675d434a62c00df3ae94c4220247dcda6cf0
CCGRI_BDCSVE_COMMON_PHYSICAL_COEFFICIENT_SPACE_PROVED=true
CCGRI_BDCSVE_JOINT_EXACT_REFINEMENT_PROVED=true
CCGRI_IMPLIES_BDCSVE_ESTIMATE=false
BDCSVE_IMPLIES_CCGRI_ESTIMATE=false
S_TO_FIXED_U_EXACT_VARIABLE_TRANSFER_PROVED=false
FIXED_U_TO_S_EXACT_VARIABLE_TRANSFER_PROVED=false
TH16_QUADRATIC_PROJECTION_IMPORTED_AS_RELATED_RESULT=true
TH16_QUADRATIC_PROJECTION_CLOSES_SCPTSM=false
JOINT_FINITE_SAMPLE_INJECTIVE=true
JOINT_PHYSICAL_FIBER_B_O1_PROVED=false
JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=false
SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
MAIN_S_ROUTE_BLOCKED_BY_X0=false
S_ROUTE_BLOCKED_BY_X0=false
T_TH_ROUTE_BLOCKED_BY_X0=false
TOOLBOX_ROUTE_BLOCKED_BY_X0=false
NEXT_RECOMMENDED=JointCommonCoreCRTPhysicalFiberLemma
```
