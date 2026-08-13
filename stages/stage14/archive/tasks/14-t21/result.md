# Stage14-t21 — partition-resolved direction/scale counting reduction

## Purpose

Stage14-t20 replaced the incorrect exactly-two collision population by raw-pair edges and reduced equal missing-face squareclasses to coprime squarefree partitions

\[
A=\alpha r^2,\qquad B=\beta u^2,\qquad (\alpha,\beta)=1.
\]

The remaining target is

\[
Q_{\rm split}(B)=\sum_{\alpha,\beta}N_{\alpha,\beta}(B)^2.
\]

Stage14-t21 resolves the internal geometry of a fixed partition `(alpha,beta)`.  The key point is that `(alpha,beta,r,u)` determines the reduced space/shared-side direction `(D,C)` exactly; after that, only an integer scale and the two Pythagorean face completions remain.

No power saving for `Q_split(B)` is claimed here.

## 1. Exact generalized-Pell direction parametrization

For a raw edge write, as in t20,

\[
g=(d,s),\qquad D=d/g,\qquad C=s/g,
\]

\[
h=(D-C,D+C)\in\{1,2\},
\]

and

\[
D-C=h\alpha r^2,\qquad D+C=h\beta u^2.
\]

Put

\[
a=\alpha r^2,\qquad b=\beta u^2.
\]

Then

\[
(a,b)=1,\qquad b>a,
\]

and

\[
\boxed{
D=\frac h2(a+b),\qquad C=\frac h2(b-a).
}
\]

The parity factor is not free.  It is determined uniquely by

\[
\boxed{
h=1\iff a,b\text{ are both odd};\qquad h=2\text{ otherwise}.}
\]

Indeed, if `a,b` are both odd then `(a+b)/2,(b-a)/2` are coprime integers.  If one is even and the other odd, the primitive pair is instead `(a+b,b-a)`.  Since `(a,b)=1`, both cannot be even.

Conversely, any positive coprime pair `a=alpha r^2`, `b=beta u^2` with `b>a`, together with this parity rule, produces coprime positive integers `(D,C)` satisfying

\[
D^2-C^2=h^2\alpha\beta r^2u^2.
\]

Thus the t20 factorization gives a genuine bijection

```text
fixed split partition (alpha,beta)
+ primitive square variables (r,u)
<->
reduced direction (D,C)=(d/g,s/g).
```

This is the generalized rational Pell/hyperbola parametrization appropriate to the collision fiber.

## 2. Scale layer and a new primitive support restriction

Once `(alpha,beta,r,u)` is fixed, `(D,C)` is fixed and every raw edge in that direction has

\[
d=gD,\qquad s=gC,
\]

with

\[
1\le g\le B/D.
\]

There is an exact additional restriction on this scale.

Let the other two cuboid sides be `x,y`.  Then

\[
x^2+y^2=d^2-s^2.
\]

If an odd prime `p=3 mod 4` divided `g`, then `p|d,s` and hence

\[
x^2+y^2\equiv0\pmod p.
\]

Because `-1` is not a quadratic residue modulo such a prime, this forces `p|x,y`.  Together with `p|s` this contradicts primitive cuboid normalization.

Likewise `2` cannot divide `g`: if `d,s` are even then `x^2+y^2` is divisible by `4`, forcing `x,y` even.

Therefore every prime divisor of the scale satisfies

\[
\boxed{p\mid g\Longrightarrow p\equiv1\pmod4.}
\]

So both the squarefree kernel from t20 and the hidden scale layer are supported on split Gaussian primes, while the scale contains no factor `2`.

This is an exact primitive restriction.  By itself it is only a multiplicative sparsity statement, not the power saving needed for the t-track target.

## 3. Fixed direction-scale fibers have subpolynomial face multiplicity

Fix `(alpha,beta,r,u,g)`, hence fix `(d,s)`.

Each integral face completion `x` satisfies

\[
s^2+x^2=H^2,
\]

so

\[
(H-x)(H+x)=s^2.
\]

A positive completion is therefore determined by a divisor pair of `s^2`.  In particular the number of possible positive `x` is at most `tau(s^2)`, and the number of ordered pairs `(x,y)` satisfying the two separate face-square conditions is at most

\[
\tau(s^2)^2.
\]

The additional requirements

\[
x^2+y^2=d^2-s^2
\]

and primitive/canonical ordering can only decrease this number.  Since `s<=d<=B`, the standard divisor bound gives uniformly

\[
\boxed{
\#\{\text{raw edges over fixed }(\alpha,\beta,r,u,g)\}=B^{o(1)}.
}
\]

This is the first uniform fiber-multiplicity bound after resolving the split partition.

## 4. Direction-scale majorant

Define the admissible direction set

