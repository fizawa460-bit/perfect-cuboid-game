# Stage14-t34 — all-character Gaussian large sieve and same-modulus boundary

## Purpose

Stage14-t33 showed that the split-torus trace

\[
A_\lambda(s)=\chi_\lambda(\alpha s^4-\beta)
\]

has a full multiplicative Mellin spectrum on characters trivial on \(\mu_4\), with genuinely higher-order modes. The quadratic Hecke-family large sieve therefore does not by itself close the sparse norm-circle problem.

Stage14-t34 asks a sharper question: can the **entire** Mellin spectrum, independent of character order, be absorbed into an ordinary Gaussian large sieve?

The answer is yes at the one-variable level. A Gauss-sum transform converts every nontrivial multiplicative residue character modulo a Gaussian prime into additive characters, and Huxley's large sieve over \(\mathbf Z[i]\) then controls all orders simultaneously.

However, independently tensorising the resulting one-variable inequalities in \(U\) and \(V\) loses the shared auxiliary modulus. On the physical norm hyperbola this produces an unavoidable factor \(\sqrt{M}\), where \(M\asymp X/\ell\) is the direction-cofactor norm scale. Therefore the naive all-character tensor product still does **not** prove the Stage14 power saving.

The exact information lost by tensorisation is also identified: for the same Gaussian prime modulus, character orthogonality forces the **same prime** to divide both Gaussian differences in a pair of Stage14 states. That shared-prime collision kernel is the next object to exploit.

No global \(A_{1,1}\) power saving is claimed in t34.

## 1. All-order multiplicative characters reduce to the Gaussian additive large sieve

Let \(\varpi\in\mathbf Z[i]\) be a Gaussian prime of odd norm

\[
q=N(\varpi),
\]

and let \(\psi\) be a nontrivial multiplicative character of

\[
(\mathbf Z[i]/(\varpi))^\times.
\]

For a coefficient sequence \(a_z\), define

\[
M_\psi=\sum_z a_z\psi(z)
\]

and the additive transform

\[
S_\varpi(c)
=\sum_z a_z\,e\!\left(\Re\frac{zc}{\varpi}\right).
\]

The finite-field Gauss sum gives

\[
\tau(\bar\psi)
=\sum_{c\bmod\varpi}\bar\psi(c)
 e\!\left(\Re\frac{c}{\varpi}\right),
\qquad
|\tau(\bar\psi)|^2=q,
\]

and hence

\[
\boxed{
M_\psi
=\tau(\bar\psi)^{-1}
\sum_{c\bmod\varpi}^{*}
\bar\psi(c)S_\varpi(c).
}
\tag{34.1}
\]

Summing over all nontrivial multiplicative characters and using multiplicative orthogonality gives the exact identity

\[
\boxed{
\sum_{\psi\ne1}|M_\psi|^2
=
\frac1q
\left(
(q-1)\sum_{c\bmod\varpi}^{*}|S_\varpi(c)|^2
-\left|\sum_{c\bmod\varpi}^{*}S_\varpi(c)\right|^2
\right)
\le
\sum_{c\bmod\varpi}^{*}|S_\varpi(c)|^2.
}
\tag{34.2}
\]

This identity is **independent of the order of \(\psi\)**.

The Stage14 Mellin family is the subfamily

\[
\mathcal X_\varpi^{(4)}
=
\{\psi:\psi|_{\mu_4}=1\},
\]

so dropping characters only improves the inequality.

Applying Huxley's Gaussian additive large sieve therefore yields

\[
\boxed{
\sum_{N(\varpi)\le L}
\sum_{\substack{\psi\in\mathcal X_\varpi^{(4)}\\\psi\ne1}}
\left|\sum_{N(z)\le Z}a_z\psi(z)\right|^2
\ll
(Z+L^2)\sum_{N(z)\le Z}|a_z|^2.
}
\tag{34.3}
\]

Thus all character orders produced in t33 — cubic, quartic, septic, nonic, decic, and so on — are absorbed by one order-free inequality.

A convenient modern reference recording Huxley's \(\mathbf Z[i]\) large sieve is S. Baier and A. Bansal, *Large sieve with sparse sets of moduli for \(\mathbf Z[i]\)*, arXiv:1811.07300, equation (4). Their Theorem 4 also gives a stronger additive estimate when the Gaussian moduli themselves are restricted to primes in a suitable range.

## 2. The \(\mu_4\)-restriction costs nothing analytically

For a split rational prime \(\lambda\equiv1\pmod4\), the residue group is cyclic of order \(\lambda-1\). Characters trivial on the four Gaussian units form a subgroup of the dual group of size

