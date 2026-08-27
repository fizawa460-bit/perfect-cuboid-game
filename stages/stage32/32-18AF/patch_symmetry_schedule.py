import os
from pathlib import Path
p=Path(os.environ['SRC'])
s=p.read_text()
old='if(reach==0 || -center>1.25L*reach){'
new='if(reach==0 || -center>1.0L*reach){'
assert s.count(old)==1, s.count(old)
s=s.replace(old,new)
assert old not in s and s.count(new)==1
p.write_text(s)
