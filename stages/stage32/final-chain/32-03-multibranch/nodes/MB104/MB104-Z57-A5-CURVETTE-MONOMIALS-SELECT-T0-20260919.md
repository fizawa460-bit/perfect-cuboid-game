# MB104 Z57 — A5 curvette monomial preflight / endpoint-globalization correction — 2026-09-19

Status: **CORRECTED PRE-AUDIT LOCAL-ONLY CALCULATION / T0 NOT PROVED / NO CREDIT**

## Correction

An earlier pre-audit version incorrectly promoted the local A5 monomials to functions on the final
contracted germ and concluded tangent type T0.

That promotion is withdrawn.

The error is precise: after contracting only the central A5 chain, the standard local coordinates

```
uv=s^6
```

exist near the A5 point, but `u,v,s` are only local functions near that point.  The final
contraction also collapses the two full elliptic endpoint curves.  A local function near the
attachment does not automatically extend around an entire elliptic endpoint neighborhood.

In fact Z51 gives the exact endpoint normal bundle

```
N_E ~= O_E(-2p),
```

which is nontrivial.  Thus a local transverse parameter `s` cannot be treated as a globally
defined principal equation for E on its full negative neighborhood without an additional
trivialization/transition adapter.

Therefore the former statements

```
y=us, z=vs, w=s^2, x=s^3 are global maximal-ideal generators,
x^2,yz in m^3 globally,
actual tangent type=T0
```

are **not retained**.

## 1. What remains exact locally

The central fixed chain

```
Gamma=C1+...+C5
```

is an A5 rational-double-point chain.

After contracting Gamma alone, one may choose local analytic coordinates

```
uv=s^6.
```

The two elliptic endpoint branches are opposite-end curvettes.  The divisorial valuations on the
seven-component resolution are locally

```
val(s)=(1,1,1,1,1,1,1),
val(u)=(6,5,4,3,2,1,0),
val(v)=(0,1,2,3,4,5,6),
```

after orientation.

Consequently the local monomials

```
us, vs, s^2, s^3
```

have exactly the valuation patterns that would produce T0 **if** they globalized to four
maximal-ideal generators on the complete elliptic plumbing.

That implication is conditional only.

## 2. Exact missing adapter

For an endpoint E with marked attachment p,

```
N_E ~= O_E(-2p).
```

Choose two analytic charts on E and local transverse coordinates t_i.  On overlaps

```
t_j = g_ij t_i + O(t_i^2),
```

where `{g_ij}` are transition functions for the nontrivial normal bundle.

The local A5 coordinate `s` agrees with a transverse parameter near p.  To globalize `s^k`
around E requires the corresponding transition class in

```
N_E^{-k} ~= O_E(2kp)
```

to be represented by a compatible holomorphic section with the required attachment jet.

Hence the actual Z55 tangent bit depends on a **global endpoint transition/gluing calculation**,
not merely the A5 valuation semigroup.

## 3. Why the contradiction check catches the error

If the four local expressions were blindly promoted to global generators, they would satisfy

```
x^2=w^3,
yz=w^4.
```

The resulting codimension-two germ

```
(x^2-w^3, yz-w^4)
```

has a non-isolated singular locus along the y/z axes when x=w=0.

But Z51/Z52 establish that the actual canonical-cover surface germ is an isolated normal
surface singularity.

This contradiction confirms that the local A5 monomials cannot by themselves be the complete
global minimal generator system.

## 4. Correct route

The valid retained state is still

```
T0 or T1,
q1=x^2,
q2=yz+c xw,
c=0 versus c!=0 unknown.
```

Z56 remains useful: it identifies one first-normal tangent direction beyond the three sections
visible on the reduced exceptional divisor.

The next calculation must globalize sections across both elliptic endpoint neighborhoods using
their exact normal bundles and the attachment-point jets.

## 5. New active leaf

```
MB104-Z57R-ENDPOINT-GLOBALIZATION-OF-MAXIMAL-IDEAL-SECTIONS
```

Target:

1. use `E_1728`, marked p and `N_E=O_E(-2p)`;
2. construct the global sections of `O_X(-F)` and the unique first-normal tangent section through
   the endpoint formal neighborhoods;
3. match them to the central A5 local basis;
4. evaluate the single product coefficient `c` in
   `yz+c xw` modulo m^3.

The local A5 valuation table is allowed only as the central matching condition.

## Firewalls

```
local_A5_valuation_table_valid=true
local_A5_monomials_global_generators=false
actual_tangent_type_T0=false
actual_tangent_type_T1=false
mixed_coefficient_c_known=false
downstairs_local_correction_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
