# Stage26-60 — generalized Saunderson two-parameter lower attack

EVIDENCE_LEVEL=PROVED_NEW_THEOREM_CANDIDATE
CHECKPOINT=60
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
DEPENDS_ON=Stage20,Stage26-40,Stage26-50

## 1. Why checkpoint60 reopens the lower side

Checkpoint40 gives the strongest certified upper family for the Euler stratum, while checkpoint50 isolates an explicit one-parameter Saunderson subfamily giving `M3(B) >> B^(1/6)`. The gap is still enormous. Checkpoint60 therefore tests whether the one-parameter specialization is an artificial bottleneck.

It is.

The Saunderson identities used by Stage20 require only a primitive Pythagorean triple

\[
u^2+v^2=w^2,
\]

not the special one-parameter choice `u=m^2-1`, `v=2m`, `w=m^2+1`.

## 2. General primitive Pythagorean input

Let

\[
u=r^2-s^2,\qquad v=2rs,\qquad w=r^2+s^2,
\]

where

```text
r>s>=1,
gcd(r,s)=1,
r-s is odd.
```

Then `(u,v,w)` is a primitive Pythagorean triple; in particular `u,v,w` are pairwise coprime.

Define

\[
A=u|4v^2-w^2|,\qquad
B_1=v|4u^2-w^2|,\qquad
C=4uvw.
\]

The two absolute-value factors never vanish: `4v^2=w^2` would imply `u^2=3v^2`, and `4u^2=w^2` would imply `v^2=3u^2`, both impossible for positive integers.

Exactly as in the audited Stage20 identities,

\[
A^2+B_1^2=w^6,
\]

\[
A^2+C^2=u^2(4v^2+w^2)^2,
\]

\[
B_1^2+C^2=v^2(4u^2+w^2)^2.
\]

Hence every such parameter pair produces an Euler cuboid.

## 3. Primitivity survives for every primitive input triple

The Stage20 prime-divisor proof does not use the one-parameter specialization. If a prime `p` divided `A,B_1,C`, then `p|C=4uvw`.

- `p=2` is impossible because `u,w` are odd and `A` is odd.
- For odd `p`, pairwise coprimality of `u,v,w` means `p` divides exactly one of them. Reducing the other edge formula modulo `p` gives a nonzero residue in each of the three cases.

Therefore

\[
\boxed{\gcd(A,B_1,C)=1}.
\]

Sorting the three positive edges gives one primitive canonical Stage20 object. No primitive reduction is needed.

## 4. Uniform height control

Because `u,v<=w`,

\[
A\le 5w^3,\qquad B_1\le 5w^3,\qquad C\le4w^3.
\]

Thus

\[
R=\sqrt{A^2+B_1^2+C^2}\le\sqrt{66}\,w^3<9w^3.
\]

If `r,s<=T`, then `w=r^2+s^2<=2T^2`, hence

\[
\boxed{R<72T^6}.
\]

Consequently every admissible primitive parameter pair with

\[
T\le(B/72)^{1/6}
\]

maps into `M3(B)`.

## 5. There are quadratically many primitive parameter pairs

Let

\[
\mathcal P(T)=\{(r,s):1\le s<r\le T,\gcd(r,s)=1,r-s\text{ odd}\}.
\]

Elementary Möbius inversion with the parity restriction gives

\[
\#\mathcal P(T)\asymp T^2.
\]

Only a positive-density statement is needed here. Equivalently, one may count even `r` and odd `s`, remove pairs sharing an odd prime, and obtain a positive proportion after the standard coprime-pair sieve.

Thus the generalized Saunderson parameter space contributes order `T^2` primitive inputs before quotienting duplicate outputs.

## 6. Duplicate outputs are only divisor-size

The key invariant is already visible in the identity

\[
A^2+B_1^2=w^6.
\]

For every input triple, one of the three face diagonals of the resulting canonical Euler cuboid is exactly

\[
\boxed{w^3}.
\]

