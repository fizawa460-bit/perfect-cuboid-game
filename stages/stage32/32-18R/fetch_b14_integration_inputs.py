#!/usr/bin/env python3
from __future__ import annotations
import argparse,hashlib,json,os,pathlib,subprocess,urllib.request,zipfile

BULK_EXCLUDED={0,15,63,64,173}
BULK_IDS=[i for i in range(256) if i not in BULK_EXCLUDED]
PILOT_IDS=[63,64,173]
HOT_IDS=[26,748]

def api_json(url:str, token:str):
    req=urllib.request.Request(url,headers={'Authorization':f'Bearer {token}','Accept':'application/vnd.github+json','X-GitHub-Api-Version':'2022-11-28','User-Agent':'stage32-18r'})
    with urllib.request.urlopen(req) as r: return json.loads(r.read())

def list_run_artifacts(repo:str,run:int,token:str):
    out=[]; page=1
    while True:
        d=api_json(f'https://api.github.com/repos/{repo}/actions/runs/{run}/artifacts?per_page=100&page={page}',token)
        xs=d.get('artifacts',[]); out.extend(xs)
        if len(xs)<100: break
        page+=1
    return {a['name']:a for a in out}

def download(repo:str,a:dict,token:str,dest:pathlib.Path,zips:pathlib.Path,inventory:list):
    aid=int(a['id']); z=zips/f'{aid}.zip'; zips.mkdir(parents=True,exist_ok=True); dest.mkdir(parents=True,exist_ok=True)
    subprocess.run(['curl','-L','--fail','--silent','--show-error','-H',f'Authorization: Bearer {token}','-H','X-GitHub-Api-Version: 2022-11-28','-o',str(z),f'https://api.github.com/repos/{repo}/actions/artifacts/{aid}/zip'],check=True)
    got=hashlib.sha256(z.read_bytes()).hexdigest(); digest=a.get('digest')
    if digest:
        want=digest.removeprefix('sha256:')
        if got!=want: raise RuntimeError(f'artifact ZIP digest mismatch {a["name"]}: {got}!={want}')
    with zipfile.ZipFile(z) as f: f.extractall(dest)
    inventory.append({'id':aid,'name':a['name'],'zip_sha256':got,'api_digest':digest,'size_in_bytes':a.get('size_in_bytes'),'expired':a.get('expired')})

def require_name(table,name):
    if name not in table: raise RuntimeError(f'missing artifact {name}')
    a=table[name]
    if a.get('expired'): raise RuntimeError(f'expired artifact {name}')
    return a

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--repo',required=True); ap.add_argument('--bulk-run-id',type=int,required=True); ap.add_argument('--pilot-run-id',type=int,required=True); ap.add_argument('--hot-run-id',type=int,required=True); ap.add_argument('--b12-artifact-id',type=int,required=True); ap.add_argument('--output',type=pathlib.Path,required=True)
    a=ap.parse_args(); token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if not token: raise RuntimeError('GH_TOKEN required')
    root=a.output; root.mkdir(parents=True,exist_ok=True); zips=root/'zips'; inventory=[]
    bulk=list_run_artifacts(a.repo,a.bulk_run_id,token); pilot=list_run_artifacts(a.repo,a.pilot_run_id,token); hot=list_run_artifacts(a.repo,a.hot_run_id,token)
    download(a.repo,require_name(bulk,'stage32-18p-b14-bulk251-prepared-g1'),token,root/'prepared',zips,inventory)
    for pid in BULK_IDS:
        download(a.repo,require_name(bulk,f'stage32-18p-b14-bulk-packet-{pid}-g1'),token,root/'bulk'/str(pid),zips,inventory)
    for pid in PILOT_IDS:
        download(a.repo,require_name(pilot,f'stage32-18o-b14-pilot-packet-{pid}-g1'),token,root/'pilot'/str(pid),zips,inventory)
    for primary in HOT_IDS:
        download(a.repo,require_name(hot,f'stage32-18s-b14-logical-primary-{primary}-of1024-g1'),token,root/'hot'/str(primary),zips,inventory)
    b12=api_json(f'https://api.github.com/repos/{a.repo}/actions/artifacts/{a.b12_artifact_id}',token)
    download(a.repo,b12,token,root/'b12',zips,inventory)
    (root/'artifact-inventory.json').write_text(json.dumps({'schema':'STAGE32_18R_B14_INPUT_ARTIFACT_INVENTORY_V2','repo':a.repo,'bulk_run_id':a.bulk_run_id,'pilot_run_id':a.pilot_run_id,'hot_run_id':a.hot_run_id,'hot_source':'Stage32-18S repaired logical parents','b12_artifact_id':a.b12_artifact_id,'artifacts':inventory},indent=2,sort_keys=True)+'\n')
    print(json.dumps({'bulk_packets':len(BULK_IDS),'pilot_packets':PILOT_IDS,'hot_primaries':HOT_IDS,'hot_source':'18S','artifact_count':len(inventory)},sort_keys=True))
if __name__=='__main__': main()
