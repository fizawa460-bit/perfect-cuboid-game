import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bm_toric_congruence import audit_flags
f=audit_flags(); assert f['split_toric'] and f['fixed_q_density_exponent']==-2 and not f['moving_q_uniformity']
print('Stage15-6bm PASS')