\[
\boxed{\frac{\lambda-1}{4}.}
\]

If a primitive root identifies multiplicative characters by exponents \(j\bmod \lambda-1\), then

\[
\psi_j|_{\mu_4}=1
\iff
j\equiv0\pmod4.
\]

This is exactly the support restriction found in t33. Therefore the higher-order Mellin modes are not an exceptional family requiring separate large-sieve theorems; they are simply a fixed-index subfamily of all multiplicative residue characters.

## 3. Mellin packet has bounded spectral energy

Normalize the t33 Mellin coefficients by

\[
c_\lambda(\psi)
=\frac{\widehat A_\lambda(\psi)}{\lambda-1}.
\]

Parseval gives

\[
\boxed{
\sum_\psi |c_\lambda(\psi)|^2
=\frac1{\lambda-1}
\sum_{s\in\mathbf F_\lambda^*}|A_\lambda(s)|^2
\le1.
}
\tag{34.4}
\]

For

\[
T_\lambda(s,t)=A_\lambda(s/t)B_\lambda(st),
\]

the t33 change of Mellin variables is

\[
(\psi,\phi)
\longmapsto
(\xi,\zeta)
=(\psi\phi,\phi\psi^{-1}).
\]

On the \(\mu_4\)-trivial support this map has multiplicity at most two. Consequently the aggregated two-variable packet satisfies

\[
\boxed{
\sum_{\xi,\zeta}|C_\lambda(\xi,\zeta)|^2\le2.
}
\tag{34.5}
\]

So the Mellin expansion itself introduces no polynomial spectral-energy loss.

A standard Weil bound for the individual mixed Mellin sums gives

\[
|c_\lambda(\psi)|\ll\lambda^{-1/2}
\]

uniformly in the allowed character order. In particular, spectral axes where one of \(\xi,\zeta\) is trivial have total energy \(O(\lambda^{-1})\). The large contribution in t33 was therefore not spectral coefficient growth; it was the geometry of the sparse integral index set.

## 4. Naive two-variable tensorisation

Let the Gaussian variables lie in a rectangle

\[
N(U)\le M,
\qquad
N(V)\le N,
\qquad M\le N.
\]

If the shared auxiliary modulus is discarded and the \(U\)- and \(V\)-characters are allowed independent Gaussian prime moduli, tensorising (34.3) gives

\[
\boxed{
\mathcal L_{\rm tensor}(M,N;L)
\ll
(M+L^2)(N+L^2)\sum_{U,V}|a_{U,V}|^2.
}
\tag{34.6}
\]

Combined with the bounded packet energy (34.5), this gives a valid all-character bound for the Stage14 trace after enlarging to independent moduli.

For a square detector using \(P(L)=L^{1-o(1)}\) split auxiliary primes of size \(L\), duality yields the schematic point bound

\[
\boxed{
N_{\rm square}^{\rm tensor}(M,N)
\ll
\frac{(M+L^2)(N+L^2)}{L^{1-o(1)}}.
}
\tag{34.7}
\]

The crucial point is that no choice of \(L\) makes this smaller than the physical norm-hyperbola mass.

Indeed,

\[
M+L^2\ge2L\sqrt M,
\qquad
N+L^2\ge N,
\]

so

\[
\boxed{
\frac{(M+L^2)(N+L^2)}L
\ge2N\sqrt M.
}
\tag{34.8}
\]

On the super-square-root Stage14 shell,

\[
M\asymp X/\ell,
\qquad
N\asymp B/\ell,
\]

while t32 showed that the actual unsieved norm skeleton has only

\[
\boxed{(B/\ell)B^{o(1)}=N B^{o(1)}}
\]

states.

Therefore tensorisation loses at least

\[
\boxed{\sqrt{X/\ell}}
\]

relative to the correct ambient hyperbolic mass whenever \(X/\ell\to\infty\).

Thus

\[
\boxed{
\text{all-character large sieve succeeds, but independent tensorisation cannot close the Stage14 norm hyperbola.}
}
\]

## 5. Exact information lost by tensorisation

The failure in section 4 is not caused by higher-order characters. It comes from forgetting that both Mellin variables use the **same** auxiliary Gaussian prime.

Let

\[
h_\lambda=|\mathcal X_\varpi^{(4)}|=(\lambda-1)/4.
\]

Character orthogonality on the quotient by Gaussian units gives

