# 36R-07 preliminary desk review: exact core, limitations, and missing replay (2026-11-10)

**Classification: BOUNDED_DESK_CHECK; NOT HOSTILE PASS.** This report checks named assertions against the original Drive texts archived under [sources](sources/) and the existing GitHub Stage29/Stage36 certified model. It does not promote a proof, close a receiver, complete the repository Cycle Safety Protocol, or supersede the audited `stages/stage36/MAIN-STATE.json`.

## 1. Review outcome by claim

| Claim from Drive | Desk-check verdict | What is and is not verified |
|---|---|---|
| 36R-06 Proposition A: infinitely many rational points on every `C_H` | **Supported from the audited quotient model** | Explicit infinite boundary family and smoothness below. No formal hostile audit credential claimed. |
| 36R-06 Proposition B using `Br(C_H)` | **Supported with the stated compactification Brauer scope** | Does not prove a statement for every class of `Br(U_H)`. |
| 36R-06 Proposition B interpreted as all Brauer–Manin methods on `U_H` | **Scope overclaim / HOLD** | Need an independent `Br(U_H)` ramification/residue calculation; etale-Brauer also unproved. |
| 36R-04 Proposition 3, `Im_U = Im_J ∩ Im_H` over branch-free `A(Q)` | **Finite F2 part PASS** | Every one of ten audited kernels, not merely three representatives; Kummer descent interpretation as in source. |
| 36R-04 Proposition 4, `(T') <=> U(Q)=empty` | **Two polynomial identities PASS; global equivalence HOLD** | Inverse substitutions, sign choices, removed/degenerate charts and complete quantifier bijection need independent replay. |
| 36R-05 `p=53/8`, additional class `(5185,34)` | **Elementary arithmetic PASS; local survival HOLD** | `36R-05_endpoint_selmer.py` / complete replay receipts were not located by Drive filename search. No all-places local witness was reconstructed. |
| 36R-06 provisional parking | **Recorded as external proposal, not formally complete** | Previous candidate-ledger exposure invalidates a genuinely independent blind pass; `B7` and `N5` remain UNTESTED. |

## 2. Proposition A: explicit infinite Q-boundary family

Take coprime positive integers `m>n`, with
```text
a1 = m^2-n^2,  a2 = 2mn,  a3 = 0.
x  = (m^2-n^2)^2, y = (2mn)^2, z = 0,
x+y = (m^2+n^2)^2.
```
The seven branch line values in the GitHub Stage29 model
`x,y,z,x+y,x+z,y+z,x+y+z` are
```text
a1^2, a2^2, 0, (m^2+n^2)^2, a1^2, a2^2, (m^2+n^2)^2.
```
All are squares in Q. The canonical sign cover `Sbar` therefore has a rational point above this base point. Exactly one branch line (`z=0`) passes through it, since `x,y,x+y` are nonzero. The canonical cover is smooth there, and the audited Stage29 adapter says `Sbar -> Cbar_H` is finite etale for **all ten** admissible kernels. Thus its image is a smooth rational point of `Cbar_H` and lifts to the minimal resolution `C_H`. Distinct coprime ratios `m/n` give infinitely many distinct base points and hence infinitely many rational quotient points.

The concrete witness `(a1,a2,a3)=(3,4,0)` has `[x:y:z]=[9:16:0]` and line values `9,16,0,25,9,16,25`. This is **outside** physical `U` because `a3=0`. Therefore **it says nothing about a non-boundary perfect cuboid**.

**Desk conclusion:** A is mathematically well-supported by the already recorded global quotient and local smoothness contracts. The old proposed goal `C_H(Q)=empty` cannot survive if those source contracts are maintained. No receiver theorem or endpoint promotion follows. External hostile audit still needs to certify this interpretation and update the formal goal.

## 3. Proposition B: correct mathematical scope

Let `X=C_H`, `V=U_H`, with smooth rational boundary point `P∈X(Q)\V`. The source's proof uses finiteness of `Br(X)/Br_0(X)`, locally constant Brauer evaluation, and almost-everywhere unramified evaluation to choose adelic points `Q_v∈V(Q_v)` arbitrarily close to `P` at finitely many exceptional places. This yields, subject to those standard hypotheses,
```text
V(A_Q) ∩ X(A_Q)^{Br(X)} != empty.
```
This is the exact claim displayed in 36R-06. It rules out a Brauer–Manin obstruction **using only classes extending to the proper compactification `X`**.

