# Stage14 targeted addendum — perfect-cuboid endpoint upper corollary

```text
ADDENDUM_KIND=TARGETED_THEOREM_SURFACE_COROLLARY
SOURCE=stages/stage14/final.md
DISCOVERED_BY=Stage29_GAP_SCAN_B_PR1316
STAGE14_ENDPOINT_COROLLARY=VALID_MISSED_COROLLARY
CHANGES_STAGE14_PROOF=false
CHANGES_STAGE14_THEOREM_2_1=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

This addendum records an immediate consequence of the already frozen Stage14 proof chain that was not advertised in the final theorem surface.

## Frozen definitions

Stage14 fixes

```text
C(B)={(a,b,c,d): 0<a<b<c, gcd(a,b,c)=1,
      a^2+b^2+c^2=d^2, d integer, d<=B}
```

and lets `N_j(B)` count members having exactly `j` integral face diagonals. Thus

```text
T(B)=N_3(B)
```

is the primitive canonical perfect-cuboid count under the same `d<=B` cutoff.

## Existing load-bearing chain

Lemma 3.1 proves on the whole physical raw-pair graph

```text
E(B)=N_2(B)+3T(B).
```

Exactly-two cuboids contribute one unordered integral-face pair and triple-face cuboids contribute three. The transcribed gluing proof proves multiplicity one after primitive normalization and orientation.

Lemma 3.2 proves for the same `E(B)`

```text
E(B)<<V(B)B^o(1).
```

Proposition 3.3 is a complete-host cover of every physical active face; later physical and third-face masks only delete candidates. Lemmas 3.4–3.5 reconstruct the complete cells with divisor/subpolynomial multiplicity and likewise treat the final masks as rejecting filters. Proposition 3.6 exhausts all physical active-face cells and proves

```text
V(B)<<B^(1/2+o(1)).
```

No step in this chain applies an exactly-two mask before bounding the raw graph or its active-face host.

## Corollary

By positivity,

```text
3T(B)<=E(B)<<V(B)B^o(1)<<B^(1/2+o(1)).
```

Hence

```text
T(B)<<B^(1/2+o(1)).
```

Equivalently:

> For every `epsilon>0` there exist constants `C_epsilon>0` and `B_epsilon>=1` such that, for every real `B>=B_epsilon`, the number `T(B)` of primitive canonical perfect cuboids with integral space diagonal `d<=B` satisfies
> `T(B)<=C_epsilon B^(1/2+epsilon)`.

This is an upper bound only. It does not prove that `T(B)` is zero for any unbounded range, that a perfect cuboid exists, or that one does not exist.

## Stage29 endpoint dictionary

Stage29 uses

```text
U(B)={0<a<b<c, gcd(a,b,c)=1, R=sqrt(a^2+b^2+c^2)<=B}
P(B)=#(all-three-face points in U(B) with R integer).
```

On the endpoint locus `R=d`, so the cutoffs and primitive/canonical conventions agree exactly. Therefore for every real `B>=1`,

```text
P(B)=T(B),
```

and the imported endpoint theorem is

```text
P(B)=T(B)<<_epsilon B^(1/2+epsilon)
```

for every `epsilon>0`.

## Historical-scope clarification

Stage14's statement that it proves no perfect-cuboid existence/nonexistence result remains correct. The missed statement is a quantitative upper bound on the perfect-cuboid counting function, not an emptiness theorem.
