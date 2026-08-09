# Stage13 — R06 canonical proof candidate

> STATUS: `STAGE13_13FN_R06_CANONICAL_PROOF_CANDIDATE`
>
> PURPOSE: one proof-facing synthesis of the Stage13 exactly-one directional asymptotic after the fresh R05 review repairs.
>
> PRECEDENCE: this file supersedes the R05 canonical proof only for construction of the future immutable R06 bundle. R03, R04 and R05 remain immutable historical review artifacts.
>
> THEOREM_CHANGED: `false`.
>
> THEOREM_CONTRACT_REOPEN_REQUIRED: `false`.

---

## 0. The theorem and scope

Count primitive canonical triples

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad d^2=a^2+b^2+c^2,\quad d\in\mathbf Z_{>0}.
\]

For `q in {ab,ac,bc}`, let `A_q(B)` count triples with `d<=B` for which face `q` has integral diagonal, allowing additional integral faces. For distinct `q,r`, let `O_{qr}(B)` count triples with both faces integral, let `T(B)` count triples with all three faces integral, and let `N_q(B)` count triples with exactly one integral face, namely `q`.

On

\[
\mathcal R=\{(x,y,z)\in S^2:0<x<y<z\}
\]

define

\[
w_{ab}=\frac1{\sqrt{x^2+y^2}},\quad
w_{ac}=\frac1{\sqrt{x^2+z^2}},\quad
w_{bc}=\frac1{\sqrt{y^2+z^2}},
\qquad I_q=\int_{\mathcal R}w_q\,d\omega.
\]

Then

\[
\boxed{N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3}
\]

and

\[
\boxed{N_1(B):=\sum_qN_q(B)\sim\frac{\kappa}{24\pi}B(\log B)^3}.
\]

Moreover

\[
\boxed{I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}},
\qquad
\boxed{\frac{N_q(B)}{N_1(B)}\to\frac{8I_q}{\pi^2}}.
\]

No effective convergence rate is claimed. Finite data are neither proof of convergence nor a refutation of the asymptotic theorem in the absence of an effective remainder. In particular, a finite sample looking closer either to `2:1:1` or to the limiting vector is diagnostic only. No assumption that perfect cuboids do not exist is used.

---

## 1. Exact combinatorics

For `{q,r,s}={ab,ac,bc}`,

\[
N_q=A_q-O_{qr}-O_{qs}+T,
\]

and

\[
N_1=\sum_qA_q-2\sum_{q<r}O_{qr}+3T.
\]

Hence it suffices to prove the raw asymptotic for each `A_q` and

\[
O_{qr}(B)=o(B(\log B)^3).
\]

---

## 2. Frozen Stage12 interface, projection fiber, and `kappa`

Stage12 uses

\[
1\le r<s,\quad(r,s)=1,
\qquad
P=hrs,\quad z=\frac{h(s^2-r^2)}2,\quad d=\frac{h(r^2+s^2)}2,
\]

with cutoff `d<=B`. Its primitive oriented distinguished-face record count satisfies

\[
\boxed{C_{\rm prim}(B)\sim\frac{\kappa}{12\pi}B(\log B)^3}.
\]

The Euler product is

\[
\kappa=
\left(\frac\pi4\right)^3\left(\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3
\prod_{q\equiv1(4)}
\frac{q^2+6q+1}{q^2-1}(1-q^{-1})^6.
\]

Absolute convergence is elementary. For `p≡3 (4)`,

\[
(1-p^{-2})^3=1-3p^{-2}+O(p^{-4}).
\]

For `q≡1 (4)`, with `x=q^{-1}`,

\[
\frac{1+6x+x^2}{1-x^2}(1-x)^6
=1-19x^2+O(x^3).
\]

Thus every normalized local factor is `1+O(p^{-2})` and the product converges absolutely.

For one primitive canonical raw incidence counted by `A_q(B)`, Stage12 has exactly two oriented preimages, `(x,y)` and `(y,x)`, for the distinguished face. The outer convention `r<s` already fixes the outer orientation; canonical sorting preserves the cutoff and gcd; the repeated-side boundary contributes nothing; and this two-element fiber holds separately on both parity branches. Therefore, for every `B`,

\[
\boxed{C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)},
\qquad
\boxed{C_{\rm prim}(B)=2\sum_qA_q(B)}.
\]

---

## 3. Real chamber factor and exact analytic normalization

For distinguished face `ab`, write

