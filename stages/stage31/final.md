# Stage31 final — self-contained closure of the Paper-E prime Sophie--Germain receiver

```text
STAGE=Stage31
STATUS=CLOSED_SELF_CONTAINED_CLOSEOUT
ORIGINAL_STAGE_AUDIT=PASS_STAGE31_CLOSED_DIRECT_QUARTIC_CERTIFICATION
SELF_CONTAINED_CLOSEOUT_CHECK=PASS
NEW_HOSTILE_AUDIT_OF_THIS_FILE=NOT_RUN
SOURCE_RECEIVER=R29-EXT-CHANG-E
SOURCE_KERNEL=K16-C2-EXT-E-INTEGRAL-CERTIFICATION
PARENT_ROUTE=J12-PARAMETRIC
RECEIVER_STATUS=CLOSED
KERNEL_STATUS=CLOSED
PARENT_ROUTE_STATUS=AMBER
PERFECT_CUBOID_CONCLUSION=NONE
```

This file is the permanent mathematical closeout surface for Stage31. The proof below is written so that the Stage31 theorem, the prime-family reduction, the complete integral-point classification, all surviving parameter cases, and the final exclusion can be followed without any other repository file. Repository paths, hashes, CAS run IDs, and audit records are placed only in the provenance section.

## 1. Exact theorem and quantified population

Let `p,q` be positive odd coprime integers with

\[
 p<q,
\]

and assume that `p` is prime. Consider the Case-B family

\[
 a=4pq,\qquad
 b=q^2-4p^2,\qquad
 c=2(q^2-p^2).
\]

Signs of the displayed algebraic edge expressions do not affect the square conditions; the physical edge length is the absolute value where needed. Under the stated odd/coprime/order hypotheses, the degenerate equal-parameter case `q=p` and the zero-edge case `q=2p` are excluded.

Stage31 proves the following receiver theorem.

> **Stage31 theorem.** No non-degenerate member of this prime-parameter Case-B Sophie--Germain family is a perfect cuboid.

Equivalently: after imposing the space-diagonal condition and then the Sophie--Germain factor split forced by it, the complete prime-parameter population reduces to a single integral genus-one quartic. That quartic has exactly six affine integral points,

\[
\boxed{
(Y,Z)\in\{(-1,\pm1),(1,\pm1),(11,\pm37)\}.
}
\]

The points with `|Y|=1` do not give a prime parameter. The only non-degenerate prime reconstruction is

\[
(p,q)=(11,71),
\]

and its remaining face diagonal is not integral. Hence the receiver is empty.

The theorem is **only** about this prime-parameter Case-B subfamily. Composite `p`, other parametrizations, the full parent route `J12-PARAMETRIC`, and the global perfect-cuboid problem are outside the conclusion.

## 2. Exact Case-B square identities

The first two face diagonals are automatically integral in this family because

\[
\begin{aligned}
a^2+b^2
&=16p^2q^2+(q^2-4p^2)^2\\
&=(q^2+4p^2)^2,
\end{aligned}
\]

and

\[
\begin{aligned}
a^2+c^2
&=16p^2q^2+4(q^2-p^2)^2\\
&=\bigl(2(q^2+p^2)\bigr)^2.
\end{aligned}
\]

The space-diagonal square is

\[
\begin{aligned}
a^2+b^2+c^2
&=5q^4+20p^4\\
&=5(q^4+4p^4).
\end{aligned}
\]

Therefore the space diagonal is integral exactly when

\[
q^4+4p^4=5r^2
\]

for some integer `r`: if `5(q^4+4p^4)=w^2`, then `5|w`, say `w=5r`, and division by `5` gives the displayed equation; the converse is immediate.

Thus a perfect cuboid in this population would have to satisfy

\[
\boxed{q^4+4p^4=5r^2}
\]

and, after that, the only remaining unchecked face is `b^2+c^2`.

## 3. Sophie--Germain split is exhaustive

Use the polynomial identity

\[
q^4+4p^4
=\bigl((q-p)^2+p^2\bigr)
 \bigl((q+p)^2+p^2\bigr).
\]

Set

\[
A=(q-p)^2+p^2,
\qquad
B=(q+p)^2+p^2.
\]

Because `p,q` are odd, both `A` and `B` are odd. If `d=gcd(A,B)`, then

\[
d\mid B-A=4pq.
\]

