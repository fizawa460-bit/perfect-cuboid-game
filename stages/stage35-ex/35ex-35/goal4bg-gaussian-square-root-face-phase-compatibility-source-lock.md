# Stage35-EX Goal4BG source lock — Gaussian face square roots and space-phase compatibility

Scope: continue exact-green Goal4BF on PR #1723. Audited authority remains V74 / Goal4AK. Goal4BG asks whether the three primitive Pythagorean face Gaussian square roots, together with the common space diagonal, determine the cross-conjugate quartic phase gauge left open by Goal4BF.

The result is mixed: the source does canonically produce six Gaussian square-root factorizations and an exact reservoir/space-gcd coupling, but the common space diagonal exposes a new valuation-stripped leading-unit sign rather than fixing the Goal4BF phase gauge. No branch pruning is obtained.

## 1. Retained primitive six-variable source

Use

```text
A=x*y*a,
B=x*z*b,
C=y*z*c,
```

with pairwise-coprime `x,y,z`, pairwise-coprime `a,b,c`, and

```text
gcd(a,z)=gcd(b,y)=gcd(c,x)=1.
```

The primitive reduced faces are

```text
r_AB^2=(y*a)^2+(z*b)^2,
r_AC^2=(x*a)^2+(z*c)^2,
r_BC^2=(x*b)^2+(y*c)^2.                         (BG-FACE)
```

Each leg pair is primitive and of opposite parity, and every `r_**` is odd.

Goal4AU/BE define

```text
h_a=gcd(a,r_BC),
h_b=gcd(b,r_AC),
h_c=gcd(c,r_AB),                                (BG-H)
```

with pairwise-coprime odd reservoirs. Goal4BF gives the source-selected Gaussian primes above every prime in the squarefree reservoir kernels `s_a,s_b,s_c`.

## 2. Each primitive face is a source-oriented Gaussian square

Define

```text
Phi_AB = y*a + i*z*b,
Phi_AC = x*a + i*z*c,
Phi_BC = x*b + i*y*c.                              (BG-Phi)
```

For a primitive opposite-parity pair `(u,v)`, `u+i*v` and `u-i*v` are coprime in `Z[i]`: an odd common Gaussian prime would divide both `u` and `v`, while `1+i` does not divide a Gaussian integer whose real and imaginary parts have opposite parity.

Since

```text
Phi_AB*bar(Phi_AB)=r_AB^2
```

and `Z[i]` is a UFD, every prime exponent in `Phi_AB` is even. Hence

```text
Phi_AB = eps_AB*Theta_AB^2,
Phi_AC = eps_AC*Theta_AC^2,
Phi_BC = eps_BC*Theta_BC^2,                         (BG-FSQ)
```

for units `eps_** in {+1,-1,+i,-i}`.

Choose each `Theta_**` to be the unique primary associate. This fixes `Theta_**` and `eps_**` source-canonically. Conjugation is not a free choice: the source signs in `(BG-Phi)` choose `Phi_**`, while conjugation gives the opposite-oriented factor.

Norms are exact:

```text
N(Theta_AB)=r_AB,
N(Theta_AC)=r_AC,
N(Theta_BC)=r_BC.                                  (BG-FN)
```

## 3. Goal4BF oriented reservoir kernels sit inside the face square roots

For `ell|s_a`, Goal4BF selects

```text
p_{a,ell}=(ell,i-iota_a(ell)),
iota_a(ell)=x*b/(y*c) mod ell,
```

and proves

```text
v_{p_{a,ell}}(x*b-i*y*c)=2*v_ell(r_BC).
```

But

```text
x*b-i*y*c = bar(eps_BC)*bar(Theta_BC)^2.
```

Therefore

```text
v_{p_{a,ell}}(bar(Theta_BC))=v_ell(r_BC),             (BG-div-a)
```

and the squarefree oriented kernel satisfies

```text
Sigma_a | bar(Theta_BC).                              (BG-Sigma-a)
```

Cyclically,

```text
Sigma_b | bar(Theta_AC),
Sigma_c | bar(Theta_AB).                              (BG-Sigma)
```

Thus Goal4BF's oriented Gaussian kernels are literal divisors of the source-canonical primitive face square roots.

## 4. Reservoirs are exactly the gcds of the opposite space-face legs

The original space square gives

```text
W^2=A^2+D_BC^2=B^2+D_AC^2=C^2+D_AB^2,
D_AB=x*r_AB,
D_AC=y*r_AC,
D_BC=z*r_BC.                                         (BG-W)
```

Using the exact coprimality dictionary and the fact that a primitive Pythagorean hypotenuse is coprime to both legs,

```text
gcd(A,D_BC)
 = gcd(x*y*a,z*r_BC)
 = gcd(a,r_BC)
 = h_a.                                               (BG-gcd-a)
```

Likewise

```text
gcd(B,D_AC)=h_b,
gcd(C,D_AB)=h_c.                                      (BG-gcd)
```

Consequently each `h_i` divides `W`, and division gives three primitive Pythagorean space triples:

```text
(A/h_a)^2+(D_BC/h_a)^2=(W/h_a)^2,
(B/h_b)^2+(D_AC/h_b)^2=(W/h_b)^2,
(C/h_c)^2+(D_AB/h_c)^2=(W/h_c)^2.                    (BG-space-triples)
```

## 5. The common space diagonal also gives three canonical Gaussian squares

Define

