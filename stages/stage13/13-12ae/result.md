# Stage13-12ae — exact inert-prime overlap / local-state closure

> STATUS: `STAGE13_12AE_COMPLETE_EXACT_PADIC_LOCAL_CLOSURE`
>
> INPUTS: Stage13-12ad quantitative raw `j=0` theorem candidate and the exact outer coordinates already fixed in Stage13-12aa
>
> R02 REVIEW STATE: Grok `OPEN`, Claude `REPAIRABLE`, Qwen `REPAIRABLE`
>
> SCOPE: close the two remaining overlap-side objections: the positive-valuation inert-prime tail and completeness of the fixed local-state refinement
>
> GLOBAL STAGE13 STATE AFTER THIS STEP: `PENDING_R03_EXTERNAL_REVIEW`

Stage13-12ae does not modify the chamber constants, the non-circular common-factor argument, or the quantitative curved-region closure of Stage13-12ad.  It replaces the only remaining soft sentence in Stage13-12ab,

```text
positive-valuation local mass = O(1/p)
```

by an exact inert-prime local series, and it writes the complete valuation/residue state map used by the pair-overlap sieve.

The conclusion is stronger than the R02 placeholder:

\[
\boxed{
\frac{\text{positive-valuation local mass}}
     {L_{p,0}(1,1,1)}
=\frac{2}{p+1}\le\frac2p,
}
\]

so the absolute constant may be taken to be

\[
\boxed{C_0=2.}
\]

Moreover the full constrained local multiplier is

\[
\boxed{
\lambda_p=\frac{p+5}{2(p+1)}
=\frac12+\frac{2}{p+1}
}
\]

for every inert odd prime `p=3 mod 4`.  Hence

\[
\boxed{\lambda_p\le\frac34\quad(p\ge7,\ p\equiv3\!\!\pmod4).}
\]

No unspecified `O(1/p)` remains in the overlap squeeze.

---

## 1. Odd-prime outer coordinates

For the selected integral face write

\[
x^2+y^2=P^2,
\qquad
P^2+z^2=d^2.
\]

On each fixed OE/EE parity branch the odd-prime part of the outer Pythagorean parameterization is

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\qquad (r,s)=1.
\]

The only difference between OE and EE is 2-adic.  For every odd prime `p`, `2` is invertible modulo `p`, and the formulas above give the same `p`-local valuation/residue classification in both parity branches.  The finite 2-adic factor therefore factors out of every inert-prime ratio below.

Fix an inert prime

\[
p\equiv3\pmod4.
\]

Write

\[
a=v_p(h),\qquad b=v_p(r),\qquad c=v_p(s).
\]

Since `(r,s)=1`,

\[
\boxed{\min(b,c)=0.}
\]

These three valuations plus the unit residues constitute all odd-prime states relevant to the outer variables.

---

## 2. Why the inert `h`-factor is exactly `1`

The historical Stage13-7h ledger records that at an inert prime the `h`-factor is exactly `1`.  Here is the primitive reason.

Assume `a>=1`.  Then `p|h`, hence from the outer formulas

\[
p\mid P,\qquad p\mid z,\qquad p\mid d.
\]

Because `p=3 mod 4`, `-1` is a quadratic nonresidue.  From

\[
x^2+y^2=P^2\equiv0\pmod p
\]

we must therefore have

\[
p\mid x,\qquad p\mid y.
\]

Thus `p` divides `x,y,z`, contradicting primitive cuboid gcd `1`.

Therefore

\[
\boxed{a=0}
\]

for every primitive raw incidence at an inert prime.  In particular all layers `v_p(h)>=1` requested by the R02 reviews have coefficient exactly zero; they are not merely small.

---

## 3. Complete valuation-state table

With `a=0` and `min(b,c)=0`, exactly three state types remain.

| state | valuations `(a,b,c)` | primitive status | `P mod p` | `z mod p` | second-face test `W_p` |
|---|---|---|---|---|---|
| U | `(0,0,0)` | allowed | unit | arbitrary | nontrivial |
| R_b | `(0,b,0)`, `b>=1` | allowed | `0` | unit | automatic pass |
| S_c | `(0,0,c)`, `c>=1` | allowed | `0` | unit | automatic pass |

