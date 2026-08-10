# Stage14-4bs — 20/21 architecture barrier and joint-denominator receiver

## Purpose

Merged 4br proves

\[
V(B)\ll B^{20/21+o(1)}.
\]

This stage asks whether the same size-splitting architecture can be re-tuned to beat `20/21`. The answer is no. We prove the exact optimization barrier, then import merged s7-04 as the next genuinely new family-level receiver.

## 1. General cutoff ledger

Replace the fixed 4bl cutoff by

\[
X_2\le B^\theta,\qquad 0<\theta\le1.
\]

The three merged mechanisms give the following exponents.

### Small partner-leg sector

Direct primitive-face counting gives

\[
E_{\rm small}(B)\ll B^{\theta+o(1)}.
\]

### Cross sector

If `X2>B^theta`, the five-factor decomposition forces one receiver of size at least `B^(theta/5)`. If the large receiver is `X2_cross`, merged 4bm gives

\[
X_{2,\rm cross}\le 2^a c h^2.
\]

Using the optimized 4br weighted split, one of `2^a,c,h` is at least `B^(theta/20)`, and each corresponding counting lemma gives the same saving. Hence

\[
E_{\rm cross}(B)\ll B^{1-\theta/20+o(1)}.
\]

### Good-cell residual

Outside the cross branch, `X2_cross<B^(theta/5)` and therefore

\[
Q=X_{2,\rm good}>B^{4\theta/5}.
\]

The 4bo normalized core then satisfies

\[
a_0b_0<B^{\theta/5},\qquad c_0d_0<B^{1-4\theta/5},
\]

so the core count is

\[
B^{1-3\theta/5+o(1)}.
\]

Merged 4bq adds only `B^(1/2+o(1))` for the smaller diagonal product. Therefore

\[
E_{\rm good}(B)\ll B^{3/2-3\theta/5+o(1)}.
\]

Thus the entire existing architecture has exponent

\[
\boxed{F(\theta)=\max\left(\theta,\ 1-\frac{\theta}{20},\ \frac32-\frac{3\theta}{5}\right)}.
\]

## 2. Exact minimization

The first term is increasing and the second is decreasing. Their intersection is

\[
\theta=1-\theta/20,
\]

hence

\[
\boxed{\theta=20/21}.
\]

At this point

\[
\theta=1-\theta/20=20/21,
\]

while

\[
3/2-3\theta/5=13/14<20/21.
\]

For `theta<20/21`, the cross term is strictly larger than `20/21`; for `theta>20/21`, the small-leg term is strictly larger. Therefore

\[
\boxed{\min_{0<\theta\le1}F(\theta)=20/21}.
\]

This is a structural barrier for the current three-part size architecture, not a loose numerical choice.

## 3. Consequence

No further retuning of

- partner-leg cutoff,
- five-factor pigeonhole,
- positive cross decomposition `2^a c h^2`, or
- diagonal-pair genus-one counting

can improve the whole-family exponent below `20/21` without a genuinely new correlation theorem.

Accordingly the old optimization loop is closed.

## 4. Next receiver from merged s7-04

Merged s7-04 supplies exactly such a new joint object. For reduced physical coordinates

\[
u=P/Q,\qquad w=R/S,
\]

one has

\[
QS=H_{\rm mult}\ll B,
\]

plus the simultaneous constraints

\[
0<R/S<P/Q<1,
\]

\[
PR/(QS)\text{ is a rational square},
\]

and

\[
\boxed{\ker(Q^2-P^2)=\ker(S^2-R^2)}.
\]

Separate projection counting is known to have optimal exponent `1` and is therefore discarded. The next main-track problem is the joint denominator-hyperbola / same-squarefree-kernel collision count, retaining both reduced coordinates simultaneously.

This receiver is not part of the 20/21 barrier because it uses a correlation absent from the positive size split.

## 5. Status

```text
STAGE14_4BS=EXACT_20_21_ARCHITECTURE_BARRIER_AND_JOINT_RECEIVER_SELECTION
GENERAL_CUTOFF_SMALL_EXPONENT=theta
GENERAL_CUTOFF_CROSS_EXPONENT=1-theta/20
GENERAL_CUTOFF_GOOD_EXPONENT=3/2-3theta/5
CURRENT_ARCHITECTURE_OPTIMAL_THETA=20/21
CURRENT_ARCHITECTURE_MIN_EXPONENT=20/21
SIZE_SPLITTING_ALONE_CAN_BEAT_20_21=false
MERGED_S7_04_JOINT_RECEIVER_IMPORTED=true
NEXT_PRIMARY_RECEIVER=JOINT_DENOMINATOR_HYPERBOLA_SAME_KERNEL
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
REMAINING_GAP_TO_SQRT=19/42
SQRT_B_UPPER_BOUND_PROVED=false
NEXT=Stage14-4bt
```
