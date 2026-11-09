# Stage35EX original E3 generic Mordell–Weil proof

> Original: https://docs.google.com/document/d/1fDhFTdYpXDySPTxqVKSVBxEGGwDMJvmNifv3y1ZWXHk/edit
> Rank-one/torsion/saturation statements over Q(t), NOT automatic claims about every rational specialization. Source calculations are not independently replayed here.

> Historical manuscript copied from Google Drive as LF-normalized readable text. No native byte/layout audit, computation replay, or new mathematical theorem PASS. The original STATUS/NEXT fields remain historical.

---

Stage35EX — E3 generic Mordell–Weil / Kummer baseline preflight


STATUS=PROVISIONAL_SUBSTANTIVE_PARTIAL_BASELINE
FORMAL_AUTHORITY=V74_GOAL4AK
SOURCE_CURRENT_ID=1gGpjEEfpfVoPvU9BobfXacwPgj4H0ITuIlYNV8eJJIY
GITHUB_ACCESSED=false
ACTIVE_TARGET=GENERIC_SECTION_LIFT_SPECIALIZATION_GROWTH_PREFLIGHT
FIRST_SUBTASK=CERTIFY_GENERIC_MW_KUMMER_BASELINE_FOR_SELECTED_QUOTIENTS
SELECTED_QUOTIENT=E3
E3_QT_TORSION=Z/2Z_x_Z/2Z
E3_QT_RANK_LOWER_BOUND=1
E3_QT_RANK_UPPER_BOUND=2
E3_GEOMETRIC_RANK_UPPER_BOUND=2
E3_GENERIC_RANK_EXACT=false
E3_GENERATOR_SATURATION_COMPLETE=false
E3_KUMMER_BASELINE=PARTIAL_EXACT
STAGE35_CREDIT_CHANGED=false
MAIN_STATE_JSON_CHANGED=false


1. Exact Stage35 E3 model


Put
A=t^2-1,
B=2t,
C=t^2+1,
so A^2+B^2=C^2.


The Stage35 normalized quotient
E3: y^2=x(x-alpha)(x+1),
alpha=((t^2-1)/(t^2+1))^2,
is Q(t)-isomorphic, by X=C^2 x and Y=C^3 y, to


E3poly: Y^2=X(X-A^2)(X+C^2)
       =X^3+B^2 X^2-A^2 C^2 X.


This is exactly the Pythagorean-triple sign pattern y^2=x(x-a^2)(x+c^2) treated by the Baghalaghdam–Izadi source, with (a,b,c)=(A,B,C). That source proves positive rank for the corresponding rational Pythagorean-triple family and supplies explicit rational points. It does not source-lock the complete generic Mordell–Weil group, so it is used here only for the exact family match and explicit-point dictionary.


2. Elliptic-surface upper bound


For E3poly,
c4=16(t^4+3)(3t^4+1),
Delta=64(t-1)^4(t+1)^4(t^2+1)^4(t^4+1)^2.


The finite singular fibers are therefore:
- I4 at t=1,-1,i,-i;
- I2 at the four roots of t^4+1=0.


At every listed zero of Delta, c4 is nonzero, so these are multiplicative fibers with the displayed Kodaira types. In the chi=2 Weierstrass model, the transformed discriminant and c4 are nonzero at t=infinity, so infinity is good. The Euler sum is 4*4+4*2=24, hence the associated smooth minimal elliptic surface is K3.


The reducible-fiber root rank is
4*(4-1)+4*(2-1)=16.
By Shioda–Tate,
rho=2+16+rank E3(Qbar(t))=18+rank E3(Qbar(t)).
Since a complex K3 surface has rho<=20,
rank E3(Qbar(t))<=2,
and therefore rank E3(Q(t))<=2.


The Naskręcki elliptic-surface source is used only for the standard Shioda–Tate / K3 framework; the displayed E3 fiber calculation above is an exact Stage35EX derivation.


