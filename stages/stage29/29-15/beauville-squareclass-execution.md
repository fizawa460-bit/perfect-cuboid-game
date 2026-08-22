# Stage29-15 audit execution — explicit Beauville squareclass function

```text
AUDIT_DISCOVERY=true
R29-BEAU1B=DISCHARGED_EXPLICIT_Q_SQUARECLASS_FUNCTION_AND_CODIM1_PARITY
R29-BEAU1C=PARTIAL_EXACT_RAMIFICATION_FORMULA_DONE_UNIFORM_SUPPORT_THEOREM_OPEN
```

The submitted triage placed `R29-BEAU1B` in class 2 because no explicit function-field generator had been materialized. The audited 29-02d data already suffice to construct one, so this receiver is an additional class-1 task and is executed here.

## 1. Geometric generator on Beauville's cover

Use the cuboid specialization

```text
C0: u^2=x*y, v^2=x^2-y^2, w^2=x^2+y^2,
X_B=(C0 x C0)/Delta(Gamma), Gamma=(Z/2)^2
```

with `Gamma` the even-sign subgroup. On the dense chart `x0*x1 != 0`, define

```text
r0=u0*v0*w0/x0^3,
r1=u1*v1*w1/x1^3.
```

Each `ri` is invariant under the diagonal even-sign `Gamma`, while the canonical deck involution (the odd-sign coset) changes both signs. Factor exchange swaps `r0` and `r1`. Hence

```text
s=r0+r1
```

is a nonzero deck-anti-invariant rational function on `X_B`, symmetric under factor exchange. Therefore it survives the audited Q(i)/Q factor-swap descent and gives a Q-rational anti-invariant generator on the descended cuboid cover `X_cub/Q`. Since the cover has degree two,

```text
Q(X_cub)=Q(S_cub)(s),  s^2=F_B.
```

## 2. Exact base function

Write Beauville's canonical invariant coordinates as

```text
A=x0*x1, B=x0*y1, C=y0*x1, D=y0*y1,
U=u0*u1, V=v0*v1, W=w0*w1.
```

Then

```text
r0^2=(C/A)*(1-(C/A)^4),
r1^2=(B/A)*(1-(B/A)^4),
r0*r1=U*V*W/A^3,
```

so

```text
F_B=s^2
=[C(A^4-C^4)+B(A^4-B^4)+2*U*V*W*A^2]/A^5.
```

This expression is symmetric in `B,C`, as required by the Q(i)/Q swap cocycle.

Under the audited linear adapter

```text
A=x+t,
B=y+i*z,
C=y-i*z,
U=u,
V=2*v,
W=2*w,
```

on the standard cuboid model

```text
t^2=x^2+y^2+z^2,
u^2=y^2+z^2,
v^2=x^2+z^2,
w^2=x^2+y^2,
```

direct expansion gives the Q-rational function

\[
\boxed{
F_{cub}=
\frac{2\left(y(x+t)^4-y^5+10y^3z^2-5yz^4+4uvw(x+t)^2\right)}{(x+t)^5}.
}
\]

On the positive physical endpoint chamber, `x>0` and `t>0`, so `x+t>0`; this chart contains every physical endpoint point.

## 3. Torsor class and divisor parity

For a physical rational point `P` away from the zero locus of the chosen generator,

```text
delta(P)=F_cub(P) mod Q*^2.
```

The canonical Beauville double cover is quasi-etale: its only ramification occurs over the 48 nodes, which are codimension two on the normal base. Therefore the quadratic function-field extension is unramified at every codimension-one valuation. Equivalently,

```text
v_D(F_cub) is even for every prime divisor D of S_cub.
```

This is the exact divisor-parity datum needed by `R29-BEAU1B`; an explicit decomposition of the even divisor is not required to know the generic torsor squareclass.

## 4. Exact pointwise ramification formula

Set

```text
L=x+t,
N=y*L^4-y^5+10*y^3*z^2-5*y*z^4+4*u*v*w*L^2.
```

Since `F_cub=2N/L^5`, in `Q*/Q*^2` one has

```text
delta(P) = 2*L*N mod Q*^2.
```

Thus for every odd prime `p`, the quadratic fiber class ramifies exactly when

```text
v_p(2*L*N) is odd.
```

At `p=2`, the complete local squareclass is likewise determined by `v_2(2LN) mod 2` and the odd unit modulo `8` after removing the even valuation part.

This pointwise formula executes the finite/local core of `R29-BEAU1C`. What remains is no longer a missing explicit model: it is a **uniform theorem over all physical endpoint points** controlling the possible support/reciprocity of these point-dependent squareclasses strongly enough to reduce the infinite twist family. Hence the residual `R29-BEAU1C` is routed to class 3 rather than class 2.

## 5. Firewalls

```text
FINITE_PHYSICAL_TWIST_SET_PROVED=false
UNIFORM_RAMIFICATION_SUPPORT_PROVED=false
BEAUVILLE_TWIST_FAMILY_CLOSED=false
ENDPOINT_QPOINT_EXCLUDED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
