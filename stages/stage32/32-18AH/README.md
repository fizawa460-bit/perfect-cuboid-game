# Stage32-18AH — pairwise exact symmetry propagation

18AF reduced the frozen b16 x1024 wall set from 12 to 6 by moving the exact symmetry scheduler from 1.25 to 1.0. 18AG then changed only the lower-48 DFS coordinate order and closed none of the six remaining walls: all six again reached the 18,000,000-node cap. Search order is therefore rejected as the next lever.

18AH strengthens branch propagation itself. The existing certifier tests each symmetry breaker separately with an exact rational Cauchy–Schwarz bound. That can miss a branch where each breaker is individually reachable but two violated breakers cannot be repaired simultaneously within the remaining norm budget.

For a scheduled pair of violated breaker rows r,s, let d=(-center_r,-center_s)>0 and let G be the exact 2x2 Gram matrix of their remaining linear forms in the D^{-1} metric. When det(G)>0 and the exact KKT multipliers G^{-1}d are both positive, the minimum remaining norm energy needed to satisfy both inequalities is d^T G^{-1}d. If that exact rational quantity exceeds the remaining budget, the branch is impossible and is rejected.

Floating arithmetic is used only to select a small deterministic set of severe violated breakers for pair testing. Every rejection is based on the exact rational 2x2 Gram/KKT certificate. The original single-row exact checks remain enabled. The x1024 partition, split coordinates, symmetry scheduler 1.0, and 18M node cap are unchanged.

Only the six frozen walls are rerun: p436/s5, p436/s362, p503/s118, p503/s665, p922/s13, p922/s38. No x2048 is authorized. All numerical/global/theorem/receiver/controller firewalls remain false.