No other state exists:

- `a>=1` is excluded by primitivity as proved above;
- `b,c>=1` is excluded by `(r,s)=1`.

For `R_b`, `r=0 mod p`, `s` is a unit, so

\[
z\equiv \frac{hs^2}{2}\not\equiv0\pmod p.
\]

For `S_c`, similarly

\[
z\equiv-\frac{hr^2}{2}\not\equiv0\pmod p.
\]

In either positive-base-valuation state, `p|P`.  Inertness again forces

\[
p\mid x,\qquad p\mid y.
\]

Therefore

\[
x^2+z^2\equiv z^2\pmod p
\]

is a nonzero square.  Hence every `R_b` and `S_c` state automatically satisfies

\[
W_p:=1_{x^2+z^2\in QR_0(\mathbf F_p)}.
\]

This proves completeness of the valuation part of the local refinement and identifies exactly where the test can reject: only the unit state `U`.

---

## 4. Exact unrestricted inert local series

At an inert prime there is no Gaussian angular representation multiplicity.  The scale valuation is forced to zero and `(r,s)=1` allows positive valuation on at most one base variable.  Thus the raw zero-mode local series is exactly

\[
\begin{aligned}
L_{p,0}(Y,Z)
&=1+\sum_{b\ge1}Y^b+\sum_{c\ge1}Z^c\\
&=\frac{1-YZ}{(1-Y)(1-Z)}.
\end{aligned}
\]

This is the explicit `j=0` form of the historical inert-prime statement “the `h`-factor is `1` and the `r-s` coprime correction is `1-YZ`.”

At the main-term point `s_r=s_s=1`, put

\[
Y=Z=p^{-1}.
\]

Then

\[
\boxed{
L_{p,0}(1,1,1)
=1+\frac{2}{p-1}
=\frac{p+1}{p-1}.
}
\]

The entire positive-valuation mass is

\[
\boxed{
T_p^+
=\frac{2}{p-1}.
}
\]

Consequently

\[
\boxed{
\frac{T_p^+}{L_{p,0}(1,1,1)}
=\frac{2}{p+1}
\le\frac2p.
}
\]

Thus the absolute constant whose existence was only asserted in R02 is explicitly

\[
\boxed{C_0=2.}
\]

No divisor-function majorant is required.

---

## 5. Unit state and the exact finite residue set

On `U`, `P` is a unit.  Normalize by `P`:

\[
X=x/P,\quad Y_*=y/P,\quad Z_*=z/P,\quad D_*=d/P.
\]

Then

\[
X^2+Y_*^2=1,
\qquad
D_*^2-Z_*^2=1.
\]

For `p=3 mod 4`, the circle has exactly `p+1` points and the hyperbola exactly `p-1` points.  The outer parameter ratio

\[
u=s/r\in\mathbf F_p^*
\]

is in bijection with the hyperbola through

\[
Z_* = \frac{u-u^{-1}}2,
\qquad
D_* = \frac{u+u^{-1}}2,
\]

because

\[
u=D_*+Z_*,\qquad u^{-1}=D_*-Z_*.
\]

Hence the complete unit residue state space is

\[
\mathscr U_p
=\{(X,Y_*,Z_*,D_*):X^2+Y_*^2=1,\ D_*^2-Z_*^2=1\},
\]

with

\[
|\mathscr U_p|=(p+1)(p-1)=p^2-1.
\]

The second-face necessary condition is precisely

\[
X^2+Z_*^2\in QR_0(\mathbf F_p),
\]

because multiplication by `P^2` does not change square class.

The exact character calculation already used in the finite-field audit gives

\[
\#\{\mathscr U_p: X^2+Z_*^2\in QR_0\}
=\frac{(p+1)^2}{2}.
\]

Therefore the unit-state acceptance is

\[
\boxed{
\alpha_p
=\frac{p+1}{2(p-1)}
=\frac12+\frac1{p-1}.
}
\]

This is not a sample-based estimate; the companion audit enumerates finite fields only as a deterministic check of the displayed exact identities.

---

## 6. Why the finite residue refinement gives the leading local density

