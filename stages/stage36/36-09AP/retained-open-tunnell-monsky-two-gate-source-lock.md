# Stage36 36-09AP source lock: retained-open Tunnell + Monsky necessary gates

Accessed: 2026-09-07

This leaf reconciles two hostile-audited Stage36 continuations after PR #1679 was squash-merged into main.

## Audited inputs

1. PR #1679, post-merge hostile audit PASS review `5127771308`, exact head `12716259951f02589ecfaf6ac8f9670b7a23f06f`, exact-head CI `34076440104 / 101603376687`, squash merge/current-main commit `6b6c541d1a6bbe229381ac0400148bd17523ca06`.
   - 36-09AN proves on the retained open that the explicit full-2 covering map lands on a non-torsion point of the congruent-number Jacobian.
   - Hence retained receiver => positive MW rank => congruent N => parity-appropriate Tunnell necessary equality.

2. PR #1680, hostile audit PASS review `5127677576`, exact head `f5db4fc0aafdc61f931b6499afb18c1966c1f99d`, exact-head CI `34077287921 / 101605797971`.
   - 36-09AO source-locks one exact Monsky-matrix convention and the Stage36 full-2-class coordinate adapter on the B=7 odd example.
   - The reconciled branch imports the exact audited AO certificate/source blobs, but not the conflicting older AM/AN controller state.

## General retained-open Selmer implication

A rational point on a Stage36 full-2 covering maps to a rational point on its Jacobian `E_N`. Therefore its full-2 Kummer class lies in the Mordell-Weil image and hence in the 2-Selmer group. Under the Monsky convention source-locked by audited 36-09AO, the corresponding pure class coordinate must lie in `ker M_N`.

Thus every retained receiver branch satisfies both necessary gates:

```text
TUNNELL_GATE: parity-appropriate Tunnell equality holds,
MONSKY_GATE : Stage36 pure full-2 vector v_stage lies in ker M_N.
```

Failure of either gate excludes that branch. Neither converse is asserted.

## Odd eta=-1 Stage36 class coordinates

Assume `eta=-1` and the normalized Jacobian parameter `N=A*B*C*D` is odd. Since `g=(e+f) mod 2=0`, one has `e=f=t` with `t in {0,1}`.

The normalized Stage36 root order is `(0,+N,-N)`.

### t=0

The Stage36 triple is

```text
(-C*D, -A*C, A*D).
```

Reorder to Monsky roots `(+N,-N,0)`:

```text
(-A*C, A*D, -C*D).
```

Multiply componentwise by the rational 2-torsion triple of `(0,0)`, namely `(-N,N,-1)`, and reduce modulo rational squares. The positive-divisor representative is

```text
(d1,d2,d3)=(B*D, B*C, C*D).
```

Therefore

```text
v_stage = ( psi_N(B*C) | psi_N(B*D) ).
```

### t=1

The Stage36 triple is

```text
(-C*D, -2*A*C, 2*A*D).
```

After root reorder, multiply by the rational 2-torsion triple of `(-N,0)`, namely `(-2N,2,-N)`, and square-reduce. The positive-divisor representative is

```text
(d1,d2,d3)=(B*D, A*D, A*B).
```

Therefore

```text
v_stage = ( psi_N(A*D) | psi_N(B*D) ).
```

These formulas use only the hostile-audited Stage36 squareclass decomposition and the audited AO Monsky convention.

## Exact same-parameter diagnostic

At the audited AF parameter `p=2/11`, take `A=73`, `C=11`, `D=13`, `eta=-1`, `e=f=1`.

### B=7

```text
N=73073=7*11*13*73,
v_stage=(0,0,1,1 | 1,0,1,0).
```

Audited AO gives `M_N*v_stage=0`, while audited AL/#1679 gives Tunnell failure. The branch is excluded by the Tunnell gate.

### B=23

```text
N=240097=11*13*23*73,
(d1,d2,d3)=(299,949,1679)=(13*23,13*73,23*73),
v_stage=(0,1,0,1 | 0,1,1,0).
```

The exact Monsky matrix has rank 6/nullity 2, but

```text
M_N*v_stage=(0,1,0,1 | 1,0,0,1) != 0.
```

Audited #1680 AN gives Tunnell equality `384=384` for this diagnostic choice. Therefore Tunnell equality alone does not pass the Stage36 branch: the Monsky-class gate excludes it. This does not make B=23 a previously viable receiver branch; audited AF already found selected-prime local-row failure. Its role is to show the two gates are logically distinct and that the Monsky test packages actual-prime local information at the Selmer level.

## Scope firewall

- `Tunnell equality` is necessary only; no BSD converse is used.
- `M_N v_stage=0` means only that this pure class passes the Monsky Selmer-kernel test under the locked convention; it does not prove MW image or a rational covering point.
- Matrix nullity alone does not identify a specific class with MW or Sha.
- This leaf treats the odd `eta=-1` Stage36 coordinate adapter exactly; even `N` and `eta=+1` class-coordinate adapters remain separate work.
- No global parameter shrink, receiver emptiness, R29/Q11/endpoint closure, or perfect-cuboid claim is granted.