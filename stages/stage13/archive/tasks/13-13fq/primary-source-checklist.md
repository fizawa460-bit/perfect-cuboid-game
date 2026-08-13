# Stage13-13fq — primary-source checklist

This checklist separates literal source facts from Stage13 deductions.

## Huang--Liu--Rudnick, §2.1

Source: B. Huang, J. Liu, Z. Rudnick, *Gaussian primes in almost all narrow sectors*, arXiv:1903.04005, §2.1.

Source facts used:

```text
Xi_k(a)=(alpha/bar(alpha))^(2k)=e^(i4k theta_a)
k != 0 => L(s,Xi_k) entire
xi(s,k)=pi^(-(s+2|k|))*Gamma(s+2|k|)*L(s,Xi_k)
xi(s,k)=xi(1-s,k)
```

Stage13 deduction:

```text
m=8*ell -> k_HLR=2*ell -> gamma shift=4*ell.
```

## Merikoski, §2.7

Source: J. Merikoski, *On Gaussian primes in sparse sets*, Compositio Math. 161 (2025), §2.7.

Source facts used:

```text
xi_j(z)=(z/|z|)^j=e^(ij arg z)
chi ranges over dual((Z[i]/u Z[i])^x)
L(s,xi_j chi) is the Gaussian Hecke L-family attached to these residue twists
```

Merikoski's Landau--Page statement further records that any exceptional zero in the indicated near-one region must occur with angular index `j=0`.

Stage13 deductions:

```text
Xi_{2ell}=xi_{8ell}.
The fixed-S Gaussian Fourier twists are members of Merikoski's finite-residue Hecke family after enlarging one fixed modulus u_S if necessary.
The zero-free lemma is not used in the contour argument.
```

## Classical Hecke continuation / functional equation

Source boundary: E. Hecke, *Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen*, Math. Z. 1 (1918), 357--376; II, Math. Z. 6 (1920), 11--51.

Imported classical fact:

```text
a primitive nontrivial Hecke character has analytic continuation with its Hecke functional equation;
the pole at s=1 belongs only to the trivial character.
```

Stage13 deductions:

```text
a finite-order residue/ray-class character has zero infinity type;
therefore Xi_{2ell}*omega retains nonzero infinity type for ell>=1 and is nontrivial;
the finite twist changes the finite conductor/root number but not the 4*ell gamma shift;
imprimitive twists differ from primitive inducing twists by finitely many Euler factors.
```

## Strip growth

The polynomial strip bound is not imported as a separate theorem. It is derived internally from:

```text
right-boundary absolute convergence
+ primitive Hecke functional equation
+ fixed-conductor factor for fixed S
+ Stirling on a fixed strip
+ Phragmen--Lindelof.
```

Hence the proof requires no Gaussian zero-free region and no theorem uniform in a modulus growing with `B`.

```text
PRIMARY_SOURCE_FAMILY_MATCH_COMPLETE=true
SOURCE_FACTS_AND_INTERNAL_DEDUCTIONS_SEPARATED=true
HLR_TO_MERIKOSKI_INDEX_TRANSLATION_EXPLICIT=true
FIXED_TWIST_ANALYTIC_CONTRACT_PRIMARY_BOUNDARY_EXPLICIT=true
```
