# Stage25-60 R504 rank-two physical-coset mod-2 repair

STATUS=REPAIR_SUBMITTED_FOR_FRESH_AUDIT
ROUTE=R504
CHECKPOINT=60
PR=995

This is the narrow repair requested by the hostile audit of the rank-two height lattice. The Rosati height form accepted by that audit is not reopened. The only purpose here is to prove the physical 2-cover membership rule inside the known sublattice `<P,R>`.

## 1. Full rational 2-torsion Kummer map

Work over `K=Q(u)` on

\[
E_H:\quad y^2=x(x-2H)(x+2H),\qquad H=N^4+M^4.
\]

For a non-2-torsion point `Q=(x,y)`, use the standard full-2-torsion Kummer map

\[
\delta(Q)=([x],[x-2H],[x+2H])
\in (K^*/K^{*2})^3,
\]

with product equal to `[y^2]=1`. Each coordinate function has divisor twice a rational 2-torsion divisor minus twice the origin, so evaluation modulo squares is a group homomorphism. Since all three nonzero 2-torsion points are K-rational, the common kernel is `2E_H(K)`. Thus

\[
\delta(Q_1+Q_2)=\delta(Q_1)\delta(Q_2),\qquad
\delta(Q)=1\iff Q\in2E_H(K).
\]

No saturation assumption on `<P,R>` is used below.

## 2. Explicit Kummer characters of P and R

The inherited section is

\[
P=(-4N^2M^2,\ 4NM(N^4-M^4)).
\]

Direct factorization gives

\[
x(P)=-4(NM)^2,
\]
\[
x(P)-2H=-8\,(u^4+4u^3-2u^2-12u+29)^2,
\]
\[
x(P)+2H=128\,(u+1)^2(u^2+2u-5)^2.
\]

Hence

\[
\boxed{\delta(P)=(-1,-2,2).}
\]

For

\[
R=(4S^2,\ 4S(F^2-G^2)),
\]

direct factorization gives

\[
x(R)=4S^2,
\]
\[
x(R)-2H=128\,(u+1)^2(u^2+2u+7)^2,
\]
\[
x(R)+2H=8\,(u^2+5)^2(u^2+4u+9)^2.
\]

Therefore

\[
\boxed{\delta(R)=(1,2,2).}
\]

The constant squareclasses `-1` and `2` are nontrivial in `Q(u)^*/Q(u)^{*2}`: a rational function whose square is a nonzero constant has no zeros or poles and is therefore a rational constant, while neither `-1` nor `2` is a square in `Q`. Consequently the two displayed Kummer classes are mod-2 independent.

## 3. The physical quartic image has exactly the P Kummer class

The physical receiver is

\[
t^4+1=(k^4+1)z^2,\qquad k=N/M.
\]

Put

\[
w=M^2/z\in K.
\]

Then physicality is exactly

\[
H=w^2(t^4+1),
\]

and the scaled elliptic map has

\[
x=-4w^2t^2.
\]

Therefore

\[
x-2H=-2w^2(t^2+1)^2,
\qquad
x+2H=2w^2(t^2-1)^2.
\]

Every nondegenerate physical quartic point thus satisfies

\[
\boxed{\delta(Q)=(-1,-2,2)=\delta(P).}
\]

The converse is also explicit. Suppose `Q in E_H(K)` has `delta(Q)=delta(P)`. Choose `r,q,s in K` with

\[
x=-4r^2,
\qquad x-2H=-2q^2,
\qquad x+2H=2s^2.
\]

Then

\[
q^2-s^2=4r^2,
\qquad q^2+s^2=2H.
\]

Away from the degenerate divisors, define

\[
t=\frac{q+s}{2r},
\qquad
w=\frac{q-s}{2},
\qquad
z=\frac{M^2}{w}.
\]

Using `(q-s)(q+s)=4r^2`, one gets

\[
t^2=\frac{q+s}{q-s},
\]

and therefore

\[
w^2(t^4+1)=\frac{q^2+s^2}{2}=H.
\]

