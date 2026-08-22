# Stage29-15 — current literature refresh

Date: 2026-08-22.

This refresh supplements, rather than replaces, the audited Stage14 Arsenal and StructureRadar corpus. Search absence is not a novelty claim.

## A. Surface Chabauty / higher-dimensional Chabauty

### Caro–Pasten

- J. Caro, H. Pasten, *A Chabauty–Coleman bound for surfaces*, Invent. Math. 234 (2023), 1197–1250, DOI 10.1007/s00222-023-01217-1; arXiv:2102.01055.
- The theorem concerns hyperbolic surfaces embedded in abelian varieties of sufficiently small Mordell–Weil rank.
- Exact Stage29 verdict: `NONAPPLICABLE_TO_FULL_ENDPOINT_BY_ALBANESE_ZERO`. The smooth endpoint resolution has `q=0`, hence trivial Albanese, so it admits no nonconstant morphism to an abelian variety.

### Balakrishnan–Caro

- J. S. Balakrishnan, J. Caro, *A refined Chabauty--Coleman bound for surfaces*, arXiv:2501.03483 (2025).
- Refines the method for `W_2=C+C` in a genus-3 Jacobian.
- Exact Stage29 verdict: `NONAPPLICABLE_TO_FULL_ENDPOINT`; useful only if a future auxiliary surface satisfies the abelian-embedding hypotheses.

## B. Curve-level rational-point methods

A 2025 article in *INTEGERS* gives an explicit rank-zero elliptic-quotient strategy for genus-3 curves and notes the same principle for higher-genus curves with suitable quotient data. This theorem species is valid and useful, but it is not a new endpoint mechanism: 29-13 already used the same rank-zero quotient logic for Saunderson.

Classical Chabauty-Coleman, elliptic Chabauty, Mordell-Weil sieve and quadratic/bielliptic quadratic Chabauty remain legitimate tools for individual Q-defined genus-2/3/5 receivers once exact rank/Selmer/reconstruction data are supplied. They do not by themselves give uniform closure over the infinite parameter bases in `R29-FIB2` or `R29-PESCH2`.

## C. K3 arithmetic

### Tawfik–Newton

- M. A. Tawfik, R. Newton, *Transcendental Brauer–Manin obstructions on singular K3 surfaces*, Research in Number Theory 11 (2025), article 16.
- Computes odd transcendental Brauer groups and obstructions for specified CM Kummer surfaces `Kum(E x E')`.
- Stage29 verdict: `APPLICABLE_AFTER_EXACT_ADAPTER`. No coordinate-sign cuboid quotient is currently identified with the exact required CM Kummer model together with the physical image locus and evaluation maps.

### Martínez-Marín

- J. Martínez-Marín, *Rational points on K3 surfaces of degree 2*, Acta Arithmetica 223 (2026), 153–166, DOI 10.4064/aa250529-15-10.
- Gives extension-degree bounds for infinite rational points and explicit Q-families with infinitely many Q-rational points.
- Stage29 verdict: background/non-emptiness direction, not an endpoint obstruction.

### Bartsch

- F. Bartsch, *New examples of geometrically special varieties: K3 surfaces, Enriques surfaces, and algebraic groups*, Manuscripta Math. 177 (2026), article 31.
- Shows elliptic K3 surfaces are geometrically special over function fields.
- Stage29 verdict: structural background; it reinforces that elliptic-K3 geometry should not be equated with Q-point emptiness.

## D. Campedelli / involutions

The load-bearing geometric involution literature already consumed in 29-11 remains Calabri–Mendes Lopes–Pardini and Mendes Lopes–Pardini–Reid. A fresh search finds later work using the rational/Enriques quotient classification for Bloch/zero-cycle questions, but no general arithmetic theorem forcing Q-point emptiness on the exact cuboid Campedelli Q-forms.

Verdict: no new receiver discharge; `R29-CAMP3` remains adapter-gated.

## E. Beauville twists

- T. Browning, S. Chan, *Almost all quadratic twists of an elliptic curve have no integral points*, J. Eur. Math. Soc., online 17 Sep 2025, DOI 10.4171/JEMS/1704.
- Strong statistical twist theorem, with a stated conditional component for partial 2-torsion.
- Stage29 verdict: `NONAPPLICABLE` as a direct Beauville closure. The endpoint requires every physically relevant twist to be controlled at rational-point level, or a finite twist reduction; “almost all” integral-point emptiness does not supply that.

## F. Modular / congruence curves

Existing `X(8)` twist constructions, including Chen's families of mod-8-congruent elliptic curves, remain structural evidence that relevant twists can carry rational points. Fresh searching found no 2025–2026 uniform theorem eliminating the sigma-twisted arithmetic defect classes in `Q11-MODULAR`, and no source discharging `R29-KUM5`.

## G. Local/sieve/counting

The refreshed literature does not change the already-audited boundary:

- ambient/toric/thin-set estimates can produce sparsity/counting once exact height and measure adapters exist;
- StructureRadar's Gaussian-Hecke, separated-character and same-measure correlation cards retain their exact transfer firewalls;
- none converts the Stage29 local data into a theorem that the endpoint adelic/rational locus is empty.

`R29-KUM-LOC3` therefore remains an exact physical-height/measure adapter gate.

## H. Refresh conclusion

```text
FRESH_GLOBAL_ENDPOINT_CLOSURE_FOUND=false
FRESH_INDIVIDUAL_CURVE_TOOL_SPECIES_FOUND=true
FRESH_FULL_ENDPOINT_SURFACE_CHABAUTY_NONAPPLICABILITY_CERTIFIED=true
FRESH_CUBOID_K3_BRAUER_OBSTRUCTION_FOUND=false
FRESH_UNIFORM_BEAUVILLE_TWIST_CLOSURE_FOUND=false
FRESH_MODULAR_DEFECT_CLASS_ELIMINATION_FOUND=false
FRESH_PESCH_E1_THEOREM_FOUND=false
SEARCH_ABSENCE_IS_NOVELTY_CLAIM=false
```