3. Explicit non-torsion direction


The exact points inherited from the Pythagorean family include


P1=(A^2 C^2/B^2, A^3 C^3/B^3),
P2=(-B^2, ABC),
P3=(AC, ABC),
P4=(-AC, ABC).


Direct group-law simplification on E3poly gives


P1=-2 P3,
P4=P3+(0,0),
P2=P1+(0,0).


Thus these four visible points do not certify four independent generic directions. They collapse to one free direction plus rational 2-torsion.


At t=2 the specialization is
E3,2: Y^2=X(X-9)(X+25).
P1 specializes to (225/16,3375/64). On this integral monic cubic, the Nagell–Lutz criterion used in the Pythagorean-family source forces a rational torsion point to have integral coordinates. Hence this specialized P1 is non-torsion. Therefore generic P1, and thus P3, have infinite order.


Consequently
rank E3(Q(t))>=1.


Combined with the elliptic-surface bound:
1 <= rank E3(Q(t)) <= 2.


4. Exact generic torsion


The t=2 fiber is good. It already contains the full rational 2-torsion
(0,0), (9,0), (-25,0).


Direct point counts at good primes give
#E3,2(F_7)=12,
#E3,2(F_11)=16.
Therefore E3,2(Q)_tors has order dividing gcd(12,16)=4, while the visible 2-torsion already has order 4. Hence
E3,2(Q)_tors = (Z/2Z)^2.


A torsion section of the good Q(t)-family specializes injectively at t=2, so
E3(Q(t))_tors = (Z/2Z)^2.


5. 2-Kummer baseline


For the full-2-torsion model
Y^2=X(X-A^2)(X+C^2),
use the ordinary Kummer squareclass triple
delta(P)=([X],[X-A^2],[X+C^2])
away from the root cases, with product 1 in Q(t)^*/Q(t)^{*2}.


For P1:
X=A^2 C^2/B^2,
X-A^2=A^4/B^2,
X+C^2=C^4/B^2,
so
delta(P1)=(1,1,1).
This is consistent with P1=-2P3.


For P3=(AC,ABC):
X=AC,
X-A^2=A(C-A)=2A,
X+C^2=C(A+C)=2t^2 C,
hence
delta(P3)=([AC],[2A],[2C]).


This is a nontrivial generic mod-2 free-direction signature. It is the first source-locked Kummer datum for a selected Stage35 quotient beyond the previously known rational 2-torsion.


6. Routing consequence


This batch does not complete the generic Mordell–Weil baseline. What is now certified for E3 is:


- exact torsion (Z/2Z)^2;
- at least one non-torsion generic section;
- geometric and rational generic rank upper bound 2;
- all four explicit Pythagorean-family points above lie in <P3,E3[2]>;
- the exact Kummer class of P3.


The remaining E3 baseline gate is sharply reduced to:


E3_RANK1_VS_RANK2_AND_SATURATION_PREFLIGHT


Required next result:
either
(a) prove rank E3(Q(t))=1 and certify saturation of <P3,E3[2]>,
or
(b) exhibit and certify a second independent generic section and then saturate the rank-2 subgroup.


Natural exact routes are a function-field 2-descent, a Picard-number bound rho<=19 for this K3 fibration, or a certified injective specialization to a rank-1 rational fiber. A bounded fiber rank computation alone is not enough without the injectivity certificate.


Even a complete E3 generic MW classification will not by itself close the Stage35 specialization-new-point wall. The Stage35 dichotomy remains unchanged: one must either force a physical specialized point outside the specialized generic subgroup in at least one quotient, or classify compatible horizontal branches as boundary/degenerate.


No Stage35, R29, J12, E1, endpoint, or Perfect Cuboid credit is promoted.


Sources
Baghalaghdam–Izadi source
Naskręcki elliptic-surface sourc


7. E3 exact generic rank-one and saturation closure


