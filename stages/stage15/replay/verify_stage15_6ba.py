from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6ba_ar012_false_trigger import audit_flags, cleared_rhs
f=audit_flags()
assert f['ar012_trigger'] is False
assert f['moving_denominator_T'] is True
assert cleared_rhs(5,2,7)==980
print('Stage15-6ba PASS')
