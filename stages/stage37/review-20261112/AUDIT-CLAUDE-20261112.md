# Audit of CONTINUATION-JUDGEMENT.md (Claude, 2026-11-12, main 9ceaab7f)

Status: reading audit. Proposal only. No STATE, ledger or credit change.

## Verdict: PASS with one change. I recommend freezing all of Stage37.

The report recommends freezing everything except one finite check (degree-4/5 rational families).
I recommend skipping that check as well, for two reasons:

- It cannot close P/M3 → 0 whatever its result. The report says so itself.
- The best it can do is raise M3 to B^{1/2}. That leaves the numerator target at o(B^{1/2}),
  which Stage14 records as open.

So the check goes on the "open questions" list. It is not a task. The user agreed on 2026-11-12.

| Item | Verdict | Note |
|---|---|---|
| Script `check_low_degree_curves.py` | PASS | Reran from the repo root. Output matches the saved `.out` byte for byte (after CRLF normalisation). ALL PASS. |
| Q1: definitions match | PASS | P(B)=T(B) ≪ B^{1/2+ε} is boxed in `29-10/result.md` l.49. Stage14 `final.md` l.31 and l.161 state that a strict B^{1/2−δ} is not proved. The census value M3(10⁶)=219 is in `stage20/final.md` l.64. |
| Q2: Lemma L (n ≤ 3) | PASS | See the checks below. |
| Q2: M3 ≪ B^{1/2+ε} under Batyrev–Manin | PASS as conditional | The argument is right: off U(ε) there are finitely many curves, and a rational curve of degree n contributes B^{2/n}, with n ≥ 4 by Lemma L. The nef-and-big height comparison is an outline only, as the report says. |
| Q3: general methods are weaker than 1/2 | PASS as conditional | The conclusion holds whatever the exact form of Salberger Thm 0.8, provided the leading exponent is ≥ 1/2. I did not check the theorem statement against the source. |
| Q3: Bombieri–Lang + Stage32 ⇒ P/M3 → 0 | PASS as conditional, no credit | This depends on Stage32's degree convention (curve degree in P⁶), which I did not check. It must not be counted as progress. |
| Q4: loop pattern | PASS as estimate | The counts come from regex matches on summary fields. The repeated "small side negligible, rest OPEN" shape is visible, and the ledger itself has an anti-loop field. |
| Q5: degenerate points | PASS | Both P and M3 require 0<a<b<c. Counting arguments bound sizes. They do not test emptiness, so the Stage33 trap does not apply. |

## Checks on Lemma L

**Proportional case for n = 3 (the report lists it as unverified).** I checked it by hand.

- Suppose deg gcd(a,b) = 3, i.e. b = λa.
- By parity, deg gcd(a,c) ∈ {1,3}.
  - If it is 3, the curve is a point.
  - If it is 1, then a = lα and c = lγ, with α and γ coprime quadratics. This is the n = 2
    proportional case, so λ = ±1 and 1+λ² = 2, which is not a square. No family.

**Non-proportional case for n = 3.**

- The three pairwise gcds are distinct linear forms. If two of them were equal, that form would
  divide gcd(a,b,c) = 1.
- So the forms can be moved to r, s, r+s, which gives a = rsα, b = r(r+s)β, c = s(r+s)γ. This
  matches the script.
- The Gröbner step shows that g1 and then g0 lie in the radical, so c ≡ 0.

**Counting points on a curve.** On a degree-n parametrised curve, R ≍ max(|a|,|b|,|c|), so the
curve has ≍ B^{2/n} points. As the report says, a map that is not 1-to-1 only lowers the count.

## Notes (not blocking)

1. In §2.3 the bound is written "B^{1/2} + B^ε". The report's own conclusion line writes
   B^{1/2+ε}. Either form serves the argument.
2. The census exponents fluctuate between 0.48 and 0.61, and M3/B^{1/2} ≈ 0.16–0.22. This is
   consistent with either a degree-4 family or pre-asymptotic behaviour. That is the open
   question recorded in the freeze note.
3. All inherited inputs (Stage14, Stage20, 28-50-r2, A44, A47) are used as recorded. None was
   re-audited here.

## Net

Freeze Stage37. Do not resume the A47 forcing line, the DEN route, or determinant-method
attempts. The restart conditions are in `stages/stage37/STAGE37-FROZEN-20261112.md`.
