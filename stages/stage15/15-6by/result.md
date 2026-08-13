# Stage15-6by — channel-gcd product divisor expansion

Base: merged PR #856. Main-batch work unit 1.

Let
\[
G_S=\gcd(m^2+n^2,r^2-s^2),\qquad G_O=\gcd(m^2-n^2,r^2+s^2).
\]
Using the exact identity `gcd(A,B)=sum_{d|A,d|B} phi(d)`, the 6bx first moment becomes
\[
\sum_{P\in A(B)}G_S(P)G_O(P)
=
\sum_{d,e\ge1}\varphi(d)\varphi(e)N_{d,e}(B),
\]
where `N_{d,e}(B)` counts physical ambient states satisfying
\[
d\mid m^2+n^2,\ d\mid r^2-s^2,\ e\mid m^2-n^2,\ e\mid r^2+s^2.
\]
This is an exact reconstruction, not a heuristic sieve weight.

The primitive Pythagorean masks imply the odd supports of the S/O channels are disjoint on the relevant states; 2-adic factors are bounded and may be isolated at `B^o(1)` cost. Thus the target is reduced to a two-modulus weighted congruence count, with expected local index `(de)^2`.

No first-moment bound is claimed yet.

```text
STAGE15_6_SUBSTAGE=6by
STAGE15_6BY_EXACT_DIVISOR_EXPANSION=true
STAGE15_6BY_WEIGHT=phi(d)*phi(e)
STAGE15_6BY_EXPECTED_LOCAL_INDEX=(d*e)^2
STAGE15_6BY_FIRST_MOMENT_PROVED=false
STAGE15_6BY_EXIT=WEIGHTED_MODULUS_SUM_AUDIT_READY
```