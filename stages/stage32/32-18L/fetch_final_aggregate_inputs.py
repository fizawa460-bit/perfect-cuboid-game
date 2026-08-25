#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, re, urllib.error, urllib.request, zipfile

API = "https://api.github.com"
LOGICAL26_ARTIFACT_NAME = "stage32-18k-b12-logical-26-of1024-g2"
LOGICAL26_ARTIFACT_ZIP_SHA256 = "066e6aa2468671bd3733f17e0ef47b6cb2e22d9ad900f17d6b7fed1b011570f4"

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

def get_json(url: str, token: str):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "stage32-18l-fetcher",
    })
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

def get_bytes(url: str, token: str) -> bytes:
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "stage32-18l-fetcher",
    })
    opener = urllib.request.build_opener(_NoRedirect())
    try:
        with opener.open(req, timeout=60) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        if e.code not in (301, 302, 303, 307, 308):
            raise
        location = e.headers.get("Location")
        if not location:
            raise RuntimeError(f"artifact redirect {e.code} missing Location")
    blob_req = urllib.request.Request(location, headers={"User-Agent": "stage32-18l-fetcher"})
    with urllib.request.urlopen(blob_req, timeout=120) as r:
        return r.read()

def list_artifacts(repo: str, run_id: int, token: str):
    out = []
    page = 1
    while True:
        data = get_json(f"{API}/repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100&page={page}", token)
        batch = data.get("artifacts", [])
        out.extend(batch)
        if len(batch) < 100:
            return out
        page += 1

def extract_flat(artifact: dict, dest: pathlib.Path, token: str, inventory: list):
    if artifact.get("expired"):
        raise RuntimeError(f"expired artifact {artifact['name']}")
    raw = get_bytes(artifact["archive_download_url"], token)
    got = hashlib.sha256(raw).hexdigest()
    declared = artifact.get("digest")
    if declared and got != declared.removeprefix("sha256:"):
        raise RuntimeError(f"ZIP digest mismatch {artifact['name']}: {got} != {declared}")
    tmp = dest.parent / f"extract-{artifact['id']}"
    tmp.mkdir(parents=True, exist_ok=True)
    zp = dest.parent / f"artifact-{artifact['id']}.zip"
    zp.write_bytes(raw)
    with zipfile.ZipFile(zp) as z:
        z.extractall(tmp)
    dest.mkdir(parents=True, exist_ok=True)
    for p in tmp.iterdir():
        if p.is_file():
            q = dest / p.name
            if q.exists():
                raise RuntimeError(f"filename collision {q}")
            p.replace(q)
    inventory.append({
        "id": artifact["id"], "name": artifact["name"], "zip_sha256": got,
        "declared_digest": declared, "size_in_bytes": artifact.get("size_in_bytes"),
        "created_at": artifact.get("created_at"),
    })
    return got

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--ordinary-run-id", type=int, required=True)
    ap.add_argument("--rescue-run-id", type=int, required=True)
    ap.add_argument("--deep-run-id", type=int, required=True)
    ap.add_argument("--logical26-run-id", type=int, required=True)
    ap.add_argument("--prepared-artifact-id", type=int, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise RuntimeError("GH_TOKEN required")

    root = args.output
    ordinary = root / "ordinary"
    rescue = root / "rescue256"
    deep = root / "deep1024"
    logical = root / "logical26"
    prepared = root / "prepared"
    inventory = []

    arts = list_artifacts(args.repo, args.ordinary_run_id, token)
    pa = next((a for a in arts if int(a["id"]) == args.prepared_artifact_id), None)
    if pa is None or pa.get("name") != "stage32-18e-b12-prepared-g1":
        raise RuntimeError("immutable Stage32-18E prepared artifact missing")
    psha = extract_flat(pa, prepared, token, inventory)
    if psha != "0671a8a8637641f5cc4da36b99700b1511c923d03e5ea446317d17b35bd88fc4":
        raise RuntimeError("Stage32-18E prepared ZIP lock mismatch")

    pat = re.compile(r"^stage32-18e-b12-exact-shard-(\d+)-g1$")
    selected = {}
    for a in arts:
        m = pat.match(str(a.get("name", "")))
        if m:
            sid = int(m.group(1))
            if sid != 26:
                selected[sid] = a
    expected = set(range(64)) - {26}
    if set(selected) != expected:
        raise RuntimeError(f"ordinary shards incomplete missing={sorted(expected-set(selected))} extra={sorted(set(selected)-expected)}")
    for sid in sorted(selected):
        extract_flat(selected[sid], ordinary, token, inventory)

    arts = list_artifacts(args.repo, args.rescue_run_id, token)
    pat = re.compile(r"^stage32-18f-b12-rescue26-subshard-(90|154|218)-g1$")
    selected = {}
    for a in arts:
        m = pat.match(str(a.get("name", "")))
        if m:
            selected[int(m.group(1))] = a
    if set(selected) != {90,154,218}:
        raise RuntimeError(f"18F rescue artifacts incomplete: {sorted(selected)}")
    for sid in sorted(selected):
        extract_flat(selected[sid], rescue, token, inventory)

    arts = list_artifacts(args.repo, args.deep_run_id, token)
    pat = re.compile(r"^stage32-18g-b12-deep-rescue26-subshard-(282|538|794)-g1$")
    selected = {}
    for a in arts:
        m = pat.match(str(a.get("name", "")))
        if m:
            selected[int(m.group(1))] = a
    if set(selected) != {282,538,794}:
        raise RuntimeError(f"18G completed deep artifacts incomplete: {sorted(selected)}")
    for sid in sorted(selected):
        extract_flat(selected[sid], deep, token, inventory)

    arts = list_artifacts(args.repo, args.logical26_run_id, token)
    la = next((a for a in arts if a.get("name") == LOGICAL26_ARTIFACT_NAME), None)
    if la is None:
        raise RuntimeError("Stage32-18K logical 26-of1024 generation-2 artifact missing")
    lsha = extract_flat(la, logical, token, inventory)
    if lsha != LOGICAL26_ARTIFACT_ZIP_SHA256:
        raise RuntimeError(f"Stage32-18K logical artifact ZIP lock mismatch {lsha}")

    inv = {
        "schema": "STAGE32_18L_CROSS_RUN_ARTIFACT_INVENTORY_V1",
        "ordinary_run_id": args.ordinary_run_id,
        "rescue_run_id": args.rescue_run_id,
        "deep_run_id": args.deep_run_id,
        "logical26_run_id": args.logical26_run_id,
        "logical26_artifact_name": LOGICAL26_ARTIFACT_NAME,
        "logical26_artifact_zip_sha256": LOGICAL26_ARTIFACT_ZIP_SHA256,
        "prepared_artifact_id": args.prepared_artifact_id,
        "ordinary_64way_ids": sorted(expected),
        "rescue_256way_ids": [90,154,218],
        "deep_1024way_ids": [282,538,794],
        "logical_1024way_id": 26,
        "artifact_count": len(inventory),
        "artifacts": inventory,
    }
    (root / "artifact-inventory.json").write_text(json.dumps(inv, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"artifact_count": len(inventory), "logical26_run_id": args.logical26_run_id, "logical26_artifact_zip_sha256": lsha}, sort_keys=True))

if __name__ == "__main__":
    main()
