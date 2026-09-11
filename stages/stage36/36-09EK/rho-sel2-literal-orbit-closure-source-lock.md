# Stage36 36-09EK — rho Sel2 literal-curve orbit closure source lock

## Purpose

36-09EJ proves exact fixed-parameter receiver exclusion for 14 positive rational parameters by combining the generic 36-09EH rho criterion with exact Sel2 dimensions on the 62-row AX box. This leaf asks what follows **without any new Sel2 computation**, using only the literal equality symmetries of the hostile-audited physical top genus-3 curve.

## Generic literal top curve

From 36-09O,

```text
c(p)=(p+1)/(p-1),
C3_p: y^2=(t^2+p^2)(t^2+p^(-2))(t^2+c(p)^2)(t^2+c(p)^(-2)).
```

The retained boundary is always `t=0,+1,-1,infinity`.

For an allowed positive rational `p != 1`, define the positive literal orbit

```text
O(p)={p,1/p,|c(p)|,1/|c(p)|}.
```

Direct identities give

```text
c(1/p)=-c(p),
c(c(p))=p.
```

Therefore all four parameters in `O(p)` produce the same unordered coefficient multiset

```text
{p^2,p^(-2),c(p)^2,c(p)^(-2)}
```

and hence the literally identical normalized curve over Q with the same retained boundary. No change of variable, twist, scalar extension, or squareclass branch is used.

Conversely, if a positive rational `q` gives the same literal coefficient multiset, then `q^2` is one of the four displayed coefficients, so `q` is one of the four positive values in `O(p)`. Thus this positive literal orbit is exact and complete.

## Orbit decomposition of the EJ registry

36-09EJ promotes the 14-value fixed-parameter exclusion registry

```text
{1/5,1/3,1/2,2/9,2/7,2/3,3/2,9/5,2,5/9,9/2,7/2,3,5}.
```

These values lie in four exact literal-curve orbits:

```text
O(2)   ={1/3,1/2,2,3},
O(1/5) ={1/5,2/3,3/2,5},
O(2/7) ={2/7,5/9,9/5,7/2},
O(2/9) ={2/9,7/11,11/7,9/2}.
```

The first three orbits are already fully represented in the EJ registry. The fourth has only `2/9` and `9/2` inside the AX box; its other two members are

```text
7/11, 11/7.
```

Because `C3_(7/11)` and `C3_(11/7)` are literally the same retained curve as the already-excluded `C3_(2/9)`, both physical receiver sectors are empty by the same exact 36-09O forward adapter. No new local, Selmer, rank, or Brauer computation is required.

## Exact impact

After CI consumption, the fixed-parameter exclusion registry expands from 14 to 16 values. In increasing numerical order it is

```text
{1/5,2/9,2/7,1/3,1/2,5/9,7/11,2/3,3/2,11/7,9/5,2,3,7/2,9/2,5}.
```

The genuinely new values relative to EJ are exactly

```text
{7/11,11/7}.
```

## Credit firewall

This is still a finite registry of proved fixed-p exclusions, not an exhaustive physical-parameter ledger. Therefore this leaf does not prove

```text
candidate_parameter_set_shrunk,
receiver_emptiness_proved,
R29_CAMP2_closed,
Q11_CAMPEDELLI_closed,
endpoint_closed,
perfect_cuboid_nonexistence_claim.
```

The next useful step is to exploit the special full-2 model symbolically, rather than enlarging the bounded box: derive a scalable Sel2 matrix / arithmetic criterion in terms of the prime factors and quadratic residue data of `N=a^2-b^2`, `d=ab`, `N+2d`, and `N-2d`.
