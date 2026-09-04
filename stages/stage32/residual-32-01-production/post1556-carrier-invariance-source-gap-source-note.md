# Stage32 post-1556 carrier-invariance retained-source gap

Scope: fixed recovered V6 class `g1-d186`, `O=210`, `q'=4`, `Q=602`, after hostile-audited and merged #1556.

The exact next semantic question is whether the descended principal-`b3` automorphism

`beta_B: B -> B`

fixes the hypothetical integral carrier normalization `N`, or equivalently whether one can prove the required correspondence invariance directly.

## Retained positive input

The hostile-audited #1556 leaf proves only the ambient quotient geometry:

- the principal `b3` lift normalizes full `G`;
- the diagonal lift normalizes `G_diag`;
- `beta_B:B->B` and `beta_X:X->X` exist;
- `X->B` is `beta_X/beta_B`-equivariant.

The retained common-double-cover certificate defines the carrier conditionally:

- `N` is the normalization of a hypothetical integral carrier mapping to `B`;
- `Y` is the normalization of `N x_B X`.

The retained V6 modular-factor source note fixes the class-level intersection geometry. In particular, any integral curve in the exact V6 class would have modular factor degrees

`m_z=105`, `m_w=81`.

These are necessary class-level data; they do not select a unique member of the class.

## Exact missing semantic datum

Within this retained source-lock set, no datum identifies the hypothetical carrier by any of the following stronger objects:

- a defining equation or ideal on `B`;
- a distinguished section whose zero divisor is the carrier;
- uniqueness of an integral carrier in the fixed V6 class;
- a source-locked action of `beta_B` on a defining carrier member/section;
- a direct source-locked identity `(b3 x b3)^* Gamma = Gamma`.

Consequently, even if one later proves that `beta_B` preserves the **Picard class**, that alone would only imply that `beta_B(N)` is another member of the same class. Without uniqueness or a fixed defining section, it does not imply

`beta_B(N)=N`.

Therefore the #1556 conditional chain cannot yet be activated:

`beta_B(N)=N => beta_X(Y)=Y => [T,b3]=0 => Q(T)!=602`.

## Arsenal check

Research OS routing was followed through `docs/arsenal/index.json`. The relevant provisional Stage32 card `S32-PW05` is a finite-group equivariant reconstruction pattern. Its contract requires an exact action, proved invariance, and complete orbit coverage, and explicitly grants no semantic/geometric identification merely from reconstructed algebra. It therefore does not supply the missing carrier-member identification.

The controller and exact source locks remain authoritative over this provisional card.

## Decision

Promote only the bounded negative statement:

`RETAINED_INPUT_DOES_NOT_YET_PROVE_CARRIER_OR_GAMMA_INVARIANCE=true`.

Do not promote:

- `beta_B(N)=N`;
- `beta_X(Y)=Y`;
- intrinsic `beta:Y->Y`;
- `(b3 x b3)^* Gamma=Gamma`;
- actual `[T,b3]=0` or `[T,b3]!=0`;
- unconditional `Q(T)!=602`;
- exclusion of `O210`;
- authorization of `O212+`;
- effectivity, FULL178, receiver, route, theorem, endpoint, or perfect-cuboid credit.

The next exact leaf is narrowed to

`SOURCE_LOCK_BETA_B_ACTION_ON_FIXED_V6_CARRIER_MEMBER_OR_DIRECT_GAMMA_IDENTITY`.

The Stage32 controller remains unchanged.
