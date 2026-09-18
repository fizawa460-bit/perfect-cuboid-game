# Stage32 MB104 — W14 active `000707` primitive restriction-map preflight — 2026-09-18

Status: **PASS TO SECOND SCAN / ONE CHARACTERISTIC-ZERO RANK BIT REMAINS / NO CREDIT**

## Target

For the active support

```
Sigma=000707000f0f,
A=7H-4 sum_(p in Sigma)E_p,
```

the retained zero-quartic geometry gives two elliptic quartics `Q0,Q1` with

```
A.Qj=0,
O_Qj(A) ~= O_Qj.
```

The direct-closing question is whether

```
H^0(S,O(A)) -> H^0(Qj,O_Qj) ~= k
```

is zero or nonzero.

## Existing size-48 computation reused as algorithm only

The historical size-48 verifier constructs the degree-7 canonical basis, imposes the exact `m_p^4` conditions at fourteen A1 nodes, and computes a good-prime rank over `p=1097`.

The same algorithm is applied here to the active `000707` support; no size-48 cohomology conclusion is imported.

## Good-prime result

Use

```
p=1097,
i=341.
```

For the active support the degree-7 jet matrix has

```
224 rows,
344 columns,
rank_p = 220.
```

Choose smooth finite-field points away from all 48 nodes:

```
Q0 point = [1,1,341,0,0,407,1],
Q1 point = [756,1,1,407,0,0,1].
```

Appending either evaluation row raises the rank to `221`; appending both still gives `221`.

Thus

```
rank_p(jet)=220,
rank_p(jet+Q0)=221,
rank_p(jet+Q1)=221,
rank_p(jet+Q0+Q1)=221.
```

A nonzero minor mod a good prime survives in characteristic zero, so

```
rank_0(jet) >=220.
```

## Characteristic-zero upper bound

For `A`,

```
chi(O(A))=120,
H^2(O(A))=0.
```

The retained connected null-union cohomology for `000707` gives

```
h^1(O(A)) >=3.
```

Hence

```
h^0(O(A)) >=123,
rank_0(jet) <=344-123=221.
```

Therefore the primitive characteristic-zero jet rank is reduced to exactly one bit:

```
rank_0(jet) in {220,221}.
```

If it is `220`, the characteristic-zero augmented rank is at least `221`, so the restriction is nonzero. The support stabilizer is transitive on the two zero quartics, hence both are nonfixed; powers then show nonfixedness for every `l>=1`.

If it is `221`, this finite-field preflight alone does not decide the restriction.

## Exploratory stability

The same numerical rank pattern was observed at ten good-looking primes congruent to one mod four:

```
1009,1013,1021,1033,1049,1061,1093,1097,1109,1129.
```

At each:

```
jet=220,
+Q0=221,
+Q1=221,
+Q0+Q1=221.
```

This cross-prime pattern is **not used as a theorem**. It only motivates one second shallow exact-rank test.

## Decision

W14 survives exactly one more shallow test.

The next test is not an adapter project. It is one exact characteristic-zero linear-algebra/cohomology question:

```
rank_0(jet)=220 or 221?
```

Equivalently, certify either a 124-dimensional primitive section space or an exact characteristic-zero dependency forcing rank 220.

No conclusion about MB104 closure is claimed.
