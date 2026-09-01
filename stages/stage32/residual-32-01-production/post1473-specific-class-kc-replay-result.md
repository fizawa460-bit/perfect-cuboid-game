# Stage32 post-1473 specific-class K_c replay result

Status: `PROVISIONAL_EXACT_KC_PUSHFORWARD_REPLAY_PASS_NONEXCLUSION`

Scope: the single recovered V6 support-47 class for `g1-d186`, `(d,e,a,u,v)=(186,266,592,-44,32)`, `z=(-15,62,-44,26,32)`. This note carries no FULL178, route, theorem, receiver, endpoint, or perfect-cuboid credit.

## Historical theorem/adaptor input

The source-locked theorem wall remains unchanged at `post1473-specific-class-kc-adapter-wall.md`; the successful replay was executed against that exact historical blob. Do not rewrite that wall and then treat the old run as a replay of the rewritten input.

The replay uses the same exact recovered V6 body:

- Picard coordinates SHA256 `2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726`.
- all140 pairings SHA256 `4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3`.
- `C^2=758`.

Two ordering/hash pitfalls were repaired fail-closed before the successful run:

1. the retained `picard_sign_rows_sha256.c = 65f90a...` is the canonical SHA of the historical `picard-action-sign-c.json` certificate, not a SHA of the bare 64x64 matrix rows; the fresh full Picard matrix is instead required to equal the nonexpiring retained `c` matrix literally;
2. Testa--Stoll's current 48-point enumeration is not identified with the Stage32 all140 exceptional suffix by array index. Each `E_pi` class is mapped to the Stage32 exceptional ordering by a unique exact 64-entry pairing fingerprint against the retained Picard basis, using the same Hperp integral all140 adapter that generated the V6 pairings.

## Successful exact replay

Workflow: `Stage32 post-1473 sigma-c exceptional replay`

- run `33480002342`
- job `99767316051`
- source head `4e7865599de58d184f160d8d779ef2a024216562`
- artifact `9789589785`
- artifact ZIP digest `sha256:4929a3b9a259077bf00b408b9d215b4822d2f6d2059ed67e663cce625a2634ce`
- replay certificate canonical SHA256 `a79b2e57e0b9e7444f3e2756542ac88f84a452a07e293226aa60917603f563b9`
- exact exceptional-order adapter SHA256 `4ce6a020b698a05122f010621b06c2a4d9ab7f9bad811b3d3a96fde1bfedb031`
- `E_pi` count `24`
- `class_sigma_c_invariant = false`
- `P^2 = 6532`
- `(pi_*C)^2 = P^2/2 = 3266`

The exact necessary condition for the non-`sigma_c`-invariant integral geometric-genus-one case is `(pi_*C)^2 >= 0`. The replay gives `3266 > 0`, so this K3 negative-self-intersection test **does not exclude** the V6 support-47 class.

Because the divisor class itself is not `sigma_c`-invariant, an integral divisor in this exact class cannot be an invariant divisor with the same class. The odd-degree invariant-curve branch therefore does not turn this positive-square result into an exclusion of this class.

## Fail-closed interpretation

This result is a successful exact adapter/replay computation but a mathematical nonexclusion:

- it closes the previous technical wall `BLOCKED_MISSING_FULL_PICARD64_SIGMA_C_AND_EPI_REPLAY` for this single V6 class;
- it does **not** prove that an integral irreducible normalization-genus-one carrier exists;
- it does **not** close the fixed-z fiber, FULL178, the general low-genus classification, multibranch, receiver, route, theorem, or endpoint;
- it does **not** authorize further FULL178 production or survivor materialization;
- it does **not** authorize a V7 rerun.

Current safe wall: `KC_PUSHFORWARD_EXACT_NONNEGATIVE_NONEXCLUSION_WALL`.
