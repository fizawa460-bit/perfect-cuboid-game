# MB104 P6E source adapter — Stoll--Testa low-span integral curves

Status: **PUBLISHED-SOURCE ADAPTER / NO CREDIT**

## Source

Michael Stoll and Damiano Testa, *Curves on the surface of cuboids*,
Mathematics of Computation (2026), DOI `10.1090/mcom/4238`.

Immutable computational companion used elsewhere in Stage32:

```
repository = MichaelStollBayreuth/Verification
commit     = 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
path       = Cuboids/cuboids.magma
blob SHA1  = 0422b69847f2afb97cb7b3ed02ebef91279f61b1
```

Only the following published statements are imported here.

## Theorem 15 / degree at most six

On the singular canonical cuboid surface `Sbar` and its minimal resolution `S`:

- all conics are among the known conics;
- there are no smooth rational curves of degree four;
- every integral degree-four curve of arithmetic genus one is among the known genus-one quartics;
- there are no integral curves of degree six;
- curve degrees are even.

The existing P6B exact replay already uses the 32 known conics and all 60 known genus-one degree-four curves.

## Theorem 16 / low projective span

Let `C subset Sbar` be an integral curve.

1. If `C` is contained in a plane, then `C` is a conic.
2. If `C` spans a `P^3`, then `C` is one of the known genus-one degree-four curves.
3. If `C` spans a `P^4`, then `C` has degree eight and is a fiber of one of the 28 Stoll--Testa fibrations. Such an integral fiber is either
   - a smooth canonical curve of genus five, or
   - one of the hyperelliptic genus-three irreducible singular fibers.

In particular, the strict transform on the smooth resolution of any integral curve spanning a `P^4` has arithmetic genus at least three.

## Scope firewall

This note does not classify curves spanning `P^5` or `P^6`; P6E handles those by an independent exact hyperplane-contact certificate.

No claim about effectivity, nefness, MB104 completion, receiver/theorem/endpoint credit, Perfect-Cuboid existence/nonexistence, or merge authorization is imported merely from this source note.
