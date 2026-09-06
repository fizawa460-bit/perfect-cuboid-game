# Stage32 post1648Z scratch source note — full KKK Bolza homology marking still does not select the retained ppav conjugator

This leaf is scratch-only and grants no MAIN or arithmetic credit.

## External source

C. Klein, A. Kokotov, D. Korotkin, *Extremal properties of the determinant of the Laplacian in the Bergman metric on the moduli space of genus two Riemann surfaces*, Math. Z. 261 (2009), 73–108, DOI 10.1007/s00209-008-0314-9.

Exact locators used: §3.2.4, equations (3.39)–(3.44), especially (3.40)–(3.43).

For the Burnside/Bolza curve `y^2=z(z^4-1)` the source fixes the same canonical cycle basis used by post1648N/U and gives three explicit curve generators

- `mu1: z -> i*z`,
- `mu2: z -> (z+1)/(z-1)`,
- `mu3: z -> -1/z`,

with exact integral actions on `(b1,b2,a1,a2)^t`:

`T_mu1 = [[0,-1,1,-1],[0,1,0,1],[-1,1,-1,1],[-1,-1,0,0]]`,

`T_mu2 = [[-1,0,0,0],[1,1,0,0],[0,1,-1,1],[-1,0,0,1]]`,

`T_mu3 = [[0,1,0,0],[1,0,0,0],[0,0,0,1],[0,0,1,0]]`.

As in post1648N, coordinate columns transform by the transpose of these displayed cycle-action matrices.

## Exact replay against the retained target

Reconstruct the exhaustive 48 polarized period-lattice isomorphisms from post1648N. For each isomorphism `M`, conjugate all three source coordinate actions by `M`.

All 48 triples land in the retained order-48 group `G12=<S=b4,T=-b3>`. The 48 maps produce exactly 24 distinct ordered triples, each with multiplicity 2. Equivalently, the full marked source `mu1,mu2,mu3` representation still leaves the central `±I` ambiguity and moves through one simultaneous target inner-conjugacy orbit.

The source-bound half-period `delta_0inf=(0,0,1,1)` from post1648U remains distributed among retained W-lines with multiplicities `L1:L2:L3 = 16:16:16`.

Thus adding the *entire* KKK integral homology representation is stronger than the previous `mu1`-only replay but still does not provide the missing non-conjugacy-invariant target marking. It is source-side data only. A genuinely resolving source must additionally bind one of these named curve generators/branch labels to a specific retained lattice word, target half-characteristic, or an actual integral ppav isomorphism.

This is a bounded closure of the route “use more KKK source-side Bolza generators to determine the missing g”. It does not claim that no external source contains such a two-sided marking.