\[
a^2+b^2=P^2,\qquad P^2+c^2=d^2.
\]

With

\[
F_1=a^2+b^2-P^2,\qquad F_2=P^2+c^2-d^2,
\]

we have

\[
\det\frac{\partial(F_1,F_2)}{\partial(P,d)}=4Pd.
\]

After scaling by the radial variable `d`, the common radial powers are absorbed into the global radial measure and the remaining directional Gelfand--Leray factor is

\[
\frac{d}{P}=\frac1{P/d}=\frac1{\sqrt{x^2+y^2}}=w_{ab}.
\]

The other faces follow by permutation.

Now prove the normalization symbolically. Let

\[
\mathcal O=\{(x,y,z)\in S^2:x,y,z>0\}
\]

and

\[
W=w_{ab}+w_{ac}+w_{bc}.
\]

`W` is invariant under all coordinate permutations, and `\mathcal O` is the disjoint union, up to measure-zero equality walls, of the six order chambers. Therefore

\[
\int_{\mathcal O}W\,d\omega=6(I_{ab}+I_{ac}+I_{bc}).
\]

For one pair use

\[
x=\sin\phi\cos\theta,\quad y=\sin\phi\sin\theta,\quad z=\cos\phi,
\qquad 0<\phi,\theta<\frac\pi2.
\]

Then `sqrt(x^2+y^2)=sin phi` and `domega=sin phi dphi dtheta`, hence

\[
\int_{\mathcal O}w_{ab}\,d\omega
=\int_0^{\pi/2}\int_0^{\pi/2}d\phi\,d\theta
=\frac{\pi^2}{4}.
\]

By symmetry the same holds for the other two pair weights. Thus

\[
6\sum_qI_q=3\frac{\pi^2}{4},
\]

so

\[
\boxed{\sum_qI_q=\frac{\pi^2}{8}}.
\]

This is the proof; numerical quadrature is validation only.

---

## 4. Zero Fourier kernel and notation separation

For a fixed face `q={i,j}` and complementary coordinate `k`, use geometric spherical variables

\[
x_i=\sin\theta\cos\alpha,\quad x_j=\sin\theta\sin\alpha,\quad x_k=\cos\theta.
\]

Here `theta` denotes only the geometric polar angle. Then

\[
w_q\,d\omega=d\theta\,d\alpha.
\]

With `psi=pi/2-theta`, let `ell_q(psi)` be the allowed inner-angle length. Writing

\[
r=R\cos\phi,\quad s=R\sin\phi,\quad \phi\in[\pi/4,\pi/2]
\]

gives

\[
\frac Pd=\sin2\phi,\quad \frac zd=-\cos2\phi,
\quad \psi=2\phi-\frac\pi2.
\]

Define

\[
k_q(\phi)=\frac4\pi\ell_q(\psi),
\qquad
J_q=\int_{\pi/4}^{\pi/2}k_q(\phi)\,d\phi.
\]

Then

\[
\boxed{J_q=\frac{2I_q}{\pi}},
\qquad
\boxed{\sum_qJ_q=\frac\pi4}.
\]

From this point onward the Gaussian local angular phase is `vartheta`, never `theta`.

---

## 5. Odd-prime coefficient system and branchwise 2-adic independence

On each OE/EE parity branch retain

\[
P=hrs,\quad z=\frac{h(s^2-r^2)}2,\quad d=\frac{h(r^2+s^2)}2,\quad(r,s)=1.
\]

The OE/EE distinction is entirely 2-adic. On each branch separately, the odd-prime Euler factors below are identical for `ab,ac,bc`; sorting/permutation changes only the real chamber label, and the Stage12 projection fiber remains exactly two. Hence one may write branch constants `Theta_OE` and `Theta_EE`, each independent of `q`, and only after the branchwise commonness proof sum them to `Theta=Theta_OE+Theta_EE`. No hidden face-dependent 2-adic multiplier is introduced.

For split `p≡1 (4)`, put `a=v_p(h)`, `b=v_p(rs)`, `e=a+b`. At zero mode the representation multiplicity is `G_e=2e+1`; at nonzero phase define

\[
H_e(\vartheta)=1+2\sum_{m=1}^e\cos(m\vartheta).
\]

The pure one-variable factors are

\[
A_\vartheta(x)=\frac{1-x^2}{1-2\cos\vartheta\,x+x^2},
\qquad
B_\vartheta(y)=\frac{1+y}{1-2\cos\vartheta\,y+y^2}.
\]

