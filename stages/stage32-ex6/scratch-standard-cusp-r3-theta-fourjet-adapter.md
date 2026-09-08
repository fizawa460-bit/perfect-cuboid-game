# Stage32EX6 scratch — standard-cusp r3 theta four-jet adapter

Status: `SCRATCH_EXACT_BOUNDED_STANDARD_CUSP_R3_THETA_FOURJET_ADAPTER_NO_ENDPOINT_CREDIT`

Scratch only.  This corrects/refines the preceding rank-3 ruling leaf.  It does
not update `MAIN-STATE`, exclude O266, authorize O264 descent, or create Stage32
MAIN / hostile-audit credit.

## Source locks

Retained/repo side:

- PR #1715 retained EX6 head inspected for this batch:
  `e722b1774134486e2d1eb34ca5f2284d9f5d27d8`;
- AN local A1 note:
  `stages/stage32/residual-32-01-production/post1648an-a1-strict-transform-delta-feasibility-source-note.md`;
- preceding scratch leaf:
  `stages/stage32-ex6/scratch-rank3-fibration-ruling-fourjet-adapter-wall.md`.

External exact formulas used:

- E. Freitag, R. Salvati Manni, *Parametrization of the box variety by theta
  functions*, Michigan Math. J. 65 (2016), 675--691; arXiv:1303.6495.
  Theorem 2.4 identifies the box coordinates with products of Jacobi theta
  functions, and Proposition 2.5 uses
  `p=exp(2*pi*i*z/8)`, `q=exp(2*pi*i*w/8)` at the standard `(infinity,infinity)`
  singular cusp.
- M. Stoll, D. Testa, *The surface parametrizing cuboids*, arXiv:1009.0388.
  The six rank-three quadrics are `q_j=a_j^2+b_j^2-c^2` and
  `r_j=a_1^2+a_2^2+a_3^2-a_j^2-b_j^2`.

Verifier:

`stages/stage32-ex6/scratch_verify_standard_cusp_rank3_theta_fourjet.py`

## 1. Correction: the standard modular cusp lies on the r3 base block

Use the coordinate identification

`a_j=W_j`, `b_j=Z_j`, `c=C`.

At `p=q=0`, the theta formulas give projectively

`(W1,W2,W3,Z1,Z2,Z3,C)=(0,0,1,1,1,0,1)`.

Hence the standard cusp lies in the singular locus of

`r3 = a1^2+a2^2-b3^2 = W1^2+W2^2-Z3^2`,

not in the singular locus of the representative `q1=a1^2+b1^2-c^2` used in
the preceding scratch leaf.

The preceding `q1` cone algebra remains valid for its own rank-three block, but
it is not the direct modular `(p,q)` standard-cusp chart.  The direct AN/theta
adapter must therefore be computed on `r3`.

## 2. Exact global ruling parameter on r3

Factor the rank-three cone over `Q(i)`:

`(W1+i*W2)(W1-i*W2)=Z3^2`.

Choose the ruling parameter aligned with the AN slope `u=q/p`:

`T=(W1+i*W2)/Z3`.

Freitag--Salvati Manni Theorem 2.4 gives

`W1+i*W2 = 2*theta00(2z)*theta10(2w)`

and

`Z3 = theta10(z)*theta10(w)`.

Therefore exactly

`T = 2*theta00(2z)*theta10(2w)/(theta10(z)*theta10(w))`.

## 3. Fourth-order transition in the AN A1 chart

With

`p=exp(2*pi*i*z/8)`, `q=exp(2*pi*i*w/8)`,

Jacobi's defining series give, to the first load-bearing orders,

`theta00(2z)=1+2*p^8+O(p^32)`,

`theta10(z)=2*p+2*p^9+O(p^25)`,

`theta10(2w)=2*q^2+O(q^18)`,

`theta10(w)=2*q+2*q^9+O(q^25)`.

Put

`u=q/p`.

Then direct formal division gives

`T = u + u*(1-u^8)*p^8 + O(p^16)`.

On the quotient A1 chart AN uses

`x=p^2`, `y=p*q`, `z=q^2`, `u=y/x=q/p`.

Thus the exact ambient fourth-jet relation is

`T = u + u*(1-u^8)*x^4 + O(x^8)`.