Since `d` is odd, `d|pq`. But

\[
A\equiv q^2\pmod p,
\]

so no prime divisor of `p` divides `A` because `gcd(p,q)=1`; and

\[
A\equiv 2p^2\pmod q,
\]

so no odd prime divisor of `q` divides `A`. Hence

\[
\boxed{\gcd(A,B)=1}.
\]

Now `AB=5r^2`. Since `A` and `B` are coprime, every prime other than `5` occurs to even exponent in each factor separately, while the prime `5` occurs to odd exponent in exactly one factor. Therefore exactly one of the following two cases holds:

\[
\begin{array}{ll}
\text{Case I:} & A=5\alpha^2,\quad B=\beta^2,\\[2mm]
\text{Case II:} & A=\alpha^2,\quad B=5\beta^2,
\end{array}
\]

for integers `alpha,beta`. These two branches are exhaustive; they are not heuristic alternatives.

## 4. Prime `p` collapses each branch to one quartic

### 4.1 Case II

In Case II,

\[
A=(q-p)^2+p^2=\alpha^2.
\]

Thus `(q-p,p,alpha)` is a primitive Pythagorean triple: `q-p` is even, `p` is odd, and `gcd(q-p,p)=gcd(q,p)=1`. Hence there are coprime integers `m>n>0` of opposite parity with

\[
p=m^2-n^2,
\qquad
q-p=2mn.
\]

Since `p` is prime,

\[
p=(m-n)(m+n)
\]

forces

\[
m-n=1,\qquad m+n=p,
\]

so

\[
m=\frac{p+1}{2},\qquad n=\frac{p-1}{2}.
\]

Therefore

\[
q-p=\frac{p^2-1}{2},
\qquad
\boxed{q=\frac{p^2+2p-1}{2}}.
\]

The constrained factor is now `B=5 beta^2`. Substituting the displayed `q` gives

\[
4B=p^4+8p^3+18p^2-8p+1=20\beta^2.
\]

Thus with

\[
Y=p,\qquad Z=\beta,
\]

we obtain

\[
\boxed{
20Z^2=Y^4+8Y^3+18Y^2-8Y+1.
}
\]

### 4.2 Case I

In Case I,

\[
B=(q+p)^2+p^2=\beta^2.
\]

Now `(q+p,p,beta)` is a primitive Pythagorean triple, so the same prime factorization argument gives

\[
q+p=\frac{p^2-1}{2},
\qquad
\boxed{q=\frac{p^2-2p-1}{2}}.
\]

The constrained factor is `A=5 alpha^2`; substitution gives

\[
4A=p^4-8p^3+18p^2+8p+1=20\alpha^2.
\]

This is the same quartic after the involution `Y -> -Y`: with

\[
Y=-p,\qquad Z=\alpha,
\]

we again obtain

\[
\boxed{
C:\quad 20Z^2=Y^4+8Y^3+18Y^2-8Y+1.
}
\]

Hence every perfect-cuboid candidate in the Stage31 population maps to an affine integral point of `C`, with the exact branch dictionary

\[
\begin{array}{lll}
\text{Case I:} & Y=-p, & q=(p^2-2p-1)/2,\\[1mm]
\text{Case II:} & Y= p, & q=(p^2+2p-1)/2.
\end{array}
\]

This proves the completeness of the algebraic funnel from the infinite prime family to the single integral quartic.

## 5. Direct integral model: the load-bearing completeness transfer

Stage31 does **not** assume that a rational quartic-to-elliptic birational map preserves integrality. Instead it moves the integral-point problem to a scaled quartic by an exact integer equivalence.

Multiply the equation of `C` by `5` and set

\[
U=10Z.
\]

Then

\[
\boxed{
Q:\quad U^2=5Y^4+40Y^3+90Y^2-40Y+5.
}
\]

For integral coordinates there is an exact equivalence

\[
\boxed{
C(\mathbf Z)
\longleftrightarrow
\{(Y,U)\in Q(\mathbf Z):10\mid U\}
}
\]

given by

\[
(Y,Z)\mapsto(Y,10Z),
\qquad
(Y,U)\mapsto(Y,U/10).
\]

There is no denominator, local condition, or exceptional point hidden in this transfer. Thus a complete enumeration of `Q(Z)`, followed by the exact divisibility filter `10|U`, is a complete enumeration of `C(Z)`.

