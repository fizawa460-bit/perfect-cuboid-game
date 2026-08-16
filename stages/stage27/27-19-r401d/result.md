# Stage27-19-r401d — R501/R502 calibration inside the natural tau-fibration

```text
TASK_ID=Stage27-19-r401d
OWNER_STAGE=Stage27
PARENT_ROUTE=Stage27-19-r401c
TRIGGER_CHECKPOINT=40
ROUTE_KIND=LOWER_REENTRY
ROUTE_LABEL=KNOWN_QUARTER_FAMILY_TAU_CALIBRATION
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_LOWER_EXPONENT=1/4
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Purpose

The audited r401a-r401c sequence showed that the natural split-factor `tau`-fibration has no rational section, that its obvious constant-u bisections are either genus one or nonphysical, and that the full affine-linear ansatz `u=a*tau+b` contains no nondegenerate physical genus-zero member.

Before searching blindly at higher nonlinear degree, this route calibrates the fibration against the two already-audited physical quarter-power families R501 and R502. The goal is to answer two exact questions:

1. where do the known physical rational curves sit in `(tau,u)` coordinates?;
2. why do both produce physical height degree eight even though their toric coordinate presentations look different?

No new lower exponent is claimed.

## 2. Universal toric reconstruction

For rational toric coordinates

\[
x=P/Q,\qquad y=R/S,
\]

with nonzero rational homogeneous pairs, the standard two-face toric host is

\[
E_0=4PQRS,
\]
\[
X_0=2RS(P^2-Q^2),
\qquad
Y_0=2PQ(R^2-S^2).
\]

Then

\[
E_0^2+X_0^2=(2RS(P^2+Q^2))^2,
\]
\[
E_0^2+Y_0^2=(2PQ(R^2+S^2))^2.
\]

If `P,Q` have common homogeneous source degree `d_x` and `R,S` degree `d_y`, all three raw edges have homogeneous degree

\[
H_{raw}=2d_x+2d_y.
\]

If a common homogeneous polynomial factor `G` of degree `g` divides `E_0,X_0,Y_0`, removing it gives algebraic physical degree

\[
\boxed{h_{alg}=2d_x+2d_y-g.}
\]

A genuine lower theorem still needs residual arithmetic gcd, multiplicity, canonical, positivity and exactly-two control. The formula is therefore a height preflight, not a theorem for arbitrary rational curves.

## 3. R501 embeds exactly as a degree-eight multisection

Use the audited R501 source parameter `t` and write its raw physical edges as `(A_1,B_1,C_1)`, with shared guaranteed-face edge `C_1`. The two Pythagorean parameters are

\[
\boxed{x_1(t)=\frac{(t-1)(t+3)}{(t-3)(t+1)}},
\]
\[
\boxed{y_1(t)=\frac{t^2+3}{2t}}.
\]

Direct substitution gives

\[
\boxed{
 z_1(t)=
 \frac{t^4+2t^3+2t^2-6t+9}
 {t^4-2t^3+2t^2+6t+9}
}
\]

and

\[
x_1^2y_1^2+1=z_1^2(x_1^2+y_1^2).
\]

The natural split coordinates are

\[
\boxed{
\tau_1(t)=
\frac{8t^2(t^4-2t^2+9)}
{(t-3)^2(t+1)^2(t^2-2t+3)(t^2+2t+3)}
},
\]

\[
\boxed{u_1(t)=
\frac{t^4-2t^3+2t^2+6t+9}
{(t-3)(t+1)(t^2-3)}
}.
\]

The numerator and denominator of `tau_1` are coprime and have degrees `6` and `8`. Hence the map of this rational curve to the `tau`-line has degree

\[
\boxed{8}.
\]

For the homogeneous source pair `t=m/n`, take

\[
P_1=(m-n)(m+3n),\quad Q_1=(m-3n)(m+n),
\]
\[
R_1=m^2+3n^2,\quad S_1=2mn.
\]

All four forms have degree two. The toric reconstruction satisfies exactly

\[
\boxed{(E_0,X_0,Y_0)=2(C_1,A_1,B_1)}.
\]

Thus `d_x=d_y=2`, there is no nonconstant common polynomial factor, and

\[
\boxed{h_{alg}=2(2)+2(2)=8.}
\]

The already-audited bounded residual primitive gcd and bounded family multiplicity then recover the certified R501 scale `Theta(B^(1/4))`.

## 4. R502 also embeds as degree eight, but by a cancellation mechanism

For audited R502, with raw physical edges `(A_2,B_2,C_2)` and shared guaranteed-face edge `C_2`, take

\[
\boxed{x_2(t)=\frac{(t^2-3)(t^2+3)}{8t^2}},
\]
\[
\boxed{y_2(t)=\frac{t^2+3}{2t}},
\]

and

\[
\boxed{z_2(t)=\frac{t^4-2t^2+9}{2t(t^2+3)}}.
\]

Again

\[
x_2^2y_2^2+1=z_2^2(x_2^2+y_2^2).
\]

The split coordinates are

\[
\boxed{
\tau_2(t)=
\frac{(t^4-2t^3+2t^2+6t+9)(t^4+2t^3+2t^2-6t+9)}
{16t^2(t^2-2t+3)(t^2+2t+3)}
},
\]

\[
\boxed{u_2(t)=
\frac{(t+3)(t^2+1)(t^2+3)}
{4t(t-1)(t^2+2t+3)}
}.
\]

The numerator and denominator of `tau_2` are coprime and have degrees `8` and `6`, so this rational curve is also a degree-eight multisection of the `tau`-line.

Homogeneously choose

\[
P_2=m^4-9n^4,\quad Q_2=8m^2n^2,
\]
\[
R_2=m^2+3n^2,\quad S_2=2mn.
\]

Here `d_x=4`, `d_y=2`, so the naive toric degree is `12`. But direct factorization gives the exact common factor

\[
\boxed{G_2=4mn(m^2+3n^2)}
\]

of homogeneous degree four and

\[
\boxed{(E_0,X_0,Y_0)=G_2(C_2,A_2,B_2)}.
\]

Therefore

\[
\boxed{h_{alg}=2(4)+2(2)-4=8.}
\]

After this structural cancellation, the already-audited residual primitive gcd is uniformly bounded by `2592`, so R502 is again exactly on the quarter-power scale.

## 5. What the calibration changes

The known physical quarter-power families are **not** low-degree sections or affine-linear bisections of the natural `tau`-fibration. They are rational curves whose projection to the `tau`-line has degree eight.

More importantly, the source of the physical exponent can now be read directly in the master receiver:

- R501: degree-eight physical height comes from `d_x=d_y=2` with no polynomial cancellation;
- R502: a nominal degree-twelve toric composition is reduced to degree eight by a degree-four common factor.

For any new one-rational-parameter curve `t` with quadratically many reduced parameters of source height `T`, the calibrated algebraic route to a lower exponent above one quarter is therefore

\[
\boxed{h_{alg}<8}
\]

provided residual arithmetic gcd, parameter multiplicity and all Stage19 physical filters are controlled without fixed-power loss. Equivalently, in the toric degree ledger,

\[
\boxed{2d_x+2d_y-g<8.}
\]

A second possibility remains the parent r401 thick-family gate: keep height degree eight but produce an effective parameter-count exponent strictly above two.

This criterion does **not** prove that no higher-degree rational curve can enjoy additional arithmetic cancellation, and it does not classify all nonlinear multisections.

## 6. Lower-lane stopping boundary

The lower reentry has now established a coherent internal boundary:

1. R501/R502 are genuinely saturated at `1/4`;
2. the master space receiver and natural genus-one fibration are exact;
3. the degree-one section route is closed;
4. constant-u and all affine-linear moving-u genus-zero shortcuts are closed on the physical chart;
5. the known physical quarter-power curves are explicitly recovered as degree-eight multisections and their physical degree-eight height mechanisms are explained.

The next lower breakthrough must therefore supply a genuinely new nonlinear rational curve with effective physical height below eight, a provable stronger cancellation, or a polynomially thicker moving family. Continuing a blind low-degree ansatz search without such a structural lead is not prioritized here.

This is a **bounded repository-state stopping rule**, not an impossibility theorem. It is reasonable after fresh audit to return effort to the Stage27 upper side while retaining this lower reopen contract.

```text
R501_TAU_EMBEDDING_PROVED=true
R502_TAU_EMBEDDING_PROVED=true
R501_TAU_PROJECTION_DEGREE=8
R502_TAU_PROJECTION_DEGREE=8
R501_TORIC_DEGREE_LEDGER=dx2_dy2_g0_h8
R502_TORIC_DEGREE_LEDGER=dx4_dy2_g4_h8
R502_DEGREE12_TO_8_POLYNOMIAL_CANCELLATION_PROVED=true
KNOWN_QUARTER_FAMILIES_CALIBRATED_IN_MASTER_FIBRATION=true
ONE_PARAMETER_ALGEBRAIC_PROGRESS_GATE=2dx+2dy-g<8
LOWER_EXPONENT_ABOVE_ONE_QUARTER_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
LOWER_BOUNDED_REENTRY_STOP_CANDIDATE=true
REOPEN_LOWER_ON=NEW_H_LT_8_RATIONAL_CURVE_OR_STRONGER_CANCELLATION_OR_POLYNOMIALLY_THICKER_FAMILY
PREFERRED_POST_AUDIT_LANE=UPPER_REENTRY
NEXT_UPPER_ROUTE=27-40af
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=Stage27-19-r401-audit
```