At zero mode,

\[
A_0(s)=\zeta(s)L(s,\chi_4)E_{h,0}(s),
\qquad
B_0(s)=\zeta(s)^2L(s,\chi_4)E_{b,0}(s).
\]

For a retained nonzero Fourier mode the Stage13 Fourier exponent is

\[
m=8\ell,\qquad \ell\ge1.
\]

Under the Huang--Liu--Rudnick normalization

\[
\Xi_k(\mathfrak a)=\left(\frac\alpha{\bar\alpha}\right)^{2k}=e^{i4k\theta_{\mathfrak a}},
\]

so the exact index translation is

\[
\boxed{k_{\rm HLR}=m/4=2\ell}.
\]

Thus the nonzero scale factor uses `L(s,Xi_{2 ell})`, not an ambiguously named `Xi_{8 ell}`.

---

## 6. Mixed correction and explicit Wiener bounds

Define

\[
M_\vartheta(x,y)=\sum_{a,b\ge1}2\cos((a+b)\vartheta)x^ay^b.
\]

The full local series is

\[
D_\vartheta=1+a_\vartheta(x)+b_\vartheta(y)+b_\vartheta(z)
+M_\vartheta(x,y)+M_\vartheta(x,z),
\]

where `a=A-1`, `b=B-1`, and there is no simultaneous positive `y,z` support because `(r,s)=1`. Put

\[
C_\vartheta(x,y,z)=\frac{D_\vartheta}{A_\vartheta(x)B_\vartheta(y)B_\vartheta(z)}.
\]

For `ell>=1` define at first use

\[
\boxed{C_{\ell,p}(s_h,s_r,s_s)=C_\vartheta(p^{-s_h},p^{-s_r},p^{-s_s})}.
\]

Let `rho=p^{-5/8}`. For `p>=13`, `rho<1/4`, and coefficientwise

\[
\|a\|_\rho\le\frac83\rho,
\quad
\|b\|_\rho\le\frac{44}{9}\rho,
\quad
\|M\|_\rho\le\frac{32}{9}\rho^2,
\]

\[
\|A^{-1}\|_\rho\le\frac53,
\qquad
\|B^{-1}\|_\rho\le\frac{25}{12}.
\]

With

\[
E=D-AB(y)B(z),
\]

exact pure-axis cancellation gives

\[
E=(M_{xy}-ab_y)+(M_{xz}-ab_z)-b_yb_z-ab_yb_z.
\]

The four `rho^2` contributions are

\[
\frac{64}{9},\quad\frac{704}{27},\quad\frac{1936}{81},\quad\frac{3872}{243},
\]

whose sum is `17744/243`. Therefore

\[
\|C_{\ell,p}-1\|_{5/8}
\le\frac{3465625}{6561}p^{-5/4}<529p^{-5/4}.
\]

The split prime `p=5` is handled separately. Since `rho_5<3/8`,

\[
\|a\|\le\frac65,
\quad\|b\|\le\frac{63}{25},
\quad\|M\|\le\frac{18}{25},
\quad\|A^{-1}\|\le\frac{11}{5},
\quad\|B^{-1}\|\le\frac{121}{40}.
\]

Hence

\[
\|E\|\le\frac{67059}{3125}
\]

and

\[
\boxed{
\|C_{\ell,5}-1\|_{5/8}
\le\frac{10799919009}{25000000}
=431.99676036<432.
}
\]

Thus the mixed Euler correction is absolutely convergent in the weighted Wiener algebra and has finite logarithmic moments uniformly over retained `ell`.

---

## 7. Exact Gaussian-Hecke external contract

For `k!=0`, Huang--Liu--Rudnick §2.1 gives

\[
\Xi_k(\mathfrak a)=\left(\frac\alpha{\bar\alpha}\right)^{2k}
\]

and an entire `L(s,Xi_k)` with completion

\[
\xi(s,k)=\pi^{-(s+2|k|)}\Gamma(s+2|k|)L(s,\Xi_k)=\xi(1-s,k).
\]

For the retained Stage13 family `k=2ell`, so the gamma shift is exactly `4ell`:

\[
\pi^{-(s+4\ell)}\Gamma(s+4\ell)L(s,\Xi_{2\ell}).
\]

Therefore every `ell>=1` mode is entire and has no pole at `s=1`. The fixed residue refinements used later form a finite family independent of `B`; twisting by those fixed finite-order characters preserves nonzero infinity type and gives the same holomorphy-at-one conclusion. No growing-modulus theorem is used.