R02 described this step too compactly as “adjoin finitely many unit residues.”  The precise fixed-prime statement is the following.

For one fixed odd prime `p`, split every local valuation state into its finitely many unit residue classes modulo `p`.  On the unit state this means the finite set `mathscr U_p` above; on `R_b,S_c` the test is already constant `1` and no finer information is needed.

A congruence class of each unit variable is imposed by finite character orthogonality.  For the rational integer variables this is ordinary Dirichlet-character orthogonality; for the Gaussian representation variable it is the corresponding fixed-conductor Gaussian ray-class character decomposition.  The principal character tuple reproduces the untwisted zero-mode pole and assigns equal leading weight to the finite admissible residue states.  Every nonprincipal fixed character tuple removes at least one principal pole and is lower order by the same fixed-conductor Selberg--Delange/Hecke theorem boundary already used in Stage13-12ad.

Important order of quantifiers:

```text
p is fixed first.
The residue character conductor is therefore fixed.
Then B -> infinity.
```

No uniform theorem in growing `p` is required.  For a fixed finite set `S`, CRT tensors these finite state spaces and the principal local densities multiply.  Nonprincipal character combinations remain lower order.

Thus the constrained leading zero-mode constant is obtained by multiplying by the actual local acceptance density computed from the complete state table, not by assuming a new direction-dependent arithmetic constant.

The OE/EE split is independent of this argument because `p` is odd; its finite 2-adic factor occurs in both constrained and unconstrained counts and cancels from the local ratio.

---

## 7. Exact constrained inert local multiplier

Normalize the unrestricted unit-state coefficient to `1`.  Section 5 says the constrained unit coefficient is `alpha_p`.  Section 3 says every positive valuation state is accepted.

Therefore

\[
\begin{aligned}
L^W_{p,0}(1,1,1)
&=\alpha_p+\frac{2}{p-1}\\
&=\frac{p+1}{2(p-1)}+\frac{2}{p-1}\\
&=\frac{p+5}{2(p-1)}.
\end{aligned}
\]

Divide by the exact unrestricted factor:

\[
\begin{aligned}
\lambda_p
&=\frac{L^W_{p,0}(1,1,1)}{L_{p,0}(1,1,1)}\\
&=\frac{p+5}{2(p+1)}\\
&=\frac12+\frac{2}{p+1}.
\end{aligned}
\]

Hence

\[
\boxed{
\lambda_p=\frac{p+5}{2(p+1)}.
}
\]

In particular

\[
\lambda_3=1,
\qquad
\lambda_7=\frac34,
\qquad
\lambda_p<\frac34\quad(p>7,\ p\equiv3\pmod4).
\]

So an explicit threshold is

\[
\boxed{p_0=3}
\]

if the sieve chooses inert primes `p>=7`, or equivalently one may state that every inert prime `p>7` has strict `<3/4`.  There are infinitely many such primes by Dirichlet's theorem.

For the squeeze it is convenient simply to choose distinct inert primes

\[
p_i\ge7.
\]

Then every factor satisfies `lambda_{p_i}<=3/4`.

---

## 8. Tagged pair-overlap injection — complete local check

Suppose the selected raw `q`-incidence has a second integral face sharing one selected leg `x`.  Then

\[
x^2+z^2=w^2.
\]

Therefore for every inert prime

\[
W_p=1.
\]

The state table proves this necessary condition is represented correctly on every local valuation stratum:

- on `U`, it is exactly the finite residue predicate counted by `alpha_p`;
- on `R_b,S_c`, it is automatic because `x=0 mod p` and `z` is a unit;
- there are no omitted `a>=1` or `b,c>=1` primitive states.

Thus every genuine pair overlap lands in the constrained tagged population at every chosen inert prime.

### Tagging multiplicity clarification

R02 used the population with both possible face-leg tags, giving a harmless factor `2`.  The exact inequality is

\[
O_{qr}(B)
\le A^{\rm tagged\ union}_{q,S}(B)
\le A^{(1)}_{q,S}(B)+A^{(2)}_{q,S}(B).
\]

Each tag family has the same fixed-prime upper multiplier and each is bounded by the corresponding raw directional main scale.  Hence

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le 2D_q\prod_{p\in S}\lambda_p.
\]