Hence

\[
t^4+1=(H/M^4)z^2=(k^4+1)z^2,
\]

and also `x=-4w^2t^2`. Thus the physical quartic map has image exactly the Kummer coset

\[
\boxed{\delta^{-1}(\delta(P))=P+2E_H(K).}
\]

This gives the requested direct symbolic physical-lift criterion; no ambient Mordell-Weil 2-saturation theorem is needed.

## 4. Exact parity rule inside <P,R>

For

\[
Q_{a,b}=aP+bR,
\]

the homomorphism property gives

\[
\delta(Q_{a,b})=\delta(P)^a\delta(R)^b.
\]

Physicality is equivalent to `delta(Q_{a,b})=delta(P)`. The first coordinate gives

\[
(-1)^a=-1,
\]

so `a` is odd. With `a` odd, the second coordinate gives

\[
(-2)^a2^b=-2,
\]

so `2^b` is a square, hence `b` is even. Conversely, if `a=1+2m` and `b=2n`, then

\[
Q_{a,b}=P+2(mP+nR)\in P+2E_H(K),
\]

so the explicit converse above produces a physical quartic lift.

Therefore

\[
\boxed{
Q_{a,b}\text{ is physical}\iff a\equiv1\pmod2,\ b\equiv0\pmod2.
}
\]

## 5. Reuse of the hostile-audited height theorem

The hostile audit already accepted

\[
\deg_u(x(aP+bR)/H)=8(a^2+b^2)
\]

and, conditional on physicality,

\[
\deg_u t=2(a^2+b^2),
\qquad
L(a,b)=4+4(a^2+b^2).
\]

The repaired parity theorem now makes those formulas unconditional on the physical subcoset. The norm-1 physical classes are only `(+/-P)` and are the previously audited degenerate classes. The next possible norm for `a` odd and `b` even is `5`, attained by `(+/-1,+/-2)`. The previously hostile-audited `P+2R` lift attains this norm.

Hence the fixed-class conclusion is repaired:

\[
\boxed{\min_{\text{nondegenerate physical }(a,b)}(a^2+b^2)=5,}
\]

\[
\boxed{\min\deg t=10,\qquad \min L=24,}
\]

and the best fixed-class growth inside the known rank-two lattice is the already audited

\[
\boxed{\Theta(B^{1/12}).}
\]

## 6. Scope firewall

This repair proves only the mod-2 physical coset and therefore completes the fixed-class height classification inside the known `<P,R>` sublattice. It does not prove that the full pulled-back Mordell-Weil group has rank exactly two, does not uniformly sum classes with `(a,b)` growing with `B`, and does not close the full-split Prym / `E0`-isogeny residual.

```text
R504_KUMMER_MAP=([x],[x-2H],[x+2H])
R504_KUMMER_KERNEL=2E_H(Q(u))
R504_KUMMER_CLASS_P=(-1,-2,2)
R504_KUMMER_CLASS_R=(1,2,2)
R504_KUMMER_P_R_MOD2_INDEPENDENT=true
R504_PHYSICAL_IMAGE_KUMMER_CLASS=(-1,-2,2)
R504_PHYSICAL_IMAGE=P+2E_H(Q(u))
R504_PHYSICAL_COSET_A_ODD_B_EVEN_PROVED=true
R504_RANK_TWO_2DESCENT_CHARACTER_CERTIFICATE=true
R504_RANK_TWO_MOD2_SATURATION_CERTIFICATE=NOT_REQUIRED
R504_MIN_NONDEGENERATE_NORM=5
R504_BEST_FIXED_CLASS_GROWTH=Theta(B^(1/12))
R504_RANK_TWO_FIXED_CLASS_HEIGHT_CLASSIFICATION_REPAIRED=true
R504_RANK_TWO_GROWING_LATTICE_UNIFORM_AGGREGATION_PROVED=false
R504_FULL_SPLIT_PRYM_ISOGENY_RESIDUAL=OPEN
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
AUDIT_REQUIRED_NOW=true
```
