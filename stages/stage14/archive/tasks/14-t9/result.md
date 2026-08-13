# Stage14-t9 — Euclid-parameter sparse-residue family sieve target

## Purpose

Stage14-t8 reduced the genuinely new reflected local gate to primes

\[
p\mid\Delta_-:=S^2-X^2,\qquad p\equiv1\pmod4,
\]

and, at such a prime, to the two exceptional residues

\[
q^2\equiv-1\pmod p.
\]

This stage converts that statement into the exact family-level sieve target needed for the triple correction. It deliberately does **not** assume that the physical small point `q` is equidistributed modulo moving primes.

## Sparse residue size

For every odd prime `p`:

- if `p == 3 (mod 4)`, `q^2=-1 (mod p)` has no solutions;
- if `p == 1 (mod 4)`, it has exactly two residue classes.

Hence the exceptional residue density among `q mod p` is exactly

\[
\rho_p=\frac{2}{p}
\]

for split primes and zero for inert primes.

The reflected obstruction is therefore not a fixed positive-density sieve. It is a moving thin-residue sieve whose formal local mass is governed by sums of `2/p` over split prime divisors of `Delta_-`.

## Correct family object

Let `F` range over primitive oriented Pythagorean bases and let `Q(F;B)` denote the raw-activated physical small points in the Stage14 height window. The triple candidates are contained in

\[
\{(F,q):q\in Q(F;B),\ q^2\equiv-1\pmod p\text{ for every reflected prime at which the nonunit branch is entered}\}.
\]

The phrase "for every" is intentionally conditional on the actual local branch of the reflected quartic; t8 proved that unit branches pass automatically.

Thus the theorem needed is a **joint family estimate** over `(F,q)`, not a count of bases alone and not a single-fiber rational-point bound.

## Relation to Stage14-s5

Stage14-s5 identified the raw activation bottleneck as a Pythagorean 2-descent large sieve with a physical small-point window. Stage14-t adds one extra layer:

1. raw activation / descent-solubility on the moving support `p|2SXH`;
2. reflected split-prime divisors `p|Delta_-`;
3. exceptional two-class condition `q^2=-1 mod p` when the reflected nonunit branch occurs.

Accordingly, a sufficient theorem for the t-track would give a saving in the joint weighted count

\[
\sum_F\sum_{q\in Q(F;B)}\prod_{\substack{p\mid\Delta_-(F)\\p\equiv1(4)}} w_p(F,q),
\]

where `w_p` records the exact reflected local-solubility condition and is supported on at most the two exceptional classes in the nonunit case.

No independence product `prod(1-2/p)` is asserted. Proving such a product law, or even a weaker averaged character cancellation sufficient for a logarithmic saving after raw activation, is the next analytic task.

## Boundary

```text
STAGE14_T9=COMPLETE_EUCLID_SPARSE_RESIDUE_SIEVE_FORMULATION
REFLECTED_NEW_PRIMES=p|Delta_minus
INERT_PRIMES_AUTOMATIC=true
SPLIT_PRIME_EXCEPTIONAL_RESIDUES=2
EXCEPTIONAL_RESIDUE_DENSITY=2/p
FIXED_POSITIVE_DENSITY_SIEVE=false
INDEPENDENCE_PRODUCT_ASSUMED=false
JOINT_BASE_POINT_FAMILY_THEOREM_REQUIRED=true
RAW_STAGE14_S5_SIEVE_IMPORTED_AS_FIRST_LAYER=true
T_O_SQRT_B_PROVED=false
NEXT=Stage14-t10 derive a character-sum / large-sieve formulation for the joint raw+reflected local conditions
```
