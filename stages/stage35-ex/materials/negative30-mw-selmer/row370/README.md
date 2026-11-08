# Stage35EX R3-07 row370

Run with Python 3.10+, SymPy, and python-flint.

    python3 verify_row370.py

The script rebuilds the two Ward polynomials from the recurrence and the
six reflected factors from their exact integer factorizations. It writes
row370_exact.json with all coefficients, modular survivor slopes, exact
root isolation intervals, and the verified rank-lower-bound classes.
Kummer bits are checked both by exponentiation in the residue fields
and by resultants giving norms. The proof gives the half-class identity,
the finite-local limitation, and the 31-adic logarithm condition.
