# Stage29-02e — endpoint L-function / coordinate-K3 source lock

```text
TASK=Stage29-02e
ROLE=ENDPOINT_LFUNCTION_PLUS_COORDINATE_K3_MODULAR_REMATCH
STATUS=SUBMISSION_PENDING_FRESH_AUDIT
```

## Primary source A — endpoint L-function

Madoka Horie; Takuya Yamauchi, `The L-function of the surface parametrizing cuboids`, arXiv `2512.22520v3`, revised 24 March 2026.

The paper studies the same Stoll--Testa canonical cuboid surface `Sbar` and its minimal resolution `S` used by Stage29.

Theorem 1.1 gives

```text
L(s,H2(S))
 = L(s,H2(Sbar)) * zeta(s-1)^24 * L(s-1,chi_-1)^24,
```

and

```text
L(s,H2(Sbar))
 = L(s,h16)^3 * L(s,h32) * L(s,h8)^3 * L(s-1,L_ell),

L(s,L_ell)
 = zeta(s)^10
   * L(s,chi_-1)^2
   * L(s,chi_-2)
   * L(s,chi_2)^3.
```

Here `h8,h16,h32` are the unique rational-coefficient weight-3 newforms at levels 8,16,32, and `chi_d` is the quadratic character of `Q(sqrt(d))`.

Theorem 4.4 gives the semisimplified l-adic decomposition

```text
H2(Sbar)
 = V_h16^3
   + V_h32
   + (chi_2 tensor V_h32)^3
   + L_ell(-1),

chi_2 tensor V_h32 ~= V_h8.
```

Lemma 2.1 gives

```text
rank H2(Sbar)=30,
H2(Sbar) pure weight 2,
H3(Sbar)=0.
```

Theorem 1.1 also gives the geometric Picard rank `64` and the field-of-definition distribution

```text
34 over Q,
26 strictly over Q(i),
1 strictly over Q(sqrt(-2)),
3 strictly over Q(sqrt(2)).
```

## Primary source B — coordinate sign K3 quotients

Damiano Testa; Michael Stoll, `Curves on the surface of cuboids` / author-PDF title `The surface parametrizing cuboids`, Mathematics of Computation, DOI `10.1090/mcom/4238`; open preprint arXiv `1009.0388`.

Section 6 studies the seven coordinate-sign K3 quotients

```text
K_a1,K_a2,K_a3,
K_b1,K_b2,K_b3,
K_c.
```

The three `K_aj` are Q-isomorphic, the three `K_bj` are Q-isomorphic, and `K_a` is isomorphic to `K_c` after a field extension stated in the source. The quotient `K_c` obtained by forgetting the long diagonal is the Euler-brick K3.

For `K_c`, Testa--Stoll prove that the minimal desingularization has geometric Picard rank `20`; their public verification source constructs the rank-20 Picard lattice and proves generation by the known curves.

## Primary source C — immutable verification code

Michael Stoll, public repository `MichaelStollBayreuth/Verification`:

```text
commit=51233ed5ef2bf228fac9416c66db9adc0ebcaadd
file=Cuboids/cuboids.magma
blob=0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

The file explicitly constructs the three-quadric `K_c` model, its singular points/known curves, the intersection pairing, the rank-20 Picard lattice, the hyperplane class, the automorphism action, and the maps between `Pic(S)` and `Pic(K_c)`.

## Stage29 model adapter

The three representative singular complete-intersection models used by the reproducible finite-field check are exact coordinate eliminations of the full cuboid equations:

```text
K_c  (forget c):
 a1^2+a2^2=b3^2
 a1^2+a3^2=b2^2
 a2^2+a3^2=b1^2

K_b1 (forget b1):
 a2^2+b2^2=c^2
 a3^2+b3^2=c^2
 a1^2+a2^2+a3^2=c^2

K_a1 (forget a1):
 a2^2+a3^2=b1^2
 a2^2+b2^2=c^2
 a3^2+b3^2=c^2.
```

Thus the finite-field calculation is performed on the literal coordinate-sign quotients, not on unrelated K3 models.

## Firewalls

```text
ENDPOINT_LFUNCTION_COMPUTED=true
ENDPOINT_RATIONAL_POINT_SET_COMPUTED=false
FINITE_PRIME_TRACE_MATCH_IMPLIES_GLOBAL_GALOIS_ISOMORPHISM=false
K3_MODULAR_IDENTIFICATION_REQUIRES_FRESH_AUDIT=true
GOOD_PRIME_TRACE_IS_NOT_PHYSICAL_HEIGHT_COUNT=true
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