## 6. Complete integral-point enumeration

The proof-capable computation used Magma V2.29-9 and the documented genus-one quartic routine

```text
IntegralQuarticPoints(
  [5,40,90,-40,5],
  [1,10]
)
```

on the curve `Q`, with the rational integral base point `(Y,U)=(1,10)`. The Magma Handbook entry for `IntegralQuarticPoints(Q,P)` specifies that the routine determines **all** integral points on the quartic, rather than searching only up to a user-supplied height bound. The Stage31 proof therefore uses the routine's completeness contract, not a bounded point search, a sampled height constant, BSD, GRH, or a database point count.

The routine returned one representative from each `U -> -U` pair:

\[
(-1,10),\qquad (1,-10),\qquad (11,370).
\]

Restoring the hyperelliptic sign gives exactly

\[
Q(\mathbf Z)=
\{
(-1,\pm10),
(1,\pm10),
(11,\pm370)
\}.
\]

Every listed `U` is divisible by `10`. Applying the exact transfer of Section 5 therefore gives the complete Stage31 quartic classification

\[
\boxed{
C(\mathbf Z)=
\{
(-1,\pm1),
(1,\pm1),
(11,\pm37)
\}.
}
\]

This six-point statement is the load-bearing finite theorem used in the family closure.

## 7. Elliptic model and Mordell--Weil cross-check

The genus-one quartic `C` is birational over `Q` to

\[
\boxed{
E:\quad y^2=x^3-275x+1750.
}
\]

This elliptic model is useful as an independent structural cross-check, but **is not used to infer the completeness of `C(Z)`**.

For `Y != 1`, the exact forward map is

\[
x=
\frac{10(2Y^2+3Y+5Z)}{(Y-1)^2},
\]

\[
y=
\frac{25(3Y^3+15Y^2+14YZ+3Y+6Z-1)}{(Y-1)^3}.
\]

One derivation is obtained by setting

\[
t=Y-1,\qquad W=20Z,
\]

\[
u=\frac{W+20+28t}{t^2},
\]

which transforms the quartic identity into

\[
(u^2-20)t^2-(56u+240)t-(40u+176)=0.
\]

Define

\[
v=2(u^2-20)t-(56u+240).
\]

Then

\[
v^2=160(u+4)(u^2+20u+68).
\]

With

\[
U_0=u+8,\qquad x=\frac{5U_0}{2},\qquad y=\frac{5v}{16},
\]

this becomes exactly `E`.

Conversely, for a finite rational point `(x,y)` on `E`, put

\[
u=\frac{2x}{5}-8,\qquad v=\frac{16y}{5},
\]

\[
t=\frac{v+56u+240}{2(u^2-20)},
\qquad
Y=1+t,
\]

\[
W=ut^2-20-28t,
\qquad
Z=\frac{W}{20}.
\]

The inverse denominator cannot vanish for rational `u`, because `u^2=20` has no rational solution. The affine source points excluded by the forward denominator are classified separately:

\[
C(1,1)\mapsto O_E,
\qquad
C(1,-1)\mapsto(9,2).
\]

Projective points at infinity are not part of the integral affine population produced from finite integer parameters `p,q,alpha,beta`, so they cannot create an omitted Stage31 candidate.

Magma's full Mordell--Weil computation gives

\[
E(\mathbf Q)\cong \mathbf Z\oplus\mathbf Z/2\mathbf Z,
\]

with torsion point

\[
T=(10,0)
\]

and free generator `(9,2)`. The generator used in the external Paper-E source,

\[
(-15,50),
\]

represents the same free rank-one lattice modulo torsion, with

\[
(-15,50)=-(9,2)-(10,0).
\]

The affine integral points on `E` are the seven signed points with

\[
x\in\{-15,9,10,46\}:
\]

\[
(-15,\pm50),\quad(9,\pm2),\quad(10,0),\quad(46,\pm294).
\]

These facts independently check the genus-one identification and full-group structure. They do not replace the direct quartic completeness proof in Section 6.

## 8. Exhaustive pullback to prime parameters

Apply the branch dictionary of Section 4 to the complete quartic list.

### 8.1 Case I

Case I requires

\[
Y=-p<0.
\]

The only negative integral `Y` in `C(Z)` is

\[
Y=-1.
\]

It would give `p=1`, which is not prime. Therefore

