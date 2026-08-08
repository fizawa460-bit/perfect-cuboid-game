# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AF_COMPLETE_POSITIVE_RANK_SPECIALIZATION_14_4AG_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 counts primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals. Stage14-1 through Stage14-3 are complete; Stage14-4 is the active growth-order track. Stage13 `R03 + Stage13-12ag` is frozen as upstream input.

## §1. Locked population and ledgers

For `B>=1`, count

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Let

\[
I_{ab}=\mathbf1_{a^2+b^2=\square},\quad
I_{ac}=\mathbf1_{a^2+c^2=\square},\quad
I_{bc}=\mathbf1_{b^2+c^2=\square}.
\]

The raw pair ledgers are

\[
O_{ab,ac}=\sum I_{ab}I_{ac},\quad
O_{ab,bc}=\sum I_{ab}I_{bc},\quad
O_{ac,bc}=\sum I_{ac}I_{bc},
\]

and the triple population is

\[
T=\sum I_{ab}I_{ac}I_{bc}.
\]

Exactly-two directions are

\[
N_a^{(2)}=O_{ab,ac}-T,
\qquad
N_b^{(2)}=O_{ab,bc}-T,
\qquad
N_c^{(2)}=O_{ac,bc}-T,
\]

where

```text
a = shared smallest edge
b = shared middle edge
c = shared largest edge
```

and

\[
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}.
\]

No perfect-cuboid nonexistence assumption is made. A `T>0` object remains a perfect-cuboid candidate.

## §2. Frozen finite facts

Two materially independent exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`. At the ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
\]

This is finite evidence only. Stage14-3 inferred no limiting ratio, monotonicity theorem, or asymptotic growth law.

## §3. Frozen Stage13 theorem contract

Stage13 downstream mathematical content is frozen at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
```

Stage14 may use

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad T(B)=o(B(\log B)^3),
\]

hence

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

The R03 overlap proof fixes a finite inert-prime set, sends `B->infinity`, then enlarges the prime set. It gives zero density but no `B`-dependent power saving. Stage14 does not import a growing-modulus theorem.

## §4. Exact two-face incidence coordinates

Let the two integral faces share edge `e`; let the other physical edges be `x<y`. Take oriented primitive Pythagorean face data

\[
F_i=(S_i,X_i,H_i),
\qquad S_i^2+X_i^2=H_i^2,
\]

with `S_i` designated as the shared-edge leg. Put

\[
g=\gcd(S_1,S_2),
\qquad \alpha=S_1/g,
\qquad \beta=S_2/g.
\]

The shared-edge scale equation has all solutions

\[
k_1=t\beta,
\qquad k_2=t\alpha.
\]

The global cuboid gcd is exactly `t`; primitivity forces `t=1`. Therefore

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2)=g\alpha\beta,\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2.
\end{aligned}}
\]

After imposing `x<y`, a fixed raw pair incidence has parameter-fiber multiplicity exactly `1`.

## §5. Rational slopes and product closure

Define

\[
t_i=X_i/S_i,
\qquad L=\operatorname{lcm}(S_1,S_2).
\]

Then

\[
\boxed{(e,x,y)=L(1,t_1,t_2)},
\qquad
\boxed{d=L\sqrt{1+t_1^2+t_2^2}}.
\]

