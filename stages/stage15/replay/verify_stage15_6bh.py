from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bh_support_restatement import audit_flags
f=audit_flags()
assert f['fixed_s_fiber_subpolynomial']
assert f['support_equivalent_to_n2_up_to_bo1']
assert f['support_theorem_as_blackbox_circular']
print('Stage15-6bh PASS')