\[
\boxed{\text{Case I has no prime-parameter survivor.}}
\]

### 8.2 Case II

Case II requires

\[
Y=p>0.
\]

The positive `Y` values in `C(Z)` are `1` and `11`. The value `1` is not prime. Thus the only prime parameter is

\[
p=11.
\]

The exact Case-II formula gives

\[
q=\frac{11^2+2\cdot11-1}{2}=71.
\]

It satisfies all source hypotheses:

\[
p,q\text{ odd},\qquad \gcd(11,71)=1,\qquad 11<71.
\]

The two quartic signs `Z=\pm37` encode the same `(p,q)` and do not create distinct cuboid parameters.

Hence the complete non-degenerate prime reconstruction before the last face test is exactly

\[
\boxed{(p,q)=(11,71)}.
\]

## 9. Exact reconstruction and terminal face test

For `(p,q)=(11,71)`, the Case-B edges are

\[
\begin{aligned}
a&=4pq=3124,\\
b&=q^2-4p^2=4557,\\
c&=2(q^2-p^2)=9840.
\end{aligned}
\]

The two automatic face squares are

\[
a^2+b^2=30\,525\,625=5525^2,
\]

\[
a^2+c^2=106\,584\,976=10324^2.
\]

The space diagonal is also integral:

\[
a^2+b^2+c^2
=127\,351\,225
=11285^2.
\]

The remaining face gives

\[
b^2+c^2=117\,591\,849.
\]

But

\[
10843^2=117\,570\,649
<117\,591\,849
<117\,592\,336=10844^2.
\]

Therefore `b^2+c^2` is not a square. The unique non-degenerate prime-family survivor before the terminal face test is not a perfect cuboid.

Combining Sections 3--9 proves

\[
\boxed{
\text{the Stage31 prime-parameter Sophie--Germain Case-B family contains no perfect cuboid.}
}
\]

## 10. Exceptional and boundary cases

All cases capable of affecting the quantified population are explicit:

1. `p=2` is outside the family because the Stage31 source population assumes odd `p,q`.
2. `Y=-1` and `Y=1` reconstruct `p=1`, so all four points `(-1,±1),(1,±1)` are rejected by the prime hypothesis.
3. The signs `Z -> -Z` change only the square-root choice in the quartic and do not change `p,q` or the reconstructed edges.
4. `q=p` would make `c=0` and is excluded by `p<q`.
5. `q=2p` would make `b=0`; it is incompatible with both `p,q` being odd.
6. The affine birational formulas have denominator `Y-1`; both integral points with `Y=1` are classified explicitly, and neither belongs to the prime population.
7. The inverse elliptic denominator `u^2-20` has no rational zero.
8. Projective points at infinity on the genus-one compactification do not arise from finite integer prime parameters and are not elements of `C(Z)`.
9. No composite-`p` point is promoted to the theorem. Stage31 does not classify the composite parameter family.

Thus there is no unclassified pole, denominator-zero case, sign orbit, degenerate source parameter, or compactification boundary capable of creating a missing Stage31 prime candidate.

## 11. Final implication and firewalls

The load-bearing chain is

\[
\begin{aligned}
&\text{prime Case-B perfect-cuboid candidate}\\
&\Rightarrow q^4+4p^4=5r^2\\
&\Rightarrow \text{exactly one of Sophie--Germain Cases I/II}\\
&\Rightarrow (Y,Z)\in C(\mathbf Z),\quad Y=\pm p\\
&\Rightarrow (Y,Z)\in\{(-1,\pm1),(1,\pm1),(11,\pm37)\}\\
&\Rightarrow \text{only prime reconstruction }(p,q)=(11,71)\\
&\Rightarrow b^2+c^2\text{ is not a square},
\end{aligned}
\]

which is a contradiction.

Therefore

```text
PRIME_SOPHIE_GERMAIN_SUBFAMILY_EXCLUSION=VERIFIED
R29_EXT_CHANG_E=DISCHARGED_DIRECT_QUARTIC_CERTIFICATION
K16_C2_EXT_E_INTEGRAL_CERTIFICATION=CLOSED
```

The following stronger claims are **not** proved:

