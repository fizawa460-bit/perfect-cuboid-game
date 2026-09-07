# EX1-05E — h=4 modular-factor projection reduction

Status: provisional same-PR candidate. No hostile-audit, Stage32 MAIN, or full-target credit is granted here.

EX1-05D excludes every h=2 component-stabilizer choice, so the live product-cover branch has h=4 only. The missing input is not a new theorem: the fixed V6 class already has source-locked modular-factor degrees 105 and 81. This leaf supplies the exact notation adapter and replays those degrees inside the EX1-05B h=4 geometry rather than inheriting a Stage32 candidate conclusion as authority.

## Notation adapter

The retained fixed-V6 product-cover notes and EX1-05A/05B describe the same tower with different names:

- EX1 `N` is the same normalization `N`;
- EX1 `D` is the retained connected Beauville pullback `Y -> N`;
- EX1 `Ctilde` is the retained connected component `D_old` of the product-cover pullback;
- therefore `h=deg(Ctilde->D)` is the retained `q'`;
- EX1 projection degrees `(alpha,beta)` are the retained `(n1,n2)` for `D_old -> X(8)`;
- EX1 `Q=deg Ram(D->N)` is the retained odd-contact ramification degree `O`.

The source geometry lock is `post1484-v6-modular-factor-bidegree-source-note.md`, blob `deeecac5599f3b542b445cd87c2070dae488bc85`. It proves, for the fixed V6 class rather than for an O=210 specialization, that the two normalization maps to `X(4)` have degrees `105` and `81`. Its transport formula gives `(n1,n2)=(105,81)` when `q'=4`.

This is consistent with EX1-05B: for h=4, `alpha+beta=186`, and `105+81=186`.

## Descend to the genus-2 quotient

EX1-05B has the etale degree-4 quotient `X(8) -> C2=X(8)/G0plus` and the etale degree-4 map `Ctilde -> D`. Hence in either factor commuting square

`4*deg(D->C2)=4*deg(Ctilde->X(8))`.

So the two descended projection degrees `D -> C2` are exactly `105` and `81`.

Since `g(C2)=2` and `Q=2g(D)-2`, Riemann--Hurwitz gives

- `R_105 = Q - 2*105 = Q-210`;
- `R_81  = Q - 2*81  = Q-162`.

Both ramification degrees are nonnegative. Therefore the first projection forces

`Q >= 210`.

EX1-05B already gives `Q` even and `186 <= Q <= 266`. Thus the h=4 residual ledger is reduced from 41 even values to the 29 values

`Q = 210,212,...,266`.

Write `Q=210+2r`, `0<=r<=28`. Then

- `R_105=2r`;
- `R_81=48+2r`;
- old slack `s=(Q-186)/2` satisfies `s=12+r`;
- `R_105+R_81=48+4r=4s=2Q-372`, exactly replaying the EX1-05B conservation law.

## Contact/parity sharpening

The 48 V6 exceptional pairings have 26 odd nodes of total mass 140 and 21 positive even nodes of total mass 126. Since the odd nodes can contribute at most 140 to `Q`, the refined `Q>=210` wall forces at least 70 ramification units onto even-pairing nodes. The seven largest positive even masses are needed to reach that capacity, so every surviving h=4 profile has at least 33 ramified surface nodes (`26+7`), improving the prior lower bound 30.

Similarly, relative to the parity baseline `Q=26`, the required extra ramification is at least `184`. Sorting the exact node capacities `m_i-(m_i mod 2)`, the largest 18 sum to less than 184 while the largest 19 reach 184. Hence every surviving h=4 profile has at least 19 multibranch nodes, improving the prior lower bound 15.

For the parameter `r`, the exact contact slack becomes

- contact half-excess `(266-Q)/2 = 28-r`;
- non-simple contact branches `<=28-r`;
- simple transverse contact branches `>=182+3r`.

The JSON artifact stores replay arrays for all 29 `r` states, including the statewise ramified-node and multibranch-node lower bounds.

## Boundary and next route

This leaf excludes only `Q=186..208` inside the already-forced h=4 branch. It does not dispose the 29 states with `Q>=210`, does not identify projection ramification with intrinsic curve delta, and does not prove existence or nonexistence of a V6 genus-1 member.

The older Stage32 source note also records a stronger extremal `Q=210` contact histogram using a local cusp/projection-ramification adapter. EX1-05E deliberately does **not** import that histogram yet. The next route is to source-lock that local adapter in EX1 notation and determine how `R_105` and `R_81` distribute over the exact node/contact ledger.

Next route: `EX1-05F_H4_PROJECTION_RAMIFICATION_TO_LOCAL_CONTACT_COUPLING`.