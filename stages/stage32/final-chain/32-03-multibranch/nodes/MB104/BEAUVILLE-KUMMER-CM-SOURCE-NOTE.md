# Stage32 MB104 source note — Beauville/Kummer elliptic quotient and CM field

Status: **EXTERNAL PUBLISHED SOURCE ADAPTER / NO CLOSURE / NO CREDIT**

## Source

Eberhard Freitag and Riccardo Salvati Manni,
*Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675--691, DOI `10.1307/mmj/1480734014`, especially Sections 2 and 5.

Only the following published facts are imported here.

## 1. The index-two elliptic quotient of `X(8)`

Let

```text
C8 = H*/Gamma[8].
```

For the index-two group `Gamma_1[8] cap Gamma[4]`, Freitag--Salvati Manni give the graded ring

```text
a^2=c^2+d^2,
b^2=c^2-d^2,
```

and identify the associated elliptic curve over `Q` with

```text
E0: y^2=x^3-x.
```

Thus

```text
j(E0)=1728,
End^0(E0)=Q(i).
```

The paper also identifies the relevant order-two modular transformation `T` as acting trivially on this elliptic quotient. Equivalently, for the corresponding involution on `C8`, the quotient is `E0`.

## 2. Relation to the box-coordinate sign involution

The paper considers the box involution

```text
sigma(Z3)=-Z3
```

and states that in the theta-parametrization it is induced by

```text
(z,w) -> (T z,w).
```

The three singular node-stabilizer types are permuted by the modular `S_3` symmetry, as recorded in the retained Stage32 node-type adapter. Therefore, after conjugating coordinates, the same statement applies to each of the three singular types `Zj=0`: if `s` is the corresponding diagonal singular involution on `C8 x C8`, then each factor quotient

```text
C8/<s_factor> 
```

is a conjugate of the displayed elliptic quotient and has CM field `Q(i)`.

For the present MB104 use, only the CM field and the fact that both factor quotients are the same elliptic quotient for one fixed singular type are required.

## 3. Kummer quotient

Freitag--Salvati Manni define two involutions `tau,rho` on `E0`, generating

```text
H ~= (Z/2)^2,
```

with `rho` fixed-point-free (translation by a two-torsion point) and `tau` an involution with fixed points. They prove

```text
(E0 x E0)/H  ~=  B/sigma
```

over the Gaussian field (and after the stated base extension identify it with a Kummer quotient).

Therefore the quotient map from `C8 x C8` to `B/sigma` factors through the two factor quotient maps to `E0` and then the fixed finite group `H` of order four.

## 4. Arithmetic fact used downstream

The rational prime `7` is inert in `Q(i)` because

```text
x^2+1
```

has no root modulo `7` (`7 == 3 mod 4`). Hence `Q_7(i)/Q_7` is the unramified quadratic extension. If `u in Q(i)^*` has field norm `1`, then its `7`-adic valuation is zero, so `u` is a unit in `Z_7[i]` and acts invertibly on the `7`-primary torsion of `E0`.

This last paragraph is elementary local number theory, not an additional published claim of Freitag--Salvati Manni.

## Firewall

- This note does not assert existence or nonexistence of a Stage32 carrier.
- It does not classify all elliptic quotients of `C8`; it imports only the quotient needed for the matching singular type, up to the retained `S_3` conjugacy.
- No receiver/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
