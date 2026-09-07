# Stage36 36-09AM source lock: uniform Tunnell branch filter

Accessed: 2026-09-07

## Tunnell theorem, unconditional direction

Primary bibliographic source:
- J. B. Tunnell, *A classical Diophantine problem and modular forms of weight 3/2*, Invent. Math. 72 (1983), 323–334.

Convenient theorem statement used by the verifier:
- MIT arithmetic-geometry notes, congruent-number section / Tunnell theorem. For squarefree positive `n`, put `a=1` when `n` is odd and `a=2` when `n` is even. If `n` is congruent, then among integer triples satisfying

```text
n/a = 2*a*x^2 + y^2 + 8*z^2,
```

the number with even `z` equals the number with odd `z`.

For odd `n`, this is equivalent to

```text
2 * #{n=2*x^2+y^2+32*z^2}
  = #{n=2*x^2+y^2+8*z^2}.
```

Only this necessary direction is used. Failure of the equality proves `n` is not congruent. Equality alone gives no unconditional congruent-number or positive-rank conclusion; the converse is BSD-conditional.

## Congruent-number curve bridge

For squarefree positive `n`,

```text
E_n : Y^2 = X^3 - n^2 X
```

has positive Mordell-Weil rank over `Q` iff `n` is congruent. Thus a failed Tunnell necessary equality implies `rank E_n(Q)=0`.

## Full-2 / Selmer decision boundary

Audited Stage36 36-09AJ identifies each common-u:v branch as a full-2 homogeneous-space class on its `E_n`; audited 36-09AK/AL establish the exact Selmer-to-Sha logic on the B=7 example.

For any Stage36 branch for which everywhere-local solubility has separately been proved:

1. the class lies in `Sel^2(E_n/Q)`;
2. if the Tunnell necessary equality fails, then `rank E_n(Q)=0`;
3. the branch is globally excluded once its explicit full-2 Kummer pair is certified outside `E_n(Q)/2E_n(Q)`;
4. if the Tunnell equality holds, Tunnell alone does not decide whether the class is in the Mordell-Weil Kummer image or maps nontrivially to `Sha(E_n)[2]`.

This is a branchwise classifier, not a uniform closure theorem.

## Stage36 same-skeleton diagnostic

The audited AF same-parameter pair has the same coarse residue skeleton

```text
(A mod 8,B mod 8,C mod 8,D mod 8,e,f,h)=(1,7,3,5,1,1,1)
```

but two actual `B` prime identities:

```text
B=7  -> n=73073,
B=23 -> n=240097.
```

Both are `1 mod 8`, yet exhaustive Tunnell counts differ:

```text
n=73073:  even-z count=480, total=896, equality fails;
n=240097: even-z count=384, total=768, equality holds.
```

The B=23 choice is not claimed locally admissible: audited AF already shows it fails selected-prime rows. Its role here is solely to prove that residue labels / mod-8 skeleton do not determine the Tunnell outcome; actual prime identity remains load-bearing.

## Scope firewall

This source lock does not use the BSD converse, does not classify all congruent numbers, does not turn Tunnell equality into a rational point, and does not prove a uniform receiver obstruction.