\[
\mathcal R_{\alpha,\beta}(B)
=
\left\{
(r,u):
(\alpha r^2,\beta u^2)=1,
\ \beta u^2>\alpha r^2,
\ D_{\alpha,\beta}(r,u)\le B
\right\},
\]

where `D_{alpha,beta}(r,u)` is given by the parity formula above.

Dropping the split-prime restriction on `g` only enlarges the count, so the fixed-fiber divisor estimate yields

\[
\boxed{
N_{\alpha,\beta}(B)
\le
B^{o(1)}
\sum_{(r,u)\in\mathcal R_{\alpha,\beta}(B)}
\left\lfloor\frac{B}{D_{\alpha,\beta}(r,u)}\right\rfloor.
}
\]

Since

\[
D_{\alpha,\beta}(r,u)
\ge
\frac{\alpha r^2+\beta u^2}{2},
\]

we obtain

\[
N_{\alpha,\beta}(B)
\le
B^{1+o(1)}
\sum_{\alpha r^2+\beta u^2\le 2B}
\frac1{\alpha r^2+\beta u^2}.
\]

Using

\[
\alpha r^2+\beta u^2\ge2\sqrt{\alpha\beta}\,ru
\]

and harmonic sums gives the explicit coarse envelope

\[
\boxed{
N_{\alpha,\beta}(B)
\ll
\frac{B^{1+o(1)}}{\sqrt{\alpha\beta}}.
}
\]

The logarithmic factors are absorbed in `B^{o(1)}`.

## 5. Why this does not yet prove the collision saving

The last bound is deliberately recorded as a boundary, not promoted as a solution.  For small kernels, especially the trivial partition `(1,1)`, it allows nearly linear size.  Squaring and summing it therefore does not prove

\[
Q_{\rm split}(B)=O(B^{1-\delta}).
\]

The reason is now precise: the majorant counts every admissible generalized-Pell direction and every scale, and uses the two integral-face equations only through the very soft divisor bound `tau(s^2)^2`.

The required power saving must therefore come from a **simultaneous face-completion correlation** across the direction-scale family, not from:

- the squarefree partition alone;
- split-prime support of `alpha beta`;
- split-prime support of `g`;
- or the divisor bound for one fixed `(d,s)`.

This identifies the next useful object.  For a fixed reduced direction `(D,C)`, define

\[
M_{D,C}(G)
=
\#\left\{
1\le g\le G:
\exists x,y>0,
\ (gC)^2+x^2=H_1^2,
\ (gC)^2+y^2=H_2^2,
\ x^2+y^2=g^2(D^2-C^2),
\ \gcd(gC,x,y)=1
\right\}.
\]

A power-saving average for these simultaneous completion counts, uniformly over the generalized-Pell directions belonging to `(alpha,beta)`, is the missing input.

## 6. Frozen finite audit

The standard-library audit regenerates every raw-pair edge through `B=2,000,000` and verifies:

- the direction reconstruction from `(alpha,beta,r,u)` on every edge;
- the parity rule for `h`;
- coprimality of the reconstructed `(D,C)`;
- the split-prime-only support of every nontrivial scale `g`;
- the fixed `(d,s)` divisor-pair face-completion envelope;
- uniqueness of observed `(D,C)`, `(alpha,beta)`, and squareclass in the frozen range.

At `B=2,000,000` the finite diagnostics are

```text
raw-pair edges                         356
h=1 / h=2                              268 / 88
g=1 edges                              317
nontrivial-g edges                      39
observed g values                 1,5,13,17,29,37,41
maximum g                               41
maximum r / u                           60 / 149
distinct reduced directions            356
distinct split partitions              356
maximum tau(s^2)                       4455
```

The finite uniqueness remains diagnostic only.

## Locked boundary

```text
STAGE14_T21=COMPLETE_PARTITION_DIRECTION_SCALE_REDUCTION
FIXED_PARTITION_DIRECTION_PARAMETRIZATION_BIJECTIVE=true
DIRECTION_FORMULA=D=h(alpha*r^2+beta*u^2)/2
SHARED_FORMULA=C=h(beta*u^2-alpha*r^2)/2
H_PARITY_RULE_EXACT=true
SCALE_PRIME_SUPPORT_ONLY_1MOD4=true
FIXED_DIRECTION_SCALE_FACE_MULTIPLICITY=B^o(1)
N_ALPHA_BETA_DIRECTION_SCALE_MAJORANT=true
N_ALPHA_BETA_COARSE_BOUND=B^(1+o(1))/sqrt(alpha*beta)
COARSE_BOUND_SUFFICIENT_FOR_Q_SPLIT_POWER_SAVING=false
SIMULTANEOUS_FACE_COMPLETION_CORRELATION_REQUIRED=true
Q_SPLIT_POWER_SAVING_PROVED=false
Q_EDGE_O_B_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t22 analyze simultaneous face-completion counts M_{D,C}(G) / extract a power-saving average over generalized-Pell directions
```
