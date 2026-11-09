# Stage35EX earliest selected physical E3 source and Kummer lift

> Original: https://docs.google.com/document/d/1J2ps_j6Z3oRQZHt3s2hTGadzNNd9t-RYaE2I7oh9qeQ/edit
> Direct parent of the selected four-square physical packet, E3 quotient and full Kummer/lift package; not a theorem that every global Stage35 point lies in Branch B.

> Historical manuscript copied from Google Drive as LF-normalized readable text. No native byte/layout audit, computation replay, or new mathematical theorem PASS. The original STATUS/NEXT fields remain historical.

---

Stage35EX — E3 physical Kummer coset / horizontal-lift preflight


STATUS=PROVISIONAL_EXACT_SUBSTANTIVE_NO_STAGE35_CREDIT
FORMAL_AUTHORITY=V74_GOAL4AK
GITHUB_ACCESSED=false
HOSTILE_AUDIT_PERFORMED=false
SOURCE_CURRENT_DOCUMENT_ID=1s43ClmstMA7FuEAq-ykN7xkD_DNU0scPUEyCt9NP1tw
SOURCE_E3_MW_DOCUMENT_ID=1fDhFTdYpXDySPTxqVKSVBxEGGwDMJvmNifv3y1ZWXHk
STAGE35_GATE=T35-R3-PHYS-EMPTY
ROUTE_CLASSIFICATION=CONTINUE_NARROWED
INPUT_E3_GENERIC_MW_STATUS=RETAINED_PROVISIONAL_SATURATED


Purpose


Continue the live E3_PHYSICAL_LIFT_VS_GENERIC_SUBGROUP_PREFLIGHT without reopening the completed E3 generic rank/saturation search. The goal is to derive the exact Stage35 genus-5 -> E3 map, identify the physical Kummer/lift condition, and compare it against the retained generic group
E3(Q(t)) = E3[2] direct-sum Z*P3.


No formal Stage35 / R29 / J12 / E1 / endpoint / Perfect Cuboid credit is changed.


1. Exact Stage35 diagonal source


Put
A=t^2-1,
B=2t,
C=t^2+1,
so A^2+B^2=C^2.


Put
alpha=A^2/C^2,
beta=B^2/C^2=1-alpha.


On the Stage35 selected diagonal genus-5 fiber, normalize by d != 0:
r=x/d,
s=y/d,
p0=p/d,
q0=q/d.


Then the exact equations are
p0^2 = alpha+r^2,
s^2  = beta-r^2,
q0^2 = 1-r^2.


For the physical chamber t>1 all original coordinates are positive/nonzero.


2. Exact E3 quotient map


Define
u = -r^2 = -(x/d)^2,
v = r*p0*q0 = x*p*q/d^3.


Then
u-alpha = -p0^2,
u+1     = q0^2,


and therefore
v^2 = u(u-alpha)(u+1).


Thus the exact selected quotient is the retained normalized E3
E3: v^2=u(u-alpha)(u+1).


The omitted Stage35 coordinate is not opaque. It is exactly the additional square condition
s^2 = beta+u.


For a positive physical point,
-beta < u < 0,
and the positive sign branch has v>0.


Hence, away from the already excluded zero/boundary loci, a rational E3 point lifts back to the selected Stage35 genus-5 fiber exactly when beta+u is a rational square; physicality adds the real interval/sign conditions.


3. Exact physical Kummer class


Use the full-2-torsion Kummer triple
delta(P)=([u],[u-alpha],[u+1])
away from the root cases.


For every physical quotient image,
u=-r^2,
u-alpha=-p0^2,
u+1=q0^2,


so
delta(P)=([-1],[-1],[1]).


Let T0=(0,0). Its 2-torsion Kummer class is
delta(T0)=([-alpha],[-alpha],[1])=([-1],[-1],[1]),
because alpha=(A/C)^2 is a square in Q(t).


Therefore the physical quotient condition forces
delta(P)=delta(T0).


Conversely, if an E3 point away from the root cases has delta(P)=delta(T0), then
-u,
-(u-alpha),
u+1
are rational squares. Adding the independent lift condition beta+u square reconstructs rational r,p0,q0,s and hence a rational Stage35 fiber point, up to sign choices. Physical positivity is then the separate real chamber condition.


Exact provisional conclusion:
E3_PHYSICAL_KUMMER_CLASS=DELTA_T0.


4. Comparison with the complete retained generic Mordell-Weil group


Retain the previously derived provisional group
E3(Q(t)) = E3[2] direct-sum Z*P3.


