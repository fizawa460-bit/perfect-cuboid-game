from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6az_small_height_size_audit import audit_flags

f=audit_flags()
assert f['petit_whole_family_adapter'] is False
assert f['product_height_controls_individual_descent_height'] is False
assert f['complete_2descent_retained'] is True
print('Stage15-6az PASS')
