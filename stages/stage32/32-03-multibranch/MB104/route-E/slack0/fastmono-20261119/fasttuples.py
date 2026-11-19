"""Same loops as monodromy.tuples, sampled more coarsely (m points per radial segment instead of 60).
monodromy._step already subdivides a step whenever nearest-root matching is ambiguous, so the coarse path gives
the same permutations; check_fast() compares against the original on stored covers."""
import numpy as np
import monodromy as md
def tuples(p, q, m=12):
    old = md.loop_path
    md.loop_path = lambda v, m_=m: old(v, m_)
    try: return md.tuples(p, q)
    finally: md.loop_path = old
