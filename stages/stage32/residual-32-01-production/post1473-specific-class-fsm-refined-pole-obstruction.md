# Stage32 post-1473 — refined Freitag–Salvati Manni pole obstruction for the exact V6 class

## Scope

This note applies only to the exact recovered V6 Picard class on the fixed projection

`g1-d186`, `z=(-15,62,-44,26,32)`, `d=186`,

and only to a hypothetical **integral curve of geometric genus 1 whose normalization map to the singular box surface is bijective**. It does not address the non-bijective/multibranch case.

Exact retained class locks:

- V6 witness-body canonical SHA256: `d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8`
- Picard coordinates SHA256: `2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726`
- all-140 pairings SHA256: `4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3`

## Source lock

Primary source:

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675–691, DOI `10.1307/mmj/1480734014`; arXiv `1303.6495`.

The source gives:

1. near a standard node, uniformizers `p=exp(2*pi*i*z/8)` and `q=exp(2*pi*i*w/8)`, with stabilizer acting by `(p,q) -> -(p,q)`, so the node is locally `(C^2)/(+/-1)`;
2. the minimal resolution is the blow-up at the nodes and has one exceptional line over each node;
3. Theorem 3.1 assumes the normalization map is bijective and uses a local cusp parametrization
   `alpha(tau)=tau*(r,s)+(Phi_1(t),Phi_2(t))`, where `t=exp(2*pi*i*tau)`,
   `r == s == 0 (mod 4)`, `r+s == 0 (mod 8)`, and `r,s>0`;
4. in that parametrization the pulled-back tensor has differential pole contribution `16k` and `Delta(z)^k Delta(w)^k` zero contribution `(r+s)k`;
5. the zero divisor of the auxiliary modular form contributes at least `2*k*d` zeros;
6. the pulled-back tensor has degree `16*k*(2g-2)` on the normalization.

These are exactly the ingredients used below. No claim is made that Freitag–Salvati Manni state the refined bound in this form.

## Exact local refinement

Write invariant local coordinates

`x=p^2`, `y=q^2`, `u=p*q`, so `x*y=u^2`.

Along the normalized branch, the holomorphic `Phi_i` terms contribute units, hence

- `ord_t(x)=r/4`,
- `ord_t(y)=s/4`,
- `ord_t(u)=(r+s)/8`.

The blow-up exceptional ideal is the node maximal ideal `(x,y,u)`. Therefore the intersection multiplicity `m=C.E` of the strict transform with that exceptional line is

`m = min(r/4, s/4, (r+s)/8) = min(r,s)/4`.

Hence

`r+s >= 8*m`.

Freitag–Salvati Manni's local pole estimate therefore refines from a uniform `<=8k` per visited node to

`local_pole_order <= max(0, 16-8*m)*k`.

For positive integral `m`, only `m=1` can contribute a pole, and it contributes at most `8k`. Every node with `m>=2` contributes no positive pole order.

Let `n1` be the number of exceptional curves with `C.E=1`. Then

`#poles <= 8*k*n1`.

Combining with `#zeros >= 2*k*d` and
`16*k*(2g-2)=#zeros-#poles` gives the refined necessary condition

`d <= 16*g - 16 + 4*n1`.

Taking the coarse bound `n1<=48` recovers Theorem 3.1:
`d <= 176 + 16*g`.

## Exact V6 evaluation

The exceptional suffix of the locked all-140 pairing vector has 48 entries:

- `C.E=0`: 1 entry;
- `C.E=1`: 9 entries;
- `C.E>=2`: 38 entries.

Thus `n1=9`. For `g=1`, the refined necessary condition is

`d <= 4*n1 = 36`.

The exact class has `d=186`, so

`186 > 36`.

Therefore this exact V6 Picard class cannot contain an integral geometric-genus-one curve whose normalization map to the singular box surface is bijective.

## Firewall

This is a **bijective-normalization branch exclusion only**. It does not exclude an integral geometric-genus-one carrier with a non-bijective normalization map (multiple branches over a singular point), does not classify all low-genus curves, does not close FULL178, and grants no receiver/theorem/endpoint or perfect-cuboid claim.
