import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bn_huang_audit import audit_flags
f=audit_flags(); assert f['species_match'] and f['effective_fixed_neighbourhood'] and not f['q_B14_window_certified'] and not f['promotion']
print('Stage15-6bn PASS')
