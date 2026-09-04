# Stage35-EX 35EX-12 — S-unit/Thue adapter test and dynamic-support blocker

## Scope

Assume the conditional exact reductions through 35EX-11 and the fresh post-three-reservoir breadth audit.

This leaf tests only the re-selected route

```text
35EX-12_SUNIT_THUE_ADAPTER_OR_DYNAMIC_SUPPORT_BLOCKER
```

The question is not whether each individual hypothetical E1 counterexample has finite prime support. It does. The question is whether the 35EX-09 three-reservoir graph can be normalized, uniformly over every Master-Hit, to either

1. one fixed finite set `S` of allowed primes for an S-unit equation; or
2. a fixed finite family of Thue/Thue-Mahler coefficient forms.

No external S-unit/Thue theorem is invoked here. This leaf tests whether the current receiver supplies the hypotheses needed to invoke such a theorem later.

## 1. Exact per-Master-Hit support

Write as before

```text
c = gcd(U1,U2),
D = U1/c,
T = U2/c,
p = gcd(W1,V2),
q = gcd(V1,V2).
```

Branch L has

```text
t = D*V2/(2*p*q),
e = gcd(c,H),
e | c,
```

and Branch R has

```text
j = D*V2/(p*q),
e = gcd(c,H),
e | c.
```

The complete 35EX-09 squareclass graph says that every individual factor squareclass is supported on the three pairwise-coprime reservoirs

```text
Branch L: t, T, e
Branch R: j, T, e.
```

Since `e|c`, define the source-known per-hit support

```text
S_L(hit) = supp(2*c*t*T),
S_R(hit) = supp(2*c*j*T).
```

Then every squarefree coefficient appearing in the 35EX-09 vertex formulas is supported on `S_L(hit)` or `S_R(hit)` respectively.

Therefore, for a fixed Master-Hit, the four-factor square condition does reduce to finitely many coefficient choices:

```text
number of squareclass allocations < infinity for that hit.
```

This is a valid per-hit finite statement.

## 2. Why this is not yet a fixed-S S-unit problem

Substituting the source formulas gives

```text
Branch L:
  t*T*c = D*V2*U2/(2*p*q),

Branch R:
  j*T*c = D*V2*U2/(p*q).
```

Thus the support still contains source-dependent prime divisors coming from the varying primitive Euclid data through

```text
D,
V2,
U2,
c,
```

modulo the exact removals represented by `p` and `q`.

The canonical gcd/coprimality theorems control overlap between these pieces. They do not prove that their odd prime divisors lie in one fixed finite set independent of the Master-Hit.

Likewise, the 35EX-10/11 Legendre routing constrains where a reservoir prime may sit and can kill some split primes. It does not replace the surviving reservoir support by a fixed finite prime set.

Hence the current identities prove

```text
PER_MASTER_HIT_FINITE_SUPPORT=true
FIXED_FINITE_S_OVER_ALL_MASTER_HITS_PROVED=false.
```

The first statement cannot be substituted for the second.

## 3. Thue/Thue-Mahler coefficient family test

One may instead absorb square factors and write each factor schematically as

```text
Li = d_i * y_i^2
```

or

```text
Ri = d_i * y_i^2,
```

where each `d_i` is squarefree and supported on the corresponding per-hit reservoir set.

The 35EX-09 allocation gives exact incidence constraints among the `d_i`, but the possible values of the `d_i` still range over squarefree divisors of the parameter-dependent integers

```text
t*T*c
```

or

```text
j*T*c.
```

Therefore the present reduction does not produce a fixed finite coefficient list for a Thue or Thue-Mahler family over all Master-Hits.

To authorize that route one would need an additional exact theorem of one of the following types:

```text
(A) fixed-prime-support theorem:
    every relevant t*T*c or j*T*c is supported on one fixed finite S;

(B) finite-normal-form theorem:
    after quotienting source squares and exact primitive factors,
    all admissible coefficient tuples (d1,d2,d3,d4)
    lie in a fixed finite family independent of the Master-Hit;

(C) uniform parameter elimination:
    transform the current receiver to finitely many fixed Thue/Thue-Mahler forms
    while preserving every Master-Hit and every E1-counterexample candidate.
```

None of (A), (B), or (C) is proved by 35EX-02 through 35EX-11.

## 4. Exact route decision

This leaf therefore freezes only the present S-unit/Thue adapter attempt:

```text
PER_MASTER_HIT_FINITE_SUNIT_SUPPORT_PROVED=true
UNIFORM_FIXED_FINITE_S_PROVED=false
FIXED_FINITE_THUE_FAMILY_PROVED=false
SUNIT_THUE_FINITE_ENUMERATION_AUTHORIZED=false
CURRENT_SUNIT_THUE_ADAPTER_ROUTE=FROZEN_DYNAMIC_SUPPORT
```

This does **not** prove that no deeper S-unit/Thue argument can exist. Reopen only if a new exact theorem supplies (A), (B), or (C), or another equivalent uniform adapter.

No finite enumeration is performed in this leaf.

## 5. Next route from the fresh breadth ledger

The fresh 35EX-11 breadth audit preserved several mathematically distinct `UNTESTED` routes. Since 35EX-12 changes no receiver and only freezes one selected adapter, the next candidate may be selected from that already-audited ledger without claiming route exhaustion.

The highest-information exact identity currently available there is the alternate norm symmetry

```text
(W1*U2)^2 + (U1*V2)^2
  = (U1*W2)^2 + (V1*U2)^2.
```

So the next exact leaf is

```text
35EX-13_ALTERNATE_NORM_SYMMETRY_COMPATIBILITY
```

Its task is to determine whether an E1 counterexample forces a second genuinely new primitive square condition through the unused `W2/V1` cross channel, or whether that view reduces to already-audited data.

The other breadth-audit candidates remain `UNTESTED`:

```text
E1-NONNAIVE-DESCENT
E1-GLOBAL-RECIPROCITY-BEYOND-LOCAL-GRAPH
E1-RECEIVER-RESTRICTED-JOINT-LOCAL
```

## Credit boundary

```text
FIXED_FINITE_SQUARECLASS_FAMILY_PROVED=false
FINITE_ENUMERATION_AUTHORIZED=false
E1_PROVED=false
R29_PESCH_E1_CLOSED=false
R29_FIB2_CLOSED=false
J12_PARAMETRIC_CLOSED=false
STAGE35_CLOSED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
