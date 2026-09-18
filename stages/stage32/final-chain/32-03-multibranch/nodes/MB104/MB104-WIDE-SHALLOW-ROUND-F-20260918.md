# Stage32 MB104 — wide shallow closure scan Round F — 2026-09-18

Status: **ROUND F COMPLETE / W26--W30 SCREENED / NO PROMOTE / BROADER DIRECTIONS RETAINED / NO CREDIT**

## W26 — equisingular T-smoothness / Severi regularity

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK (HIGHER VALUE)**

This direction is structurally attractive: the retained dangerous ray is extremely special, so any theorem forcing expected-codimension equisingular behavior could contradict it.

But the readily available theorems do not directly apply.

- Chiantini--Sernesi's general-type result is formulated for curves numerically proportional to the canonical class `pK`.
- Keilen's clean Theorem 2.1 assumes `NS(S)=Z.L`, i.e. Picard rank one.

The MB104 class

```
D_l=7lH-4l sum E_i
```

lives in the high-rank cuboid lattice and is not proportional to `K=H`.

Therefore direct theorem import is invalid.

The broader direction remains important: a cuboid-specific high-rank version of the same Bogomolov/zero-dimensional-scheme argument could attack the exact retained superabundance.

## W27 — semiregularity map

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

The canonical morphism is to `P6`, so `p_g=7`; with `chi(O_S)=8`, this gives `q=0`.

For an immersed elliptic normalization map,

```
deg N_f=-K.D_l=-112l.
```

Hence on the elliptic normalization

```
h0(N_f)=0,
h1(N_f)=112l.
```

The classical semiregularity target has dimension

```
h2(O_S)=p_g=7.
```

Thus a map

```
H1(N_f) -> H2(O_S)
```

cannot be injective for any `l>=1`.

So ordinary semiregularity cannot turn the negative expected dimension into an emptiness statement.

A reduced/cosection obstruction theory remains a different, open mechanism.

## W28 — multiplier ideal / connectedness

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

The standard non-klt connectedness architecture needs log-Fano positivity, schematically

```
-(K_S+B) nef and big.
```

Here `K_S=H` is already big and nef and the carrier boundary is effective.  Thus `K_S+B` points in the positive, not negative, direction.

The usual connectedness theorem therefore cannot force the fourteen packet centers to form one connected non-klt locus.

Multiplier ideals used for interpolation or vanishing, rather than connectedness, remain logically separate.

## W29 — cotangent semistability on the elliptic normalization

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

For an immersed normalization

```
0 -> N_f^* -> f^*Omega_S -> Omega_E -> 0.
```

The degrees are

```
deg f^*Omega_S = K.D_l =112l,
deg N_f^*=112l,
deg Omega_E=0.
```

This is compatible with generic nefness/semipositivity: there is no forced negative quotient.

A sufficiently strong stability theorem might forbid the degree-zero quotient, but generic restriction theorems do not automatically apply to this very special singular carrier.

## W30 — Wahl/Gaussian dimension

**tested architecture: HARD-DROP**  
**broader direction: SOFT-PARK**

Let `L=nu^*O_S(H)`, `deg L=112l`.  The ambient canonical coordinates span only a seven-dimensional subspace `V subset H0(E,L)`.

The first Gaussian map built from that ambient subspace has source

```
wedge^2 V,
dim=21,
```

while the natural elliptic target has dimension

```
h0(E,L^2)=224l.
```

Thus there is no source-to-target dimension overload; non-surjectivity is automatic.

A special Gaussian identity coming from the four-quadric canonical model could still be meaningful, but bare dimensions cannot close MB104.

## Round F result

```
W26 architecture HARD / direction SOFT (higher-value)
W27 architecture HARD / direction SOFT
W28 architecture HARD / direction SOFT
W29 architecture HARD / direction SOFT
W30 architecture HARD / direction SOFT

PROMOTE = none
```

No mathematical credit changes.
