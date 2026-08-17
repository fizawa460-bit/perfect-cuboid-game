# Stage27-20-r301j — squareclass support/fiber gate at the half-power wall

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301i
SOURCE_STAGE=Stage20

## 1. The squareclass index costs no fixed positive exponent after q1 is fixed

Let `Q(B)` denote the set of first torus coordinates `x=q1` actually occupied by Stage27 survivors under `R<=B`.  For each `x`, let `D_x(B)` be the set of common squareclasses `delta` occurring above that coordinate.

R301h gives, uniformly for physical `x` under the cutoff,

\[
\boxed{|D_x(B)|=B^{o(1)}.}
\]

For an occupied pair `(x,delta)`, write

\[
w_{x,\delta}(B)
:=\#\{\text{Stage27 survivors in that fixed fiber}\}.
\]

Then exactly

\[
N_2(B)=\sum_{x\in Q(B)}\sum_{\delta\in D_x(B)}w_{x,\delta}(B).
\]

Thus the squareclass index itself contributes no fixed positive exponent beyond the support exponent of `q1`.

## 2. Max-fiber progress gate

Suppose an **independent** occupied-coordinate support theorem gives

\[
|Q(B)|\ll B^{\sigma+o(1)},
\]

and a **uniform moving-fiber** theorem gives

\[
\max_{x,\delta}w_{x,\delta}(B)
\ll B^{\phi+o(1)}.
\]

Then r301h absorbs the squareclass multiplicity and yields

\[
\boxed{
N_2(B)\ll B^{\sigma+\phi+o(1)}.
}
\]

Therefore this decomposition breaks the current half-power wall precisely when

\[
\boxed{\sigma+\phi<\frac12.}
\]

In particular, a uniform subpower fiber theorem `phi=0` would still require an independent strict sub-half bound for the occupied `q1` support.

## 3. Why the currently available facts do not satisfy the gate

R301i proves only the pointwise statement

\[
w_{x,\delta}(B)=B^{o_{x,\delta}(1)}
\]

for each fixed fiber.  It does **not** prove a uniform `phi=0` as `(x,delta)` move with `B`.

Also, the tautological survivor support bound

\[
|Q(B)|\le N_2(B)
\]

cannot be fed back as an independent `sigma` theorem.  Doing so would be circular.  The elementary ambient count of possible Pythagorean face slopes is at polynomial scale and by itself is much weaker than the current `B^(1/2+epsilon)` theorem.

Thus the attractive fixed-fiber genus-one picture is not yet an upper-bound improvement.

## 4. Second-moment version and diagonal firewall

Let

\[
\mathcal C(B)=\{(x,\delta):w_{x,\delta}(B)>0\},
\qquad
E_{q,\delta}(B)=\sum_{(x,\delta)\in\mathcal C(B)}w_{x,\delta}(B)^2.
\]

Since `#C(B)<=|Q(B)| B^{o(1)}`, if independently

\[
|Q(B)|\ll B^{\sigma+o(1)},
\qquad
E_{q,\delta}(B)\ll B^{\eta+o(1)},
\]

then Cauchy gives

\[
\boxed{N_2(B)\ll B^{(\sigma+\eta)/2+o(1)}.}
\]

The sufficient strict-half gate is

\[
\boxed{\sigma+\eta<1.}
\]

But the full second moment contains the diagonal:

\[
E_{q,\delta}(B)\ge N_2(B).
\]

So at an unresolved support wall `sigma=1/2`, proving `eta<1/2` would already contain a strict-half theorem.  Full energy is therefore not a shortcut around the diagonal barrier; an off-diagonal/exceptional-mass theorem or a strict support deficit would be needed.

## 5. Exact reopen contract

This Stage20 squareclass reentry becomes quantitatively competitive with the current half-power theorem only after at least one genuinely new input of the following type:

1. an independent occupied-`q1` support theorem with exponent `sigma<1/2`, together with uniform subpower or sufficiently small-power genus-one fibers;
2. a uniform/averaged moving `(q1,delta)` genus-one fiber theorem giving `sigma+phi<1/2` when combined with an independently proved support exponent;
3. a strict support plus off-diagonal collision/weighted exceptional-mass theorem satisfying the corresponding second-moment gate;
4. a coupling of the squareclass receiver to the existing half-power representation that proves a new saving without double-charging a variable already paid for in the Stage14/Stage27 host ledger.

No such theorem is proved in this batch.

```text
STAGE27_20_R301J_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
SQUARECLASS_INDEX_FIXED_POWER_COST_ZERO_AFTER_FIXED_Q1=true
MAX_FIBER_PROGRESS_GATE=sigma+phi<1/2
SECOND_MOMENT_PROGRESS_GATE=sigma+eta<1
POINTWISE_FIXED_FIBER_BOUND_USED_AS_UNIFORM=false
TAUTOLOGICAL_Q1_SUPPORT_USED_AS_INDEPENDENT_BOUND=false
FULL_SECOND_MOMENT_DIAGONAL_IGNORED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301k
STOP_REASON=UNIFORM_OR_AVERAGED_MOVING_GENUS_ONE_FIBER_PLUS_INDEPENDENT_SUPPORT_THEOREM_REQUIRED
```
