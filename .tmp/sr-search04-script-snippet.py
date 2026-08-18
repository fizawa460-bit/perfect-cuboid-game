from pathlib import Path
s=Path('scripts/structure_radar.py').read_text().splitlines()
keys=['chunks(searchable','recommended_source_tasks_per_main_invocation','initial_execution_estimate','estimated_main_invocations']
out=[]
for i,line in enumerate(s,1):
    if any(k in line for k in keys):
        a=max(1,i-8); b=min(len(s),i+12)
        out.append(f'### around line {i}\n'+''.join(f'{j}: {s[j-1]}\n' for j in range(a,b+1)))
Path('.tmp/sr-search04-script-snippet.txt').write_text('\n'.join(out))
