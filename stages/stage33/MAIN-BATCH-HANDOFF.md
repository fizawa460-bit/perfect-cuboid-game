# Stage33 MAIN — latest batch handoff

This file is the **mandatory ordinary-MAIN continuation note**.
It is intentionally small and disposable: overwrite it after every MAIN batch that learns anything useful, even when the detailed mathematical state is not promoted.

It is not a proof certificate and does not override `MAIN-STATE.json`, the detailed controller, or exact certificates. Its job is to prevent the next agent from repeating already-completed narrowing work.

## Base branch state

- branch: `stage33-12-j2-ptsK-qPicK-continuation`
- branch head at the start of the narrowing batch: `823d940a69552e60dd162995260ce22e87099df2`
- no new PR, merge, or downstream release
- no mathematical state promotion was made during the narrowing-only follow-up batches described below

## Already fixed before this narrowing

- named J2 retained10 source:
  `[0,1,1,0,0,0,0,0,0,0]`
- locked J2 75D target is materialized.
- exact relation already fixed:
  `C2 + C3 = h_J2`
- named source-target relation rank is `1`.
- standard 75D columns individually materialized remain `0/10`.

Do not reinterpret the J2 relation as one standard column.

## Latest narrowing result: companion beta2

The Picard-adjoint certificate already contains an exact companion `beta2` source.
Its retained10 coordinate is:

`[0,1,1,0,0,1,1,1,0,1]`

This is linearly independent from the J2 retained10 source

`[0,1,1,0,0,0,0,0,0,0]`.

Therefore an **exact 75D finite-V4 H1/Kummer image for companion beta2** would immediately provide a second independent source-target relation and should raise relation rank `1 -> 2`.

### What is still missing

The companion beta2 75D target is **not yet materialized**.
Do not guess it from the retained10 coordinate or from semantic `u2` alone.

The existing `full-surface-pic2-kummer-target.json` contains the 75D quotient-basis infrastructure, but the generic Kummer extension class is explicitly missing. It therefore does not currently expose a linear map that can simply be applied to beta2 to manufacture its 75D image.

The exact current leaf is:

> materialize `companion beta2 / semantic u2 -> finite-V4 75D H1 target`, verify it, then add the independent source-target relation and require rank increase.

## Semantic u2 information already known

Do not redo the Picard-adjoint/source-coordinate calculation merely to rediscover this.
The current compact state records semantic discriminant pullback data and the J2 adjoint certificate records the companion beta2 source.

The important distinction is:

- source-side beta2 coordinate: already exact;
- 75D H1/Kummer image of beta2: still missing.

## Route checked and rejected for the next relation

`q1` was checked as a possible next named class.
Existing exact work shows that `q1` does **not** Q-descent, so it is not a valid replacement for the requested next Q-defined proper-Br2 source in the current leaf.

Also, the old q1 producer scripts depend on old generated JSON that is not tracked on the current branch. Do not spend an ordinary compact MAIN batch reconstructing old Stage33-05 state just to retry q1 unless a new exact reason explicitly reopens that route.

## Anti-repeat instructions for the next MAIN agent

Do **not** repeat these investigations in an ordinary MAIN batch:

1. Do not search broadly for another named class before attempting the already-independent companion beta2.
2. Do not redo J2 source orientation or Picard adjoint placement.
3. Do not treat `q1` as Q-defined.
4. Do not infer a beta2 75D image from `u2`, retained10 coordinates, or the quotient basis without an exact Kummer/H1 adapter.
5. Do not count `C2+C3=h_J2` as an individually materialized standard column.

## Immediate next action

Stay narrow. Locate or construct the smallest exact producer/adapter for

`companion beta2 / semantic u2 -> 75D finite-V4 H1 target`.

If it succeeds, certify the new source-target relation and verify that the source-relation rank increases from 1 to 2 before syncing controller/MAIN-STATE.
If it fails, record the exact blocker in this handoff before ending the batch so the next agent does not retry the same failed route.
