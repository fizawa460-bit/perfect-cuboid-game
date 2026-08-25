#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, pathlib, re, urllib.request, zipfile

API = "https://api.github.com"


def get_json(url: str, token: str):
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "stage32-18h-artifact-fetcher",
    })
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def get_bytes(url: str, token: str) -> bytes:
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "stage32-18h-artifact-fetcher",
    })
    with urllib.request.urlopen(req) as r:
        return r.read()


def list_artifacts(repo: str, run_id: int, token: str):
    out = []
    page = 1
    while True:
        data = get_json(f"{API}/repos/{repo}/actions/runs/{run_id}/artifacts?per_page=100&page={page}", token)
        batch = data.get("artifacts", [])
        out.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return out


def download_extract(artifact: dict, out_dir: pathlib.Path, token: str, inventory: list):
    if artifact.get("expired"):
        raise RuntimeError(f"artifact expired: {artifact['name']}")
    raw = get_bytes(artifact["archive_download_url"], token)
    digest = artifact.get("digest")
    got = hashlib.sha256(raw).hexdigest()
    if digest:
        want = digest.removeprefix("sha256:")
        if got != want:
            raise RuntimeError(f"zip digest mismatch {artifact['name']}: {got} != {want}")
    out_dir.mkdir(parents=True, exist_ok=True)
    zp = out_dir / f"artifact-{artifact['id']}.zip"
    zp.write_bytes(raw)
    extract = out_dir / "extracted"
    extract.mkdir(exist_ok=True)
    with zipfile.ZipFile(zp) as z:
        z.extractall(extract)
    inventory.append({
        "id": artifact["id"], "name": artifact["name"],
        "zip_sha256": got, "declared_digest": digest,
        "size_in_bytes": artifact.get("size_in_bytes"),
        "created_at": artifact.get("created_at"),
    })
    return extract


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--ordinary-run-id", type=int, required=True)
    ap.add_argument("--rescue-run-id", type=int, required=True)
    ap.add_argument("--deep-run-id", type=int, required=True)
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
    prepared = root / "prepared"
    inventory = []

    arts = list_artifacts(args.repo, args.ordinary_run_id, token)
    by_id = {int(a["id"]): a for a in arts}
    pa = by_id.get(args.prepared_artifact_id)
    if not pa or pa.get("name") != "stage32-18e-b12-prepared-g1":
        raise RuntimeError("immutable prepared artifact not found in ordinary run")
    ex = download_extract(pa, prepared, token, inventory)
    for p in ex.iterdir():
        if p.is_file():
            target = prepared / p.name
            if target.exists(): target.unlink()
            p.replace(target)

    pat = re.compile(r"^stage32-18e-b12-exact-shard-(\d+)-g1$")
    selected = {}
    for a in arts:
        m = pat.match(a.get("name", ""))
        if m:
            sid = int(m.group(1))
            if sid != 26:
                selected[sid] = a
    expected = set(range(64)) - {26}
    if set(selected) != expected:
        raise RuntimeError(f"ordinary artifact ids mismatch missing={sorted(expected-set(selected))} extra={sorted(set(selected)-expected)}")
    ordinary.mkdir(parents=True, exist_ok=True)
    for sid in sorted(selected):
        ex = download_extract(selected[sid], ordinary / f"artifact-{sid}", token, inventory)
        for p in ex.iterdir():
            if p.is_file():
                target = ordinary / p.name
                if target.exists():
                    raise RuntimeError(f"ordinary filename collision {target.name}")
                p.replace(target)

    arts = list_artifacts(args.repo, args.rescue_run_id, token)
    pat = re.compile(r"^stage32-18f-b12-rescue26-subshard-(26|90|154|218)-g1$")
    selected = {}
    for a in arts:
        m = pat.match(a.get("name", ""))
        if m:
            selected[int(m.group(1))] = a
    required = {90,154,218}
    if not required.issubset(selected):
        raise RuntimeError(f"missing required 256-way rescue artifacts: {sorted(required-set(selected))}")
    rescue.mkdir(parents=True, exist_ok=True)
    for sid in sorted(selected):
        ex = download_extract(selected[sid], rescue / f"artifact-{sid}", token, inventory)
        for p in ex.iterdir():
            if p.is_file():
                target = rescue / p.name
                if target.exists():
                    raise RuntimeError(f"rescue filename collision {target.name}")
                p.replace(target)

    arts = list_artifacts(args.repo, args.deep_run_id, token)
    pat = re.compile(r"^stage32-18g-b12-deep-rescue26-subshard-(26|282|538|794)-g1$")
    selected = {}
    for a in arts:
        m = pat.match(a.get("name", ""))
        if m:
            selected[int(m.group(1))] = a
    required = {26,282,538,794}
    if set(selected) != required:
        raise RuntimeError(f"deep rescue artifacts mismatch missing={sorted(required-set(selected))} extra={sorted(set(selected)-required)}")
    deep.mkdir(parents=True, exist_ok=True)
    for sid in sorted(selected):
        ex = download_extract(selected[sid], deep / f"artifact-{sid}", token, inventory)
        for p in ex.iterdir():
            if p.is_file():
                target = deep / p.name
                if target.exists():
                    raise RuntimeError(f"deep filename collision {target.name}")
                p.replace(target)

    inv = {
        "schema": "STAGE32_18H_CROSS_RUN_ARTIFACT_INVENTORY_V1",
        "repo": args.repo,
        "ordinary_run_id": args.ordinary_run_id,
        "rescue_run_id": args.rescue_run_id,
        "deep_run_id": args.deep_run_id,
        "prepared_artifact_id": args.prepared_artifact_id,
        "ordinary_shards": sorted(expected),
        "rescue256_available": sorted(selected for selected in []),
        "artifact_count": len(inventory),
        "artifacts": inventory,
    }
    # Record actual rescue availability separately without shadowing the deep selection above.
    rescue_ids=[]
    for p in rescue.glob('d16-b12-exact-subshard-*-of256.json'):
        rescue_ids.append(int(p.stem.split('-')[5]))
    inv["rescue256_available"] = sorted(rescue_ids)
    inv["deep1024_available"] = [26,282,538,794]
    (root / "artifact-inventory.json").write_text(json.dumps(inv, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"artifact_count": len(inventory), "rescue256_available": sorted(rescue_ids), "deep1024_available": [26,282,538,794]}, sort_keys=True))


if __name__ == "__main__":
    main()
