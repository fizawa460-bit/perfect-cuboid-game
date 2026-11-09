"""Replay the unreviewed R3 resume delta in a temporary working directory."""
import argparse, hashlib, json, platform, shutil, subprocess, sys, tempfile
from pathlib import Path
HERE=Path(__file__).resolve().parent
if not __debug__: raise RuntimeError('Python -O is unsupported')
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--parent',type=Path,help='Already restored row393 package')
p.add_argument('--output',type=Path,help='Write replay result outside the source tree')
a=p.parse_args()
with tempfile.TemporaryDirectory(prefix='r3-resume-') as tmp:
    work=Path(tmp); parent=work/'row393'
    if a.parent:
        shutil.copytree(a.parent,parent)
    else:
        restore=HERE.parents[1]/'materials/classgroup-and-different/restore_package.py'
        subprocess.run([sys.executable,str(restore),'--row','393','--destination',str(parent)],check=True)
    lock=json.loads((HERE/'PARENT-SHA256.json').read_text())
    for name,expected in lock.items():
        if hashlib.sha256((parent/name).read_bytes()).hexdigest()!=expected:
            raise RuntimeError('Parent source mismatch: '+name)
    shutil.copytree(HERE/'new394',work/'new394')
    commands=[]
    for script in ['verify_returned_candidate.py','verify_new_relation.py','dual_obstruction.py']:
        run=subprocess.run([sys.executable,str(work/'new394'/script)],capture_output=True,text=True)
        commands.append(dict(script=script,exit_status=run.returncode,
            stdout_sha256=hashlib.sha256(run.stdout.encode()).hexdigest()))
        if run.returncode: raise RuntimeError(run.stdout+run.stderr)
        print('PASS',script)
    names=['results_candidate394.json','new_relation_verification.json','dual_obstruction.json']
    for name in names:
        if json.loads((work/'new394'/name).read_text())!=json.loads((HERE/'new394'/name).read_text()):
            raise RuntimeError('Result mismatch: '+name)
    report=dict(status='AUTHOR_REPLAY_PASS_NOT_INDEPENDENT_AUDIT',python=sys.version,
        platform=platform.platform(),parent_files_verified=len(lock),commands=commands,
        result_json_equal=names,new_relations=1,formal_residual=181,p827_zero=False,
        unconditional_exclusions=0)
    if a.output: a.output.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS exact result JSON equality; residual181; P827 not eliminated; exclusion0')
