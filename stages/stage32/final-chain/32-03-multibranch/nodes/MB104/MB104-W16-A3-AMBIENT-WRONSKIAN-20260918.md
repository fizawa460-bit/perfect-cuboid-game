# Stage32 MB104 — W16-A3 solo: ambient differential / Wronskian degeneracy — 2026-09-18

Status: **A3 CLOSED NEGATIVE AS AN INDEPENDENT ROUTE / W16 STILL OPEN / NO MATHEMATICAL CREDIT**

## Scope

This checkpoint advances W16-A3 only.

The retained residual coordinate admits the ambient candidate

`t=(C+W1)/(W2+iW3)`

and

`f_t=(t-i)/(t+i)`.

Algebraically this is the ratio of the two canonical linear forms

`U=C+W1+W3-iW2`,
`V=C+W1-W3+iW2`.

The archive currently source-locks the residual square-class comparison but explicitly warns that `f_t|E=h o phi` is not retained as a literal equality. Therefore the calculation below deliberately grants the **strongest favorable assumption**: suppose the degree-`56l` map `phi:E->P1` is literally the moving pencil obtained from `[U:V]` after cancelling common zeros.

If even this favorable model does not produce the W16 CB scheme, the current A3 interface cannot do better.

## 1. Wronskian on the normalization

Let

`L=nu^*K_S`.

Because `K_S.D_l=112l`,

`deg L=112l`.

Under the favorable literal-pencil assumption, removing the common base divisor `B` from `U|E,V|E` gives a base-point-free pencil defining `phi` of degree `56l`. Hence

`deg B =112l-56l =56l`.

On the smooth elliptic normalization form the Wronskian

`W=U dV - V dU`.

It is a section of

`omega_E tensor L^2`.

Since `omega_E` is trivial,

`deg div(W)=2 deg L=224l`.

Write locally

`U=g*u`, `V=g*v`

where `g` cuts out `B` and `(u,v)` is the moving pencil. Then the cross terms cancel:

`U dV - V dU = g^2 (u dv-v du)`.

The second factor cuts out the ramification divisor of `phi`. Therefore exactly

`div(W)=2B+R_phi`.

Numerically

`deg(2B)=112l`,
`deg(R_phi)=112l`,
`deg(2B+R_phi)=224l`.

So the normalization-side differential decomposition is perfectly linear.

## 2. Returning the differential to the singular carrier restores the quadratic conductor

The carrier is Cartier/Gorenstein on the smooth surface. Its dualizing sheaf is

`omega_C ~= O_C(K_S+D_l)`.

For the normalization `nu:E->C`, the conductor divisor `A_cond` satisfies

`nu^*omega_C ~= omega_E(A_cond)`

and

`deg A_cond =2Delta =336l^2+112l`.

The intrinsic Wronskian/different of the two canonical sections on the singular curve lives in

`omega_C tensor K_S^2|_C`

or equivalently

`O_C(D_l+3K_S)`.

Its degree is

`D_l.(D_l+3K_S)=336l^2+336l`.

After normalization the divisor is exactly of the expected form

`A_cond + 2B + R_phi`.

The degrees reconcile:

`(336l^2+112l)+112l+112l =336l^2+336l`.

This is the same conormal/differential mechanism encoded by the standard conormal exact sequence for a Cartier divisor and by the different of a generically etale map. The relevant general references are Stacks Project tags `06BB` and `0BWJ`.

## 3. Why determinantal geometry does not supply the missing CB condition

The full ambient differential degeneracy is therefore quadratic because it contains the complete conductor divisor.

To recover the desired small object one must remove

`A_cond`

and the doubled common-base contribution

`2B`.

After that removal one is left with

`R_phi`

and, after passing to the surface as in A2, the reduced image

`Z_red=(nu(R_phi))_red`.

But this is exactly the A2 candidate. The act of removing the conductor and the common base divisor destroys the automatic ambient determinantal presentation that one hoped would force Cayley--Bacharach.

In particular, the Wronskian identity itself gives no relation saying that a section of `|D_l|` through all but one point of `Z_red` must pass through the last point.

If instead one keeps the full ambient degeneracy scheme so that its determinantal origin is retained, its size is quadratic and it is unusable in the W16 Bogomolov window.

Thus A3 gives a strict dichotomy:

- keep the ambient determinant -> canonical but quadratic;
- strip conductor/base excess -> linear, but return to A2 with CB unresolved.

## 4. Semantic firewall strengthens the negative conclusion

The archive only retains square-class matching between the ambient `f_t` model and the residual base-cover function. It does not currently retain literal equality of the ambient pencil with `phi` on every hypothetical carrier.

The calculation above granted the stronger literal identification anyway. Since no independent CB mechanism emerges even under that favorable assumption, the weaker source-locked interface cannot make A3 succeed.

## A3 disposition

`W16-A3 = CLOSED_NEGATIVE_AS_INDEPENDENT_DIFFERENTIAL_ROUTE`.

This does **not** close W16.

A2 remains useful: it gives the linear-size lci candidate `Z_red`. What remains is still the actual CB/evaluation dependency, to be attacked by the later B1 branch.

Next solo branch: `W16-A1 direct descent`.

## Firewalls

- No literal identification `phi=[U:V]` is promoted to theorem status.
- No CB property is proved or disproved for `Z_red`.
- No locally-free Serre extension is proved.
- No `l>=2` exclusion.
- No MB104/finite-window/receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
