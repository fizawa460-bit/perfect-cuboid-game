# Stage29-02e — Horie--Yamauchi source lock

```text
ROLE=ENDPOINT_LFUNCTION_PRIMARY_SOURCE_LOCK
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

Primary source:

- Madoka Horie, Takuya Yamauchi, `The L-function of the surface parametrizing cuboids`, arXiv:2512.22520v3, revised 24 March 2026.
- Subjects: math.NT / math.AG.

The paper studies exactly the Stoll--Testa full cuboid surface `Sbar` and its minimal resolution `S`, i.e. the same Stage29 endpoint geometry.

## Theorem 1.1

For every prime `ell`, the source proves

```text
L(s,H2(S))
 = L(s,H2(Sbar)) * zeta(s-1)^24 * L(s-1,chi_{Q(i)})^24.
```

For the singular canonical model,

```text
L(s,H2(Sbar))
 = L(s,h16)^3 * L(s,h32) * L(s,h8)^3 * L(s-1,L_ell),
```

where `h_N` is the unique weight-3 newform of level `N in {8,16,32}` with rational Fourier coefficients and

```text
L(s,L_ell)
 = zeta(s)^10
   * L(s,chi_{Q(i)})^2
   * L(s,chi_{Q(sqrt(-2))})
   * L(s,chi_{Q(sqrt(2))})^3.
```

The same theorem determines `Pic(S_Qbar)` as a free rank-64 Galois module with generators distributed by fields of definition as

```text
34 over Q,
26 strictly over Q(i),
1 strictly over Q(sqrt(-2)),
3 strictly over Q(sqrt(2)).
```

## Cohomological dimensions

The source's Lemma 2.1 proves

```text
rank H2(Sbar)=30,
H2(Sbar) pure of weight 2,
H3(Sbar)=0.
```

The smooth resolution has `rank H2(S)=78`; the 48 exceptional curves account for the difference.  The surface has `q=0`, so the smooth model has no H1/H3 contribution to good-prime point counts.

The transcendental/non-Tate part of `H2(Sbar)` has dimension 14:

```text
3 copies of h16,
1 copy of h32,
3 copies of h8,
```

each weight-3 modular representation being two-dimensional.  The remaining 16 dimensions are Tate/Dirichlet-character algebraic pieces.

## Modular-cover provenance

The source also recalls and uses the exact modular presentation

```text
Sbar_{Q(i)} ~= (X(8) x X(8))/Delta G,
G=ker(PSL2(Z/8Z) -> PSL2(Z/4Z)),
```

with `X(8)` genus 5.  This provides an independent route from the endpoint geometry to the modular forms appearing in Theorem 1.1.

## Stage29 scope firewall

```text
ENDPOINT_LFUNCTION_COMPUTED=true
ENDPOINT_GALOIS_PICARD_MODULE_COMPUTED=true
RATIONAL_POINT_SET_COMPUTED=false
PERFECT_CUBOID_EXISTENCE_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
LOCAL_TRACE_TO_PHYSICAL_COUNT_ADAPTER_REQUIRED=true
```

An L-function factorization is arithmetic structure, not a perfect-cuboid point-count theorem.
