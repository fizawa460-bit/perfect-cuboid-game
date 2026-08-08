# Stage14-e11 — literature audit for explicit thin-cover exponent and growing-prime sieve

Search date: 2026-08-09.

Classification vocabulary:

```text
EXACT_COLLISION
ADJACENT_RESULT
REUSABLE_METHOD
NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```

Absence from the present search is not a novelty certificate.

## 1. Huang v3 — primary theorem-level input

Zhizhong Huang, *Equidistribution of rational points and the geometric sieve for toric varieties*, arXiv:2111.01509v3, revised 17 July 2026.

Classification:

```text
REUSABLE_METHOD + THEOREM_LEVEL_INPUT
```

The paper proves effective Manin--Peyre equidistribution for smooth proper split toric varieties with globally generated anticanonical bundle, develops a uniform Selberg sieve, and gives quantitative bounds for adelic images of fibrations.

The exact inputs used by e11 are:

1. Theorem 1.4: effective equidistribution with error polynomial in the finite adelic covering exponent;
2. Theorem 3.11 and Corollary 3.13: uniform Selberg sieve for growing collections of local congruence conditions;
3. Theorem 1.6(1): a log-power saving for the adelic image of a proper generically finite map of degree greater than one;
4. the proof of Theorem 1.6(1), where the two explicit terms are

   \[
   \frac{B(\log B)^{r-1}}{N^{1-\varepsilon}}
   \quad\text{and}\quad
   N^{2(r+2\dim X+1)+\varepsilon}B(\log B)^{r-3/2+\varepsilon};
   \]

5. the multiplicative-function step used later in the paper to turn a prime sum of dimension `theta` into `G(N)=c(log N)^theta+O((log N)^(theta-1))`.

For Stage14-e,

```text
r = 6
dim X = 2
2(r+2 dim X+1) = 22
```

so balancing the proof terms gives the admissible supremum `1/46`.  Because Huang's proof retains arbitrary epsilon losses, e11 states every `eta<1/46`, not the endpoint.

The paper itself does not state `1/46`; that is a Stage14-specific substitution into the displayed proof bounds.

Primary link:

`https://arxiv.org/abs/2111.01509`

## 2. Iwaniec--Kowalski — multiplicative/Selberg sieve input

Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory*, AMS Colloquium Publications 53, 2004.

Classification:

```text
REUSABLE_METHOD
```

Huang explicitly cites this source for the Selberg sieve theorem and for the multiplicative-function asymptotic used to evaluate `G(N)`.  E11 does not import a new independent sieve framework; it instantiates Huang's own cited machinery with the e10 weight

\[
w_p=\frac{\delta_p}{1-\delta_p}=\frac2p+O(p^{-2}),
\]

which has sieve dimension two.

## 3. Relation to classical effective Hilbert irreducibility

Huang explains Theorem 1.6(1) as an effective Hilbert irreducibility statement for type-II thin sets over a toric base.  The proof invokes the standard fact that a generically finite cover of degree greater than one misses a fixed positive proportion of residue classes on a positive-density set of primes.

Classification:

```text
REUSABLE_METHOD
```

E11 does not claim a new general Hilbert-irreducibility theorem.  Its only use is to read the already-proved toric estimate quantitatively for the fixed Stage14 Euler-brick K3 cover.

## 4. Stage14-specific toric blocker identification

The new repository-local calculation is that the e10 state `G`

\[
|v_p(q_1)|=|v_p(q_2)|>0
\]

is exactly specialization along one of the four exceptional fan rays

```text
(1,1), (1,-1), (-1,1), (-1,-1)
```

of `Bl_4(P1 x P1)`.  The leading unit ratio used by the e10 nonsquare blocker is a residue coordinate on the corresponding exceptional divisor.  Hence the blocker is detected modulo `p` on the canonical toric integral model and Huang's uniform sieve condition holds with `n0=1` outside a fixed finite bad-prime set.

The current literature search did not locate this exact Stage14 physical-coordinate formulation.

```text
DIRECT_STAGE14_E11_EXCEPTIONAL_RAY_BLOCKER=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
```

## 5. Explicit exponent collision search

The current search did not locate a source stating the Stage14-specific value

\[
\eta<\frac1{46}
\]

for this Euler-brick cover.  The value is obtained by substituting `r=6`, `dim X=2` into Huang's displayed proof and balancing its two errors.

```text
HUANG_GENERAL_LOG_SAVING=KNOWN_THEOREM
STAGE14_SUBSTITUTION_ETA_LT_1_OVER_46=NO_COLLISION_FOUND_IN_CURRENT_SEARCH
NOVELTY_BY_SEARCH_ABSENCE=false
```

## 6. Boundary

E11 does not claim:

- the endpoint `eta=1/46`;
- optimality of `1/46` among all methods;
- a power saving in `B` from Huang's thin-cover theorem;
- an Euler-brick `sqrt(B)` asymptotic;
- that the local blocker-only sieve matches the full degree-two cover sieve.

The two quantitative routes are kept separate:

```text
EXPLICIT_THIN_COVER_LOG_POWER=FOR_EVERY_ETA_LT_1_OVER_46
EXPLICIT_LOCAL_BLOCKER_GROWING_SIEVE=B_LOG5_OVER_LOGLOG2
ENDPOINT_1_OVER_46=false
SQRT_B_ASYMPTOTIC=false
NOVELTY_BY_SEARCH_ABSENCE=false
```
