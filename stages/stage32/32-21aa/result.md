# Stage32-21aa — anti-fixed coset penalty representation

Status: `AWAITING_EXACT_CI`

## Target

Restore a rigorous finite piece of the information lost by the Reynolds fixed projection without materializing the 27-digit terminal family and without solving a 59-dimensional closest-vector problem.

Write `P=N/64`, `p=P(x)`, and `q=x-p` for an integral Picard class `x`. The locked Reynolds facts give:

- `P` is a Gram-self-adjoint idempotent;
- `x=p+q` is Gram-orthogonal;
- `phi(q)=0`;
- the slice kernel is strictly negative definite.

Hence

`x^2 = p^2 + q^2 = p^2 - (-q^2)`

with `-q^2 >= 0`.

## Exact finite representation

The existing exact column-module computation enumerates

`P(Pic_Z) / Pic_Z^G ~= im(N) mod 64`

with exactly `16384` projection classes.

For a canonical projection residue `r = N*x mod 64`, integrality of `x` gives

`q_i = -r_i/64 (mod Z)`

in every retained coordinate.

Choose an exact integral basis `K` of `ker(phi)` and set

`B = -K^T G K`.

`B` is exactly positive definite. For retained coordinate `i`, compute the exact dual norm

`c_i = K_i B^-1 K_i^T`.

Exact Cauchy-Schwarz gives

`-q^2 >= dist(r_i/64,Z)^2 / c_i`.

Taking the maximum over retained coordinates defines a deterministic safe class penalty

`lambda(r) <= -q^2`.

The implementation enumerates all `16384` exact Reynolds projection classes, checks that only the zero class has zero penalty, and emits a compact deterministic certificate plus stream hash. It does **not** store the full class table as an artifact; it is regenerated from retained sources.

## Safety / credit

- no legacy prefix DFS re-arm;
- no 256M/512M/1B heavy production;
- no terminal-family materialization;
- no 59-dimensional CVP;
- `lambda(r)>0` alone is not a prune until compared with projected self-intersection slack;
- numerical row completion remains false;
- theorem / receiver / route / perfect-cuboid credit remain false.

## Execution preflight

This leaf uses one ordinary Ubuntu runner, no matrix, and uploads one compact JSON certificate with 7-day retention. It does not touch a Stage32 heavy run key and cannot overlap as a heavy Stage32 workload.

## Exit criterion

Close 32-21aa only after the exact CI certificate passes and records the class count / positivity / deterministic hashes. Then advance to `32-21ab`, the exact quotient-class map from the rank-2 Smith affine coordinates into the 16384-class penalty state.
