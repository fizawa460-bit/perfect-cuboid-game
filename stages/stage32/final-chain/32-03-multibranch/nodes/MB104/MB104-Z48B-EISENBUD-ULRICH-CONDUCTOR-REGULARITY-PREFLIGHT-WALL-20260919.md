# MB104 Z48B — Eisenbud--Ulrich conductor-regularity preflight — 2026-09-19

Status: **PARALLEL PRE-AUDIT NEW-THEOREM PREFLIGHT / HYPOTHESIS WALL / NO CREDIT**

## Candidate theorem

Eisenbud--Ulrich, *The Regularity of the Conductor* (Clay Math. Proc. 18, 2013),
Theorem 3.1, proves the following graded statement.

Let `X subset P^r` be reduced of codimension `c`, with homogeneous coordinate ring
`A` Gorenstein, and let `A subset B subset normalization(A)` be a graded finite
Cohen--Macaulay intermediate ring.  Then the conductor ideal in the ambient polynomial ring is
perfect of codimension `c+1` and

```text
reg(conductor) = reg(X) - 1 - indeg(B/A).
```

For geometrically reduced irreducible `X`, this gives the strict bound

```text
reg(conductor) < reg(X)-1.
```

This is exactly the kind of theorem that could turn Z48's finite conductor scheme into a
postulation/syzygy restriction rather than merely a length identity.

## Why it cannot yet be applied to the MB104 carrier

The exact MB104 receiver supplies

```text
C subset S subset P^6,
C integral Cartier on the smooth resolution S,
C in |lP|,
C is locally Gorenstein,
normalization genus(E)=1.
```

Local Gorensteinness of the curve is **not** the same as the homogeneous coordinate ring of the
embedded curve `C subset P^6` being arithmetically/projectively Gorenstein.

The Eisenbud--Ulrich theorem needs the latter graded hypothesis on the homogeneous coordinate
ring `A_C`, together with Cohen--Macaulay control of the chosen graded normalization/intermediate
ring.

No retained MB104 asset proves, uniformly for every hypothetical `C in |lP|`, that

```text
A_C is Gorenstein,
or even that C is arithmetically Cohen--Macaulay in P^6.
```

The fact that the ambient cuboid surface is a complete intersection of four quadrics does not
supply this automatically for an arbitrary divisor class `lP`, which is not the ambient
hyperplane class.

Therefore importing the regularity formula would be an invalid hypothesis transfer.

## Exact route disposition

Z48 gives an intrinsic surface conductor scheme

```text
Z_cond subset S,
length(Z_cond)=168l^2+56l.
```

Eisenbud--Ulrich would become usable only after a new graded adapter proving one of:

```text
(1) the P^6-embedded carrier is arithmetically Gorenstein uniformly in l; or
(2) a relative/section-ring version of the conductor theorem applies to the P-polarized section
    ring with all Cohen--Macaulay/Gorenstein hypotheses verified.
```

Absent such an adapter, no Castelnuovo--Mumford regularity bound is claimed.

## Firewalls

```text
eisenbud_ulrich_theorem_source_locked=true
carrier_locally_gorenstein=true
carrier_arithmetically_gorenstein_proved=false
carrier_ACM_proved=false
conductor_regularilty_bound_applied=false
finite_degree_window_proved=false
carrier_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
