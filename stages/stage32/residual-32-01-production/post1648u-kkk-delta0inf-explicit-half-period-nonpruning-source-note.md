# Stage32 post1648U scratch source note — KKK explicit delta_0inf half-period is still nonpruning

This leaf is scratch-only and grants no MAIN or arithmetic credit.

Klein–Kokotov–Korotkin, Math. Z. 261 (2009), §3.2.4, equations (3.39)–(3.44), use the Burnside/Bolza model
`y^2 = z(z^4-1)` and the canonical cycle basis shown in their Fig. 6 (specialized to `r=i`). Their named
automorphism `mu1: z -> i*z` fixes the two Weierstrass branch points `0` and `infinity`, and equation (3.43)
gives the integral action of `mu1` on the ordered cycle basis `(b1,b2,a1,a2)`.

The displayed matrix acts on the cycle basis; coordinate columns therefore transform by its transpose. Modulo 2
that coordinate action has fixed subspace
`{(0,0,0,0),(0,0,1,1)}`.
The divisor class `delta_0inf=[0-infinity]` is nonzero 2-torsion: twice the difference is principal by the
hyperelliptic coordinate, while the difference itself cannot be principal on a genus-2 curve because that would
give a degree-1 map to `P^1`. Since `mu1` fixes both branch points, `delta_0inf` is fixed by `mu1`. Hence in the
KKK canonical basis its exact mod-2 half-period vector is forced to be

`delta_0inf = (0,0,1,1)` in `(b1,b2,a1,a2)` coordinates.

This avoids a generic/unmarked Thomae invocation: the needed source half-period is extracted from the named
branch points and the exact KKK homology action itself.

The post1648N 48-element polarized period-lattice isomorphism torsor is then replayed. The explicit source vector
`(0,0,1,1)` maps to the three retained nonzero W-lines with multiplicities

- `L1=(0,0,1,0)`: 16,
- `L2=(0,0,0,1)`: 16,
- `L3=(0,0,1,1)`: 16.

Thus the source-side branch-point -> half-period marking is now explicit, but it still does not choose one target
marked ppav isomorphism or one absolute retained W-line. The remaining load-bearing datum must be target-side
non-inner-conjugacy-invariant marking, or an actual source-bound marked ppav isomorphism.
