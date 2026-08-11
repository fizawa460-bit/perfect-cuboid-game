# Stage14-4ey — fixed-ray squareclass reconstructs the xi-agreement product

## Status

`COMPLETE_FIXED_RAY_SQUARECLASS_TO_XI_AGREEMENT_PRODUCT_RECONSTRUCTION`

Consumes merged `Stage14-4ex`, merged `Stage14-s7-29`, merged `Stage14-s7-46`, merged `Stage14-s7-70`, merged `Stage14-Work-boX27`, and latest main `7f8b5c1f683a68ba2bcf8a9393b26d8872a5c457`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

Merged 4ex freezes one heavy primitive reciprocal ray and gives, after finite sign/two-primary localization,

```text
T = K*w^2,
T = 4*Xr*Yr*epsilon_x*U*V,
```

where `K` is the fixed squarefree kernel of the primitive-ray difference, `(U,V)` is the primitive xi-agreement pair, and `Xr*Yr` is the physical root-product coordinate from the exact second reciprocal identity.

Put

```text
Z := oddpart(Xr*Yr),
D := U*V = oddpart(R*J).
```

Merged s7-46 gives

```text
R,J squarefree and coprime,
D=oddpart(RJ),
gcd(U,V)=1.
```

Hence `D` itself is odd squarefree. Freeze the finite two-primary/unit squareclass from `4*epsilon_x`; it costs `B^o(1)` and changes no fixed-power statement. In the odd squareclass group the 4ex identity is exactly

```text
[Z] [D] = [K].
```

Because a positive odd squareclass has a unique squarefree representative and `D` is already squarefree,

```text
boxed:
D = sf_odd(K*Z)
```

up to the already-frozen `B^o(1)` endpoint/2-primary decoration convention.

Thus the agreement product is **not** an independent polynomial squareclass once `(K,Z)` is fixed. After `D` is reconstructed, the ordered coprime split

```text
D=U*V
```

has at most

```text
tau(D)=B^o(1)
```

possibilities, with all physical range/allocation masks only reducing the set.

This is a charged-once squareclass reconstruction, not a generic square-density saving. The moving variable is now the root product `Z`, and the physical selector becomes whether its squareclass against fixed `K` produces the required balanced xi-agreement product.

```text
XI_AGREEMENT_PRODUCT_ODD_SQUAREFREE=true
FIXED_RAY_SQUARECLASS_IDENTITY=[Z][D]=[K]
XI_AGREEMENT_PRODUCT_RECONSTRUCTED_FROM_K_AND_Z=true
FIXED_K_Z_TO_U_V_MULTIPLICITY=Bo1
GENERIC_SQUARE_DENSITY_RECHARGE_ALLOWED=false
RECEIVER_MATERIALLY_CHANGED=false
NEXT_H_NEEDED=false
NEXT=Stage14-4ez
```