Fix one canonical output cuboid `E`. Its three face diagonals are fixed. Hence a preimage can use at most three possible values of `w`: `w^3` must equal one of those three diagonals.

For a fixed `w`, the number of primitive Pythagorean triples with hypotenuse `w` is at most the number of representations of `w^2` as a sum of two squares. The standard representation bound gives

\[
r_2(w^2)\le4\tau(w^2).
\]

For every fixed `epsilon>0`, the elementary divisor bound gives

\[
\tau(n)\ll_\epsilon n^\epsilon.
\]

Therefore every canonical Euler cuboid has at most

\[
B^{o(1)}
\]

generalized-Saunderson preimages among inputs producing height `R<=B`; more explicitly, for every fixed `epsilon>0` the fiber is `O_epsilon(B^epsilon)` after harmless renaming of epsilon.

This is the missing injectivity substitute: global one-to-one behavior is unnecessary.

## 7. New lower theorem candidate

Take

\[
T=\left\lfloor(B/72)^{1/6}\right\rfloor.
\]

There are `>>T^2` admissible primitive parameter pairs, and every output fiber has size `B^{o(1)}`. Hence

\[
M_3(B)\ge B^{1/3-o(1)}.
\]

Equivalently, for every fixed `epsilon>0`,

\[
\boxed{M_3(B)\gg_\epsilon B^{1/3-\epsilon}.}
\]

This strictly improves the audited one-parameter lower exponent `1/6`.

The precise statement is endpoint-free: checkpoint60 does **not** claim `M3(B)>>B^(1/3)` with a fixed positive constant.

## 8. Improved Stage26 completion corridor

Since Stage18 gives

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

checkpoint60 yields, for every fixed `epsilon>0`,

\[
\boxed{
\frac{M_3(B)}{M_2(B)}
\gg_\epsilon
B^{-2/3-\epsilon}(\log B)^{-5}
}.
\]

The exact adapters from checkpoint30 therefore give the same improved polynomial lower scale for the literal object completion

\[
\Phi=\frac{M_3}{M_2+M_3}
\]

and, up to the exact multiplicity factor three, for

\[
\Theta=\frac{3M_3}{M_2+3M_3}.
\]

Combining with checkpoint40, for every fixed `epsilon>0` and every fixed `0<delta<1/46`,

\[
B^{-2/3-\epsilon}(\log B)^{-5}
\ll_\epsilon
\Phi(B),\Theta(B)
=o((\log B)^{-\delta}).
\]

The upper and lower sides still do not match.

## 9. What checkpoint60 learned about the true-scale search

The former `1/6` lower exponent was caused by restricting the primitive Pythagorean input to a one-dimensional curve. Restoring the full two-dimensional primitive Pythagorean parameter space raises the certified lower exponent candidate to `1/3-o(1)`.

This localizes the next genuine obstruction:

```text
OLD_LOWER_BOTTLENECK=ONE_PARAMETER_SPECIALIZATION
OLD_LOWER_BOTTLENECK_REMOVED=true
NEW_LOWER_POWER_FLOOR=1/3_MINUS_EPSILON
NEXT_GAP=GENERAL_SAUNDERSON_FAMILY_VS_K3_THIN_COVER_UPPER
```

Checkpoint70 should close Stage26 only after fresh hostile audit decides whether the divisor-fiber argument is accepted. If accepted, Stage26's final handoff must use the improved `1/3-o(1)` lower theorem, not the old `1/6` floor.

## 10. Firewalls

```text
GENERAL_SAUNDERSON_TWO_PARAMETER_FAMILY_USED=true
GLOBAL_INJECTIVITY_CLAIMED=false
DIVISOR_FIBER_BOUND_USED=true
M3_LOWER_B_ONE_THIRD_MINUS_EPSILON_CANDIDATE=true
M3_LOWER_B_ONE_THIRD_WITHOUT_EPSILON_PROVED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
UPPER_LOWER_MATCH=false
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
K3_MANIN_TRANSFER=false
INDEPENDENCE_CLAIM=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=70
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage26-audit
```
