# Stage32 post1648AN — A1 strict-transform delta adapter and simultaneous-feasibility wall

Scratch-only local adapter and bounded wall. This leaf asks whether the currently extracted V6 branchwise FSM constraints, the AM Beauville ramification bound, the exact exceptional mass vector, and the required genus defect `472` are already mutually inconsistent. They are not: an exact local/combinatorial feasibility witness exists. This does not construct a global V6 carrier.

## Parent lock

- AM source-lock certificate: `stages/stage32/residual-32-01-production/post1648am-beauville-fibration-picard-source-lock.json`
- AM canonical SHA256: `184debdb65c679242fadcc1e1ca176faf720c651b67f09368bc45c14dabb44c8`
- AM finalized scratch head: `a09446f18019cc866e5303bdc352710a9831a36b`
- AM dedicated CI: run `34086680869`, job `101631945753`, SUCCESS.

AM source-locks the unordered Beauville projection degrees `{81,105}` and therefore the necessary bounds `r>=210`, node-preimages `>=210`, branch excess `>=163`, and at least `19` multibranch surface nodes.

## Sources

### FSM cusp parametrization

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691, DOI `10.1307/mmj/1480734014`.

Author preprint:
`https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`

In the proof of Theorem 3.1, printed pp.10–11, a branch approaching a cusp is written

`alpha(tau) = tau*(a1,a2) + (Phi1(Q),Phi2(Q))`, `Q=exp(2*pi*i*tau)`,

with `a1,a2>0`, `a1 == a2 == 0 mod 4`, and `a1+a2 == 0 mod 8`.

Near the standard box node the invariant coordinates are

`x=p^2`, `y=pq`, `z=q^2`, `xz=y^2`.

Put

`A=a1/4`, `B=a2/4`.

Then `A,B` are positive integers and `A+B` is even, while along the normalized branch

`ord_Q(x)=A`,
`ord_Q(y)=(A+B)/2`,
`ord_Q(z)=B`.

### Delta invariant

Hong Duc Nguyen, *Invariants of plane curve singularities and Plücker formulas in positive characteristic*, Annales de l'Institut Fourier 66 (2016), 2047–2066, DOI `10.5802/aif.3057`.

We use only the characteristic-zero standard identities recalled there: for a reduced plane curve singularity with `r` branches, `mu=2*delta-r+1`; equivalently, for a unibranch plane singularity `delta=mu/2`. We also use the standard decomposition of delta into branch deltas plus pairwise intersection multiplicities; in particular, smooth branches at distinct points on the resolved surface contribute no local delta to one another.

## A1 branch-to-resolution adapter

Suppose first `A<=B`. On the `x`-chart of the blowup resolving `xz=y^2`, write

`y=x*u`, `z=x*u^2`.

Along the branch,

`ord_Q(x)=A`,
`ord_Q(u)=(B-A)/2` when `A<B`.

Hence the strict transform intersects the exceptional curve `x=0` with multiplicity exactly `A`. If `A<B`, it lands at the distinguished point `u=0`. If `A=B`, then `u` tends to a nonzero constant `lambda` determined by the leading unit ratio and the branch lands at the point `u=lambda` of the exceptional curve.

The symmetric `z`-chart gives the same conclusion for `A>=B`. Therefore the exact exceptional intersection multiplicity of one FSM branch is

`m=min(A,B)`.

The resolved Beauville double cover is ramified on that normalization branch exactly when `m` is odd, as in AL.

For the FSM-minimal cusp type `(a1,a2)=(4,4)`, one has `(A,B)=(1,1)`, so `m=1`. Its strict transform is smooth and transverse to the exceptional curve. The branchwise FSM exponents do not fix its nonzero exceptional landing coordinate `lambda`.

An explicit invariant-coordinate germ realizing any such landing point is

`gamma_lambda(t): (x,y,z)=(t, lambda*t, lambda^2*t)`,

which satisfies `xz=y^2`, has invariant orders `(1,1,1)`, and after resolution meets the exceptional curve transversely at `u=lambda`.

Thus several minimal branches over the same box node may be assigned pairwise distinct `lambda` values and then become pairwise disjoint after resolution. Their noninjectivity on the singular box surface need not produce any delta contribution on the strict transform.

## Exact simultaneous-feasibility witness for the V6 exceptional vector

Let `M_i` be the 48 exact V6 exceptional pairings, whose sum is `266`, with positive support `47`.

At each met node `i`, choose exactly `M_i` minimal branches `gamma_lambda` with pairwise distinct nonzero `lambda` values on that node's exceptional curve.

This realizes, purely locally:

- exact exceptional mass `M_i` at every one of the 48 nodes;
- total normalization preimages over surface nodes `266`;
- every branch has odd exceptional multiplicity `1`, so Beauville ramification count `r=266`;
- all `266` branches are FSM-minimal `(4,4)`, so the AI/AJ minimum of at least `47` minimal branches is satisfied;
- exactly the `38` positive nodes with `M_i>1` are multibranch, so the AM minimum `19` is satisfied;
- branch excess is `266-47=219`, above the AM minimum `163`;
- every strict-transform branch is smooth at the exceptional divisor and all are separated there, so the forced delta contribution on the exceptional locus is exactly `0`.

This is a compatibility witness for the extracted local/scalar constraints, not a global algebraic curve.

## The remaining genus defect can be local away from the exceptional locus

The V6 arithmetic genus is `473`; a hypothetical normalization genus `1` requires total strict-transform delta

`sum_P delta_P = 472`.

The exceptional-locus witness above consumes none of this budget. The scalar delta budget itself can be realized analytically at one smooth point of the ambient resolved surface by the irreducible plane branch

`v^2 = u^945`.

It is unibranch because `gcd(2,945)=1`. Its Milnor algebra is

`C[[u,v]]/(u^944,v)`,

of dimension `944`; hence `mu=944` and `delta=mu/2=472`.

Therefore the numerical requirement `sum delta_P=472` is compatible with the branchwise FSM/AM exceptional data at the level of local analytic singularity budgets.

Again, this does not assert that a member of the V6 global linear system with these germs exists.

## Exact bounded conclusion

The conjunction

- exact V6 exceptional vector, total mass `266`;
- branchwise FSM cusp lattice conditions;
- at least `47` FSM-minimal branches;
- AM `{n1,n2}={81,105}`;
- Beauville ramification `r>=210`;
- node-preimages `>=210`;
- at least `19` multibranch nodes;
- strict-transform genus defect `472`

is not contradictory by itself.

Consequently `exceptional mass 266`, node-preimage counts, multibranch counts, and the scalar identity `sum delta=472` cannot be combined without an additional global or tangent-identification input to exclude V6.

A productive next interface must constrain at least one of:

1. exceptional landing parameters/tangent coincidences, forcing strict-transform branches to meet after resolution;
2. the possible smooth-locus singularity delta of members of the V6 linear system (jet separation, polar/contact, or fibration constraints);
3. a global coupling between the two genus-5 fibrations and the singularity/conductor divisor.

## Firewalls

- This is a bounded feasibility wall, not a V6 existence result.
- No global member of `|V6|` is constructed.
- `Q602_excluded=false`.
- `O210_excluded=false`.
- `O212_plus_advance_allowed=false`.
- shared `MAIN-STATE.json` and Stage32 authority remain unchanged.
- no receiver, route, theorem, endpoint, or perfect-cuboid credit.
