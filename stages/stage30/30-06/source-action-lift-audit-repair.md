# Stage30-06 — bounded source-action lift audit repair

The submission's original `S_hat,T_hat` form a correct projective `S4` action and give the correct `V_mod` sign-deck restriction, but they were selected as lifts of the Stage30-05 branch action rather than derived from the diagonal modular action on the Testa--Stoll common model. That is too weak for the Stage30 action-level adapter.

Audit repairs the lift directly from the source model

```text
X(8): u^2=2xy, v^2=x^2-y^2, w^2=x^2+y^2.
```

Using the audited X(4) gauge, choose on one X(8) factor

```text
S:
x'=(-x+y)/sqrt(2), y'=(x+y)/sqrt(2),
u'=i*v, v'=i*u, w'=w,

T:
x'=i*x, y'=y,
u'=zeta_8*u, v'=i*w, w'=i*v.
```

These preserve the X(8) equations exactly and project to the required X(4) actions. Different choices of the square-root signs differ by `G0`, hence disappear under the diagonal `G0` quotient.

Applying the transformations diagonally to `X(8)xX(8)` and passing through

```text
U=u1u2=2b1, V=v1v2=2b2, W=w1w2=2b3,
X=x1x2=a1+c, Y=y1y2=-a1+c,
T=x1y2=a2+i*a3, Z=x2y1=a2-i*a3
```

gives the Q(i)-defined source-derived endpoint action

```text
S0:
a1->-a2, a2->-a1, a3->-a3,
b1->-b2, b2->-b1, b3->b3, c->c,

T0:
a1->-c, c->-a1,
a2->i*a2, a3->i*a3, b1->i*b1,
b2->-b3, b3->-b2.
```

The original submitted lifts differ from these by sign-deck corrections

```text
S_submitted = delta_{b1,b2} * S0
T_submitted = delta_{b2,b3} * T0.
```

Therefore the original section was a sign-deck-twisted splitting, not yet the literal source-derived diagonal modular action.

Crucially, replacing it by `S0,T0` leaves the load-bearing Stage30-06 conclusions unchanged:

```text
S0^2=1, T0^4=1, (S0*T0)^3=1 in PGL7(Q(i));

g12=T0^2              -> negate {a2,a3,b1}
g06=S0*T0^2*S0^-1     -> negate {a1,a3,b2}
g14=g12*g06           -> negate {a1,a2,b1,b2};

c_sigma=delta_a3;
theta(S)=S;
theta(T)=T^-1;
theta|V_mod=id;

sigma(S0)=c_sigma*S0*c_sigma^-1;
sigma(T0)=c_sigma*T0^-1*c_sigma^-1.
```

Thus the V4 sign-deck lift and generator-level semilinear identity survive exactly, but the source-action anchor is now explicit rather than inferred from an arbitrary lift of the branch permutation action.

The exhaustive all-24 check remains intentionally owned by Stage30-06C and receives no credit from this bounded audit repair.
