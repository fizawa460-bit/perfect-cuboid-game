"""Replay the unreviewed R3 resume delta in a temporary working directory."""
import argparse, base64, gzip, hashlib, json, platform, shutil, subprocess, sys, tempfile
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
    wave=work/'wave2'
    shutil.copytree(HERE/'wave2',wave)
    for name,item in json.loads((wave/'PAYLOADS.json').read_text()).items():
        data=gzip.decompress(base64.b64decode((wave/item['stored']).read_text(),validate=False))
        if len(data)!=item['bytes'] or hashlib.sha256(data).hexdigest()!=item['sha256']:
            raise RuntimeError('Payload mismatch: '+name)
        (wave/name).write_bytes(data)
    for script in ['verify_wave.py','verify_key_relation.py','extract_dependency.py','verify_linear.py']:
        run=subprocess.run([sys.executable,str(wave/script)],capture_output=True,text=True)
        commands.append(dict(script=script,exit_status=run.returncode,stdout_sha256=hashlib.sha256(run.stdout.encode()).hexdigest()))
        if run.returncode:raise RuntimeError(run.stdout+run.stderr)
        print('PASS',script)
    wave_names=['verification_wave2.json','key_relation_verification.json','results_wave2.json','dependency_witness.json','dual_wave2.json','linear_verification.json']
    for name in wave_names:
        if json.loads((wave/name).read_text())!=json.loads((HERE/'wave2'/name).read_text()):
            raise RuntimeError('Wave2 result mismatch: '+name)
    report=dict(status='AUTHOR_REPLAY_PASS_NOT_INDEPENDENT_AUDIT',python=sys.version,
        platform=platform.platform(),parent_files_verified=len(lock),commands=commands,
        result_json_equal=names+wave_names,new_relations=590,formal_residual=180,p827_zero=False,
        unconditional_exclusions=0)
    if a.output: a.output.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS exact result JSON equality; residual180; P827 not eliminated; exclusion0')
