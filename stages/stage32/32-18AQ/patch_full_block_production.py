import os
from pathlib import Path

p=Path(os.environ['SRC'])
s=p.read_text()

old='''        f<<"  \\\"status\\\": \\\"FRONTIER_COMPLETE\\\",\\n";
'''
new='''        const bool full_block_complete = (replay_started_==frontier_states_ && replay_completed_==frontier_states_ && replay_limit_>=frontier_states_);\n        f<<"  \\\"status\\\": \\\""<<(full_block_complete?"COMPLETE":"PARTIAL_REPLAY")<<"\\\",\\n";\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

old='''        f<<"  \\\"LOWER_BLOCK_ENUMERATED\\\": false,\\n";
'''
new='''        f<<"  \\\"LOWER_BLOCK_ENUMERATED\\\": "<<(full_block_complete?"true":"false")<<",\\n";\n'''
assert s.count(old)==1
s=s.replace(old,new,1)

p.write_text(s)