Each `t_i` is a positive rational Pythagorean slope. The three directions are only chamber inequalities:

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1
```

The space-diagonal condition also has the exact product-Pythagorean closure

\[
\boxed{(X_1X_2)^2+(gd)^2=(H_1H_2)^2.}
\]

With

\[
\rho_i=X_i/H_i,
\]

this becomes

\[
\boxed{1-(\rho_1\rho_2)^2\in(\mathbf Q^\times)^2.}
\]

Exactly-two additionally excludes

\[
t_1^2+t_2^2\in(\mathbf Q^\times)^2.
\]

## §6. Elliptic reduction of the space-square condition

Fix the first face and parameterize the second rational unit circle by

\[
\rho_2=\frac{2q}{1+q^2}.
\]

The space condition becomes the nonsingular Jacobi quartic

\[
W^2=q^4+2Aq^2+1,
\qquad A=1-2\rho_1^2.
\]

The explicit birational model is

\[
\boxed{E_{t_1}:Y^2=X(X-1)(X+t_1^2).}
\]

Its `j`-invariant

\[
j(t_1)=256\frac{(1+t_1^2+t_1^4)^3}{t_1^4(1+t_1^2)^2}
\]

is nonconstant, so the family is non-isotrivial.

## §7. Physical fiber height

Write the second-face circle parameter in lowest terms as

\[
q=u/v,
\qquad 0<u<v,
\qquad (u,v)=1.
\]

For `delta in {1,2}` the primitive second face is

\[
S_2=\frac{v^2-u^2}{\delta},
\qquad X_2=\frac{2uv}{\delta},
\qquad H_2=\frac{u^2+v^2}{\delta}.
\]

Hence

\[
\boxed{\frac{v^2}{2}<H_2<2v^2.}
\]

The physical space diagonal satisfies uniformly

\[
\boxed{
\frac{S_1H_2}{\sqrt2\,g}
<d<
\frac{\sqrt3\,S_1H_2}{g}.
}
\]

Therefore on a fixed first-face/gcd stratum,

\[
\boxed{v\asymp\sqrt{Bg/S_1}.}
\]

This is a rigorous structural source of a square root in the **fiber height**. It is not a theorem that the full Stage14 population has square-root order.

The elliptic inverse coordinate is

\[
\boxed{q(P)=\frac{X(P)}{sY(P)}},
\qquad s=S_1/H_1.
\]

For a fixed nonsingular fiber this is a degree-2 rational function, so

\[
h(q(P))=2\widehat h(P)+O_{t_1}(1).
\]

Thus one fixed rank-`r` fiber contributes only polylogarithmically in `B`; any power of `B` must come from the moving base and gcd strata.

## §8. Full `t`-line generic rank

For

\[
\mathscr E:y^2=x(x-1)(x+t^2),
\]

\[
\Delta=16t^4(1+t^2)^2,
\qquad c_4=16(1+t^2+t^4).
\]

The geometric singular fibers are

```text
t=0        I4
t=+i       I2
t=-i       I2
t=infinity I4
```

with Euler sum `12`. The surface is rational, with geometric Picard rank `10`; the reducible-fiber root rank is `8`. Shioda--Tate gives

\[
\boxed{\operatorname{rank}\mathscr E(\overline{\mathbf Q}(t))=0.}
\]

Stage14-4af must nevertheless check the actual Pythagorean base change, because finite base change can in principle create new generic sections.

## §9. Stage14-4af — the actual Pythagorean base remains rank zero

For a genuine first face define

\[
u=\frac{X_1}{H_1+S_1}.
\]

Then

\[
\boxed{
t=\frac{2u}{1-u^2},
\qquad
\frac{H_1}{S_1}=\frac{1+u^2}{1-u^2}.
}
\]

This is a degree-two base change. It branches at `t=+/-i`. The pullback of the `I4,I4,I2,I2` surface has six geometric `I4` fibers:

```text
u=0
u=infinity
u=+1
u=-1
u=+i
u=-i
```

The Euler number is

\[
6\cdot4=24,
\]

so the pullback is an elliptic K3 surface. Its trivial lattice already has rank

\[
2+6(4-1)=20.
\]

Since a K3 surface has geometric Picard rank at most `20`, the Neron--Severi rank is exactly `20`, and Shioda--Tate gives

\[
\boxed{
\operatorname{rank}E(\overline{\mathbf Q}(u))=20-2-18=0.
}
\]

Therefore the generic-rank-zero conclusion survives the **actual Pythagorean restriction**. No hidden non-torsion generic section appears after the base change.

## §10. Torsion is entirely nonphysical

On a genuine Pythagorean base put

\[
h=H_1/S_1,
\qquad h^2=1+t^2.
\]

The fiber has full rational 2-torsion

\[
(0,0),\qquad(1,0),\qquad(-t^2,0).
\]

Because `1+t^2=h^2`, `(1,0)` has rational halves with

\[
X=1\pm h.
\]

They have order `4`. Under

\[
q=\frac{X}{sY},\qquad s=1/h,
\]

all rational order-4 points map to

\[
\boxed{q=\pm1},
\]

the degenerate second-face boundary. They are not physical `0<q<1` points.

Rational 8-torsion would force a rational order-4 point to be divisible by `2`. The full-2-torsion divisibility criterion would force

\[
h-1,\qquad h,\qquad h+1
\]

to be rational squares. These are three rational squares in arithmetic progression of common difference `1`, equivalent to a rational right triangle of area `1`, impossible by Fermat's right-triangle theorem.

Since the curve already contains `Z/2 x Z/4`, Mazur's torsion theorem then gives

\[
\boxed{
E_t(\mathbf Q)_{tors}\cong\mathbf Z/2\mathbf Z\times\mathbf Z/4\mathbf Z.
}
\]

Therefore

\[
\boxed{
\text{every physical Stage14 raw-pair point is non-torsion.}
}
\]

Combined with §9:

\[
\boxed{
\text{physical raw pair incidence}
\Longrightarrow
\text{positive-rank Pythagorean specialization}.
}
\]

The `extra torsion` alternative left open by Stage14-4ae is removed from the physical problem.

## §11. The raw-pair problem is now a small-point rank-jump problem

A Pythagorean base value contributes only if the specialized fiber acquires positive Mordell--Weil rank and contains a non-torsion point whose reduced `q=u/v` satisfies the physical cutoff

\[
v\ll\sqrt{Bg/S_1}.
\]

Thus rank parity alone is insufficient. The missing global input is quantitative control of **rank-jump specializations carrying a sufficiently small first non-torsion point**, together with:

1. uniform `q`-height versus canonical-height comparison;
2. first-point height / regulator / successive minima;
3. the gcd condition `gcd(S_1,S_2)=g`;
4. the lcm coupling;
5. frozen R03 local restrictions.

## §12. Triple condition is a genus-5 fixed-base intersection

Exactly-two requires subtracting triple-face objects. Fix the first-face slope `t`.

The space-square quartic is

\[
W^2=q^4+2Aq^2+1,
\qquad A=\frac{1-t^2}{1+t^2}.
\]

The third-face condition `t^2+t_2^2=square`, with

\[
t_2=\frac{2q}{1-q^2},
\]

is another Jacobi quartic

\[
R^2=q^4+2Cq^2+1,
\qquad C=\frac{2}{t^2}-1.
\]

For a genuine Pythagorean `t`, both are nonsingular and

\[
\boxed{
A-C=-\frac{2}{t^2(1+t^2)}\ne0.
}
\]

Hence their four simple branch sets are disjoint. Adjoining both square roots gives a connected degree-4 `(Z/2)^2` cover of `P^1_q` with eight branch values. Riemann--Hurwitz gives

\[
2g-2=4(-2)+16=8,
\]

therefore

\[
\boxed{g=5.}
\]

By Faltings, each fixed first-face triple curve has finitely many rational points.

This does **not** provide a uniform rational-point bound as the first face varies. Stage14-4af therefore does not prove

\[
T(B)=o(\sqrt B)
\]

or perfect-cuboid nonexistence.

The exact ledger relation remains

\[
\boxed{O_{\rm pair}^{raw}(B)=N_2(B)+3T(B).}
\]

## §13. Deterministic validation

The Stage14-4af audit uses the exact face-pair bijection at `B=10000` and records

```text
oriented primitive face data          3186
raw pair incidences                     25
exactly-two direction                (9,11,5)
triple                                    0
distinct first-face fibers with hits    23
q denominator range                    5..57
```

For all 3,186 oriented first faces it verifies the Pythagorean base-change identities and rational order-4 boundary points. Every physical raw hit has `0<q<1` and is not killed by multiplication by `8`.

Artifacts:

```text
stages/stage14/archive/stage14-4af-specialization-triple.md
stages/stage14/scripts/14-4/specialization_triple_audit.py
stages/stage14/data/14-4/specialization_triple_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## §14. Locked Stage14-4af decision

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
STAGE14_4AE=COMPLETE
STAGE14_4AF=COMPLETE