This resolves the previously missing standard-cusp AN-to-rank3 slope adapter
through normal order four.

## 4. Branch coefficient transport

For an FSM-minimal resolved branch write

`u(x)=lambda+c1*x+c2*x^2+c3*x^3+c4*x^4+O(x^5)`

with finite nonzero `lambda`.

Substitution into the ambient relation yields

`T(x)=lambda
      +c1*x+c2*x^2+c3*x^3
      +(c4+lambda*(1-lambda^8))*x^4
      +O(x^5)`.

Therefore, if `d_k` are the rank-three ruling coefficients,

`d1=c1`, `d2=c2`, `d3=c3`,

and exactly

`d4=c4+lambda*(1-lambda^8)`.

Consequences:

- rank3-four-flatness is equivalent, through this standard-cusp chart, to
  `c1=c2=c3=0` and
  `c4=-lambda*(1-lambda^8)`;
- AN four-flatness `c1=c2=c3=c4=0` implies rank3-four-flatness **iff**
  `lambda^8=1`;
- if AN four-flatness holds and `lambda^8 != 1`, then
  `T-T(lambda)` has exact order four, so the global rank-three fibration consumes
  exactly three RH ramification units at that branch;
- if AN four-flatness holds and `lambda^8=1`, then the local degree is at least
  five and the RH cost is at least four.

Hence AN four-flatness, if obtained independently, has a universal rank-three RH
cost at least three, not four.  The fourth unit requires the special landing
condition `lambda^8=1` (or an independent fifth-order vanishing input).

## 5. Endpoint consequence

This is a genuine improvement over `AN_TO_RANK3_SLOPE_FOURJET_ADAPTER=UNTESTED`:
the standard-cusp adapter is now explicit and replayable.

It does **not** close O266 because the preceding formal-neighborhood leaf did not
prove AN four-flatness at any required population of branches.  Nor is there a
retained theorem forcing `lambda^8=1` for the minimal landing values.

Even conditionally, charging only the universal three RH units per AN-four-flat
branch is weaker than the previous hypothetical four-unit capacity count.  No
new eta/rho cap follows merely from this adapter.

The remaining load-bearing possibilities are now sharper:

1. prove AN four-flatness for a sufficiently large V6 branch population;
2. prove a finite landing restriction, especially `lambda^8=1`, on a sufficiently
   large population;
3. transport this exact standard-cusp formula under the pinned automorphism action
   and materialize the 48/48 node-to-six-rank3-block adapter;
4. extract a fixed V6 member equation/jet relation that prescribes `c4` relative
   to `lambda*(1-lambda^8)`.

## Canonical scratch decisions

- `STANDARD_MODULAR_CUSP_RANK3_BLOCK = r3`
- `STANDARD_CUSP_GLOBAL_RULING_PARAMETER = (W1+iW2)/Z3`
- `AN_TO_STANDARD_R3_FOURJET_ADAPTER = EXACT`
- `T_MINUS_U_FOURTH_TERM = u*(1-u^8)*x^4`
- `RANK3_D4 = c4+lambda*(1-lambda^8)`
- `AN_FOURFLAT_IMPLIES_RANK3_FOURFLAT_IFF_LAMBDA8_EQ_1 = true`
- `AN_FOURFLAT_UNIVERSAL_RANK3_RH_COST_MINIMUM = 3`
- `LAMBDA8_EQ_1_FOR_V6_MINIMAL_LANDINGS = UNTESTED`
- `AN_FOURFLAT_REQUIRED_POPULATION_PROVED = false`
- `EXC_TO_SIX_RANK3_BLOCK_ADAPTER_48_OF_48 = UNMATERIALIZED`
- `INDEPENDENT_ETA_RHO_CAP_OBTAINED = false`
- `O266_ENDPOINT_EXCLUDED = false`
- `O264_DESCENT_AUTHORIZED = false`

## Firewalls

- The theta calculation is a local/formal adapter, not a global V6 member.
- Standard-cusp exactness is not silently promoted to a numbered 48/48 adapter.
- No independence of branch conditions is assumed.
- No hostile-audit, retained consolidation, Stage32 MAIN, endpoint, lower-O, or
  Perfect Cuboid credit follows.