However, there is a potentially strict restriction map
```text
Br(X) -> Br(V).
```
For an open variety, `Br(V)` can have additional ramified classes, which this boundary-point argument does not test. Thus the broad prose conclusion *"Brauer–Manin cannot establish V(Q)=empty"* is **not justified** without showing that those additional classes are harmless or absent. The etale-Brauer extension in 36R-06 is explicitly only a sketch.

**Required correction in any future authoritative Stage36 state:** distinguish `COMPACTIFICATION_BRAUER_OBSTRUCTION_BLOCKED` from `FULL_OPEN_BRAUER_OBSTRUCTION_NOT_YET_EXCLUDED`. Do not automatically demote all `B5`/Brauer variants to permanently BLOCKED from Proposition B alone.

## 4. Proposition 3: exact ten-kernel F2 check

The repo source [36-02 representative inventory](../36-02/representative-inventory.json) encodes three Q-symmetry orbits of sizes `6+2+2=10`. Independently apply all six permutations of the side-index `S3` to the three published 4-vector upstairs kernel bases. Their union contains **ten distinct 16-element F2 subgroups**. With `Gamma=F2^7/<1111111>` and even-weight character space `V` of dimension six, set `g=e_B1+e_B2`. For every one of the ten `H`:

```text
g not in H
dim_F2(V_H)=3
dim_F2(V_J)=5
V_H+V_J=V  (dimension 6)
```

For branch-free base points `P∈A(Q)`, the Kummer criterion is `kappa_P|W=0` iff `P` lifts to the cover belonging to `W`. Hence `P` lifts to both the `J` and the `C_H` covers iff `kappa_P` vanishes on all `V`, i.e. `P` lifts to `S`. This is the precise scope of `Im_U = Im_J ∩ Im_H`. It is **not** a claimed equality of rational point sets or an inverse lift from arbitrary `C_H(Q)`.

The finite computation and exact dimension checks are reproducible with the pure standard-library script [verify_formal_core.py](verify_formal_core.py).

## 5. Proposition 4: exact identities versus full adapter

Let `p=v+u` with `v²-u²=1`, so `u=(p-p^-1)/2`, `v=(p+p^-1)/2`. Set the fiber coordinate `t=a/(d+v)`, `s=a²=4v²t²/(1-t²)²`, `c=(p+1)/(p-1)`. The two identities from Drive 36R-04 check exactly:
```text
(s+1)(1-t²)² = (t²+p²)(t²+p^-2)
(s+u²)(1-t²)² = u² (t²+c²)(t²+c^-2).
```
The verifier clears denominators and tests exact polynomial coefficient identities; there is no floating-point tolerance. The squareclass conditions are therefore consistent on the nondegenerate chart `p != 0,+1,-1`, `t != +1,-1`.

**Still required:** audit whether the converse construction covers every relevant point, its sign choices and rational chart transitions, and all cases omitted by denominators. These are essential before a formal `(T') <=> U(Q)=empty` promotion. Neither an identity check nor a bounded search is a substitute.

## 6. p=53/8 exception: what was checked

For `p=53/8`, `H=a²+b²=2873=17·13²` and `a²-b²=2745=3²·5·61`. The source's proposed additional pair `(d1,d3)=(5185,34)` satisfies `5185=17·5·61`, `34=2·17`, and lies in the **reported candidate factor shape**. This is an arithmetic consistency check only.

The stronger assertion that this class passes the local image at **all places**, including `v=2`, requires the original 36R-05 exact local-image algorithm and replay outputs. They were not found in the searched Drive files. The finite-count claim `1465/1469` and the full local counterexample therefore remain **REPRODUCTION_HOLD**, not accepted independently in this review.

## 7. Actions and promotion firewall

1. Obtain and run the exact local-image source and recorded output for `p=53/8`; separately check the global-to-local squareclass conventions.
2. Investigate the open Brauer group `Br(U_H)` and whether any additional classes survive restriction from `Br(C_H)`.
3. Complete an exact inverse-map / deleted-chart audit of the `(T')` adapter.
4. Have a **different session** perform blind route generation without prior B/N candidate identifiers; compare only afterward.
5. Seek an independent hostile mathematical review; only after PASS may an explicit separate promotion PR revise `MAIN-STATE` or old completion wording.

Until then: `R29_CAMP2_CLOSED=false`, `Q11_CAMPEDELLI_CLOSED=false`, `ENDPOINT_CLOSED=false`, `PERFECT_CUBOID_NONEXISTENCE_CLAIM=false`, and **Stage36 parking stays provisional**.

**No repository-wide verifier/Actions workflow was created or automatically triggered by this review.**
