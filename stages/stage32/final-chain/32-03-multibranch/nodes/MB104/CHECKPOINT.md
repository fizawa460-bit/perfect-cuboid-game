# Stage32 MB104 checkpoint — finite window reduced to a minimal-cusp branch bound

Status: **ACTIVE RETAINED CHECKPOINT / MB104 NOT COMPLETE / NO CREDIT**

## Baseline insufficiency

MB101 plus MB102 alone do not force a finite upper bound on canonical degree `d=H.D`. Their numerical contracts admit formal arbitrary even-degree data such as

```text
g=1: D^2=-d,   Delta_total=0,
g=0: D^2=-d-2, Delta_total=0,
```

which satisfy the retained adjunction/normalization identity and Hodge upper bound. This is an insufficiency witness only; it is not an existence claim for curves.

## New progress: branchwise Freitag--Salvati Manni extension

The proof of Freitag--Salvati Manni Theorem 3.1 was re-opened at the exact point where bijective normalization is used. The published proof has

```text
16(2g-2)k = #zeros - #poles,
#zeros >= 2kd.
```

For one normalization branch over a box node with cusp vector `(a1,a2)`, the differential contributes pole order `16k` and the discriminant factors contribute zero order `(a1+a2)k`. The translation-lattice congruences force

```text
a1,a2>0,
a1 == a2 == 0 mod 4,
a1+a2 == 0 mod 8.
```

Thus a positive pole occurs only when `a1+a2=8`, equivalently in MB101 notation only for `(A,B)=(1,1)`, and then its order is `8k`.

Let

```text
R8 = number of normalization branches over the 48 nodes with (A,B)=(1,1).
```

Summing branchwise yields the retained necessary inequality

```text
d <= 16g - 16 + 4R8.                 (MB104-FSM-MB)
```

For bijective normalization, `R8<=48`, and the published bound is recovered exactly:

```text
d <= 16g-16+4*48 = 176+16g.
```

The detailed proof and certificate are in:

- `FSM-MULTIBRANCH-POLE-LEMMA.md`
- `FSM-MULTIBRANCH-POLE-CERTIFICATE.json`
- `verify_mb104_fsm_multibranch_pole.py`

## MB101 interface

Every minimal cusp branch `(A,B)=(1,1)` has `m=min(A,B)=1`. Therefore

```text
R8 <= R <= M=sum_i D.E_i,
```

and hence also

```text
d <= 16g-16+4M.
```

The latter is not a finite degree bound because no adequate population-wide upper bound on `M` is currently retained.

## Sharpened bottleneck

MB104 no longer needs a generic new inequality. The exact missing object is a bound on the minimal-cusp branch count `R8`. A finite degree window follows from either

```text
R8 <= constant,
```

or

```text
R8 <= alpha*d + beta,  alpha < 1/4.
```

The later symmetric-differential literature constrains **distinct node support** but does not bound normalization multiplicity `R8` at one node, so it does not by itself close this gap.

## Firewalls

No absolute `R8` bound is claimed. MB104 remains incomplete; finite Picard enumeration is unreleased. There is no receiver, effectivity, final-milestone, theorem, endpoint, Perfect Cuboid, or merge credit.
