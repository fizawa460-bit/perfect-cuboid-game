# MB104 P6M — singularity-type log-BMY correction preflight wall — 2026-09-19

Status: **PRE-AUDIT SOURCE-INCOMPLETE CORRECTION-TERM WALL / NO CREDIT**

## Target

P6L shows that the source-complete irreducible-curve Miyaoka inequality is compatible with the hostile ray for every `l>=1`. P6M asks whether retained local information determines singularity types strongly enough to insert a sharper log/orbifold correction.

For a hypothetical integral genus-one carrier

```text
C in |lP|,
P^2=336,
K.C=112l,
p_g(C)=1,
```

adjunction fixes the arithmetic genus and hence the total delta mass:

```text
p_a(C)=1+(C^2+K.C)/2
      =1+168l^2+56l,

delta(C)=p_a-p_g=168l^2+56l.
```

This is exact, but it is only a total singularity invariant.

## Retained local information

P6D2 forces, at the fourteen supported exceptional box nodes,

```text
r_odd=R=M=d=112l,
m_b=1
```

and therefore `8l` normalization branches over each supported box node.

The same note explicitly firewalls the stronger local assertion:

```text
m_b=1 does not imply (A,B)=(1,1).
```

P6F retains only the weaker Lu--Miyaoka consequence that for `l>=3` there are at least `112l-224` ordinary node-or-triple singularities. It does not identify all singularities, their multiplicity sequence, Milnor/Tjurina numbers, or local orbifold weights.

## Coefficient-level gap

The delta budget grows quadratically:

```text
delta(C)=168l^2+56l,
```

whereas the source-locked exceptional-contact population is only linear:

```text
112l.
```

Thus the retained exceptional-contact data cannot classify the singularities carrying the quadratic delta mass. Even assigning the strongest permitted ordinary interpretation to the known linear population leaves an uncontrolled `Theta(l^2)` part of the singularity budget.

A refined log/orbifold BMY substitution needs local correction terms determined by singularity type, not merely total delta. No retained adapter converts the uncontrolled delta remainder into a source-complete sum of such local corrections.

Therefore none of the following substitutions is currently justified:

```text
delta = number of nodes,
all carrier singularities are ordinary,
all singularities occur at exceptional contacts,
m_b=1 => diagonal A1 type,
orbifold correction = a function of delta alone.
```

## Disposition

P6M fails at the preflight interface. The current retained data controls total delta and a linear exceptional-contact package, but not the coefficient-level singularity decomposition required for a sharper log/orbifold BMY inequality.

Accordingly no refined inequality is evaluated and no finite `l` window is claimed. Reopening P6M requires a new exact local-classification adapter covering the quadratic delta mass (or a theorem whose correction depends only on already-retained invariants).

The route is parked and control should return to a different packet-sensitive isolated-carrier mechanism.

## Source locks

- P6L note blob `a653c0077f1c751cbfffb982e870cddae731b5c5`;
- P6L certificate blob `97fecde97985598b456983d87e534605ad129883`;
- P6F note blob `e89426128010ae97a10fbd908346f6cf07fff109`;
- P6D2 note blob `1194fdd228c394d79262579df3930b4d8f619cf9`.

## Firewalls

```text
delta_budget_exact=true
singularity_types_source_complete=false
refined_log_BMY_applied=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
