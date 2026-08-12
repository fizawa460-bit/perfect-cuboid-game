import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from stages.stage15.scripts.stage15_6bl_joint_rootline import joint_index,roots_ok
assert joint_index(35)==1225
assert roots_ok(2,1,5,1)
assert roots_ok(1,4,1,17)
print('Stage15-6bl PASS')
