#!/usr/bin/env python3
"""Stage12-N1-2i: Ramanujan/exponent-pair compatibility audit.

Exact checks:
  c_q(n)=sum_{r|(q,n)} r mu(q/r),
  sum_{n mod q}|c_q(n)|^2=q phi(q),
  sum_{n<=K}|c_q(n)|<=K 2^omega(q).

The analytic entries are exponent budgets conditional on standard smoothed
Poisson/stationary-phase and exponent-pair estimates.  No asymptotic theorem is
claimed.
"""
from __future__ import annotations
import argparse, json, math
from fractions import Fraction
from pathlib import Path

OUT = Path("data/exponent_budget_stage12_n1_2i_report.json")
QMAX, KMAX = 128, 256
LOGS = [16, 32, 64, 128, 256, 512, 1024]


def primes(n: int) -> list[int]:
    out, p = [], 2
    while p*p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def divisors(n: int) -> list[int]:
    out = []
    for d in range(1, math.isqrt(n)+1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return out


def mu(n: int) -> int:
    ans = 1
    for p in primes(n):
        if n % (p*p) == 0:
            return 0
        ans = -ans
    return ans


def phi(n: int) -> int:
    ans = n
    for p in primes(n):
        ans -= ans//p
    return ans


def cq(q: int, n: int) -> int:
    return sum(d*mu(q//d) for d in divisors(math.gcd(q, n)))


def direct_cq(q: int, n: int) -> int:
    z = sum(
        (complex(math.cos(2*math.pi*a*n/q), math.sin(2*math.pi*a*n/q))
         for a in range(1, q+1) if math.gcd(a, q) == 1),
        0j,
    )
    value = int(round(z.real))
    if abs(z.real-value) > 1e-8 or abs(z.imag) > 1e-8:
        raise ArithmeticError((q, n, z))
    return value


def checks() -> dict[str, int]:
    formula = parseval = first = 0
    for q in range(1, QMAX+1):
        vals = []
        for n in range(q):
            v = cq(q, n)
            if v != direct_cq(q, n):
                raise ArithmeticError(("formula", q, n))
            vals.append(v)
            formula += 1
        if sum(v*v for v in vals) != q*phi(q):
            raise ArithmeticError(("parseval", q))
        parseval += 1
        total, factor = 0, 1 << len(primes(q))
        for k in range(1, KMAX+1):
            total += abs(cq(q, k))
            if total > k*factor:
                raise ArithmeticError(("first moment", q, k))
            first += 1
    return {"formula": formula, "parseval": parseval, "first_moment": first}


def shallow(t: float) -> float:
    return 6*t*t - 8*t**3 + 3*t**4


def report() -> dict:
    k, l = Fraction(1, 6), Fraction(2, 3)
    den = Fraction(3, 2)+k
    delta = {
        "Qd": str(1/den),
        "U": str((l-1)/den),
        "R": str((Fraction(-1, 2)+k)/den),
    }
    wing = {"X": str(k/(1+k)), "Y": str((k+l)/(1+k))}
    assert delta == {"Qd": "3/5", "U": "-1/5", "R": "-1/5"}
    assert wing == {"X": "1/7", "Y": "5/7"}

    rows = []
    for L in LOGS:
        tau = L**(-0.25)
        S0 = math.exp(0.5*tau*tau*L)
        rows.append({
            "log_B": L,
            "tau_sigma": tau,
            "shallow_fraction": shallow(tau),
            "terminal_fraction": tau,
            "S0": S0,
            "S0^-3/5": S0**(-0.6),
            "S0^-1": S0**(-1),
        })

    return {
        "metadata": {
            "stage": "12-N1-2i",
            "title": "Ramanujan and exponent-pair budget",
            "generated_by": "scripts/audit_exponent_budget_stage12_n1_2i.py",
            "claim_status": "Exact identities and exponent algebra; compatibility audit only.",
        },
        "plain_language": {
            "result": (
                "The retained 15/32 clustered core and 1/4 wing are compatible "
                "with classical tools. The remaining conservative primitive obstacle "
                "is the shallow/terminal boundary-layer mass."
            )
        },
        "ramanujan": {
            "divisor_formula": "c_q(n)=sum_{r|gcd(q,n)}r*mu(q/r)",
            "pointwise": "|c_q(n)|<=gcd(q,n)",
            "second_moment": "sum_{n mod q}|c_q(n)|^2=q*phi(q)",
            "first_moment": "sum_{1<=n<=K}|c_q(n)|<=K*2^omega(q)",
            "key_correlation": (
                "A large divisor contribution r requires r|n, so large arithmetic "
                "coefficients occur only at proportionally larger dual frequencies."
            ),
            "checks": checks(),
        },
        "exponent_pair": {
            "pair": "(1/6,2/3)",
            "phase": "A*u^(-1/2), Z=A/sqrt(U)",
            "weighted_u_bound": "R^(1/2)*Z^(1/6)*U^(2/3)",
        },
        "core_Q_le_R": {
            "scope": "Both 9/32 and 15/32 two-dimensional zones.",
            "axis": "Each axis error is <=polylog(B)*M_block/Y.",
            "interior_shell": (
                "E_K<<W*U^lambda*R^(1/2+kappa)*Q^(-1/2-kappa)"
                "*K^(1/2+kappa)."
            ),
            "smoothing": {
                "Fourier": "W*U^lambda*R^(1/2+kappa)*Delta^(-1/2-kappa)",
                "boundary": "U*R*Delta/(Q*d)",
                "Delta_star": "(Q*d)^(3/5)*U^(-1/5)*R^(-1/5)",
                "Delta_exponents": delta,
                "relative_if_Delta_star_ge_1": "<=W*(d/R)^(3/5)",
                "relative_if_Delta_star_lt_1": "<=W/R",
            },
            "deep_result": (
                "Y=R/(c*d)>=S0 implies relative error "
                "<=polylog(B)*S0^(-3/5)."
            ),
            "decision": "The 15/32 clustering barrier disappears at exponent-budget level.",
        },
        "wing_Q_gt_R": {
            "coordinates": "X=R/(b*d)>=Y=R/(c*d)>=S0",
            "if_X_le_Y2": "D<<W*X^(1/7)*Y^(5/7), relative <=W*Y^(-8/7)",
            "wing_exponents": wing,
            "if_X_gt_Y2": "Trivial D<<W*Y, relative <W*Y^(-2)",
            "order_boundary": "Relative error <=W/Y",
            "decision": "The 1/4 wing has polylog(B)*S0^(-1) relative saving.",
        },
        "weighted_sum": {
            "divisor_weights": (
                "Fixed moments of 2^omega and tau cost only powers of log B "
                "after lambda_1-weighted harmonic summation."
            ),
            "S0_choice": "exp(0.5*sqrt(log B))",
            "retained_error": (
                "polylog(B)*exp(-c*sqrt(log B)), hence smaller than every "
                "fixed negative power of log B."
            ),
        },
        "boundary_layers": {
            "current_choice": "tau=sigma=(log B)^(-1/4)",
            "shallow_size": "B*(log B)^(7/2)",
            "terminal_size": "B*(log B)^(15/4)",
            "problem": (
                "They are o(B log^4 B), but exceed the conservative raw target "
                "B*(log B)^(2-eta) needed before absolute global Mobius inversion."
            ),
            "incompatibility": {
                "set": "tau=L^(-p), sigma=L^(-q)",
                "needed_to_discard": "p>1 and q>2",
                "log_short_side": "(1/2)*L^(1-p-q)",
                "conclusion": (
                    "Those requirements destroy growth of the short side. "
                    "The boundary layers must be evaluated, not discarded."
                ),
            },
        },
        "diagnostics": rows,
        "literature": [
            "Trudgian-Yang, Toward optimal exponent pairs, arXiv:2306.05599",
            "Pliego, Estimates for a three-dimensional exponential sum with monomials, arXiv:2211.02096",
            "Chan-Kumchev, On sums of Ramanujan sums, arXiv:1009.4432",
        ],
        "decision": {
            "classification": "A_retained_core_and_wing_close_boundary_layers_remain",
            "closed": [
                "15/32 clustered core exponent budget",
                "1/4 eccentric wing exponent budget",
                "retained deep/small-d discrepancy at the conservative primitive scale",
            ],
            "not_closed": [
                "shallow-height boundary layer",
                "terminal-u boundary layer",
                "full raw polynomial expansion or Mobius-coupled boundary treatment",
                "theorem-level smoothing and endpoint bookkeeping",
            ],
            "next_stage": (
                "12-N1-2j: restore shallow and terminal layers using floor-first "
                "summation, Mellin/Perron separation, or Mobius inversion before truncation."
            ),
        },
        "not_claimed": [
            "A proved raw or primitive asymptotic.",
            "That Ramanujan second moments alone suffice.",
            "Final constants or complete endpoint bookkeeping.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=OUT)
    args = parser.parse_args()
    data = report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(data["decision"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
