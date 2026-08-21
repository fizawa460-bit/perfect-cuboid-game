# Stage29-02e — coordinate-sign K3 / modular-form identification

```text
ROLE=R29_L3_COORDINATE_K3_FROBENIUS_MODULE_IDENTIFICATION
STATUS=PASS_CANDIDATE_PENDING_FRESH_AUDIT
```

## 1. Why this is the missing adapter

Horie--Yamauchi decompose the non-Tate part of the full endpoint surface as

```text
3 * h16  +  1 * h32  +  3 * h8.
```

Testa--Stoll exhibit seven natural coordinate-sign K3 quotient directions grouped as

```text
3 * K_b  +  1 * K_c  +  3 * K_a.
```

The old Stage29-02e note recorded the matching `3+1+3` multiplicity only as suggestive. This suffix now tests the three quotient orbits independently by exact finite-field counting.

## 2. Exact finite-field results

The reproducible script `k3_trace_check.py` counts the literal three-quadric quotient models, detects rational A1 nodes by Jacobian rank, resolves them by adding `p` points per rational exceptional `P^1`, and computes

```text
T_K(p)=#K_smooth(F_p)-1-p^2.
```

At every tested prime

```text
p=3,5,7,11,13,17,19,23,29,31,37,41,43,47,
```

the following identities hold exactly:

```text
K_b:
 T_Kb(p)
 = a_p(h16) + p*(15 + 5 chi_-1(p)).

K_c:
 T_Kc(p)
 = a_p(h32) + p*(16 + chi_-1(p) + 3 chi_2(p)).

K_a:
 T_Ka(p)
 = a_p(h8)
   + p*(13 + 4 chi_-1(p) + 2 chi_2(p) + chi_-2(p)).
```

Thus the orbit-to-newform assignment is

```text
3 * K_b  <-> 3 * h16,
1 * K_c  <-> 1 * h32,
3 * K_a  <-> 3 * h8
```

at all tested good odd primes.

## 3. Rematch to Stage19 / Stage20

The merged Stage29-02b adapter identifies the Stage20 Euler/third-face K3 with the long-diagonal coordinate quotient `K_c` on the relevant dense physical open, and the Stage19 space-completion K3 with a face-diagonal quotient in the `K_b` orbit.

Therefore the new trace identification gives the candidate arithmetic labels

```text
Stage19 space K3  -> h16,
Stage20 Euler K3  -> h32.
```

This is a substantially sharper bridge than the earlier statement that both marginals are merely K3 covers with the same physical polarization.

## 4. Source consistency checks

### K_c

Testa--Stoll independently prove that the smooth `K_c` has geometric Picard rank `20`. A K3 has `b2=22`, so its transcendental l-adic part is two-dimensional. The exact trace regression leaves precisely the two-dimensional `h32` part after the displayed rank-20 algebraic character term.

### K_a

Testa--Stoll relate `K_a` and `K_c` after an explicit field extension. Horie--Yamauchi prove

```text
V_h8 ~= chi_2 tensor V_h32.
```

This makes the `K_a -> h8` exact trace pattern structurally consistent with the known quotient geometry rather than an isolated numerical coincidence.

### K_b

The `K_b` exact traces isolate `h16` with algebraic trace `p*(15+5 chi_-1)`. At completely split primes the algebraic multiplicity is 20, again matching the singular-K3 pattern. A separate global Picard/Galois proof for `K_b` is not silently assumed here.

## 5. Certification boundary

Finite equality of Frobenius traces at 14 primes is not by itself a proof that the global l-adic representations are isomorphic. The fresh audit must determine which of the following is justified:

```text
A. R29-L3 fully discharged from source quotient action + exact trace identification;
B. R29-L3 reduced to a short CM/Faltings/Sturm-bound style global-identification adapter;
C. keep the assignment as exact finite-prime evidence only.
```

No choice is self-awarded by this main-lane submission.

## 6. Project-level meaning

In plain terms, the three kinds of K3 that appeared separately in the cuboid geometry now line up with the three modular signals in the full endpoint L-function. If audit promotes the identification, Stage19, Stage20 and the full Stage29 endpoint stop being three unrelated geometric descriptions: their non-algebraic Frobenius pieces become explicitly connected.

```text
R29_L3=PASS_CANDIDATE
STAGE19_TO_H16=PASS_CANDIDATE
STAGE20_TO_H32=PASS_CANDIDATE
KA_TO_H8=PASS_CANDIDATE
GLOBAL_GALOIS_ISOMORPHISM_SELF_CERTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
```
