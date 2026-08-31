# Stage32-21aa — anti-fixed coset penalty representation

Status: `CLOSED_CHECKPOINTED`

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

## Exact CI checkpoint

Workflow: `Stage32 Reynolds anti-fixed coset penalty`

- run: `33307921980`
- job: `99247655675`
- verdict: `PASS_STAGE32_21AA_ANTI_FIXED_COSET_PENALTY_REPRESENTATION`
- projection classes: `16384`
- zero-penalty classes: `1`
- positive-penalty classes: `16383`
- distinct penalty values: `23`
- minimum positive penalty: `1/572`
- maximum coordinate-Cauchy penalty: `5/39`
- canonical penalty-stream SHA256: `8bd09aa4a7e942b7bb772815a05475d04604985556325203dec0851437c0c76e`
- canonical certificate SHA256: `f5e6e363fa2c8f2258e340054948319aae2ad805bd2ca5412f8e3a76231e0238`
- artifact: `9731071290`
- artifact ZIP SHA256: `e0c683d2343f1cb6ff212c606d1f28db1e20fd54c27429bf46b38bd82fe203f7`
- artifact size: `1799` bytes

The full 16384-class table is not stored as an artifact; it is deterministically regenerated from retained exact sources and committed by the penalty-stream hash.

## Safety / credit

- no legacy prefix DFS re-arm;
- no 256M/512M/1B heavy production;
- no terminal-family materialization;
- no 59-dimensional CVP;
- `lambda(r)>0` alone is not a prune until compared with projected self-intersection slack;
- numerical row completion remains false;
- theorem / receiver / route / perfect-cuboid credit remain false.

This closure is an exact representation checkpoint only. It does not release downstream mathematical credit beyond the explicit finite interface.

## Next leaf

`32-21ab — EXACT_QUOTIENT_CLASS_MAP`

Derive the exact map from the rank-2 projected Smith affine coordinates to the `16384` Reynolds projection classes so the certified anti-fixed penalty can be attached to each projected candidate without materializing the terminal family.
