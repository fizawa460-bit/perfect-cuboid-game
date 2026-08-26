#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, shutil, subprocess, time, urllib.error, urllib.request, zipfile

EXCLUDED={0,15,63,64,173}
BULK_IDS=[i for i in range(256) if i not in EXCLUDED]
PILOT_IDS=[63,64,173]
HOT_IDS=[26,748]
SNAPSHOT_NAME='stage32-18t-b14-source-snapshot-g2'
RESUME_SUMMARY_NAME='stage32-18t-b14-resume-summary-g2'
PREPARED_NAME='stage32-18p-b14-bulk251-prepared-g1'


def api_json(url:str, token:str):
    last=None
    for attempt in range(6):
        req=urllib.request.Request(url,headers={
            'Authorization':f'Bearer {token}',
            'Accept':'application/vnd.github+json',
            'X-GitHub-Api-Version':'2022-11-28',
            'User-Agent':'stage32-18r',
        })
        try:
            with urllib.request.urlopen(req,timeout=60) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            last=e
            if e.code not in {429,500,502,503,504} or attempt==5: raise
        except urllib.error.URLError as e:
            last=e
            if attempt==5: raise
        time.sleep(2**attempt)
    raise last


def list_run_artifacts(repo:str,run:int,token:str):
    out=[]; page=1
    while True:
        d=api_json(f'https://api.github.com/repos/{repo}/actions/runs/{run}/artifacts?per_page=100&page={page}',token)
        xs=d.get('artifacts',[]); out.extend(xs)
        if len(xs)<100: break
        page+=1
    table={}
    for a in out: table.setdefault(a['name'],[]).append(a)
    return table


def latest_artifact(table,name):
    xs=[a for a in table.get(name,[]) if not a.get('expired')]
    if not xs: raise RuntimeError(f'no live artifact {name}')
    return max(xs,key=lambda a:int(a['id']))


def artifact_by_id(repo:str,aid:int,token:str):
    a=api_json(f'https://api.github.com/repos/{repo}/actions/artifacts/{aid}',token)
    if a.get('expired'): raise RuntimeError(f'expired artifact id {aid}')
    return a


def download(repo:str,a:dict,token:str,dest:pathlib.Path,zips:pathlib.Path,inventory:list,expected_zip_sha:str|None=None,expected_run:int|None=None,kind:str='artifact'):
    aid=int(a['id'])
    if expected_run is not None and int(a.get('workflow_run',{}).get('id',-1))!=expected_run:
        raise RuntimeError(f'artifact {aid} run mismatch')
    z=zips/f'{aid}.zip'; zips.mkdir(parents=True,exist_ok=True); dest.mkdir(parents=True,exist_ok=True)
    subprocess.run([
        'curl','-L','--fail','--silent','--show-error','--retry','6','--retry-all-errors','--retry-delay','2',
        '-H',f'Authorization: Bearer {token}','-H','X-GitHub-Api-Version: 2022-11-28',
        '-o',str(z),f'https://api.github.com/repos/{repo}/actions/artifacts/{aid}/zip'
    ],check=True)
    got=hashlib.sha256(z.read_bytes()).hexdigest(); digest=a.get('digest')
    if digest and got!=digest.removeprefix('sha256:'):
        raise RuntimeError(f'artifact ZIP digest mismatch {a["name"]}')
    if expected_zip_sha is not None and got!=expected_zip_sha:
        raise RuntimeError(f'locked ZIP SHA mismatch {a["name"]}: {got}')
    with zipfile.ZipFile(z) as f: f.extractall(dest)
    inventory.append({'kind':kind,'id':aid,'name':a['name'],'zip_sha256':got,'api_digest':digest,
        'size_in_bytes':a.get('size_in_bytes'),'expired':a.get('expired'),
        'workflow_run_id':a.get('workflow_run',{}).get('id')})
    return got