\[
\boxed{
\sum_{\psi\in\mathcal X_\varpi^{(4)}}
\psi(U)\overline{\psi(U')}
=
h_\lambda\,
\mathbf 1_{\,U\equiv uU'\ (\varpi)\text{ for some }u\in\mu_4}.
}
\tag{34.9}
\]

For the two-variable family with the **same modulus**,

\[
\boxed{
\sum_{\xi,\zeta\in\mathcal X_\varpi^{(4)}}
\xi(U)\overline{\xi(U')}
\zeta(V)\overline{\zeta(V')}
=
h_\lambda^2
\mathbf 1_{U\equiv uU'\ (\varpi)}
\mathbf 1_{V\equiv vV'\ (\varpi)}.
}
\tag{34.10}
\]

Hence every off-diagonal collision requires one and the same Gaussian prime \(\varpi\) to divide

\[
U-uU'
\quad\text{and}\quad
V-vV'.
\]

Equivalently, its rational norm \(\lambda\) divides both

\[
N(U-uU')
\quad\text{and}\quad
N(V-vV').
\]

This simultaneous divisibility is completely destroyed by the independent-modulus enlargement used in (34.6).

The next useful inequality must exploit precisely this shared-prime collision kernel together with the physical norm relation

\[
N(V)=k\delta,
\qquad
k\mid\varepsilon N(U),
\qquad
N(U)\delta\ll B/\ell.
\]

## 6. Revised analytic architecture

The analytic picture after t34 is now:

```text
local quartic character
        |
        v
split-torus Mellin expansion
        |
        +-- arbitrary character orders: CLOSED by Gauss transform + Gaussian large sieve
        |
        +-- mu_4 spectral support: exact fixed-index restriction
        |
        v
same-modulus two-variable packet
        |
        +-- independent tensorisation: too expensive by sqrt(X/ell)
        |
        v
shared-prime collision / dispersion problem
        |
        v
physical norm hyperbola k|epsilon*m, m*delta << B/ell
```

So t33's higher-order spectral obstruction is removed. The remaining obstruction is a genuinely **bilinear same-modulus dispersion problem on a divisor-coupled Gaussian hyperbola**.

## 7. Frozen finite audit

The deterministic t34 audit retains the t33 model

\[
A_\lambda(s)=\chi_\lambda(s^4-4)
\]

for

```text
lambda = 13, 17, 29, 37, 41.
```

It verifies:

1. the exact finite-field Gauss-transform energy identity (34.2) for a deterministic coefficient vector;
2. the \(\mu_4\)-trivial character count \((\lambda-1)/4\);
3. full quotient-character orthogonality (34.9) on every nonzero residue pair;
4. Mellin Parseval energy \(\le1\);
5. two-factor packet energy \(\le2\);
6. the conservative sampled individual coefficient bound \(|c_\lambda(\psi)|\le4/\sqrt\lambda\);
7. the algebraic tensor barrier (34.8).

Frozen sample energies:

```text
lambda   all nontrivial mult. energy   mu4-trivial subfamily
  13              515                         158
  17              911                          67
  29             3136                         364
  37             5075                         602
  41             6199                        1229
```

In every case the all-nontrivial multiplicative energy equals the additive Gauss-transform expression to numerical precision.

These are finite Fourier diagnostics only; the asymptotic inequality (34.3) comes from the Gaussian additive large sieve, not from the finite sample.

## Boundary

```text
STAGE14_T34=COMPLETE_ALL_CHARACTER_GAUSSIAN_LARGE_SIEVE_AND_TENSOR_BARRIER
ALL_CHARACTER_GAUSS_TRANSFORM_EXACT=true
ALL_CHARACTER_GAUSSIAN_MULTIPLICATIVE_LARGE_SIEVE=true
MU4_SUBFAMILY_FIXED_INDEX=true
MELLIN_PACKET_L2_ENERGY_BOUNDED=true
HIGHER_ORDER_MELLIN_MODES_LARGE_SIEVE_OBSTRUCTION=false
NAIVE_TWO_VARIABLE_TENSORIZATION_BOUND=(M+L^2)(N+L^2)
TENSOR_SQUARE_DETECTOR_LOWER_ENVELOPE=2N*sqrt(M)
TENSOR_LARGE_SIEVE_CLOSES_NORM_HYPERBOLA=false
SAME_MODULUS_SHARED_PRIME_COLLISION_IDENTITY=true
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
VISIBLE_BRANCH_POWER_SAVING_PROVED=false
INVISIBLE_BRANCH_POWER_SAVING_PROVED=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t35 prove a same-modulus dispersion/large-sieve bound from the shared-prime collision conditions varpi|(U-uU') and varpi|(V-vV'), retaining k|epsilon*N(U) and N(U)*delta<<B/ell
```