The Kummer map identifies E3(Q(t))/2E3(Q(t)). Therefore the generic points with physical Kummer class are exactly one coset:
T0 + 2E3(Q(t)).


Equivalently, every generic horizontal physical-compatible quotient point is
Q_n = T0 + 2n P3,
n in Z.


This is the main reduction of the batch. The generic-horizontal branch is no longer the whole rank-one Mordell-Weil group plus torsion. It is one explicit rank-one arithmetic progression/coset.


5. First horizontal members are boundary


Q_0=T0 has u=0, hence r=x/d=0. This is the x=0 boundary.


For n=+/-1, retain the exact doubled-generator coordinate
u(2P3)=alpha/beta.


On E3, translation by T0=(0,0) satisfies
u(R+T0) = -alpha/u(R).


Hence
u(Q_{+/-1})
 = -alpha/(alpha/beta)
 = -beta.


Therefore
beta+u(Q_{+/-1})=0,
so s=y/d=0. These are y=0 boundary points.


Thus any nonboundary generic horizontal Stage35 lift must satisfy
|n| >= 2.


6. Remaining horizontal lift sequence


Define
L_n(t)=beta+u(Q_n).


A nonboundary generic horizontal Stage35 lift requires
L_n(t) in Q(t)^{*2},
with |n|>=2.


Since
Q_n=T0+2nP3,
translation by T0 gives
u(Q_n)=-alpha/u(2nP3).


Also
u(2P3)=alpha/beta.


Therefore
L_n
 = beta-alpha/u(2nP3)
 = beta * (u(2nP3)-u(2P3))/u(2nP3).


For n != 0, 2nP3 lies in 2E3(Q(t)), so its Kummer class is trivial. In particular [u(2nP3)]=[1], and beta is already a square. Hence, for |n|>=2,


[L_n]
=
[u(2nP3)-u(2P3)]
in Q(t)^*/Q(t)^{*2}.


So the unresolved generic-horizontal lift problem is an exact one-dimensional elliptic difference-square problem.


7. Genus-2 lift-cover reformulation


The same lift condition admits a clean genus-2 model.


Let z^2=beta+u, so u=z^2-beta. In normalized coordinates:
v^2=(z^2-beta)(z^2-1)(z^2+alpha).


Scale
S=C*z
and use the integral E3 coordinate
X=C^2*u=S^2-B^2.


Then the lift cover is


H_t:
V^2=(S^2-B^2)(S^2-C^2)(S^2+A^2),


with the exact map
H_t -> E3poly,
X=S^2-B^2,
Y=V.


Indeed
X-A^2=S^2-C^2
and
X+C^2=S^2+A^2.


Thus the generic-horizontal lift question can also be viewed as the intersection of H_t(Q(t)) with the single E3 coset T0+2Z*P3.


8. Sharper candidate closure route


A generic identity L_n(t)=square in Q(t) must remain a square under every good specialization where it is defined. This suggests a substantially cheaper horizontal-branch attack than solving the moving genus-5 family directly:


choose one certified good rational specialization t0,
classify H_t0(Q) completely,
map every rational point to E3,t0(Q),
and determine the intersection with
T0 + 2Z*P3(t0).


The retained E3 work already source-locks an injective specialization at t0=4, so t0=4 is the preferred checkpoint if a complete genus-2 point classification can be certified.


At t=4:
A=15,
B=8,
C=17,


and the fixed genus-2 lift cover is


H_4:
V^2=(S^2-64)(S^2-289)(S^2+225).


If a complete proof shows that its image in the specialized generic subgroup contains only n=0,+1,-1, then every generic horizontal lift is boundary. This would close the generic-horizontal side of the Stage35 dichotomy in one fixed specialization.


This complete rational-point classification has NOT been proved in this batch.


A second possible reformulation uses the standard division-polynomial identity for differences x(nP)-x(mP) and function-field elliptic divisibility sequences. However, primitive-divisor existence alone does not supply the required odd-valuation/square obstruction. That parity gap remains load-bearing, so no EDS/primitive-divisor theorem is claimed here.


9. Routing consequence


The previous target
E3_PHYSICAL_LIFT_VS_GENERIC_SUBGROUP_PREFLIGHT
has advanced materially.


