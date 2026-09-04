# Stage33 33-12 V71/V73/V77 J1 source / column-3 repair micro-roadmap

```text
ROLE=PLANNING_AND_EXECUTION_CHECKLIST_ONLY
LIVE_GLOBAL_AUTHORITY=stages/stage33/controller.json
BRANCH_EXACT_FRONTIER=stages/stage33/33-12/e3-b1-c22-j1-xalpha-kernel-correction-v77.json
CURRENT_LOCKED_FRONTIER=V61_THROUGH_V77_WITH_V65_V69_V75_HISTORICAL_SUPERSESSION
EFFECTIVE_DISCOVERY_ROUTING=V58_ARSENAL_FIRST_REPEATABLE_BOUNDED_SEARCH_NO_FIXED_CAP
CURRENT_LEAF=D4_REPAIR_LITERAL_LAMBDA_A_TO_PROPER14_COLUMN3_AFTER_J1_XALPHA_ZERO
ATOMICITY_RULE=ONE_SMALL_VERIFIABLE_GOAL_PER_COMMIT
MERGE_ALLOWED=false
```

This roadmap supersedes the V75 D2.2 minimum-norm leaf. Exact certificates, controller firewalls, and `MAIN-STATE.json` remain authoritative over prose.

## Locked frontier

- V61-V64 fix the B1 source basis, literal `lambda_A={f_A,g22}`, `kappa_A=J1`, `kappa_D=J2`, and the retained J2 proper14/marked-Kc route.
- V65 historically reduced J1 to two **nonzero** marked-Kc candidates `u2=[0,1]` and `u1+u2=[1,1]`. V68-V69 then reduced their transport to shear versus identity. These remain historical exact reductions under their nonzero-J1 premise.
- V71 constructs the literal nonzero J1 E[2]-valued cocycle from `(f1,1)`, with splitting field `Kgeom(sqrt(f1))` and `rho_f1 -> Tr`.
- V73 materializes the direct semilinear quartic torsor from that same E[2] cocycle.
- V75 proves its degree-two quotient is `d`-independent and records why blindly transplanting the J2 full-kernel conclusion was not justified under the then-active V65 premise.
- V77 wires in the older exact `xalpha_pair_galois_repair.py`: the Möbius-section / `s=1` x-alpha difference is exactly `J1`, `J1_in_xalpha_image_exact=true`, and the geometric Brauer quotient has basis `{J2,q1}`. Therefore the named source J1 is **zero in the geometric Brauer/Ogg-Shafarevich quotient**.
- Consequently V71 remains a nonzero E[2] Kummer-boundary cocycle, but its image in `H^1(Kgeom,E)` is zero. V73's smooth projective torsor is the trivial OS class. Its transcendental lattice is `T(Kc)=<4>+<8>` with minimum norm `4`; this `4` is the zero-class kernel and must **not** be read as `u2`.
- The degree-two quotient pullback `T(Kc)(2)=<8>+<16>` is compatible: it has index `2` inside the trivial torsor lattice `T(Kc)`.
- Thus the V65/V69 nonzero J1 marked-Kc orientation gate and V75 4-vs-12 next contract are superseded for the actual J1 Brauer/OS image. J2 -> u1 authority is unchanged.
- Stage33 remains `6/11`; Stage33-12 is open; Stage33-13 is unreleased; merge is forbidden.

## Arsenal routing

Use `docs/arsenal/index.json` first. Current cards:
- `S33-PW04` — primary exact marked-source / Picard-adjoint binding firewall for the repaired column-3 route;
- `S33-PW07` — retain only as the source/cocycle/torsor/Brauer-layer firewall. Do not revive the old nonzero J1 kernel discriminator.

Historical contact/Weil pairing and identity-vs-shear data are not an active decision gate after V77.

## D2.1 — literal J1 E[2] torsor — PASS V73, retained

The exact quartic remains:

```text
d=f1=(t-r1)/(t-r4)
d*V^2 = N^4 - 2*a*d*N^2*Z^2 + d^2*q^2*Z^4
```

V77 changes only its cohomological interpretation: nonzero in `H^1(E[2])`, zero after passage to the geometric Brauer/Ogg-Shafarevich class.

## D2.2 — minimum-norm discriminator — RETIRED V77

Historical nonzero-kernel lookup:
- `u2` -> minimum norm `4`;
- `u1` -> minimum norm `8`;
- `u1+u2` -> minimum norm `12`.

For J1, V77 gives the **zero** class, whose kernel is all of `T(Kc)` and also has minimum norm `4`. Therefore `4 -> u2` is invalid here. No identity/shear selection is made.

## D4 — repair marked proper14 column 3 — CURRENT

The retained literal object is V63:

```text
kappa_A = J1 = [P_r1-P_r4]
f_A=(t-r1)/(t-r4)
lambda_A=alpha({f_A,g22})
```

V57 defines the exact branch route

`Phi_B1 : H1(C21_tilde disjoint_union C22_tilde,F2) -> Br(Kc_tilde_bar)[2]`.

The next atomic question is now source-bound and finite:

**Is V63 `lambda_A` / `Phi_B1(kappa_A)` exactly the same geometric Brauer quotient class called `J1` in the locked x-alpha repair?**

Acceptance:
- source-lock the identification of V61/V63 `f_A=(t-r1)/(t-r4)` with the x-alpha `J1` generator;
- source-lock that the CV x-alpha quotient and V57 `Phi_B1` codomain are the same geometric `Br(Kc_tilde_bar)[2]` layer;
- if yes, materialize proper14 column 3 as the zero vector/mask `0` and explain that the literal H2(mu2) lift can be Picard/Kummer even when its Brauer image is zero;
- if that codomain identification is not source-locked, stop at the exact missing adapter. Do not infer column3=0 merely from name equality.

Do **not** route through a nonzero marked-Kc coordinate for J1.

## D5 — finish B1 14x4 and mask20 solve

Blocked until D4 and the conjugate columns are exact. Once all four columns are exact, solve `M*x=mask20` over F2 and only then consider B1-route membership credit.

## Firewalls

Forbidden: direct identification of contact `(L,R)` with marked Kc bits; arbitrary GL2 complement; choosing identity/shear; interpreting J1 minimum norm `4` as `u2`; reviving V65's nonzero-J1 premise without defeating the exact x-alpha relation; setting proper14 column3 to zero without an exact same-codomain/source crosswalk; search-miss-to-absence promotion; merge/closure/receiver/endpoint/theorem/perfect-cuboid credit.

## Batch rule

Each `stage33main batch` works the first unfinished leaf, uses Arsenal first, constructs/replays one exact object per commit, and reevaluates this roadmap.
