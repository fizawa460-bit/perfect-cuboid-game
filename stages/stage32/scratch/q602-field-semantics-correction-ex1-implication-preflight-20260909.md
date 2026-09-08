# Stage32 MAIN scratch — Q602 field-semantics correction and EX1 implication preflight

Status: **scratch only / unaudited / no MAIN credit**.

## 1. Correction of the previous field wall

The previous scratch leaf correctly observed the retained Galois facts

- `cc(V6) != V6`;
- `cc(V6)` is not in the retained `Aut(S)` orbit of `V6`.

Hence a divisor defined over `Q` cannot have exact Picard class `V6`, and an `Aut(S)` twist does not repair that particular descent problem.

What does **not** follow is that the active Stage32 same-member Q602 interface is thereby blocked.

The retained O210/Q602 construction does not assume that the hypothetical V6 carrier is defined over `Q`. Its input is a hypothetical integral carrier `N -> B` in the geometric setting. The Beauville pullback produces a common double cover `Y`, two maps

`f1,f2 : Y -> C0`,

and the actual correspondence

`T=(f1)_*(f2)^* in End(J(C0))`.

The Q602 residue filter is the mod-2 predicate on this actual geometric endomorphism. The symbol `Q602` is a Stage32 target invariant, not a declaration that the carrier is defined over the rational field.

Therefore the prior inference

`V6 not Q-defined => same-member Q602 interface has a field-descent blocker`

is withdrawn. The retained BI/BJ Galois computations remain valid scratch facts; only their application to the active interface was too strong.

## 2. Actual remaining same-member interface

If the positive-member branch were pursued, the remaining interface is geometric:

1. materialize an actual integral irreducible geometric-genus-1 member of class V6;
2. construct the carrier-derived common cover and the same maps `f1,f2` for that member;
3. bind its local/contact data to the resulting `T mod 2` data without changing population/model/marking;
4. leave the absolute `delta_0inf` retained-W-line marking to EX4 unless an invariant replacement obstruction bypasses it.

No extra `Q`-descent hypothesis is inserted.

## 3. EX1 negative-branch preflight

PR #1728 has advanced to head

`e3c4a04d5010e6dca9428722e334890e2614297a`.

The most recent completed hostile audit is review `5147516314` on old head

`beec62400f5f2b49d325083fd9b745c3fd66763f`.

That audit reports the mathematical 05AF bridge repaired and fails only because `STAGE32-PROOF-PATH.md` still projected V1 as current instead of V1 `SUPERSEDED` / V2 `PROVISIONAL`. Therefore no terminal credit is available yet.

If a future hostile audit passes the repaired V2 full-target claim, the first MAIN promotion target is only

`S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1`.

An explicit EX1-to-MAIN scope adapter is still required.

After that, two further implications are plausible but must remain typed:

- **O210:** if the exact O210 population is contractually a subpopulation of integral irreducible geometric-genus-1 V6 carriers, V6 population nonexistence empties O210. Encode that implication explicitly before granting O210 credit.
- **Q602:** the Q602 claim allows a residue-specific obstruction *or an equally exact population-preserving obstruction*. V6 population nonexistence may therefore bypass residue-by-residue arithmetic, but only through a claim adapter that states the target population is empty. Do not rewrite this as an arithmetic exclusion of 73, 97, and 235 individually.

Neither implication closes Stage32, because FULL178 numerical census and other FINAL-CHECK components remain separate.

## Firewalls

- scratch only;
- no hostile-audit credit self-granted;
- no MAIN-STATE edit;
- no EX1 promotion;
- no O210 or Q602 exclusion;
- no receiver/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorized.
