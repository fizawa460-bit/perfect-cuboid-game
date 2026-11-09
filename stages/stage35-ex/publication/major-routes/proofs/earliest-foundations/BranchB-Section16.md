# Stage35EX Branch-B original Section16, with Section17 correction

> Exact historical Section16 excerpt and following Section17 correction from https://docs.google.com/document/d/1CKLon3eRKjsEVuIwgpSTV4DKHQ5GRWsfDw2SA6T5vNI/edit
> **Only** the arithmetic lemma a(t)=(t²−1)/(t²+1) is nonsquare for rational t>1 is retained for S194/S195, conditional on the cited classical Fermat fourth-power descent. The once-proposed unrestricted same-rank saturation/specialization split was NOT retained. This is NOT the unrelated Section16 common-G/K-support audit.

> Historical manuscript copied from Google Drive as LF-normalized readable text. No native byte/layout audit, computation replay, or new mathematical theorem PASS. The original STATUS/NEXT fields remain historical.

---

16. Same-rank index-two saturation locus is empty


STATUS=PROVISIONAL_EXACT_SUBSTANTIVE_NO_STAGE35_CREDIT
SOURCE_PRIMITIVITY_DOCUMENT_ID=1BwCwKePwVCJAg3XfVTE_3e8qNOmzToZ1F8paLYoIns0
EXTERNAL_THEOREM_LOCK=FERMAT_X4_MINUS_Y4_NOT_SQUARE
EXTERNAL_REFERENCE=Keith_Conrad_Infinite_Descent_or_equivalent_classical_Fermat_descent


Section 15.6 reduced every same-rank free-lattice enlargement on E'_t to index 2 and showed that such an enlargement requires
a(t)=(t^2-1)/(t^2+1)
to be a rational square.


We now eliminate that locus.


Assume
a=s^2
with s in Q and 0<s<1.
Since
a^2+b^2=1,
we have
b^2=1-s^4.


Write
s=p/q
in lowest positive integers with
0<p<q.
Then
b^2=(q^4-p^4)/q^4,
so
(b q^2)^2=q^4-p^4.


Because the right side is an integer and b q^2 is rational, b q^2 is an integer. Thus there is a positive integer r with
q^4-p^4=r^2.


Fermat's classical infinite-descent theorem states that
X^4-Y^4=Z^2
has no solution in positive integers X,Y,Z.
Therefore the assumed nonzero rational square a is impossible.


Hence, for every rational t>1,
a(t) notin Q^2.


Consequences:
E_PRIME_SAME_RANK_SATURATION_REQUIRES_A_SQUARE=true
E_PRIME_A_SQUARE_SPECIALIZATION_LOCUS_EMPTY=true
E_PRIME_SAME_RANK_SATURATION_GROWTH_POSSIBLE=false


Together with Section 15, the repaired exhaustive Branch-B specialization split sharpens to


BRANCH_B_SPECIALIZATION_SPLIT=
  GENERIC_IMAGE_MULTIPLE
  OR
  RANK_GROWTH.


There is no specialized torsion-growth branch and no same-rank free-saturation branch.


This still does not close Branch B: a physical quotient point may lie in the specialized generic image
<P3'(t),(0,0)>
and satisfy the two-square physical interval while its same D-point projects to nR on E.


16.1 Updated route


PREVIOUS_TARGET=E3_BRANCH_B_2ISOGENOUS_FREE_SPECIALIZATION_SPLIT_PREFLIGHT
PREVIOUS_TARGET_STATUS=PARTIAL_SUCCESS_TORSION_AND_SAME_RANK_SATURATION_BRANCHES_UNIFORMLY_ELIMINATED


LATEST_NEXT_ACTIVE_TARGET=E3_BRANCH_B_GENERIC_IMAGE_MULTIPLE_TWO_SQUARE_PREFLIGHT


FIRST_SUBTASK:
Write
S_t=mP3'(t)+epsilon(0,0)
with m in Z and epsilon in {0,1}.
Derive an exact uniform formula or squareclass identity for
2B^2-x(S_t)
under the already forced condition x(S_t) in Q^2.
Then combine it with
B^2<x(S_t)<=2B^2
and the same-D-point constraint
pi_E(U,V)=nR, |n|>=3.
Do not enumerate m, n, or t.
If the generic-image multiple branch survives, freeze the exact coupled multiple equation before broadening routes.


The RANK_GROWTH alternative remains a separate specialization branch and must not be silently identified with the generic-image case.


Credit firewall unchanged:
FORMAL_AUTHORITY=V74_GOAL4AK
HOSTILE_AUDIT_PERFORMED=false
T35_R3_PHYS_EMPTY_PROVED=false
STAGE35_MAIN_UNIFORM_ARITHMETIC_THEOREM_PROVED=false
RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false

---

## Section17: original dependency-audit correction (verbatim)

17. Dependency-audit correction: Branch-A primitivity remains open after cancellation-aware repair


