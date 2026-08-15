# Stage25-60 R504 nonsplit squareclass — commuting involution classification

STATUS=ACTIVE_RESEARCH
ROUTE=R504
CHECKPOINT=60

The hostile-audited complete Q-degree-2 descent gives the nonsplit stratum
\[
\phi(u)=\frac{A(u^2+d)+Bu}{C(u^2+d)+Du},
\qquad d\in\mathbf Q^*/(\mathbf Q^*)^2,
\]
with nonsplit deck involution
\[
\delta:u\mapsto d/u.
\]
Put
\[
t=u+d/u,\qquad m(t)=\frac{At+B}{Ct+D},
\qquad \Delta=AD-BC\ne0.
\]
Then `phi=m(t)`.

## 1. Q-rational reduced involutions on the inherited elliptic quotient

The quartic quotient is the fixed genus-one curve `z^2=k^4+1`, birational to the audited `E0`.  Its Q-rational reduced involutions are represented on the `k`-line by
\[
g_-:k\mapsto-k,
\qquad g_+:k\mapsto1/k,
\qquad g_{-+}:k\mapsto-1/k.
\]
These are the three nontrivial translations by the rational 2-torsion after quotienting by the elliptic negation; the extra CM automorphisms are not Q-rational.  Hence this is the complete Q-rational reduced involution list for the fixed quartic model.

For each `g`, transport it to the `t`-line:
\[
T_g=m^{-1}gm.
\]
After clearing the common determinant `Delta`, the matrices are
\[
T_-:\begin{pmatrix}
-AD-BC & -2BD\\
2AC & AD+BC
\end{pmatrix},
\]
\[
T_+:\begin{pmatrix}
-AB+CD & -B^2+D^2\\
A^2-C^2 & AB-CD
\end{pmatrix},
\]
\[
T_{-+}:\begin{pmatrix}
-AB-CD & -B^2-D^2\\
A^2+C^2 & AB+CD
\end{pmatrix}.
\]

## 2. Exact Q-lift criterion through the nonsplit double cover

A Q-rational involution of the `u`-line commuting with `delta` has the form
\[
\epsilon_{p,q}(u)=\frac{pu+dq}{-qu-p},
\qquad (p,q)\ne(0,0).
\]
Its action on `t=u+d/u` is
\[
T_{p,q}(t)=
-\frac{(p^2+dq^2)t+4dpq}{pq\,t+(p^2+dq^2)}.
\]
Thus a trace-zero matrix
\[
T(t)=\frac{a t+b}{c t-a}
\]
lifts to such a Q-rational **involution** only if
\[
b=-4dc
\]
and the lift discriminant
\[
a^2-4dc^2
\]
is a square in Q.  For an actual `epsilon_(p,q)` it equals `(p^2-dq^2)^2`.

Applying this criterion to the three transported reduced involutions gives the complete commuting-lift loci below.

### N1: lift of `k -> -k`

The condition `b=-4dc` is
\[
\boxed{BD=4dAC}.
\]
On this locus,
\[
(AD+BC)^2-16dA^2C^2=(AD-BC)^2=\Delta^2,
\]
so the lift obstruction is automatically a rational square.  Therefore every nondegenerate rational point on this locus gives a Q-rational commuting extra involution.

### N2: lift of `k -> 1/k`

The condition is
\[
\boxed{D^2-B^2+4d(A^2-C^2)=0}.
\]
Substituting this identity into the lift discriminant gives
\[
(-AB+CD)^2-4d(A^2-C^2)^2=(AD-BC)^2=\Delta^2.
\]
Again the Q-lift obstruction vanishes identically on the locus.

### N3: attempted lift of `k -> -1/k`

The condition is
\[
\boxed{B^2+D^2=4d(A^2+C^2)}.
\]
But now
\[
(-AB-CD)^2-4d(A^2+C^2)^2
=-(AD-BC)^2=-\Delta^2.
\]
For nondegenerate `Delta != 0`, this is not a square in Q.  Hence this entire candidate locus has **no Q-rational involutive lift**.

Therefore the nonsplit commuting-involution search is exactly reduced to two genuine algebraic loci:

```text
R504_NONSPLIT_DECK=u->d/u
R504_NONSPLIT_N1=BD-4*d*A*C=0;Q_LIFT=true
R504_NONSPLIT_N2=D^2-B^2+4*d*(A^2-C^2)=0;Q_LIFT=true
R504_NONSPLIT_N3=B^2+D^2-4*d*(A^2+C^2)=0;Q_LIFT=false
R504_NONSPLIT_COMMUTING_EXTRA_INVOLUTION_LOCUS=N1_UNION_N2
R504_NONSPLIT_COMMUTING_LIFT_CLASSIFICATION=CLOSED_WITH_SYMBOLIC_CERTIFICATE
```

## 3. Scope firewall

This is a complete classification of Q-rational extra involutions **commuting with the deck involution** in the nonsplit squareclass stratum.  It does not yet prove that the elliptic quotients on N1/N2 are not Q-isogenous to `E0`, and it does not exclude noncommuting / degree-4 elliptic-subcover / Prym mechanisms.

```text
R504_NONSPLIT_N1_COMPLEMENT_ISOGENY_CHECK=OPEN
R504_NONSPLIT_N2_COMPLEMENT_ISOGENY_CHECK=OPEN
R504_NONSPLIT_NONCOMMUTING_OR_PRYM_RESIDUAL=LIVE
R504_FULL_Q_DEGREE2_COMMUTING_LIFT_CLASSIFICATION_PROVED=true
R504_FULL_Q_DEGREE2_RANK_JUMP_CLASSIFICATION_PROVED=false
GLOBAL_STAGE25_LOWER_CHANGED=false
CHECKPOINT60_DEEP_STOP_RULE_SATISFIED=false
STAGE70_ALLOWED=false
```

## 4. Next attack

Compute explicit complementary genus-one quotient models on N1 and N2 and test Q-isogeny to `E0` with a source-independent certificate.  Only after those are closed should the remaining noncommuting/Prym locus be compared to the Bruin/Shaska external theorem species.
