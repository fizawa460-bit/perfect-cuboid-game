# Stage32 32-01-178 N349 — Freitag–Salvati Manni boundary-equality contract

Status: `AUDIT_REQUIRED_PREFLIGHT`

Scope: the current 21 exact Picard numerical classes at the two boundary rows
`g0-d176` and `g1-d192`.  This note derives a necessary local condition only for an
**integral irreducible curve whose normalization maps bijectively to its image**.  It
does not claim that such a member exists in any of the 21 effective divisor classes.

## Locked upstream interfaces

Current exact checkpoints:

- `N342/RESULT.json`, canonical
  `0a556575c4ad365d5f0816a60c380de16ca609310961e58f6e63834082a61c88`:
  21 terminals, every one with exact labelled support on all 48 exceptional divisors.
- `N347/RESULT.json`, canonical
  `ccafa29bdbc2f9463fe3a0ef16eb328319214574440074365f35d2a1761b6f80`:
  all 21 have an exact integral Picard class meeting the self-square necessary condition.
- `N348/RESULT.json`, canonical
  `9a1f1cd3ec4060239d74e552d63126fe4b948d3accb3fe0fbe3e8e0213b51672`:
  Riemann--Roch gives a geometric effective divisor representative in every one of the
  21 locked classes.  This is not integral/irreducible/low-genus credit.

Previously audited Stage32 refinement:

- merged PR `#1472`, merge commit `8cb707ffdc4ea72094d397df1896b374a4bbb1a7`;
- `stages/stage32/32-21/post-21bl-freitag-node-support-refinement.md`;
- under the Freitag--Salvati Manni bijective-normalization hypothesis, if an irreducible
  curve meets `n` box-variety nodes then

```text
d <= 16g - 16 + 4n.
```

Primary published source:

- Eberhard Freitag and Riccardo Salvati Manni,
  *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016),
  Theorem 3.1 and proof;
- DOI `10.1307/mmj/1480734014`;
- author PDF `https://www.mathi.uni-heidelberg.de/~freitag/preprints/box.pdf`;
- proof locator: printed pp. 10--11 / PDF pages indexed 9--10.

The proof states, for a local cusp parametrization,

```text
alpha(z) = z(a1,a2) + (Phi1(q),Phi2(q)),
a1 == a2 == 0 (mod 4),
a1+a2 == 0 (mod 8),
a1>0, a2>0,
```

hence `a1+a2 >= 8`.  It also states

```text
16(2g-2)k = #zeros - #poles,
#zeros >= 2kd,
local pole order <= 8k,
#poles <= 384k.
```

The local pole estimate comes from a `16k` pole contribution from `(dz dw)^(8k)` and
a zero contribution `(a1+a2)k` from `Delta(z)^k Delta(w)^k`.

## Boundary equality consequence

For both current residual rows,

```text
g=0,d=176  => d=176+16g,
g=1,d=192  => d=176+16g.
```

Suppose an integral irreducible curve `C` in one of these classes has bijective
normalization of genus `g`.  Put `Z=#zeros` and `P=#poles` for the tensor in the
published proof.  Then

```text
16(2g-2)k = Z-P
           >= 2kd-P
           >= 2kd-384k.
```

At `d=176+16g`, the first and last expressions are equal.  Therefore every
intermediate inequality must be equality.  In particular:

1. `P=384k`;
2. all 48 possible node-pole locations must occur;
3. every one of the 48 local pole orders must equal its maximum `8k`;
4. at every node, `a1+a2=8`;
5. because `a1,a2` are positive multiples of four, necessarily
   **`(a1,a2)=(4,4)` at every node**.

This is stronger than the already-audited support condition `n=48`.  Exceptional-divisor
support records whether the strict transform meets a given exceptional divisor; a Picard
intersection number does not by itself record the local modular cusp translation pair of a
particular integral member.

## Current exact-data diagnosis

The retained N342/N347/N348 evidence contains:

- the numerical Picard class;
- all 48 exceptional-divisor support labels (indeed all 48 are present);
- exact self-intersection witnesses;
- geometric divisor effectivity from Riemann--Roch.

It does **not** contain an actual integral irreducible low-genus member, its normalization,
or 48 local branch/cusp parametrizations.  Repository search at this checkpoint finds no
source-locked adapter from the Picard numerical class / exceptional pairing `1` to the
local `(a1,a2)` pair.

Therefore the next load-bearing datum is not another Picard scalar filter.  It is an exact
member-level adapter that either:

```text
(A) constructs an integral irreducible genus-0/1 member and computes all 48 local cusp
    pairs, which must all be (4,4),
```

or

```text
(B) proves that no integral irreducible member in the locked class can realize (4,4) at
    all 48 nodes.
```

## Firewalls

```text
FSM_BOUNDARY_EQUALITY_LOCAL_PAIR_NECESSARY=true
CURRENT_21_ALREADY_HAVE_ALL48_NODE_SUPPORT=true
PICARD_PAIRING_ONE_IMPLIES_LOCAL_PAIR_4_4=false
LOCAL_CUSP_PAIR_DATA_PRESENT=false
INTEGRAL_IRREDUCIBLE_MEMBER_CERTIFICATE_PRESENT=false
BIJECTIVE_NORMALIZATION_LOW_GENUS_CLOSED=false
MULTIBRANCH_CASE_CLOSED=false
Q_DEFINED_EFFECTIVE_MEMBER_PROVED=false
N350_PRODUCER_REGISTRY_CHANGED=false
FULL178_COMPLETE=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
MERGE_AUTHORIZED=false
```
