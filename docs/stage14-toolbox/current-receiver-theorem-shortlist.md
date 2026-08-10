# Stage14 theorem-source shortlist for current receivers

This note applies the receiver-ready certificate from toolbox-ar. Similar vocabulary is not compatibility: a candidate must preserve the current coefficient space, physical labels, scale, centering and selector before it may be imported.

## Verdict classes

- `DIRECT`: all hypotheses are already certified and the quoted output closes the live receiver.
- `ADAPTER_NEEDED`: the theorem shape is promising, but one explicit exact adapter is missing.
- `STRUCTURAL_ONLY`: useful for local geometry or proof design, but it cannot currently yield the requested estimate.
- `REJECT`: application would be circular or would discard a required physical structure.

No candidate below is `DIRECT`.

## S receiver: LargeSwitchPrimitivePythagoreanTwoLegIncidence

The live positive pair retains `(H0,L0,W0,K_switch,K_agree,xi0)`, the primitive parameters `(m,n)`, and the original physical lift. It requires a fixed-power saving for the lift count, not merely a count of bare primitive Pythagorean triples.

| source family | verdict | useful feature | missing exact adapter / rejection |
|---|---|---|---|
| Wilson, Jacobi bilinear forms over hyperbolic regions | `ADAPTER_NEEDED` | cancellation is compatible with product cutoffs and variables away from axes | prove a bounded-multiplicity map from physical lifts to separated squarefree Jacobi coefficients, with `K_switch divides m^2+n^2` and `xi0 divides W0` retained |
| quadratic large sieve / quadratic Hecke families | `ADAPTER_NEEDED` | can average genuine quadratic-character families | produce coefficients before squareclass collapse and prove their L2 energy independently; using the collision energy itself is circular |
| Gaussian spin / Dirichlet-symbol bilinear machinery | `STRUCTURAL_ONLY` | indicates what a separated reciprocity kernel would look like | no exact statewise Gaussian-symbol factorization exists for the positive Pythagorean lift |
| divisor bounds for primitive Pythagorean triples | `STRUCTURAL_ONLY` | controls allocations after a triple is fixed by `B^o(1)` | does not control how many physical lifts land on the same `(m,n)` |
| row/column or one-leg estimates | `REJECT` | none sufficient globally | they discard the two-leg correlation and may suffer a polynomial Latin-square loss |

### Minimal S adapter certificate

A later stage may promote the Wilson/large-sieve route only after proving all of:

1. an exact pre-collapse kernel on the physical lift;
2. bounded or near-linear lift multiplicity into its coefficient labels;
3. squarefree/coprimality and away-from-axes hypotheses uniformly on the endpoint shell;
4. a quantitative theorem output giving `B^{-delta}` after all dyadic and divisor refinements;
5. no use of the unknown same-`(xi,k)` collision energy as input coefficient energy.

Until then the recommended route is direct integer/bilinear geometry in s7-20.

## Fixed-U receiver: SharedUInvisibleCenteredProjectiveSelectorDispersion

The live sum retains fixed primitive `U`, moving canonical `pi`, primitive `V`, moving `delta`, the hyperbola, branch, interval, canonical and reconstruction masks, and the centered physical selector. Complete `P1 x P1` trace cancellation has already been proved; only transfer to the sparse arithmetic selector remains.

| source family | verdict | useful feature | missing exact adapter / rejection |
|---|---|---|---|
| Ping Xi, bilinear forms with trace functions over arbitrary sets | `ADAPTER_NEEDED` | genuine two-variable sparse-support cancellation for certified trace sheaves over one finite field | certify the Stage14 kernel as a bounded-conductor non-exceptional one-field sheaf and transfer the two-prime, divisor-coupled selector to admissible supports with the required energy bounds |
| Wilson, Jacobi forms over hyperbolic regions | `ADAPTER_NEEDED` | handles a product cutoff once the kernel is a genuine Jacobi symbol | prove an exact separated Jacobi-symbol identity uniform in `U`, branch and masks; tH15 currently says none is known |
| Goldmakher--Louvel quadratic large sieve over number fields | `REJECT` for post-collapse use; `ADAPTER_NEEDED` pre-collapse | valid quadratic Hecke-family averaging | post-squareclass coefficients have L2 energy `E_U`, making the proof circular; a non-circular pre-collapse Hecke family is not constructed |
| Friedlander--Iwaniec Gaussian symbol machinery | `REJECT` direct; `STRUCTURAL_ONLY` | model for reciprocity and separated Gaussian coefficients | moving `V` and modulus-dependent rotations destroy the required coefficient separation |
| K3 / genus-one fiber bounds | `STRUCTURAL_ONLY` | explains both one-variable slices and exceptional loci | fiberwise bounds do not control the total bivariate physical incidence |
| complete finite-field Weil cancellation | `STRUCTURAL_ONLY` | supplies the already closed complete trace | complete box cancellation does not imply centered sparse-selector dispersion |

### Minimal fixed-U adapter certificate

The Ping Xi route may be promoted only after all of:

1. a one-field reduction before the `(p,q)` square and without pair-to-squareclass collapse;
2. bounded-conductor, geometrically non-exceptional sheaf certification uniform in fixed `U` and legal branches;
3. an exact encoding of the physical `(pi,V,delta)` selector into supports to which the theorem applies;
4. support-size/additive-energy or multiplicative-energy hypotheses at the critical balanced height;
5. restoration of the centered two-prime Frobenius energy with no fixed `B^omega`, `omega>0`, loss;
6. separate treatment of the mixed visible branch and all bad-prime masks.

Until then the receiver remains owned by the t line; toolbox supplies only this import gate.

## Routing decision

- S and fixed-U receivers remain independent and may progress in parallel.
- No cross-promotion between their theorem candidates is permitted.
- No additional toolbox-H line is needed: the missing items are receiver-specific construction lemmas, not a shared ambiguity.
- Toolbox main does not wait for those lemmas.
- The unconditional whole-family exponent remains `7/8`.