STATUS=PROVISIONAL_EXACT_E3_GENERIC_MW_CLOSURE_HOSTILE_AUDIT_REQUIRED
FORMAL_AUTHORITY=V74_GOAL4AK
GITHUB_ACCESSED=false
E3_QT_RANK_EXACT=1
E3_GENERATOR_SATURATION_COMPLETE=true
E3_MW_GROUP_CANDIDATE=E3[2]_DIRECT_SUM_Z_P3
STAGE35_CREDIT_CHANGED=false
MAIN_STATE_JSON_CHANGED=false


7.1 Exact mod-3 function-field L-polynomial


Reduce the integral K3 fibration


Y^2 = X(X-A^2)(X+C^2),
A=t^2-1, B=2t, C=t^2+1,


modulo 3.


The discriminant divisor remains squarefree at the level of distinct bad places:


Delta mod 3 =
(t-1)^4 (t+1)^4 (t^2+1)^4 (t^4+1)^2.


At every finite bad place c4 is nonzero. The Kodaira packet therefore remains
I4 at t=+1,-1 and the two geometric roots of t^2+1,
and I2 at the four geometric roots of t^4+1.
After the K3 scaling at infinity,


X=s^(-4) X_inf,
Y=s^(-6) Y_inf,


the infinity fiber is


Y_inf^2 = X_inf^3 + 4 s^2 X_inf^2 - (1-s^4)^2 X_inf,


hence at s=0 in characteristic 3 it is the smooth fiber


Y_inf^2 = X_inf^3 - X_inf.


Thus the mod-3 elliptic surface has the same eight geometric multiplicative bad fibers, conductor degree 8, and base genus 0. Its elliptic L-polynomial has degree


deg L = 8 - 4 = 4.


An exact finite-field replay was made over F_(3^n), n=1,2,3,4. One may use


F_9  = F_3[z]/(z^2+1),
F_27 = F_3[z]/(z^3-z+1),
F_81 = F_3[z]/(z^4+z^2+z+1).


For every t in P^1(F_(3^n)), including the bad fibers with their usual multiplicative local trace, direct point counting gives


S_1 = sum_t a_t = 2,
S_2 = sum_t a_t = -4,
S_3 = sum_t a_t = -46,
S_4 = sum_t a_t = -196.


Writing


L_3(T)=prod_i (1-gamma_i T)


and using


sum_i gamma_i^n = -S_n,


Newton identities give exactly


L_3(T)
= 1 + 2 T - 18 T^3 - 81 T^4
= (1-3T)(1+3T)(1+2T+9T^2).


Therefore


ord_(T=1/3) L_3(T)=1.


At this good reduction prime, divisor classes of Q(t)-sections specialize into the Frobenius-fixed Neron-Severi/Mordell-Weil quotient. The standard cohomological rank upper bound therefore gives


rank E3(Q(t)) <= 1.


The previously certified non-torsion section


P3=(AC,ABC)


gives the reverse inequality. Hence


rank E3(Q(t)) = 1.


This is an exact arithmetic generic-rank result, not a bounded-fiber inference.


7.2 Exact Shioda height of P3


The K3 surface has chi(O)=2.


At infinity, after the same K3 scaling,


P3 -> (X_inf,Y_inf)=(1,0),


so P3 does not meet the zero section and


P3.O=0.


At each of the four I4 fibers, P3 passes through the nodal point. In local node coordinates the I4 singularity has the form


u v = unit * pi^4,


and P3 has branch valuations {1,3}. Hence it meets component Theta_1 or Theta_3 and contributes


contr_v(P3)=1*(4-1)/4=3/4.


At each I2 fiber t^4+1=0, X(P3)=AC is not the coalesced root, so P3 meets the identity component and contributes 0.


Shioda's height formula therefore gives


<P3,P3>
= 2 chi(O) + 2(P3.O) - sum_v contr_v(P3)
= 4 - 4*(3/4)
= 1.