Right-boundary absolute convergence, the functional equation, Stirling and Phragmen--Lindelof yield polynomial fixed-strip growth in `|t|+ell`. Thus there exist fixed `delta_H>0`, `C_H,D_H>=0` such that

\[
S_\ell(X)\ll X^{1-\delta_H}(1+\ell)^{C_H}(\log(2X))^{D_H}.
\]

To pass from a smoothed Riesz/Perron sum to this ordinary sharp sum, choose a Riesz order larger than the vertical-growth exponent, shift the smoothed contour, and apply finite differences. The transition shell is controlled by the positive coefficient majorant; choosing its width as a fixed power smaller than `X` absorbs it into a slightly weakened positive `delta_H`. Hence no unsmoothed contour-shift shortcut is used.

---

## 8. Vaaler convention and curved-region accumulation

Use Vaaler's finite sawtooth approximation to build interval majorants/minorants. The interval indicator is taken with the conventional midpoint value at endpoints. In the canonical problem those endpoints are equality walls of the strict chamber or repeated-side degeneracies, which are excluded from the canonical count; changing the endpoint convention therefore does not change the counted population. The pointwise majorant/minorant has

\[
\widehat P^\pm(0)=|I|\pm\frac1{L+1},
\qquad
|\widehat P^\pm(h)|\le\frac1{\pi|h|}+\frac1{L+1}<1.
\]

Write

\[
\Lambda=\log B,
\quad H_0=U=e^{\Lambda^{1/4}},
\quad \eta=\Lambda^{-8}.
\]

After removing the positive-majorant wings `h<H0` and `min(r,s)<U`, the core is partitioned by a multiplicative mesh `e^eta`. One coordinate requires at most

\[
1+\frac{\log(2B/H_0)}\eta
=O\left(\frac{\log(2B)}\eta\right)
=O(\Lambda^9)
\]

intervals. Therefore the crude three-coordinate product bound is

\[
\boxed{N_{\rm box}=O(\Lambda^{27})}.
\]

This bound deliberately ignores the curved constraint; being crude only strengthens safety.

With finite Perron order `N=64`, the per-box endpoint remainder `O(B\Lambda^{-62})` sums to

\[
O(B\Lambda^{-35}).
\]

Rectangle power tails are

\[
B\Lambda^{C_{\rm rect}+27}e^{-(3/16)\Lambda^{1/4}},
\]

and the boundary and interior mesh errors are `O(B\Lambda^{-5})` up to already-accounted lower-order terms.

For a nonconstant mixed-correction convolution shift, finite logarithmic moments give

\[
(\log(X/n))^j-(\log X)^j
=O((1+\log n)\Lambda^{j-1}),
\]

and summing against the absolute Wiener coefficients yields the global mixed-log-shift bound

\[
\boxed{O(B\Lambda^2)}.
\]

Thus

\[
A_q^{(0)}(B)=\Theta J_qB\Lambda^3+o(B\Lambda^3)
\]

with one arithmetic `Theta` independent of `q`.

---

## 9. Retained harmonics and the exponent ledger

Take Vaaler degree

\[
L=\lfloor\Lambda^4\rfloor.
\]

One retained mode costs

\[
B\Lambda^{D_H+2}(1+\ell)^{C_H}e^{-\delta_H\Lambda^{1/4}}.
\]

Summing `ell<=L` gives

\[
\sum_{\ell\le L}(1+\ell)^{C_H}=O(L^{C_H+1})=O(\Lambda^{4C_H+4}).
\]

The two positive base channels contribute `Lambda^2`, while the Hecke bound contributes `Lambda^{D_H}`. Hence the full polylogarithmic exponent is visibly

\[
\boxed{(4C_H+4)+D_H+2=4C_H+D_H+6}.
\]

Therefore

\[
\mathcal E_{\rm harm,core}
\ll B\Lambda^{4C_H+D_H+6}e^{-\delta_H\Lambda^{1/4}}
=o_A(B\Lambda^{-A})
\]

for every fixed `A>0`. The historical fixed choice `A=48` is not needed.

The Vaaler zero-mode excess is `1/(L+1)`, so positivity and the Stage12 total give `O(B\Lambda^{-1})`. Stage12 is used here only as an error majorant, not to seed directional constants.

---

## 10. Common-Theta calibration

