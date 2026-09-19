# MB104 Z33 compact restart handoff — 2026-09-19

Status: **AUDITED-PREDECESSOR HANDOFF / ACTIVE RESEARCH / NO CREDIT**

## Split purpose

PR #1819 reached a hostile-audited exact head after substantial retained growth. This restart intentionally does not copy that research surface.

Predecessor:

```
PR = #1819
branch = stage32mb-uniform-closure-20260917
audited exact head = b28adadc95776762754e1415a0ecab0da1d4cd8e
hostile audit review = 5254494158
hostile audit = PASS
```

Compact restart base:

```
main = 83ae3f66cfcbdfaaaebf149bea078d1b0ff11c49
```

Older immutable historical MB104 archive:

```
archive head = ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

## Retained mathematical frontier

The audited predecessor boundary retains, with zero downstream credit:

1. coverage repair: nodewise-unibranch complement of MB101 is finite-side via the historical branchwise FSM pole inequality;
2. BTVA: any unbounded geometric-genus 0/1 family must meet at least 14 box nodes;
3. Z31/Z32: N=14 is the first BTVA-uncontrolled support and fixed finite jet/hyperplane-power tricks do not repair the cubic deficit;
4. Z33: in the potentially unbounded genus-one span-five sector,
   ```
   M<=d,
   M>=d,
   O>=d,
   O<=R<=M
   ```
   hence
   ```
   M=R=O=d,
   ```
   every normalization branch over a box node has exceptional contact `m=1`, and
   ```
   div(nu^*h)=B_node
   ```
   is the reduced divisor of all node-preimages.

For genus zero, the hyperplane-supported MB sector is incompatible with the retained `M>=d+4` lower bound.

## Active source locks on audited predecessor

At exact head `b28adadc95776762754e1415a0ecab0da1d4cd8e`:

- `MB104-Z33-SPAN5-HYPERPLANE-CONTACT-EQUALITY-20260919.md`
  blob `65656518d30f69ab3a4a892c8d4ae1d5ed72670e`;
- `verify_mb104_z33_span5_hyperplane_contact.py`
  blob `7ba0b4eb4fffda7fe1b88b958d952276c8af271b`;
- predecessor MB `STATE.json`
  blob `7fa7b24fc8e28727ff2c63d893128b9cf2099ba5`.

## Archived span-five geometry to consume next

At exact archive head `ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11`:

- finite hyperplane reduction note:
  `08eee3d3492db710c7161fdf17ce1eca35e50413`;
- finite hyperplane reduction certificate:
  `b6035b2e525a08ab0fc028e1e1f81519548e1a5b`;
- 12-orbit classification note:
  `c3bcc580b5bd43b7805c7227c7420445f14c4b8c`;
- 12-orbit classification certificate:
  `3bc4453affce96e87a60864c99f745bb4c28c794`.

Retained archive facts:

```
1,655 node-spanned P5 hyperplanes with incidence >=14
12 Aut(S) hyperplane orbits
incidence 24 = two orbits, sizes 4 and 24
every incidence-24 hyperplane section = union of eight smooth conics
each of its 24 box nodes lies on exactly two section conics
```

These facts must be consumed through an explicit archive-root/exact-head adapter.

## Active leaf

`MB104-Z33-SPAN5-HYPERPLANE-ORBIT-SIMPLE-CONTACT`

First target: the two incidence-24 orbits.

At each supported node, determine exactly how the support hyperplane and eight-conic section geometry constrain the two fixed non-diagonal A1 landing directions under the Z33 equality package.

Legal success shapes:

- orbitwise elimination of one/both non-diagonal landing bins;
- a stronger collision lower bound feeding Z14;
- an irreducibility/component obstruction valid for arbitrary unequal `M_i=r_i` with `sum M_i=d`;
- an exact feasible packet that proves incidence-24 survives and permits moving to incidence 20/19/16/15/14.

Do not infer contradiction from finitely many forbidden free `lambda` values alone, do not assume arbitrary local choices globalize, and do not reopen bare etale-correspondence finiteness.

## Credit firewall

```
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