STATUS=PROVISIONAL_EXACT_DEPENDENCY_REPAIR_NO_STAGE35_CREDIT
DEPENDENCY_AUDIT_ID=1nOcsEq6Vbh0HGf7-tF5IsTpVK6BB71yayiGqemeLf1o
DEPENDENCY_AUDIT_VERDICT=FAIL_HOLD
REPAIRED_SOURCE_ID=1BwCwKePwVCJAg3XfVTE_3e8qNOmzToZ1F8paLYoIns0
REPAIRED_SOURCE_REVISION_ID=ANLCKQkaWWdkY6QoI2pCcWkszN87eDm1kvaGkaxuvdkXEA9mJCPHYHf2FI-KuelZElRJJAeeA2X4jX7Y4hmN7TV0kIarOK_4Pv6RdTEobjI


17.1 Audit correction


The dependency hostile audit is accepted.
The former use of
P3(t) primitive in E_t(Q)/torsion for every rational t>1
inside Sections 15.6-16 was not justified by the old Branch-A Section 13.


Therefore the following Branch-B claims are withdrawn from the current safe state:
E_PRIME_SAME_RANK_SATURATION_INDEX_IF_NONTRIVIAL=2
E_PRIME_SAME_RANK_SATURATION_GROWTH_POSSIBLE=false
FREE_ISOGENY_SATURATION_GROWTH=false


The Section-16 arithmetic lemma itself remains retained:
E_PRIME_A_SQUARE_SPECIALIZATION_LOCUS_EMPTY=true.
It eliminates the specific index-two target-isogeny lattice defect conditional on the source lattice being primitive enough for that reduction, but it does not eliminate possible odd source-lattice saturation of P3(t).


The specialized torsion theorem also remains retained and audit-PASS:
E_PRIME_SPECIALIZED_TORSION_UNIFORM=Z/4Z
SPECIALIZED_TORSION_IMAGE_GROWTH=false.


17.2 Safe Branch-B specialization split


Until Branch-A specialized primitivity is repaired and re-audited, the exhaustive safe split is


BRANCH_B_SPECIALIZATION_SPLIT=
  GENERIC_IMAGE_MULTIPLE
  OR
  FREE_ISOGENY_SATURATION_GROWTH
  OR
  RANK_GROWTH.


The previous two-way split is superseded and must not be used.


17.3 New exact information from the Branch-A repair


The Branch-A source has now been rewritten cancellation-aware.


For each parity model, after factoring all p/q square support already contained in kappa, the actual translated reduced denominator roots are D1,E1, with:
B-even:
  D1|n,
  E1|m;
B-odd:
  D1||m-n|,
  E1|m+n.


The residual packet satisfies
(D1 E1)^2 | (p^2-q^2),
G^2 | (p^4+q^4),
where G=gcd(D,E), and the two odd support channels are disjoint because
gcd(p^2-q^2,p^4+q^4)|2.


For a hypothetical odd-prime magnification
[ell]H=P,
ell>=5,
the kappa-support primes are no longer treated by EDS denominators.
Instead, split-multiplicative component groups give the exact exponent sieve:
if rho|pq and
alpha=v_rho(kappa),
h=v_rho(pq)>0,
then
alpha/gcd(alpha,h)=ell.
In particular
ell|alpha=v_rho(kappa).


Thus every possible odd source-saturation prime >=5 lies in
L(kappa)=
{ odd primes ell>=5 : ell divides v_rho(kappa) for some rho|kappa }.


This is substantive narrowing but NOT uniform primitivity, because L(kappa) moves with t and may be nonempty.


17.4 Current dependency blocker


The exact remaining dependency is now:


E3_BRANCH_A_KAPPA_EXPONENT_RESIDUAL_PACKET_UNIFORM_CLOSURE_PREFLIGHT


Question:
Can one combine
ell|v_rho(kappa),
(D1E1)^2|p^2-q^2,
G^2|p^4+q^4,
and the residual square equations
to exclude every ell>=5 uniformly over primitive Pythagorean parameters?


A successful answer restores specialized primitivity and permits re-audit of Sections 15.6-16.
A failure must leave FREE_ISOGENY_SATURATION_GROWTH open.


17.5 Routing


PREVIOUS_TARGET=E3_BRANCH_B_GENERIC_IMAGE_MULTIPLE_TWO_SQUARE_PREFLIGHT
PREVIOUS_TARGET_STATUS=PAUSED_BY_LOAD_BEARING_PRIMITIVITY_DEPENDENCY


LATEST_NEXT_ACTIVE_TARGET=E3_BRANCH_A_KAPPA_EXPONENT_RESIDUAL_PACKET_UNIFORM_CLOSURE_PREFLIGHT


FIRST_SUBTASK:
work on the cancellation-aware Branch-A residual packet at ell>=5.
Do not resume the Branch-B generic-image multiple branch until the free-saturation branch is either closed or explicitly accepted as an independent open branch.
Do not reuse the invalid old implications d0|n or e0|m at primes dividing kappa.


Credit firewall remains unchanged:
FORMAL_AUTHORITY=V74_GOAL4AK
HOSTILE_AUDIT_PERFORMED=false
T35_R3_PHYS_EMPTY_PROVED=false
STAGE35_MAIN_UNIFORM_ARITHMETIC_THEOREM_PROVED=false
RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
