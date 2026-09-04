# Stage32 post-1550 principal-b3 relative-V4 torsor normalizer

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, `Q=602`, after hostile-audited and merged #1550.

This leaf tests one exact re-entry condition left open by #1550:

> Does the principal Bolza automorphism `b3` normalize the source-locked relative-V4 cover `Z=X(8) -> C0=Z/H`, and hence lift diagonally to the ambient relative torsor `X=(Z x Z)/H_diag`?

The answer is **yes at the ambient relative-V4 torsor level**, and this still does not prove equivariance of the hypothetical carrier `Y` or the correspondence `Gamma`.

## Exact retained inputs

The hostile-audited retained F2^4 adapter uses the ordered basis

`(e1,e2,r*e1,r*e2)`

of `J(C0)[2]` and identifies the V4 character plane as

`W = span_F2{(0,0,1,0),(0,0,0,1)} = ker(r mod 2)`.

The hostile-audited single-`b3` reduction gives, in that same ordered basis,

`b3_mod2 = [[1,1,0,0],[1,0,0,0],[0,0,1,1],[0,0,1,0]]`.

Therefore `W` is invariant. The restriction to `W` is

`B = [[1,1],[1,0]]`,

with `det(B)=1` over `F2` and `B^3=I`. In particular,

`b3(W)=W`.

This conclusion is coordinate-exact because both the definition of `W` and the `b3` matrix are locked to the same retained basis. No arbitrary symplectic change of basis is used.

## Torsor consequence

The retained relative-V4 asset identifies

`Z -> C0`

as a connected finite-etale `H ~= F2^2` torsor and

`W=image(H^* -> H^1(C0,F2))`

as its character plane. For an elementary abelian 2-cover, pullback by an automorphism of the base sends the character plane to its pullback image. Thus `b3(W)=W` means that `b3^*Z` is isomorphic to `Z` after the induced automorphism `A` of `H`.

Equivalently, one can choose a lift

`tilde_b3: Z -> Z`

covering `b3` and satisfying the semilinear deck relation

`tilde_b3(z*h)=tilde_b3(z)*A(h)`.

Using the same lift on both factors,

`(tilde_b3,tilde_b3): Z x Z -> Z x Z`

normalizes the diagonal subgroup `H_diag`, since `(h,h)` is sent to `(A(h),A(h))`. Hence it descends to an automorphism

`beta_X: X=(Z x Z)/H_diag -> X`

covering `b3 x b3` on `C0 x C0`.

So the exact ambient quotient-normalizer/lift gate is positive:

`B3_NORMALIZES_RETAINED_V4_CHARACTER_PLANE=true`

`DIAGONAL_B3_LIFT_TO_RELATIVE_V4_TORSOR_X=true`.

## Why this still does not prove the needed commutator

The carrier-information boundary remains unchanged: retained Stage32 data does not contain an actual equation or exact intrinsic model for the hypothetical carrier normalization `Y`.

Therefore the ambient lift `beta_X` does **not** by itself prove any of:

- `beta_X(Y)=Y`;
- existence of an intrinsic `beta:Y->Y` with `f1 o beta=b3 o f1` and `f2 o beta=b3 o f2`;
- `(b3 x b3)^* Gamma = Gamma`;
- `[T,b3]=0` for `T=(f1)_*(f2)^*`.

This is precisely the semantic distinction required by #1550: ambient quotient-normalizer data is useful only if it is connected by an exact source-locked bridge to the actual carrier/correspondence.

## Decision / firewall

Promote only the ambient normalizer fact:

`RETAINED_V4_TORSOR_B3_NORMALIZER = PASS_EXACT_AMBIENT`.

The next exact re-entry condition is now narrower:

`PROVE_CARRIER_OR_CORRESPONDENCE_INVARIANCE_UNDER_THE_AMBIENT_B3_LIFT`.

Do **not** infer:

- actual `[T,b3]=0` or `[T,b3]!=0`;
- intrinsic carrier `b3` equivariance;
- correspondence/divisor invariance;
- unconditional `Q(T)!=602`;
- exclusion of `O210`;
- authorization of `O212+`;
- effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit.

The Stage32 controller remains unchanged.