Provisional exact results:
E3_PHYSICAL_QUOTIENT_MAP_LOCKED=true
E3_PHYSICAL_LIFT_CONDITION=beta+u_IS_SQUARE
E3_PHYSICAL_KUMMER_CLASS=DELTA_T0
E3_GENERIC_HORIZONTAL_COSET=T0+2E3(Q(t))
E3_GENERIC_HORIZONTAL_PARAMETRIZATION=Q_n=T0+2nP3
E3_GENERIC_HORIZONTAL_BOUNDARY_N={0,+1,-1}
E3_GENERIC_HORIZONTAL_NONBOUNDARY_REQUIRES_ABS_N_GE_2=true
E3_GENERIC_HORIZONTAL_LIFT_SQUARECLASS=[u(2nP3)-u(2P3)]
E3_GENERIC_HORIZONTAL_GENUS2_COVER_LOCKED=true


The remaining generic-horizontal theorem gate is now:
E3_GENERIC_HORIZONTAL_LIFT_SPECIALIZATION_GENUS2_PREFLIGHT.


First subtask:
source-lock one fixed good specialization, preferably t=4 because the retained E3 work already certifies generic-subgroup injectivity there, and determine whether H_4(Q) can be completely classified with a proof-capable genus-2 / covering / Chabauty / Mordell-Weil method. Then pull every point back to E3,4 and test the exact coset intersection.


If that route cannot give a complete point set, the fallback is:
E3_DIVISION_POLYNOMIAL_DIFFERENCE_SQUARE_PARITY_PREFLIGHT,
with an explicit requirement to bridge primitive-divisor existence to odd valuation of the difference squareclass before any theorem credit.


Anti-loop:
- do not redo E3 rank-one or generator saturation;
- do not replace the exact Kummer coset by a bounded n search;
- do not count one fixed genus-2 search as a proof without complete rational-point certification;
- do not infer square obstruction from primitive-divisor existence without valuation parity;
- do not forget physical real interval/sign conditions in any final lift claim;
- do not promote Stage35, R29, J12, E1, endpoint, or Perfect Cuboid closure.


10. Credit firewall


T35_R3_PHYS_EMPTY_PROVED=false
STAGE35_MAIN_UNIFORM_ARITHMETIC_THEOREM_PROVED=false
RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


Hostile audit/source-lock review remains required before any formal promotion.


11. Exact second elliptic quotient of the genus-2 lift cover


The genus-2 model H_t has an additional exact elliptic quotient that is already present in Stage35.


Work in normalized coordinates
H_t:
v^2=(z^2-beta)(z^2-1)(z^2+alpha),
where z^2=beta+u.


Besides the involution z -> -z giving the E3 quotient through u=z^2-beta, compose this involution with the hyperelliptic involution. On z != 0 put
U=z^2,
W=z*v,
q=1/U=1/z^2,
h=W/U^2=v/z^3.


Then
h^2=(1-beta*q)(1-q)(1+alpha*q).


Now define
X0=beta*(1+alpha*q),
Y0=alpha*beta*h.


Direct substitution gives
Y0^2 = X0*(X0-(1-alpha^2))*(X0-1).


This is exactly the retained Stage35 quotient E0, not merely a curve with the same j-invariant.


Thus H_t has explicit degree-two quotient maps to
E3: v^2=u(u-alpha)(u+1)
and
E0: Y0^2=X0(X0-(1-alpha^2))(X0-1).


At the obvious horizontal boundaries:
- Q_0 on E3 has z^2=beta and maps to the E0 2-torsion point X0=1;
- Q_{+/-1} has z=0 and maps to the E0 point at infinity after projective completion.


This gives a more structured next attack on the generic-horizontal branch.


Important anti-loop distinction:
the previously audited statement that unconstrained E0+E3 pair compatibility regenerates the full Stage35 source remains valid and is not being reopened. The new restriction is that the E3 coordinate has already been proved, for a generic horizontal physical-compatible image, to lie in the single coset
T0+2Z*P3.
The new question is whether E0 arithmetic can classify the H_t-points lying over that one coset. This is strictly narrower than arbitrary E0+E3 compatibility.


Updated preferred next target:
E3_COSET_E0_BIELLIPTIC_HORIZONTAL_INTERSECTION_PREFLIGHT.


First subtask:
derive/source-lock the generic Mordell-Weil baseline of the retained E0 factor only to the extent needed for H_t, and determine whether the exact map above forces every Q(t)-rational H_t point over T0+2Z*P3 to one of the boundary packets. Do not redo the old unconstrained pair-compatibility argument.


Fallback if the E0 baseline does not collapse the horizontal intersection:
use the already identified good injective specialization t=4 and attempt a complete proof-capable classification of
H_4: V^2=(S^2-64)(S^2-289)(S^2+225),
followed by exact pullback to the specialized E3 coset.


This E0 identification changes routing priority only; it grants no theorem/closure credit.