# Stage32 MB104 — U12 dyadic Bolza-level normalizer wall — 2026-09-17

Status: **RAMIFIED DYADIC LOCAL LEVEL CLASSIFIED ENOUGH TO REMOVE IT AS A DEGREE SOURCE / SPIN TRANSFER STILL OPEN / NO CREDIT**

## Scope

The preceding U12 work reduced a hypothetical dangerous `000707000f0f` realization to a primitive equal-degree etale correspondence on the Bolza genus-two curve with the exact spin passport

```text
p2^* O(w0) ~= p1^* O(w1).
```

A previous note excluded a symmetry-equivariant standard Hecke subclass supported away from the dyadic prime and left open the possibility that a nontrivial local component at the ramified prime `(sqrt(2))` might supply the missing level change.

This note checks that local possibility at the level of the Bolza congruence subgroup.  It does **not** classify the full spin transport of an arbitrary commensurator double coset.

## 1. Local division-algebra structure

Let

```text
K=Q(sqrt(2)),
pi=sqrt(2),
v=(pi),
D=D_B.
```

Katz--Katz--Schein--Vishne prove that `D` is ramified at `v` and split at every other finite place.

For a quaternion division algebra over a nonarchimedean local field, the valuation ring `O_D` is the unique maximal order.  Its maximal ideal `P` is the unique two-sided maximal ideal, all two-sided ideals are powers of `P`, and

```text
P^2 = pi O_D.
```

Consequently every local division-algebra element normalizes `O_D` and its two-sided ideal filtration.  Projectively, the only extra valuation parity beyond units is represented by a division uniformizer.

## 2. Katz's exact mod-2 Bolza order

Section 12 of Katz--Katz--Schein--Vishne gives

```text
Q_B/2Q_B
 = F4 + F4 beta' + F4 eps + F4 eps beta',

eps^2=0,
beta'^2=eps,
beta' alpha=(alpha+1) beta',
F4=F2[alpha], alpha^2=alpha+1.
```

The maximal-ideal filtration is

```text
J=beta' Qbar,
J^2=eps Qbar,
J^3=eps beta' Qbar,
J^4=0.
```

Theorem 13.2 / Remark 13.5 identify the Bolza group modulo the principal level-2 subgroup as

```text
B / P Q_B^1(2)
 ~= Qbar_B^1(eps beta')
 ~= (Z/2)^2.
```

Since

```text
J^3=F4 eps beta',
```

this four-element subgroup is exactly

```text
H = { 1 + c eps beta' : c in F4 }.              (H)
```

Every element of `(H)` has norm one.

## 3. The division uniformizer preserves the Bolza level image

The element `beta'` is the residue-model division uniformizer: `beta'^2=eps`, matching `P^2=pi O_D`.

The skew relation gives

```text
beta' c = sigma(c) beta',
```

where

```text
sigma:F4->F4,
sigma(c)=c^2
```

is Frobenius.  Hence conjugation by the uniformizer sends

```text
1+c eps beta'
 -> 1+sigma(c) eps beta'.
```

Therefore

```text
beta' H beta'^(-1)=H.                            (UNIF-NORM)
```

The companion verifier

```text
verify_mb104_u12_bolza_dyadic_level.py
```

replays this finite `F4` action exactly.

## 4. Units also preserve the level image

`J^3` is a two-sided ideal in the local maximal order.  Therefore

```text
1+J^3
```

is normal in the local unit group.  Its norm-one part is precisely the subgroup `(H)` appearing above.  Thus local units normalize the Bolza level-2 image.

Together with `(UNIF-NORM)` and the valuation decomposition of the local division algebra, this shows that the complete projective local commensurator at the ramified dyadic place normalizes the local Bolza subgroup:

```text
for every g_v in P D_v^*,
g_v B_v g_v^(-1)=B_v.                           (DYADIC-NORMAL)
```

In particular, for the canonical primitive double-coset correspondence,

```text
B_v cap g_v^(-1) B_v g_v = B_v.
```

So the dyadic place contributes local index `1` to the correspondence degree.

## 5. Consequence for U12 routing

The route

```text
"the remaining degree-56l correspondence might be produced by a new
ramified-dyadic level drop"
```

is blocked.  The ramified place has a nontrivial division-uniformizer class, but that class normalizes the Bolza level rather than producing a smaller local source subgroup.

Hence every nontrivial index of a primitive arithmetic Bolza correspondence must come from split finite places away from `(sqrt(2))`.

This is useful but does **not** yet close U12.  The exact MB104 passport asks for equality of two pulled-back odd theta characteristics.  `J(C2)[2]` has dimension four, whereas the explicit congruence quotient

```text
B/PQ_B^1(2)
```

sees only two mod-two characters.  A single spin equality can therefore involve a noncongruence mod-two character that is invisible to the local level quotient above.

Accordingly, `(DYADIC-NORMAL)` removes the dyadic place as a source of degree/level change, but it does not prove that an arbitrary split-prime commensurator double coset cannot satisfy the one specified spin equality.

## 6. Refined next target

The remaining arithmetic question is no longer a local-level classification.  It is the **spin transport** of split-place primitive double cosets:

```text
U12-SPIN-TRANSFER:
  for a primitive commensurator double coset Gamma g Gamma at split places,
  determine the intersection of
      p1^*{six odd theta characteristics}
  and p2^*{six odd theta characteristics}
  inside Pic(B),
  and test specifically the retained adjacent-type pair (w0,w1).
```

For the fully `S4`-equivariant standard-Hecke subclass, the previous note already excludes the correspondence.  What remains is the non-`S4`-invariant/twisted split-prime double-coset sector.

## External source boundary

K. Katz, M. Katz, M. Schein, U. Vishne,
*Bolza Quaternion Order and Asymptotics of Systoles Along Congruence Subgroups*, Experimental Mathematics 25 (2016), 399--415:

- Proposition 5.5: ramification only at `(sqrt(2))` among finite places;
- Proposition 12.2 and Section 12: exact ring `Q_B/2Q_B` and its radical filtration;
- Theorem 13.2 / Remark 13.5: `PQ_B^1(2)<B<PQ_B^1(sqrt(2))` and `B/PQ_B^1(2)~=(Z/2)^2`.

Standard local quaternion input: in a quaternion division algebra over a nonarchimedean local field, the valuation ring is the unique maximal order and its maximal ideal is unique/two-sided with square equal to the central uniformizer ideal.

## Firewalls

```text
dyadic_local_Bolza_level_normalized=true
dyadic_local_index_source=false
split_prime_spin_transfer_classified=false
arbitrary_commensurator_excluded=false
U12_closes_000707=false
U12_large_l_bound_proved=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
