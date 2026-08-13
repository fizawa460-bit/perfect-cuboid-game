# Stage14-4bm — merged s6-08 integration note

After the initial 4bm branch was prepared, Stage14-s6-08 merged to `main`.

4bm therefore formally imports the following merged s6-08 facts:

- the complete good gcd matrix is an automatic square prefactor,
  `Delta0 = X2_good^2 * Delta_norm`;
- the normalized residual is an exact square;
- it splits into two coupled difference-of-squares factors `F,G` with
  `ker(F)=ker(G)` on every physical image;
- independent tensorization of the two normalized factors is not the correct next model;
- the correct analytic receiver is a same-modulus normalized kernel collision.

These merged facts strengthen, but do not alter, the new 4bm theorem:

```text
X2_cross >= B^(4/21)
=> physical cross sector << B^(61/63+o(1)),
```

which gains exactly `1/126` relative to the current `41/42` physical exponent.

Thus the only unresolved 4bm branch is now the merged-s6-08 normalized same-kernel family with

```text
X2 > B^(20/21),
X2_cross < B^(4/21),
max(q--,q-+,q+-,q++) >> B^(4/21),
ker(F)=ker(G).
```

The next main-track target remains Stage14-4bn: obtain signed same-modulus cancellation on this normalized kernel collision without charging the automatic gcd square prefactor a second time.

```text
MERGED_S6_08_FORMALLY_IMPORTED=true
NORMALIZED_BIQUADRATIC_KERNEL_COLLISION_IMPORTED=true
CROSS_SECTOR_BOUND_UNCHANGED=B^(61/63+o(1))
NEXT=Stage14-4bn
```