```text
Omega_a = D_BC/h_a + i*A/h_a
        = z*(r_BC/h_a) + i*x*y*(a/h_a),
Omega_b = D_AC/h_b + i*B/h_b,
Omega_c = D_AB/h_c + i*C/h_c.                        (BG-Omega)
```

Each reduced space leg pair is primitive and of opposite parity. The same Gaussian-UFD argument gives unique primary square roots and units

```text
Omega_a = nu_a*Psi_a^2,
Omega_b = nu_b*Psi_b^2,
Omega_c = nu_c*Psi_c^2,                              (BG-SSQ)
```

with

```text
N(Psi_a)=W/h_a,
N(Psi_b)=W/h_b,
N(Psi_c)=W/h_c.                                      (BG-SN)
```

So the endpoint supplies six source-oriented Gaussian square roots: three face roots `Theta_**` and three space roots `Psi_*`.

## 6. What a reservoir prime sees after the common gcd is stripped

Fix `ell|s_a` and write

```text
m_a=v_ell(h_a)=min(v_ell(a),v_ell(r_BC)),
a'=a/ell^m_a,
r'=r_BC/ell^m_a.                                    (BG-leading)
```

At least one of `a',r'` is an `ell`-adic unit. The BF source orientation is determined before this division by

```text
iota_a(ell)=x*b/(y*c) mod ell,
iota_a(ell)^2=-1.                                   (BG-iota)
```

The reduced space factor instead is

```text
Omega_a = z*r' + i*x*y*a'.                           (BG-Omega-a-local)
```

There are two exact cases.

### Unequal valuation case

If

```text
v_ell(a) != v_ell(r_BC),                              (BG-unequal)
```

then exactly one of `a',r'` vanishes modulo `ell`. Hence `Omega_a mod ell` has only one nonzero leg and the space triple supplies no new square root of `-1` modulo `ell`. In particular there is no second Gaussian-prime orientation above `ell` to compare with the BF orientation.

### Tied-leading-unit case

If both `a'` and `r'` are units and additionally

```text
ell | W/h_a,                                          (BG-secondary)
```

then reducing `(BG-space-triples)` gives

```text
(z*r'/(x*y*a'))^2=-1 mod ell.                         (BG-lambda-square)
```

Define

```text
lambda_a(ell)=z*r'/(x*y*a') mod ell.                  (BG-lambda)
```

Both `lambda_a(ell)` and `iota_a(ell)` are square roots of `-1`, so necessarily

```text
lambda_a(ell)=sigma_a(ell)*iota_a(ell),
sigma_a(ell) in {+1,-1}.                             (BG-sigma)
```

This `sigma_a(ell)` is a new valuation-stripped source sign. Cyclic analogues `sigma_b,sigma_c` exist in the corresponding secondary-orientation cases.

## 7. Why the Goal4BF cross-conjugate phase gauge is not fixed yet

Goal4BF's unresolved phases are represented by

```text
G_ab=[bar(Sigma_b)/Sigma_a]_4,
G_ac=[bar(Sigma_c)/Sigma_a]_4,
G_bc=[bar(Sigma_c)/Sigma_b]_4.                        (BG-G)
```

The face square roots now source-lock the locations of `Sigma_i` through `(BG-Sigma)`. The common `W` square roots add `(BG-SSQ)`, but at a reservoir prime they do not universally identify the selected BF prime with a space-side selected prime:

- in the unequal-valuation case there is no secondary space orientation at all;
- in the secondary case the comparison introduces the new sign `sigma_i(ell)` from the leading quotients after removal of `h_i`.

The retained AU/BE/BF source equations do not determine these `sigma_i(ell)` or provide a cyclic product formula for them. Therefore the common space diagonal does not yet produce enough source-locked equations to fix all `G_ij`.

This is a precise blocker, not a claim that no deeper Gaussian relation exists.

## 8. Verdict and next missing object

Certified provisionally:

```text
THREE_FACE_GAUSSIAN_SQUARE_ROOTS=true;
PRIMARY_FACE_PHASE_SOURCE_LOCKED=true;
SIGMA_A_DIVIDES_BAR_THETA_BC=true;
SIGMA_B_DIVIDES_BAR_THETA_AC=true;
SIGMA_C_DIVIDES_BAR_THETA_AB=true;
H_A_EQUALS_GCD_A_DBC=true;
H_B_EQUALS_GCD_B_DAC=true;
H_C_EQUALS_GCD_C_DAB=true;
THREE_SPACE_GAUSSIAN_SQUARE_ROOTS=true;
SECONDARY_SPACE_ORIENTATION_CONDITIONAL=true;
NEW_LEADING_UNIT_SIGMA_BITS_EXPOSED=true;
BF_CROSS_CONJUGATE_GAUGE_FIXED=false;
BRANCH_PRUNING=false.
```

Not certified:

```text
quartic-phase contradiction;
any sigma_i fixed globally;
any h_i=1;
any d_i=1;
E1;
Stage35 closure;
Perfect Cuboid existence/nonexistence.
```

The next exact leaf is

```text
35EX-35_GOAL4BH_RESERVOIR_LEADING_UNIT_SPACE_FACE_SIGN_CYCLE_PREFLIGHT
```

Question: use the full `ell`-adic expansions of the face equation and the reduced space triple to determine the secondary signs `sigma_i(ell)` prime-by-prime, and test whether their cyclic product closes the remaining Goal4BE/Goal4BF phase freedom.

No merge. No hostile-audit credit. MAIN-STATE remains V74 / Goal4AK.