The factor `2` enlarges the upper bound and therefore cannot invalidate the inequality; it is independent of `S,k` and disappears when the product tends to zero.  No claim of an exact two-to-one map is needed.

---

## 9. Fixed-set squeeze with no hidden constants

Fix `k`.  Choose distinct inert primes

\[
S_k=\{p_1,\ldots,p_k\},\qquad p_i\ge7.
\]

Hold `S_k` fixed while `B->infinity`.  By the fixed residue-state transfer of Section 6 and the exact local multiplier,

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q\prod_{i=1}^k
\frac{p_i+5}{2(p_i+1)}.
\]

Since every factor is at most `3/4`,

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le2D_q\left(\frac34\right)^k.
\]

Only now let `k->infinity`.  Therefore

\[
\boxed{O_{qr}(B)=o(B(\log B)^3).}
\]

The triple overlap is a subset of every pair overlap, so

\[
\boxed{T(B)=o(B(\log B)^3).}
\]

This proof uses neither a growing modulus nor an unspecified local tail constant.

---

## 10. Exactly-one theorem candidate restored for R03

Stage13-12ad supplies the quantitatively closed non-circular raw theorem candidate

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
\]

The exact inclusion--exclusion identities are

\[
N_q=A_q-\text{two incident pair overlaps}+T.
\]

By Section 9 all overlap terms are lower order.  Hence the repaired R03 candidate is

\[
\boxed{
N_q(B)\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

and

\[
\boxed{N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.}
\]

The normalized candidate limit remains

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

Stage13 is **not** self-declared externally `CLOSED`; this is now the theorem candidate to place in a fresh neutral R03 bundle.

---

## 11. Review crosswalk and remaining R03 presentation items

The R02 objections are now mapped as follows.

```text
R01 circular direction-neutrality
  -> 13-12aa structural repair
  -> 13-12ad quantitative closure

Grok/Claude/Qwen weighted-l1 / curved / harmonic objection
  -> 13-12ad explicit 529 q^(-5/4), log moments and fixed error budget

Grok/Qwen inert positive-valuation O(1/p) objection
  -> 13-12ae exact tail ratio 2/(p+1), C0=2

Grok local-state completeness objection
  -> 13-12ae complete (a,b,c) table + fixed residue/ray-class transfer

Qwen tagging-factor minor
  -> clarified in Section 8

Qwen OE/EE odd-prime minor
  -> clarified in Sections 1 and 6
```

Two presentation clarifications should be made explicit again in the R03 synthesis even though they do not reopen the repaired argument:

1. Stage13-12ad uses the frozen Stage12 total only as a positive total-mass upper bound for the Vaaler bracketing error; it is not used to seed a categorywise constant before commonness of `Theta` is proved.
2. The R03 current-proof should reproduce the analytic change-of-variables proving `J_q=2I_q/pi`, rather than relying only on the historical numerical audit.

These are R03 exposition requirements, not new open asymptotic mechanisms.

---

## 12. Status

```text
STAGE13_12AE=COMPLETE_EXACT_PADIC_LOCAL_CLOSURE

P_ADIC_POSITIVE_VALUATION_TAIL=REPAIRED_EXACTLY
P_ADIC_TAIL_RATIO=2/(p+1)
P_ADIC_ABSOLUTE_C0=2
INERT_LOCAL_MULTIPLIER=lambda_p=(p+5)/(2(p+1))
INERT_LAMBDA_LE_3_OVER_4_FOR_P_GE_7=true

LOCAL_STATE_REFINEMENT_COMPLETENESS=REPAIRED
OE_EE_ODD_PRIME_COMPATIBILITY=EXPLICIT
TAGGING_FACTOR_TWO=CLARIFIED_AS_HARMLESS_UPPER_MULTIPLICITY

PAIR_OVERLAP_LOWER_ORDER=RESTORED_WITH_EXACT_LOCAL_FACTOR
TRIPLE_OVERLAP_LOWER_ORDER=RESTORED_WITH_EXACT_LOCAL_FACTOR
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=R03_CANDIDATE

STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
NEXT=Stage13-12af
```
