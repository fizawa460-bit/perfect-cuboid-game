# Stage30-01 — source lock and action-object freeze

Base main SHA: `a039cabd0cb17fa8e958a752bd40185eacb4b6ac`.

## Authoritative merged inputs

Stage30 consumes the following audited Stage29 records without reopening discharged receivers.

| role | path | blob SHA |
|---|---|---|
| arrangement/source | `stages/stage29/29-02ha/source-lock.md` | `a6f2c371d730bcf75cb87ddaec1986f36effc13c` |
| arrangement exact output | `stages/stage29/29-02ha/arrangement-check-output.md` | `39a527efa4920c9354ea99af90ecd259b5940394` |
| arrangement checker | `stages/stage29/29-02ha/arrangement_check.py` | `1f056af7311292944444ddfe87371171d8386adc` |
| exact Q-moduli datum | `stages/stage29/29-02g/exact-q-moduli-adapter.md` | `facd6a799868ad135d6f19cb588b14d237d337e5` |
| K8 defect compression | `stages/stage29/29-02g/torsion-descent-defect.md` | `e79c7573eaa08d5e0975937453cd153731ead239` |
| modular synthesis | `stages/stage29/29-02g/result.md` | `4357c7698bd16e1f356243029c7ce52271d6c517` |
| modular attack audit | `stages/stage29/29-11/audit.md` | `a501a879934e69a5e413f1585cdc867017d76a48` |
| bounded modular execution | `stages/stage29/29-15/bounded-execution.md` | `d839065f8087dcd49eec6f13bd01b09f65daea0b` |
| bounded checker | `stages/stage29/29-15/verify_bounded_execution.py` | `b1c2473545675cff25b66416f3b1ce748b55b6a4` |
| post-Work audit | `stages/stage29/29-15/post-work-audit.md` | `6ee23eaa295c231a59a9c9ccfe322922ce8036e7` |
| active-kernel ledger | `stages/stage29/29-16/active-kernel-ledger.json` | `5d6d4c7709b57064aea5dc0ece672c5170c39550` |
| Stage29 handoff | `stages/stage29/29-17/final-handoff.json` | `c1b86f5216a897e31378b0121a6c9fe8da0ba63d` |

Primary provenance remains Testa--Stoll, *The surface parametrizing cuboids* (arXiv:1009.0388 / current author PDF), as locked upstream. Stage30 does not grant any stronger statement than the merged audits.

## Frozen fields and receiver

```text
Q0 = Q
K  = Q(i)
sigma = nontrivial element of Gal(K/Q)
receiver = R29-KUM5
kernel = K16-C2-MODULAR-S4-ACTION
parent route = Q11-MODULAR
```

Physical work remains on the audited noncuspidal/stabilizer-free endpoint open. Generic degree 24 is not promoted to an everywhere-finite compactified morphism.

## Arrangement-side action object

The seven branch lines are frozen in the exact upstream labels

```text
A1=x
A2=y
A3=z
B3=x+y
B2=x+z
B1=y+z
C =x+y+z
```

with

```text
Omega_arr_4 = (A1,A2,A3,C)
Omega_arr_3 = (B1,B2,B3)
G_arr = Aut_P2(D), |G_arr|=24, G_arr ~= S4.
```

The Q-liftable subgroup is the coordinate-permutation `S3`; over `K=Q(i)` all 24 base automorphisms lift. The line orbits are `3+3+1` over Q and `4+3` over K.

For deterministic downstream certificates, freeze two arrangement generators as exact permutations on the seven labels:

```text
s_arr = (A1 A2)(B1 B2)
t_arr = (A1 A2 A3 C)(B1 B3)
```

with `A3,C,B3` fixed by `s_arr` and `B2` fixed by `t_arr`. In the dual-line convention used by `arrangement_check.py`, witnesses are

```text
s_arr_matrix = [[0,1,0],[1,0,0],[0,0,1]]
t_arr_matrix = [[0,0,1],[-1,0,1],[0,-1,1]].
```

Task A must independently recover/verify these permutations from the existing exact checker rather than trusting the display.

## Modular-side action object

Freeze

```text
G_mod = PSL2(Z/4) = SL2(Z/4)/{+/-I}, |G_mod|=24.
```

Use deterministic matrix-generator representatives

```text
S_mod = [[0,-1],[1,0]] mod 4
T_mod = [[1, 1],[0,1]] mod 4
```

with equality taken in `PSL2(Z/4)`. Task A must verify that their generated projective group has order 24 and certify its relations; the roadmap does not assume a presentation by name alone.

Let

```text
V_mod = ker(PSL2(Z/4) -> PSL2(F2)).
```

The finite modular action objects are defined intrinsically, without assuming an arrangement identification:

```text
Omega_mod_3 = V_mod - {1}, acted on by conjugation;
Omega_mod_4 = { H <= G_mod : |H|=6, H intersect V_mod={1}, H*V_mod=G_mod }, acted on by conjugation.
```

Task A must certify `|V_mod|=4`, `|Omega_mod_3|=3`, `|Omega_mod_4|=4`, or stop with an exact counter-certificate. These are the canonical `3+4` residual-action objects to be compared later with `Omega_arr_3+Omega_arr_4`; defining them does not yet identify the two S4 actions.

## Frozen marked data carried but not yet interpreted

The endpoint modular datum on the physical noncuspidal locus is

```text
E/K,
(P1,P2) basis of E[4],
psi:E[8] -> E^sigma[8],
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

Freeze the displayed level-4 sign label

```text
D4 = diag(1,-1) mod 4
```

as semilinear/descent data, not as an element of `G_mod`. Its exact action/cocycle role is deferred to Stage30-06.

Also freeze

```text
K8 = ker(SL2(Z/8)->SL2(Z/4)), |K8|=8,
kappa=psi^sigma o psi in K8,
SIGMA_ACTION_ON_K8=TRIVIAL,
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8.
```

The eight K8 elements are labels only during Task A/Task B. No Q-descent or arithmetic-defect compatibility credit is allowed before the Stage30-06 cocycle derivation and audit.

## Reusable exact code

- `stages/stage29/29-02ha/arrangement_check.py`
- `stages/stage29/29-02g/defect_orbits.py`
- `stages/stage29/29-15/verify_bounded_execution.py`

New code must reuse or import these semantics where practical rather than silently redefining them.

## Firewalls

```text
ABSTRACT_S4_MATCH_IS_ADAPTER=false
QI_ACTION_IDENTIFICATION_PROVED=false
Q_GALOIS_COCYCLE_PROVED=false
K8_DEFECT_ELIMINATION_COUNT=0
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
