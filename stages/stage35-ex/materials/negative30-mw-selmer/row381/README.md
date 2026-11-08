# Row381 reproducibility

Use Python 3 with python-flint. Run from this directory.

    sha256sum -c SHA256SUMS
    python verify_row381.py > class_replay.json
    cmp class_replay.json row381_exact.json
    python verify_units381.py > unit_replay.json
    cmp unit_replay.json units381_exact.json
    python verify_rank31.py > rank_replay.json
    cmp rank_replay.json rank31_exact.json
    python zero_pair_sieve.py > sieve_replay.json
    cmp sieve_replay.json zero_pair_sieve_exact.json

The first replay verifies all 3,682 new exact principal witnesses, binary
relations and both Arb signs. It consumes the independently audited
row380 parent supports, the row378 table and row379 degree-one counts.
The second verifies integral valuation cancellation in 55 norm-one units
using 259 referenced generators, and the exact 2-adic and real images.
The third starts from the rational Mumford divisors and computes the entire
31-adic scalar chains with iterative reduction and a checked function
reduction. The final replay gives the optional conditional zero-Artin
slope table. It uses the same-source reductions established in row378.

The only analytic hypothesis of the signed exclusion is GRH for the
nontrivial ordinary unramified quadratic Hecke L-functions of K. The
Selmer dimension formula in PROOF.md is unconditional. Row381 is pending
independent mathematical audit.