PYTHAGOREAN_BASE_CHANGE_K3=true
PYTHAGOREAN_BASE_FIBERS=I4_X6
PYTHAGOREAN_BASE_GENERIC_MW_RANK=0

TORSION_EXACT_Z2xZ4_ON_GENUINE_BASES=true
RATIONAL_4_TORSION_PHYSICAL=false
RATIONAL_8_TORSION_EXISTS=false
PHYSICAL_RAW_PAIR_IMPLIES_POSITIVE_RANK_SPECIALIZATION=true

TRIPLE_FIXED_BASE_GENUS=5
TRIPLE_FIXED_BASE_RATIONAL_POINTS_FINITE=true
UNIFORM_TRIPLE_POINT_BOUND_PROVED=false
T_O_SQRT_B_PROVED=false

SQRT_B_STRUCTURAL_HEIGHT_SOURCE_IDENTIFIED=true
SQRT_B_FINITE_CANDIDATE_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_RIGOROUS_UPPER_BOUND=false
SQRT_B_RIGOROUS_LOWER_BOUND=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false

NEXT=Stage14-4ag quantitative rank-jump/small-point counting with uniform triple control
```

The next problem is no longer whether the elliptic family has generic points or whether torsion can fake a Stage14 object. Both are settled negatively. The remaining question is quantitative: how often does the Pythagorean base produce a **small non-torsion rank-jump point**, and how uniformly can the genus-5 triple fibers be controlled?
