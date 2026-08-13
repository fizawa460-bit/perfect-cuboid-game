# Stage14-tH1 — Gaussian primary / ray-class normalization

## Purpose

Stage14-tH0 established an independent support track which may advance without waiting for the live t route.  Stage14-tH1 now freezes the Gaussian arithmetic conventions needed by every later tH spectral or large-sieve tool.

The minimum imported t interface remains merged Stage14-t32.  No t34-or-later identity is required here.

The goal is to remove recurring ambiguity from

- Gaussian associates and primary generators;
- the ramified prime above 2;
- orientation of split rational primes;
- arbitrary-order residue characters at split prime ideals;
- unit corrections in the passage from residue characters to ideal/ray-class characters;
- conductor bookkeeping under CRT composition.

No Stage14 power saving is claimed in this stage.

---

## 1. The ramified prime and primary normalization

Write

\[
\varpi=1+i,
\qquad (2)=(-i)\varpi^2.
\]

For every nonzero Gaussian integer `alpha` with odd norm, exactly one of its four associates

\[
\{\alpha,-\alpha,i\alpha,-i\alpha\}
\]

satisfies

\[
\boxed{\alpha^{\rm pr}\equiv1\pmod{\varpi^3}.}
\tag{H1.1}
\]

Call it the **primary associate**.

The uniqueness is elementary: the four units represent the four units of
`Z[i]/(varpi^3)`, whose norm is 8 and whose unit group has order 4.

Primary normalization is multiplicative.  If `alpha_pr` and `beta_pr` are primary, then

\[
\alpha^{\rm pr}\beta^{\rm pr}\equiv1\pmod{\varpi^3},
\]

so

\[
\boxed{(\alpha\beta)^{\rm pr}=\alpha^{\rm pr}\beta^{\rm pr}.}
\tag{H1.2}
\]

Because `Z[i]` has class number one, every odd nonzero ideal therefore has a unique primary generator.

This is the canonical generator convention used by all later tH stages.

```text
GAUSSIAN_PRIMARY_MODULUS=(1+i)^3
ODD_GAUSSIAN_IDEAL_HAS_UNIQUE_PRIMARY_GENERATOR=true
PRIMARY_NORMALIZATION_MULTIPLICATIVE=true
```

---

## 2. Oriented split prime ideals

Let

\[
p\equiv1\pmod4
\]

be a rational prime and choose a primitive root `g mod p`.  Put

\[
\iota=g^{(p-1)/4}\pmod p,
\qquad \iota^2\equiv-1\pmod p.
\]

The two oriented Gaussian prime ideals above `p` are encoded by

\[
\boxed{
\mathfrak l_{p,+}=(p,i-\iota),
\qquad
\mathfrak l_{p,-}=(p,i+\iota).
}
\tag{H1.3}
\]

Equivalently, if `rho in {+1,-1}` then the residue embedding sends

\[
i\longmapsto \iota_\rho=g^{\rho(p-1)/4}.
\]

Conjugation changes only the orientation:

\[
\overline{\mathfrak l_{p,\rho}}=\mathfrak l_{p,-\rho}.
\]

The machine key for an oriented split prime is therefore

```text
GaussianPrimeKey = (p, rho),   rho in {+1,-1}.
```

This separates rational-prime data from the Gaussian orientation state and avoids silently identifying conjugate prime ideals.

---

## 3. Arbitrary-order local residue characters

For one oriented split prime `mathfrak l_(p,rho)`, identify its residue field with `F_p` through the chosen orientation.  For

\[
j\in\mathbf Z/(p-1)\mathbf Z,
\]

define the multiplicative residue character `psi_(p,rho,j)` by

\[
\psi(g)=\exp\!\left(\frac{2\pi i j}{p-1}\right).
\]

Its exact order is

\[
\boxed{
\operatorname{ord}(\psi)
=\frac{p-1}{\gcd(j,p-1)}
}
\tag{H1.4}
\]

for `j!=0`, with order one for `j=0`.

No quadratic-only assumption is made.  The local character key is

```text
LocalCharKey = (p, rho, j mod p-1).
```

This is deliberately compatible with the higher-order Mellin modes observed by merged t33, but t33 is not a dependency of the construction.

---