For every section Q on this I4/I2 K3 fibration,


<Q,Q> is in (1/4) Z_(>0)


because the intersection term is integral and all local correction denominators divide 4.


7.3 Saturation of the visible rank-one subgroup


Since rank E3(Q(t))=1, write a hypothetical divisibility relation as


P3 = n Q + T,


with T torsion and n>=1.


The height identity gives


1 = n^2 <Q,Q>,


with <Q,Q> in (1/4) Z_(>0).


Thus n>=3 is impossible, and the only possible proper index is n=2.


Use the full-2-torsion Kummer map for


Y^2=X(X-A^2)(X+C^2).


The previously certified class is


delta(P3)=([AC],[2A],[2C]).


The first Kummer coordinates of the four torsion cosets are only


[1] or [-1]:


delta(O) first = [1],
delta((0,0)) first = [-1],
delta((A^2,0)) first = [1],
delta((-C^2,0)) first = [-1].


But


[AC]=[t^4-1]


is neither [1] nor [-1] in Q(t)^*/Q(t)^{*2}, since it has simple zeros at t=1,-1 and at the two roots of t^2+1.


Therefore delta(P3) is not the Kummer class of any torsion point. If P3=2Q+T, then delta(P3)=delta(T), a contradiction.


Hence P3 is primitive modulo torsion. Together with the already certified torsion group,


E3(Q(t)) = (Z/2Z)^2 direct-sum Z*P3.


Equivalently,


E3_QT_TORSION=(Z/2Z)^2,
E3_QT_RANK_EXACT=1,
E3_GENERATOR=P3,
E3_GENERATOR_SATURATION_COMPLETE=true.


7.4 Independent injective-specialization backup


The Gusic-Tadic full-2-torsion specialization criterion also gives a clean independent checkpoint at t0=4.


For roots


e1=0,
e2=A^2,
e3=-C^2,


the relevant pair-products have nonconstant squarefree factors among


t-1,
t+1,
t^2+1,
t^4+1,


and, where present, the constant factor 2.


At t=4 these evaluate to


3, 5, 17, 257,


with the extra constant prime 2. Every nonempty squarefree product is therefore nonsquare in Q. Thus the criterion certifies injectivity of


E3(Q(t)) -> E3,t=4(Q).


The specialized curve is


Y^2=X(X-225)(X+289),


and P3 specializes to


(255,2040).


No claim about the full specialized rank is needed for the generic rank-one proof above.


7.5 Routing consequence


The previous gate


E3_RANK1_VS_RANK2_AND_SATURATION_PREFLIGHT


is closed at the Stage35EX provisional-research level.


The next active theorem-development task is not another generic-rank search. It is


E3_PHYSICAL_LIFT_VS_GENERIC_SUBGROUP_PREFLIGHT.


FIRST_SUBTASK:
derive/source-lock the exact Stage35 genus-5 -> E3 quotient map on physical coordinates, identify the additional lift/squareclass condition carried by a physical point, and compare that condition against the complete generic subgroup


(Z/2Z)^2 direct-sum Z*P3.


Required downstream dichotomy remains:


A. prove a physical specialized point must force a specialization-new MW/Kummer class in at least one relevant quotient, with a uniform obstruction to that growth; or


B. prove every physical quotient image comes from the specialized generic subgroup and classify every compatible horizontal lift as boundary or receiver-degenerate.


Nothing in this section proves T35-R3-PHYS-EMPTY by itself.


7.6 Credit firewall


Still false / not promoted:


T35_R3_PHYS_EMPTY_PROVED=false
STAGE35_MAIN_UNIFORM_ARITHMETIC_THEOREM_PROVED=false
RECEIVER_MATCHED_REPLACEMENT_THEOREM_PROVED=false
E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false


Hostile audit/source-lock review is required before any formal promotion outside Stage35EX.
e