The arithmetic coefficient system is common across categories and, branchwise, across OE/EE; category dependence appears only through `J_q`. Therefore

\[
A_q(B)\sim\Theta J_qB(\log B)^3.
\]

Only now sum over `q`. Since `sum J_q=pi/4` and `C_prim=2 sum A_q`, comparison with Stage12 gives

\[
\Theta\frac\pi2=\frac\kappa{12\pi},
\qquad
\boxed{\Theta=\frac\kappa{6\pi^2}}.
\]

Using `J_q=2I_q/pi`,

\[
\boxed{A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3}.
\]

The order is non-circular:

```text
branchwise local arithmetic commonness
-> common Theta
-> sum over q
-> frozen Stage12 total calibration.
```

---

## 11. Inert local multiplier, including `p=3`

For inert odd `p≡3 (4)`, primitivity leaves valuation states

```text
U=(0,0,0),  R_b=(0,b,0),  S_c=(0,0,c).
```

The unrestricted local mass is `(p+1)/(p-1)`. The accepted unit fraction is

\[
\alpha_p=\frac{p+1}{2(p-1)},
\]

and after adding automatically accepted positive-valuation mass,

\[
\boxed{\lambda_p=\frac{p+5}{2(p+1)}}.
\]

At `p=3`,

\[
\boxed{\lambda_3=1}.
\]

Thus `p=3` gives no contraction. For inert `p>=7`,

\[
\boxed{\lambda_p\le\frac34}.
\]

This is why the overlap squeeze begins with inert primes `>=7`.

---

## 12. Fixed-S principal pole sector on the constrained residue set

Fix a finite inert set `S` and a valuation profile. After fixing valuations, admissible unit residues form a finite constrained subset `X_{S,nu}` of an ambient finite abelian unit group. We do **not** assume `X_{S,nu}` is itself a group.

Fourier-expand the acceptance indicator in ambient characters, then identify two characters whenever they agree pointwise on `X_{S,nu}`. This quotient removes all algebraic auxiliary-character aliasing before analytic pole classification.

At zero mode the explicit unbounded pole slots are the five zeta copies

\[
\boxed{\mathscr P=\{H,R_1,R_2,S_1,S_2\}},
\]

coming from `zeta(s_h)`, `zeta(s_r)^2`, `zeta(s_s)^2`. Each effective character class induces a five-component pole signature. Define the principal pole sector to be the kernel of this reduced signature map: all five induced slot characters are principal.

Let `Res_S(F)` be the coefficient of the full raw principal polar term after inserting a finite residue function `F`. This is linear in `F`. Every effective character outside the kernel has zero full principal residue because at least one pole slot is replaced by a holomorphic fixed-conductor `L`-factor. Therefore the complete kernel contribution equals `Res_S(W_S)`.

Evaluate that same functional directly in local physical variables. At every `p in S`, the constrained/unrestricted local ratio is `lambda_p`; CRT tensors the fixed local insertions. Hence

\[
\boxed{\frac{Res_S(W_S)}{Res_S(1)}=\prod_{p\in S}\lambda_p}.
\]

This proves that the **entire** principal sector, including any harmless mixed-only auxiliary characters, has multiplier `prod lambda_p` without assuming linear independence of redundant auxiliary coordinates.

---

## 13. Tagged factor two and nonprincipal pole loss

For each raw `q` incidence, tag one of its two face legs. The ambient tagged set therefore satisfies the exact finite identity

\[
\boxed{|\mathcal T_q(B)|=2A_q(B)}.
\]

For distinct faces `(q,r)`, the two faces share exactly one edge. A true pair-overlap object maps injectively to the accepted tagged set by choosing that unique shared edge. Hence for every finite `B` and fixed `S`,

\[
\boxed{O_{qr}(B)\le A^{\rm tag}_{q,S}(B)}.
\]

The factor two may overcount accepted tags but can never undercount a true pair overlap.

Outside the principal-sector kernel, at least one of the five reduced slot characters is genuinely nonprincipal after aliasing has already been removed. The corresponding zeta pole is replaced by a fixed-conductor Dirichlet or Gaussian/ray-class Hecke factor holomorphic at `s=1`. The phase-uniform mixed Wiener correction is holomorphic and cannot restore the pole. Thus the pole order drops by at least one and, for fixed `S`, the finite sum of all nonprincipal sectors is

\[
\boxed{o_S(B(\log B)^3)}.
\]

Therefore

