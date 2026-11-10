"""Same parent algorithms with arbitrary-size modular polynomial coefficients."""
from functools import cache
from flint import fmpz_mod_poly_ctx, nmod_poly
@cache
def context(p):return fmpz_mod_poly_ctx(int(p))
def polynomial(coefficients,p):
    return nmod_poly(coefficients,p) if p<2**64 else context(p)(coefficients)
def activate(units,parent,primality):
    # Clear factor caches before installing the per-modulus representation adapter.
    parent.prime_factors.cache_clear()
    parent.nmod_poly=polynomial
    units.nmod_poly=polynomial
    parent.is_prime=primality
