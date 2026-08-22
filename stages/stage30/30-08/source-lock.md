# Stage30-08 — physical endpoint adapter source lock

This stage does not introduce a new theorem.  It determines the exact scope of the already-audited Stage30 action/cocycle/defect computation on the physical endpoint open.

## 1. Frozen post-Stage29 target

Authoritative source:

- `stages/stage29/29-16/active-kernel-ledger.json`

The Class-2 root is

```text
K16-C2-MODULAR-S4-ACTION
child = R29-KUM5
parent route = Q11-MODULAR
```

with exact wall

```text
action-level arrangement-to-modular S4 identification compatible with the audited Q/Q(i) descent cocycles
```

and completion consequence

```text
attach the eight marked modular defects to the exact arrangement action
```

The same ledger explicitly says the kernel is not endpoint-decisive alone and that no marked defect is eliminated merely by identifying the action.

Therefore Stage30-08 must not silently strengthen the kernel completion criterion into an arithmetic nonexistence theorem.

## 2. Exact modular datum over Q

Authoritative source:

- `stages/stage29/29-02g/exact-q-moduli-adapter.md`

On the noncuspidal fine-moduli locus, a rational endpoint point gives the exact conjugate-self level structure

```text
P in Sbar(Q)
=>
E/Q(i),
(P1,P2) basis of E[4],
psi:E[8] -> E^sigma[8],
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

This is an 8-torsion correspondence, not an elliptic-curve descent statement.

## 3. Full physical-open coverage

Authoritative source:

- `stages/stage29/29-15/bounded-execution.md`, receiver `R29-MOD1D`

The exact diagonal quotient has

```text
U=u1*u2=2*b1
V=v1*v2=2*b2
W=w1*w2=2*b3.
```

A physical endpoint has positive nonzero face diagonals, hence

```text
b1*b2*b3 != 0.
```

Therefore both X(8) factors are noncuspidal and the diagonal G0 action is stabilizer-free on every physical endpoint preimage.  The audited conclusion is

```text
R29-MOD1D=DISCHARGED_PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE
PHYSICAL_ENDPOINT_INTERSECTS_MODULAR_CUSP_LOCUS=false
PHYSICAL_ENDPOINT_MODULAR_G0_STABILIZER_TRIVIAL=true
```

Thus no compactified-boundary extension is needed to apply the Stage30 modular adapter to the physical endpoint open itself.

## 4. Audited Stage30 inputs

### 30-05

The Testa--Stoll common Q(i) model on the same cuboid surface is verified, and the modular residual action projects to the seven branch squareclasses with kernel `V_mod ~= V4` and image of order 6.

### 30-06 / 30-06C

Authoritative audit state:

- `stages/stage30/30-06C/audit-state.json`

Verified exactly:

```text
PSL2(Z/4) order = 24
endpoint projective group order = 24
theta all 24 = verified
V_mod sign-deck intersection = verified
c_sigma = delta_a3
c_sigma cocycle = verified
semilinear identity all 24 = verified
failed element count = 0
```

### 30-07

Authoritative audit state:

- `stages/stage30/30-07/audit-state.json`

Verified exactly:

```text
K8 order = 8
all 24 x 8 equivariance = verified
ordinary S4 orbit sizes = 1,3,3,1
sigma action on K8 = trivial
marked Q-descent classes = 8 singleton classes
defect elimination count = 0
```

The eight states are attached to endpoint sign patterns on `(b1,b2,b3)`.

## 5. Scope decision encoded by Stage30-08

Combining sections 1--4 gives the exact physical conclusion:

1. every physical endpoint lies in the noncuspidal stabilizer-free modular locus;
2. on that locus, the source-derived residual action and Q(i)/Q semilinear cocycle are exact and exhaustively checked;
3. all eight marked K8 defects are transported to the exact endpoint sign-deck action;
4. no defect is eliminated.

This meets the literal completion consequence of `K16-C2-MODULAR-S4-ACTION` / `R29-KUM5` without producing an endpoint obstruction.

The submitted Stage30-08 outcome is therefore roadmap Outcome B:

```text
R29-KUM5 discharged
8 arithmetic states explicitly located
0 arithmetic states eliminated
Q11-MODULAR remains AMBER
```

Final credit is pending Stage30-audit.

## Firewalls

```text
GENERIC_DEGREE_24_COMPACTIFICATION_CLAIM=false
ELLIPTIC_CURVE_Q_DESCENT_INFERRED=false
ORDINARY_8_CONGRUENCE_IMPLIES_ENDPOINT=false
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false
PRIMITIVE_CANONICAL_POPULATION_THEOREM_PROVED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
