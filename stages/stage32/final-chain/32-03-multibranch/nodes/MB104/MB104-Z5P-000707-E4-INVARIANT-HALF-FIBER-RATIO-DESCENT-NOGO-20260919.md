# MB104 Z5' — 000707 e=4 invariant half-fiber ratio descent no-go — 2026-09-19

Status: **PARALLEL PRE-AUDIT EXACT DESCENT NO-GO / NO CREDIT**

## Purpose

Continue the exact e=4 ambient theta factorization

```text
h = (1-i)(d_z-i e_z)(d_w-e_w)
```

for the surviving dangerous support

```text
Sigma=000707000f0f.
```

The preceding gate reduced the possible singular-carrier obstruction to first-jet/conductor
compatibility of the two individual half-fiber factors.

Freitag--Salvati Manni Lemma 2.3 resolves that question.

## 1. Exact G-characters of d and e

Write

```text
d=theta00(2z),
e=theta10(2z).
```

For the generators

```text
G=Gamma[4]/Gamma[8]=<T,T',R> ~= (Z/2)^3,
```

Freitag--Salvati Manni Lemma 2.3 gives, on the ordered five theta generators,

```text
T  -> diag(1,-1,1, 1, 1),
T' -> diag(1, 1,-1, 1, 1),
R  -> diag(1, 1, 1,-1,-1).
```

Hence the pair `(d,e)` transforms by the same scalar character:

```text
T:  (d,e)->( d, e),
T': (d,e)->( d, e),
R:  (d,e)->(-d,-e).
```

Therefore every linear form

```text
d-alpha e
```

has the same character

```text
chi(T)=chi(T')=+1,
chi(R)=-1.
```

## 2. The two half-fiber factors have identical character

Define

```text
s_z=d_z-i e_z,
s_w=d_w-e_w.
```

Under the diagonal G-action on the product,

```text
s_z -> chi(g) s_z,
s_w -> chi(g) s_w.
```

Thus:

```text
s_z s_w
```

is invariant, explaining the support-hyperplane factorization, but also

```text
f := s_z/s_w
```

is invariant.

Therefore

```text
f in k(C8 x C8)^{diag(G)}
   = k(box surface).
```

So the ratio of the two half-fiber factors is an honest rational function on the box surface.

## 3. Consequence on a hypothetical singular carrier

Restrict f to any integral carrier C not contained in the pole divisor.  Its pullback to the
normalization E is exactly the ratio of the two factor-fiber sections:

```text
nu^*f = s_z/s_w.
```

For the e=4 dangerous packet,

```text
div_E(s_z)=B_z=phi_1^{-1}(i),
div_E(s_w)=B_w=phi_2^{-1}(1),
```

so

```text
div_E(nu^*f)=B_z-B_w.
```

Because f already lives on the singular carrier, this divisor difference is not merely principal on
the normalization.  Its conductor gluing is automatically the pullback of a principal rational
function downstairs.

In particular, every local first-jet sign around the conductor which arises from comparing
`s_z` and `s_w` is already globally compatible.  There is no additional generalized-Jacobian
obstruction in this ratio.

## 4. Interpretation

The newly discovered distinguished factorization

```text
support hyperplane
 = saturated factor-1 fiber
 + saturated factor-2 fiber
```

is genuine and exact, but its obvious conductor test is tautologically compatible because the
ratio of the two factors descends through the diagonal modular quotient.

Thus the hoped-for route

```text
two half-fiber factors
 -> compare their first-jet descent signs
 -> obtain an e=4 contradiction
```

is closed in the negative direction.

This does **not** trivialize the absent-type residual character eta.  The latter comes from the
0/infinity half-fibers of each individual factor map and remains the nonzero class in the e=4 case.
The present descended function compares the distinguished used-type fibers `t_z=i` and
`t_w=1`, a different divisor problem.

## 5. Z5' routing consequence

The exact X(4) adapter and grid remain useful data, but they have now exhausted:

- one-factor scalar passports;
- one-factor individual six-value Nielsen feasibility;
- distinguished two-fiber support-hyperplane factorization;
- conductor/first-jet comparison of those two factors.

Any further Z5' progress must involve a genuinely different simultaneous invariant, for example:

```text
the absent-type eta classes themselves,
an actual common-G-cover relation not equivalent to Kummer square classes,
or conductor data not expressible as the ratio of the two distinguished theta factors.
```

Do not deepen the distinguished-half-fiber ratio route again.

## Source locks

External:
- Freitag--Salvati Manni, *Parametrization of the box variety by theta functions*,
  Michigan Math. J. 65 (2016), Lemma 2.3 and Theorem 2.4.

Retained:
- `FREITAG-SALVATI-MANNI-LOCAL-NODE-THETA-SOURCE-NOTE.md`
  blob `36664f4443e508bb0d9b264f4fe9bb88030bdf38`;
- current e=4 ambient-theta factorization gate;
- current exact factor-cusp/grid adapter.

## Firewalls

```text
half_fiber_ratio_descends_to_box_surface=true
distinguished_factor_conductor_obstruction=false
absent_eta_trivial=false
e4_excluded=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
