# Stage29-02c-LG2 — finite search contract

## Population

Integral curves `C` on the smooth cuboid surface `S` whose image on the canonical model is nonexceptional and whose normalization map to the image is bijective.

Two audited genus windows are considered:

```text
G0: geometric genus 0, even canonical degree d<=176
G1: geometric genus 1, even canonical degree d<=192
```

The degree bound is inherited from audited PR #1292. The even-degree condition is inherited from audited Stage29-02a/Testa--Stoll Picard geometry.

## Exact lattice encoding

Let `H=K_S`, so `H^2=16`, and let `d=H.C`. Define

```text
r=gcd(d,16)
m=16/r
n=d/r
y=m*C-n*H.
```

Then `y` is integral and `H.y=0`.

The inverse reconstruction is exact:

```text
C=(y+nH)/m,
```

subject to the Picard divisibility congruence.

For genus zero, adjunction and `p_a>=0` give

```text
C^2>=-d-2,
-y^2<=m^2*(d^2/16+d+2).
```

For genus one, `p_a>=1` gives

```text
C^2>=-d,
-y^2<=m^2*(d^2/16+d).
```

Since `H^perp` is negative definite, each degree produces finitely many possible `y`, hence finitely many numerical Picard classes `C`.

## Necessary filters

Every candidate must pass all applicable conditions:

1. exact degree and Picard congruence;
2. adjunction lower bound;
3. nonnegative intersection with every known irreducible curve not equal to the candidate;
4. exceptional-divisor incidence lower bounds from Testa--Stoll Lemma 21;
5. automorphism-orbit deduplication;
6. known degree-<=6 classification subtraction;
7. real/positive/nondegenerate physical-chamber compatibility where the class has an explicit carrier;
8. bijective-normalization hypothesis.

These filters do not by themselves certify effectivity.

## Completion criterion

`R29-LG2` is discharged only if a finite computation produces a complete orbit list of every numerical class in both windows, and every survivor is then either:

- proved ineffective;
- represented only by a known boundary/degenerate curve;
- or promoted to an explicit effective carrier for separate arithmetic analysis.

A numerical class with unknown effectivity is not a closed case.

## Separate multibranch firewall

Freitag--Salvati Manni Theorem 3.1 requires the normalization map to the singular curve to be bijective. Curves with multiple normalization points above a singular point are outside the theorem and outside this finite degree cap.

```text
UNIBRANCH_WINDOW_COMPLETE_IMPLIES_ALL_LOW_GENUS_COMPLETE=false
MULTIBRANCH_LEDGER_REQUIRED=true
ISOLATED_RATIONAL_POINTS_EXCLUDED=false
```