def copy_embedded_packet(snapshot_root:pathlib.Path,pid:int,dest:pathlib.Path):
    src=snapshot_root/'carryover'/'packets'/str(pid)
    if not src.exists(): raise RuntimeError(f'missing embedded carry packet {pid}')
    if dest.exists(): shutil.rmtree(dest)
    shutil.copytree(src,dest)
    if not (dest/'packet-certificate.json').exists() or not (dest/'packet-canonical.bin').exists():
        raise RuntimeError(f'embedded carry packet files incomplete {pid}')


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',required=True); ap.add_argument('--legacy-run-id',type=int,required=True); ap.add_argument('--resume-run-id',type=int,required=True)
    ap.add_argument('--snapshot-artifact-id',type=int,required=True); ap.add_argument('--snapshot-artifact-zip-sha256',required=True)
    ap.add_argument('--prepared-artifact-id',type=int,required=True); ap.add_argument('--prepared-artifact-zip-sha256',required=True)
    ap.add_argument('--pilot-run-id',type=int,required=True); ap.add_argument('--hot-run-id',type=int,required=True)
    ap.add_argument('--hot26-artifact-id',type=int,required=True); ap.add_argument('--hot26-artifact-zip-sha256',required=True)
    ap.add_argument('--hot748-artifact-id',type=int,required=True); ap.add_argument('--hot748-artifact-zip-sha256',required=True)
    ap.add_argument('--b12-artifact-id',type=int,required=True); ap.add_argument('--b12-artifact-zip-sha256',required=True)
    ap.add_argument('--output',type=pathlib.Path,required=True)
    a=ap.parse_args(); token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if not token: raise RuntimeError('GH_TOKEN required')
    root=a.output; root.mkdir(parents=True,exist_ok=True); zips=root/'zips'; inventory=[]

    resume_table=list_run_artifacts(a.repo,a.resume_run_id,token); pilot_table=list_run_artifacts(a.repo,a.pilot_run_id,token)
    snap_art=artifact_by_id(a.repo,a.snapshot_artifact_id,token)
    if snap_art['name']!=SNAPSHOT_NAME: raise RuntimeError('snapshot artifact name mismatch')
    snapshot_root=root/'control'/'snapshot'
    download(a.repo,snap_art,token,snapshot_root,zips,inventory,a.snapshot_artifact_zip_sha256,a.resume_run_id,'union_snapshot')
    summary_art=latest_artifact(resume_table,RESUME_SUMMARY_NAME)
    download(a.repo,summary_art,token,root/'control'/'resume',zips,inventory,expected_run=a.resume_run_id,kind='union_summary')

    snap=json.loads((snapshot_root/'source-completion.json').read_text())
    summary=json.loads((root/'control'/'resume'/'resume-summary.json').read_text())
    if snap.get('schema')!='STAGE32_18T_B14_RESUME_UNION_SNAPSHOT_V2': raise RuntimeError('bad union snapshot schema')
    if summary.get('schema')!='STAGE32_18T_B14_OPTIMIZED_RESUME_SUMMARY_V2': raise RuntimeError('bad union summary schema')
    if int(snap.get('source_run_id',-1))!=a.legacy_run_id or int(summary.get('source_run_id',-1))!=a.legacy_run_id:
        raise RuntimeError('legacy source run mismatch')

    source_ids=sorted(int(x) for x in snap['source_complete_ids'])
    source_missing=sorted(int(x) for x in snap['source_missing_bulk_ids'])
    carry_ids=sorted(int(x) for x in snap['carry_complete_packet_ids'])
    remaining_ids=sorted(int(x) for x in snap['missing_bulk_ids'])
    if sorted(source_ids+source_missing)!=BULK_IDS or set(source_ids)&set(source_missing):
        raise RuntimeError('source snapshot is not exact BULK_IDS partition')
    if not set(carry_ids)<=set(source_missing): raise RuntimeError('carry packet outside source complement')
    if remaining_ids!=sorted(set(source_missing)-set(carry_ids)):
        raise RuntimeError('remaining set differs from source complement minus carry')
    if [int(x) for x in summary.get('source_complete_ids',[])]!=source_ids: raise RuntimeError('summary source set differs from snapshot')
    if [int(x) for x in summary.get('carry_complete_packet_ids',[])]!=carry_ids: raise RuntimeError('summary carry set differs from snapshot')
    if [int(x) for x in summary.get('resume_expected_ids',[])]!=source_missing: raise RuntimeError('summary expected complement differs from snapshot')
    if [int(x) for x in summary.get('resume_complete_ids',[])]!=source_missing: raise RuntimeError('18T union complement is not complete')
    if summary.get('resume_missing_ids')!=[] or summary.get('resume_extra_ids')!=[] or summary.get('ready_for_18r') is not True:
        raise RuntimeError('18T union not ready for 18R')

    prepared=artifact_by_id(a.repo,a.prepared_artifact_id,token)
    if prepared['name']!=PREPARED_NAME: raise RuntimeError('prepared artifact name mismatch')
    download(a.repo,prepared,token,root/'prepared',zips,inventory,a.prepared_artifact_zip_sha256,a.legacy_run_id,'prepared')

    complete_meta={int(x['packet_id']):x for x in snap.get('complete_artifacts',[])}
    if set(complete_meta)!=set(source_ids): raise RuntimeError('snapshot source artifact ledger mismatch')
    carry_meta={int(x['packet_id']):x for x in snap.get('carry_packet_artifacts',[])}
    if set(carry_meta)!=set(carry_ids): raise RuntimeError('snapshot carry artifact ledger mismatch')

    bulk_sources={}
    for pid in source_ids:
        meta=complete_meta[pid]; art=artifact_by_id(a.repo,int(meta['artifact_id']),token)
        if art['name']!=meta['artifact_name'] or art.get('digest')!=meta.get('artifact_digest'):
            raise RuntimeError(f'legacy artifact metadata changed packet {pid}')
        download(a.repo,art,token,root/'bulk'/str(pid),zips,inventory,expected_run=a.legacy_run_id,kind='18P_source_packet')
        bulk_sources[str(pid)]='18P_frozen_snapshot'

    for pid in carry_ids:
        copy_embedded_packet(snapshot_root,pid,root/'bulk'/str(pid))
        m=carry_meta[pid]
        inventory.append({'kind':'18T_prior_success_embedded_in_union_snapshot','packet_id':pid,
            'source_run_id':m.get('run_id'),'source_job_id':m.get('job_id'),'source_job_name':m.get('job_name'),
            'source_artifact_id':m.get('artifact_id'),'source_artifact_name':m.get('artifact_name'),
            'source_artifact_digest':m.get('artifact_digest'),'container_snapshot_artifact_id':a.snapshot_artifact_id})
        bulk_sources[str(pid)]='18T_prior_success_carryover'

    for pid in remaining_ids:
        art=latest_artifact(resume_table,f'stage32-18t-b14-packet-{pid}-g2')
        download(a.repo,art,token,root/'bulk'/str(pid),zips,inventory,expected_run=a.resume_run_id,kind='18T_current_packet')
        bulk_sources[str(pid)]='18T_union_resume_current'

    for pid in PILOT_IDS:
        download(a.repo,latest_artifact(pilot_table,f'stage32-18o-b14-pilot-packet-{pid}-g1'),token,root/'pilot'/str(pid),zips,inventory,expected_run=a.pilot_run_id,kind='18O_pilot')
    hot_locks={26:(a.hot26_artifact_id,a.hot26_artifact_zip_sha256),748:(a.hot748_artifact_id,a.hot748_artifact_zip_sha256)}
    for primary in HOT_IDS:
        aid,want=hot_locks[primary]; art=artifact_by_id(a.repo,aid,token)
        if art['name']!=f'stage32-18s-b14-logical-primary-{primary}-of1024-g1': raise RuntimeError(f'hot artifact name mismatch {primary}')
        download(a.repo,art,token,root/'hot'/str(primary),zips,inventory,want,a.hot_run_id,'18S_hostile_audited_hot')
    b12=artifact_by_id(a.repo,a.b12_artifact_id,token)
    download(a.repo,b12,token,root/'b12',zips,inventory,a.b12_artifact_zip_sha256,kind='hostile_audited_b12')

    source_n=len(source_ids); carry_n=len(carry_ids); current_n=len(remaining_ids); resume_n=len(source_missing)
    if source_n+resume_n!=len(BULK_IDS) or carry_n+current_n!=resume_n or len(bulk_sources)!=len(BULK_IDS):
        raise RuntimeError('union handoff count invariant failed')
    out={'schema':'STAGE32_18R_B14_INPUT_ARTIFACT_INVENTORY_V4','repo':a.repo,
        'legacy_run_id':a.legacy_run_id,'resume_run_id':a.resume_run_id,
        'snapshot_artifact_id':a.snapshot_artifact_id,'resume_summary_artifact_id':int(summary_art['id']),
        'prepared_artifact_id':a.prepared_artifact_id,'pilot_run_id':a.pilot_run_id,'hot_run_id':a.hot_run_id,
        'hot_artifact_ids':{'26':a.hot26_artifact_id,'748':a.hot748_artifact_id},
        'hot_source':'Stage32-18S hostile-audited repaired logical parents','b12_artifact_id':a.b12_artifact_id,
        'legacy_source_complete_ids':source_ids,'resume_complement_ids':source_missing,
        'carryover_packet_ids':carry_ids,'current_resume_packet_ids':remaining_ids,
        'bulk_packet_sources':bulk_sources,'artifacts':inventory,'handoff_exact':True,
        'legacy_packet_count':source_n,'resume_complement_packet_count':resume_n,
        'carryover_packet_count':carry_n,'current_resume_packet_count':current_n,
        'D16_B14_NUMERICAL_CREDIT':False,'GLOBAL_B14_AGGREGATION_COMPLETE':False,'AUDIT_STATUS':'PENDING'}
    (root/'artifact-inventory.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'legacy_packets':source_n,'resume_complement':resume_n,'carryover_packets':carry_n,
        'current_resume_packets':current_n,'pilot_packets':PILOT_IDS,'hot_primaries':HOT_IDS,
        'artifact_count':len(inventory),'handoff_exact':True},sort_keys=True))

if __name__=='__main__': main()