## 4. Unit signature: the entire 2-adic correction is four-state

Under the oriented embedding,

\[
i\mapsto g^{\rho(p-1)/4}.
\]

Hence

\[
\boxed{
\psi_{p,\rho,j}(i)=i^{\rho j}.
}
\tag{H1.5}
\]

Define the local **unit signature**

\[
s(p,\rho,j)=\rho j\pmod4.
\]

For a finite CRT product of local characters, define

\[
\boxed{
J=\sum_{\mathfrak l}s(p,\rho,j)\pmod4.
}
\tag{H1.6}
\]

Then the whole product character satisfies

\[
\Psi(i)=i^J,
\qquad
\Psi(-1)=(-1)^J.
\]

Thus every unit ambiguity in the later Hecke/ray-class lift is compressed to one element

```text
J in Z/4Z.
```

Conjugating one prime ideal changes its contribution from `j` to `-j mod 4`.

```text
UNIT_CORRECTION_STATE_COUNT=4
CONJUGATE_ORIENTATION_FLIPS_UNIT_SIGNATURE=true
```

---

## 5. Exact 2-adic conductor exponent

Let

\[
U_e=\{u\in\{\pm1,\pm i\}:u\equiv1\pmod{\varpi^e}\}.
\]

Directly,

\[
U_0=U_1=\{\pm1,\pm i\},
\qquad
U_2=\{\pm1\},
\qquad
U_3=\{1\}.
\tag{H1.7}
\]

Therefore a product residue character with total signature `J` becomes well-defined on ideal classes modulo the odd modulus times `varpi^e` exactly when it is trivial on `U_e`.

The minimal ramified exponent is

\[
\boxed{
e_2(J)=
\begin{cases}
0,&J\equiv0\pmod4,\\
2,&J\equiv2\pmod4,\\
3,&J\equiv1,3\pmod4.
\end{cases}
}
\tag{H1.8}
\]

In particular,

\[
\boxed{e_2=1\text{ is never primitive}.}
\tag{H1.9}
\]

This is the principal reusable output of tH1: later stages never need to redo the Gaussian unit correction prime by prime.

---

## 6. Exact conductor of a finite CRT product

Take finitely many distinct oriented split prime ideals and local character indices

\[
(\mathfrak l_r,j_r).
\]

Omit every trivial local character `j_r=0` and put

\[
\mathfrak q_{\rm odd}
=\prod_{j_r\ne0}\mathfrak l_r.
\]

Distinct Gaussian prime ideals are coprime, including the two conjugate primes over the same rational split prime, so CRT gives the odd character uniquely.

Using the unique primary generator of each odd ideal, the character lifts multiplicatively to an ideal/ray-class character.  Its primitive conductor is

\[
\boxed{
\mathfrak f
=\varpi^{e_2(J)}\mathfrak q_{\rm odd}.
}
\tag{H1.10}
\]

Consequently its conductor norm is

\[
\boxed{
N\mathfrak f
=2^{e_2(J)}
\prod_{j_r\ne0}p_r,
}
\tag{H1.11}
\]

where a rational prime appears twice if both conjugate prime ideals above it occur nontrivially.

The proof of exactness is local:

- a nontrivial residue character at `mathfrak l_r` cannot lose that odd prime from its conductor;
- the only remaining ambiguity is multiplication of a principal generator by a Gaussian unit;
- (H1.7) gives the exact minimal power of `varpi` required to kill that ambiguity.

Thus conductor bookkeeping is additive/multiplicative except for the four-state unit signature, which is combined by addition modulo four.

```text
ODD_CONDUCTOR_IS_PRODUCT_OF_NONTRIVIAL_ORIENTED_PRIMES=true
TWO_ADIC_CONDUCTOR_EXPONENT_VALUES=0,2,3
TWO_ADIC_CONDUCTOR_EXPONENT_ONE_OCCURS=false
CONDUCTOR_NORM=2^e2*PRODUCT_ACTIVE_RATIONAL_PRIMES
CRT_UNIT_SIGNATURE_ADDS_MOD_4=true
```

---

## 7. Canonical downstream data structure

Later tH stages should pass character families using the following normalized record rather than ad hoc Gaussian generators:

```text
GaussianRayCharacter:
  local_factors:
    - p: rational split prime
      rho: +1 or -1
      j: integer modulo p-1
      order: (p-1)/gcd(j,p-1)
  unit_signature_J: sum(rho*j) mod 4
  two_adic_conductor_exponent: e2(J) in {0,2,3}
  odd_conductor_prime_ideals: local factors with j != 0
  conductor_norm: 2^e2 * product(p over active factors)
```

The actual primitive generator chosen for an odd ideal is always the unique element congruent to one modulo `(1+i)^3`; it need not be carried as extra character-family state.

This removes unit/associate duplication before hyperbola or large-sieve bookkeeping begins.

---

## 8. Deterministic audit

The dedicated tH1 audit freezes:

```text
odd Gaussian elements checked for unique primary associate    1200
primary multiplicativity checks                              40000

unit subgroup sizes U_0,U_1,U_2,U_3                          4,4,2,1

split rational primes audited
5,13,17,29,37,41,53,61,73,89,97

oriented Gaussian prime ideals checked                          22
local arbitrary-order characters checked                      1008
maximum sampled character order                                 96

local e2 counts
0 -> 252
2 -> 252
3 -> 504

CRT two-factor cases checked                                  63888
CRT e2 counts
0 -> 15972
2 -> 15972
3 -> 31944
```

Every CRT case independently recomputes the minimal ramified exponent from the unit subgroups and matches (H1.8).

---

## 9. Interaction with the live t route

This stage does not wait for t34 or any later t result.

If t later supplies a concrete all-character spectral family, tH1 offers a ready-made normalization:

```text
raw residue modes
 -> oriented split-prime keys
 -> local j indices
 -> total unit signature J mod 4
 -> exact primitive conductor
 -> primary-generator ideal character.
```

If t changes its live spectral object, the tH1 infrastructure remains valid for any finite product of multiplicative residue characters at split Gaussian prime ideals.

---

## 10. Proof boundary

Stage14-tH1 closes algebraic normalization only.

It does not prove a character-family large sieve or a norm-index power saving.

```text
ALL_ORDER_GAUSSIAN_RAY_CLASS_NORMALIZATION_PROVED=true
UNIQUE_PRIMARY_GENERATOR_CONVENTION_FROZEN=true
EXACT_UNIT_SIGNATURE_COMPOSITION_PROVED=true
EXACT_TWO_ADIC_CONDUCTOR_EXPONENT_PROVED=true
EXACT_FINITE_CRT_CONDUCTOR_FORMULA_PROVED=true
ALL_CHARACTER_MELLIN_HECKE_LARGE_SIEVE_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
```

---

## Boundary

```text
STAGE14_TH1=COMPLETE_GAUSSIAN_PRIMARY_RAY_CLASS_AND_CONDUCTOR_NORMALIZATION
TH_MINIMUM_FROZEN_T_INPUT=Stage14-t32
TH_REQUIRES_FUTURE_T_RESULT=false
PRIMARY_MODULUS=(1+i)^3
ODD_GAUSSIAN_IDEAL_HAS_UNIQUE_PRIMARY_GENERATOR=true
PRIMARY_NORMALIZATION_MULTIPLICATIVE=true
ORIENTED_SPLIT_PRIME_KEY=(p,rho)
LOCAL_CHARACTER_KEY=(p,rho,j_mod_p_minus_1)
ARBITRARY_LOCAL_CHARACTER_ORDER_SUPPORTED=true
UNIT_SIGNATURE=rho*j_mod_4
GLOBAL_UNIT_SIGNATURE=sum_unit_signatures_mod_4
TWO_ADIC_CONDUCTOR_EXPONENT_J0=0
TWO_ADIC_CONDUCTOR_EXPONENT_J2=2
TWO_ADIC_CONDUCTOR_EXPONENT_J1_OR_J3=3
TWO_ADIC_CONDUCTOR_EXPONENT_ONE_OCCURS=false
ODD_CONDUCTOR_IS_PRODUCT_OF_NONTRIVIAL_ORIENTED_PRIMES=true
EXACT_CRT_CONDUCTOR_NORM_FORMULA=true
ALL_CHARACTER_MELLIN_HECKE_LARGE_SIEVE_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH2
```
