# Stage14-4fi — endpoint strips are too small for a surviving heavy radial packet

## Status

`COMPLETE_RECIPROCAL_WINDOW_ENDPOINT_STRIP_REMOVAL`

Consumes batch-local `Stage14-4fh` and merged `Stage14-4ff/4fg`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Freeze the radial exponent cell

On one surviving heavy ray let

```text
n = B^(nu+o(1)),
|N_*| >= B^(mu-o(1)),
0<mu<=nu,
```

where merged 4ff gives

```text
nu <= rho-delta,
rho=1/4-phi<=1/24.
```

Batch-local 4fh gives the exact geometric radial window

```text
N_geom=[N_-,N_+]
```

and the logarithmic L-window overlap `omega(n)`, vanishing only at `N_-` and `N_+` and growing linearly in logarithmic distance from an active endpoint.

## 2. Define polynomially thin endpoint strips

Fix any exponent

```text
theta>nu-mu.
```

Because `mu>0`, one may choose `theta<nu` whenever `nu>mu`; in the near-capacity case `nu=mu+o(1)`, any fixed sufficiently small positive `theta` works.

Define the two endpoint strips by logarithmic distance

```text
E_-(theta): 0 <= log(n/N_-) <= B^(-theta),
E_+(theta): 0 <= log(N_+/n) <= B^(-theta).
```

For `n` on scale `B^nu`, each strip contains at most

```text
O(1+B^(nu-theta+o(1)))
```

integers. Therefore

```text
#(E_-(theta) union E_+(theta))
 <= B^(nu-theta+o(1))+B^o(1)
 = o(B^mu).
```

Thus the endpoint strips cannot carry the required heavy support.

```text
RADIAL_ENDPOINT_STRIP_COUNT_EXPONENT=nu_minus_theta
THETA_GT_NU_MINUS_MU_KILLS_ENDPOINT_SUPPORT=true
HEAVY_SUPPORT_CANNOT_CONCENTRATE_AT_RECIPROCAL_WINDOW_ENDPOINTS=true
```

## 3. Surviving mass is forced into the interior overlap region

Let

```text
N_int(theta)
 := N_* \ (E_-(theta) union E_+(theta)).
```

Then

```text
|N_int(theta)| >= B^(mu-o(1)).
```

By the exact piecewise-linear overlap profile from 4fh, there is a frozen chart constant `c>0` such that every `n in N_int(theta)` satisfies

```text
omega(n) >= c*B^(-theta)
```

until the overlap reaches its fixed chart cap. Equivalently the geometric L-window has multiplicative width

```text
sup W(n)/inf W(n)
 >= exp(c*B^(-theta))
 = 1 + B^(-theta+o(1)).
```

So a heavy survivor is not an endpoint phenomenon. It requires polynomially many normalized radial integers for which the two physical root windows have a genuine interior intersection of explicitly controlled relative width.

```text
HEAVY_INTERIOR_RADIAL_SUPPORT_EXPONENT=mu
INTERIOR_L_WINDOW_RELATIVE_WIDTH_LOWER_BOUND=B^(-theta+o(1))
ENDPOINT_HEADROOM_ANALOGUE_REMOVED_ON_GLOBAL_HEAVY_BRANCH=true
```

## 4. No divisor theorem has yet been charged

This stage counts only the outer integer coordinate `n`. It does not assume that an interval of relative width `B^-theta` contains an admissible squareclass divisor with any particular probability.

The existing facts remain charged once:

```text
fixed n -> admissible L candidates = B^o(1),
bare Jab=c0*n support is dense,
all primitive/canonical/reverse masks remain attached to the same L candidate.
```

Hence endpoint removal is a geometric support reduction, not a divisor-density saving.

```text
SHORT_DIVISOR_INTERVAL_DENSITY_NOT_ASSUMED=true
FIXED_N_L_FIBER_RECHARGED=false
```

## 5. Receiver and H decision

The heavy receiver is unchanged in arithmetic type, but its mass is now forced onto the interior part of the reciprocal window. The next stage should package this as the minimal interior physical divisor-window selector and determine whether any remaining bundled physical mask must be opened before an independent theorem audit.

```text
RECEIVER_MATERIALLY_CHANGED=false
NEW_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fj
```
