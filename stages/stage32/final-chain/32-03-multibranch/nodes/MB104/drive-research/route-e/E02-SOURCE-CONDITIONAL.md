# MB104 — auxiliary squareclass in box coordinates

Batch: MB104-DRIVE-20261026-SQUARECLASS-03. Conditional algebraic adapter, independent audit pending, zero credit. Parent E OPEN; unramifiedness subroute PARKED.

## Inputs and source boundary
Historical intermediate-H quotient model, exact blob d2e3056137360a9e15ae7c820088d2977a5eb137, recovered from GitHub at commit 7c755ce70874a018cdcd6ab0791f96b5c2d784b7. This is historical evidence, not new mathematics. The current conditional hypotheses and definitions of SQUARECLASS-01/02 remain required, including the immersion/transversality and balanced passport hypotheses. No historical-source recovery alone audits those results.

Use factor 1=z, factor 2=w, and multipliers a=u1/u2, b=v1/v2, c=a/b. These multipliers must not be confused with the historical note's theta-coordinate letters a,b. H invariance makes a,b rational on E. Set U=u1*u2, V=v1*v2, qplus(r)=r^4+4, qminus(r)=r^4-4.

## Exact rational-function adapter
The historical model gives u2^2=qplus(r2)/4 and v2^2=qminus(r2)/4, hence

    a=4U/qplus(r2), b=4V/qminus(r2),
    c=(U/V)*qminus(r2)/qplus(r2).

On its displayed box chart, U/V=Z2/Z1 and r2^2=2(C+W3)/(W1+iW2). Put D=W1+iW2 and Q=C+W3. Then

    c=(Z2/Z1)*(Q^2-D^2)/(Q^2+D^2).

This is an identity of rational functions after pullback along the retained carrier normalization. It does not require the single displayed chart to contain every point. Z1,Z2 here are box coordinates, not normalization curve Z. The auxiliary cover is the normalization of w_aux^2=c; the coordinate w_aux is unrelated to factor coordinate w.

The expression is invariant under residual simultaneous sign (r1,r2)->(-r1,-r2), because U,V and r2^2 are invariant. It therefore descends as a rational function on B. Invariance of its defining function does NOT make its quadratic extension unramified, trivial, or equal to the residual G/H extension.

## Why the historical residual double cover does not supply the missing proof
The residual extension is k(X_H)=k(B)(r2), with r2^2 already a function on B. Along the e=2 lift j:E->X_H, its defining square is r2^2 with r2 in k(E); consequently its generic pullback quadratic algebra splits. No claim about every singular chart or conductor specialization follows. By SQUARECLASS-02, under the surviving coreless/no-clump hypotheses c has a positive branch divisor and its quadratic extension is connected. It therefore cannot be identified with that split generic residual algebra under these hypotheses. This rules out that proposed identification; it does not rule out the coreless object.

The older retained absent_eta_character_line record is common-G-cover building data in a different construction, not an available identification of this W. Historical residual eta, factor delta_fac, and absent eta require separate definitions and proved adapters.

## Precise residual and reopening condition
One needs the valuations of the displayed box rational function on the actual normalized carrier, including all points outside the chart, or a theorem forcing their parity. The ambient quotient formula and line-bundle equivalences do not provide those valuations. No actual carrier parametrization/conductor-preimage specialization was recovered in the inspected source. No exhaustive repository absence claim is made. Do not repeat the ambient formula, old passport, or eta-by-name argument as new progress. Reopen only with branch-specific data or an independent theorem controlling this divisor; parent E remains OPEN.

## Verification limits
The companion standard-library verifier checks the exact Laurent-monomial identities for a,b,c, the factor-of-four cancellation in the box substitution, and invariance under simultaneous sign. It locks the historical blob bytes. It does not verify global divisor parity, construct a carrier, independently audit geometric inputs, or establish closure. No heavy computation or GitHub writes.
