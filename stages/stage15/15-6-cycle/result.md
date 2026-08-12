# Stage15-6-cycle — aj through am

Base: merged Stage15-6ai (`PR #841`, merge commit `cad267c7`).

This cycle advances four consecutive exact substages and stops at the first genuine new theorem boundary.

## Cycle path

```text
6aj
  exact raw-gcd / physical-height bridge
  G=gamma*h_alpha*h_beta, gamma in {2,4}
  R=(2/gamma)*k*N(z)*N(w)
  -> exact product height k*N(z)*N(w)<=2B

6ak
  remove the fake polynomial outer-curve sum
  x+i y=K_alpha*z^2, p+i q=K_beta*w^2
  toric compatibility iff x*y*p*q is square
  -> unique reconstruction of (m,n),(r,s),h_alpha,h_beta

6al
  define coordinate-product core
  kappa=sf(x*y)=sf(p*q)
  -> exact four pairwise-coprime squareclass cells
  -> gcd(k,kappa)=1
  -> kappa is a new legal primitive root-line modulus

6am
  large kappa: root-line spacing gives
    N_{kappa>=L} << B^o(1)*(min(Z,W)+Z*W/L)
  kappa^2>=Z*W -> sqrt(Z*W) collapse
  small kappa: exact separable quartic genus-one receiver
    kappa*T^2=f_K(a,b)*g_K(a,b)
  -> stop at new moving-quartic counting theorem gate
```

## Cycle verdict

The cycle materially changes the post-6ai picture.

The smooth genus-one curve family indexed by `(m,n)` remains a correct local model, but `(m,n)` is not an independent global counting index once both primitive Gaussian square values are retained. The physical count can instead be covered by global Gaussian data with one coordinate-product squareclass condition and the exact hyperbola height.

A second squarefree core `kappa` then appears. It is coprime to the original norm core `k`, so using it is not a recharge. Its large branch is quantitatively controlled. The unresolved branch is now the small-`kappa` quartic family, not the original moving two-quadric family.

## Frozen cycle exit

```text
STAGE15_6_CYCLE_START=6aj
STAGE15_6_CYCLE_END=6am
STAGE15_6_CYCLE_EXACT_PRODUCT_HEIGHT=true
STAGE15_6_CYCLE_OUTER_PAIR_RECONSTRUCTED_FROM_GLOBAL_POINT=true
STAGE15_6_CYCLE_COORDINATE_CORE_DEFINED=true
STAGE15_6_CYCLE_NORM_AND_COORDINATE_CORES_COPRIME=true
STAGE15_6_CYCLE_LARGE_COORDINATE_CORE_SQRT_COLLAPSE=true
STAGE15_6_CYCLE_SMALL_KAPPA_QUARTIC_GENUS_ONE_GATE=true
STAGE15_6_CYCLE_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6_CYCLE_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6_CYCLE_EXIT=SMALL_KAPPA_MOVING_QUARTIC_COUNTING_THEOREM_AUDIT_READY
```

The next substage, if opened, is `Stage15-6an`: audit the exact theorem species for the small-`kappa` moving quartic family under `k*N(z)*N(w)<=2B`, preserving every physical mask and the common `kappa` coupling. No averaged elliptic-curve result may be promoted without an AR-027 exceptional-set bridge.
