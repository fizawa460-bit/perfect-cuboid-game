# SR-STR-019 ChatGPT pre-Work external-search follow-up

Date: 2026-08-19  
Baseline: PR #1146.

```text
DIRECT_FULL_TARGET_THEOREM_COUNT=0
CHATGPT_SEARCH_VERDICT=ESCALATE_TO_WORK
ARSENAL_PROMOTION=NO
CARD_STATUS_CHANGE=NO
KEY_NEW_LEAD=Zehavi joint distribution of pairs of polynomial-congruence roots
NARROWED_GAP=joint roots + nested divisor allocation + every-principal-cell pointwise uniformity
```

## Frozen receiver

The repo target is a first moment over each retained fixed-E primitive rectangle/cell with

```text
t_p | m^circ,
t_q | m^circ,
f | t_p t_q,
```

plus two simultaneous moving quadratic-root congruence conditions and the already-frozen core/parity/coprimality/endpoint masks. Repo-side witness multiplicity is already `B^{o(1)}`, so the live problem is this first moment itself rather than a new second-moment support conversion.

## Search result

No published theorem was found that simultaneously preserves all three defining features:

1. nested divisors from the same parent `m^circ`;
2. two simultaneous moving quadratic-root congruences;
3. pointwise uniformity for every retained principal cell rather than averaging over the frozen outer variable/modulus family.

The most useful new near result is Zehavi, *On the Joint Distribution of the Roots of Pairs of Polynomial Congruences* (arXiv:2003.13100), Theorem 1.2: it genuinely treats two polynomial-congruence roots jointly. However, its equidistribution is obtained while summing over the modulus and does not retain the nested divisor weight or the fixed-cell quantifier.

Irving, *The Divisor Function in Arithmetic Progressions to Smooth Moduli* (arXiv:1403.8031), supplies strong pointwise individual-modulus/class divisor-AP control for smooth squarefree moduli, but only for a standard divisor function in one progression. Grimmelt–Merikoski supplies strong factorable-modulus divisor-AP technology but with averaging/almost-all features incompatible with the frozen every-cell receiver. Frei–Sofos supplies primitive-lattice binary-form divisor sums and moving character weights, but no theorem preserving the exact three-layer nesting `t_p,t_q | m^circ`, `f | t_p t_q` together with both moving root conditions. Ngo remains a one-root near miss.

## Narrowed missing adapter

```text
NestedDivisorJointQuadraticRootsEveryCellAdapter
```

A plausible route would expand the two root indicators into additive/character sums and reduce the nested divisor allocation to a multilinear Kloosterman/divisor form. What is not published in the checked sources is the uniform estimate that simultaneously:

- preserves the common parent `m^circ`;
- keeps the moving target `N=t_p t_q` rather than replacing it by a fixed residue;
- keeps `f | N`;
- controls every fixed `(E,x,y,U,V,K_*)` principal cell with a fixed-power gain or exponent-full lower bound.

## Focused Work handoff

Do not repeat the literature census for Ngo 2107.13301, Grimmelt–Merikoski 2508.17979, Irving 1403.8031, Nguyen divisor-AP papers, Shparlinski restricted-divisor AP, Zehavi 2003.13100, Frei–Sofos 1609.04002, Bettin 1701.06608, or recent one-root modular-square-root bilinear papers.

Test only the exact missing step: after expanding the two quadratic congruence indicators, can the resulting nested divisor/Kloosterman multilinear form be controlled **pointwise** in every retained principal cell with currently published complete/incomplete-sum estimates while preserving `t_p,t_q | m^circ` and `f | t_p t_q`?

Acceptable outputs are a uniform exponent-full lower bound, a uniform fixed-power upper deficit, or a rigorous parameter dichotomy. Averaging over the frozen outer variables/cells is forbidden. If no published theorem closes the form, state the first exact multilinear estimate that is missing, with modulus/length ranges and required saving.

## Firewall

No direct theorem or exact adapter was found; SR-STR-019 remains an external gate.