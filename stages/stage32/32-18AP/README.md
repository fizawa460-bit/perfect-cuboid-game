# Stage32-18AP — b16 lower-block replay scout

18AO found a tractable exact upper frontier for `p436/s5`: cut39 completed with 4,103 frontier states and cut31 completed with 1,492,567 states. 18AP tests whether those frontier states are actually useful resumable work units.

The scout preserves the frozen x1024 ownership boundary and the immutable exact source. It first applies the existing 18AO block-frontier patch. At the selected cut, instead of only counting a frontier state, the first N exact frontier states are replayed all the way through the lower coordinates with the ordinary exact DFS. The upper traversal then resumes and continues discovering frontier states.

This is deliberately a replay/consumption scout, not a numerical closure claim and not yet a meet-in-the-middle join. It measures how many lower subtrees can be completed under a fixed global node/wallclock budget and reports the exact lower-node cost of completed replay units. A resource exit while replaying a lower subtree is evidence against that cut/sample size, not wall completion.

Matrix: cut39 with replay limits 1/4/16/64, plus cut31 with replay limits 1/4. A cut has a structural replay signal if a run with at least 16 requested replay units completes all requested lower subtrees without a resource exit. Runtime is not used to select a winner.

Firewalls remain unchanged: no finer shard split, no D16 b16 numerical credit, no global aggregation credit, no theorem/receiver/controller credit.