\[
\boxed{
A^{\rm tag}_{q,S}(B)
=2D_q\left(\prod_{p\in S}\lambda_p\right)B(\log B)^3
+o_S(B(\log B)^3),
}
\]

where `D_q=kappa I_q/(3 pi^3)`.

---

## 14. Pair/triple overlap squeeze

Choose `k` distinct inert primes `p_i>=7` and hold `S_k={p_1,...,p_k}` fixed. Then

\[
\limsup_{B\to\infty}\frac{O_{qr}(B)}{B(\log B)^3}
\le2D_q\prod_{p\in S_k}\lambda_p
\le2D_q\left(\frac34\right)^k.
\]

Only after the `B`-limit do we let `k->infinity`. Hence

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}.
\]

Since `T(B)` is contained in every pair overlap,

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

The quantifier order is permanently

```text
fix S -> B -> infinity -> enlarge S.
```

There is no modulus growing with `B`.

---

## 15. Exactly-one conclusion

Insert the overlap estimates into the exact inclusion-exclusion identities. Then

\[
\boxed{N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3}.
\]

Summing and using the analytic identity `sum I_q=pi^2/8` gives

\[
\boxed{N_1(B)\sim\frac\kappa{24\pi}B(\log B)^3}.
\]

Therefore

\[
\boxed{\frac{N_q(B)}{N_1(B)}\to\frac{8I_q}{\pi^2}}.
\]

---

## 16. Quantitative and dependency ledger

With `Lambda=log B`:

```text
H0=U=exp(Lambda^(1/4))
eta=Lambda^(-8)
epsilon=1/16
finite Perron order N=64
Vaaler degree L=floor(Lambda^4)
mesh intervals per coordinate=O(log(2B)/eta)=O(Lambda^9)
box count=O(Lambda^27)
all-box finite remainder=O(B Lambda^(-35))
mixed-log shifts=O(B Lambda^2)
retained harmonic exponent=4*C_H+D_H+6
p=5 Wiener bound <432
lambda_3=1
```

Repository audits are reproducibility/consistency evidence only. They do not replace the analytic arguments.

Imported external boundary:

1. frozen Stage12 R09 total primitive-oriented theorem and counting definition;
2. Gaussian Hecke continuation/functional equation in the exact HLR normalization, plus fixed finite twists;
3. classical continuation/functional equation for `L(s,chi_4)`;
4. Vaaler's finite sawtooth approximation.

Not required: a Gaussian-Hecke zero-free region, general Selberg--Delange as a black box, Dirichlet's theorem on primes in progressions, a growing-modulus sieve theorem, or perfect-cuboid nonexistence.

```text
STAGE13_13FN=COMPLETE_R06_CANONICAL_PROOF_SYNTHESIS
R06_CANONICAL_PROOF_SINGLE_ENTRYPOINT=true
R06_MANDATORY_THEOREM_LEVEL_GATES_A_B_C_COMPLETE=true
SUM_IQ_ANALYTIC_PROOF_COMPLETE=true
HECKE_PRIMARY_SOURCE_CONTRACT_VERIFIED=true
PROOF_TO_HLR_INDEX=k_HLR=2*ell
PRINCIPAL_POLE_SECTOR=KER_REDUCED_POLE_SIGNATURE_MAP
TAGGED_FACTOR_TWO_UPPER_BOUND_PROVED=true
NONPRINCIPAL_POLE_LOSS_PROVED=true
WIENER_MIXED_TERM_EXPLICIT=true
P5_EXPLICIT_FINITE_BOUND_LT=432
RETAINED_ELL_MIN=1
LAMBDA_3=1
FINITE_DATA_POSITIVE_CONVERGENCE_EVIDENCE_CLAIMED=false
GELFAND_LERAY_RADIAL_FACTOR=1/(P/d)
OE_EE_FACE_INDEPENDENCE_BRANCHWISE=true
BOX_COUNT_DERIVATION_EXPLICIT=true
HARMONIC_EXPONENT_DECOMPOSED=true
VAALER_ENDPOINT_CONVENTION_EXPLICIT=true
THETA_VARTTHETA_SEPARATION=true
KAPPA_ABSOLUTE_CONVERGENCE_EXPANSION_EXPLICIT=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R03_IMMUTABLE=true
R04_IMMUTABLE=true
R05_IMMUTABLE=true
R06_BUNDLE_CREATED=false
R06_FRESH_EXTERNAL_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fo
```