```text
C_TO_E_INTEGRALITY_TRANSFER_PROVED=false
COMPOSITE_P_FAMILY_CLOSED=false
J12_PARAMETRIC_CLOSED=false
ROUTE_COLOR_CHANGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

The Stage31 receiver is closed by the direct scaled-quartic completeness route, not by asserting that the rational birational map `C <-> E` preserves integrality.

## 12. External theorem/software dependency

The sole external completeness dependency used in the load-bearing finite classification is the documented completeness semantics of Magma V2.29-9 `IntegralQuarticPoints(Q,P)` for genus-one quartics with a supplied rational point. Stage31 used the University of Sydney Magma implementation and pinned the handbook locator:

```text
Magma Handbook: IntegralQuarticPoints
https://magma.maths.usyd.edu.au/magma/handbook/text/1567
```

The Stage31-specific hypotheses supplied to that routine are explicit in Section 6: the exact quartic coefficients and the rational point `(1,10)`. No heuristic height cutoff or conjectural analytic assumption enters the completeness claim.

## 13. Reproducibility provenance

The mathematical proof above does not require these files to be understood; they record how the Stage31 computation and audit were reproduced.

### Frozen external Paper-E snapshot

```text
repository=weiqi-kids/perfect-cuboid-problem
commit=bd3018b896c8ac15b56cadc382af1477dca9e97a
paper-e/paper.tex blob=1ff42f5a657ab9edafcfd6060f015a19e4322a83
paper-e/scripts/01_identity_and_reduction.gp blob=a117cf78176d6818d6dca99388e827bcc1e2269e
paper-e/scripts/01b_case_I_recheck.gp blob=9db55907129920b96c7175419145a703271d0e5b
paper-e/scripts/02_curve_rank_label.gp blob=b0c30169a920ef7ab6ba7040875ab8d99de5aa18
paper-e/scripts/03_integral_points.gp blob=80a113d42641e474de01c1cbe1b15c06a9744892
paper-e/scripts/04_height_completeness.gp blob=ba372d9c0a4f6fad2884ad192f5f64f85244396a
```

### Stage31 source and certificate records

```text
stages/stage31/source-lock.md
  blob=ae08801fa9629c8b9e5b84003f5050d24fcf72b7

stages/stage31/31-01/result.md
  blob=5c87c63da39535962dc063ec568260279ee0ea3c

stages/stage31/31-01/birational-map.json
  blob=973f61023b7b0b5d322168331b3ecc68a281ca25

stages/stage31/31-01/integral-points-certificate.json
  blob=69eb32c5d93a9cee569e7ccd3767c4ac983421cc

stages/stage31/31-01/reconstruction-ledger.json
  blob=0b829208f4d2b9a67538adc4617af38addbeb00e

stages/stage31/31-01/verify_stage31.py
  blob=92b956d570367d145d87692ae25c0da5da312233

stages/stage31/31-06/audit.md
  blob=149c9025752a8ee39f6a57f45d26f58385edf412

stages/stage31/31-06/audit-state.json
  blob=25fb3c509926da9dfdaef6ca38c5731369073c3f

stages/stage31/controller.json
  blob=f2fe655f623f519705f8acd04d9e0b6486af2b35
```

### Complete-quartic execution

```text
software=Magma V2.29-9
workflow_run=32607148918
workflow_job=97113828969
artifact=9484415535
artifact_sha256=32c6f9ab32b60faa29b7a8cf7cfc3133115ea19ece422facf51ff255089f8a17
runtime_error=false
```

The original final hostile audit closed Stage31 under verdict

```text
PASS_STAGE31_CLOSED_DIRECT_QUARTIC_CERTIFICATION
```

and the merged Stage31 closure PR was `#1338` (`merge_commit=e1e44bfe04b3194c6d1732c9c099642b49741444`).

## 14. Self-contained closeout gate

Destructive-check result:

```text
KEEP_ONLY=stages/stage31/final.md
OTHER_REPOSITORY_FILES=HIDDEN
EXPLICIT_EXTERNAL_DEPENDENCY=Magma IntegralQuarticPoints handbook semantics
EXACT_THEOREM_IDENTIFIABLE=true
POPULATION_COMPLETE=true
ALGEBRAIC_REDUCTION_COMPLETE=true
FINITE_FUNNEL_COMPLETE=true
TERMINAL_REPRESENTATIVES_COMPLETE=true
EXCEPTIONAL_CASES_CLASSIFIED=true
FINAL_IMPLICATION_COMPLETE=true
FIREWALLS_EXPLICIT=true
SELF_CONTAINED=PASS
```
