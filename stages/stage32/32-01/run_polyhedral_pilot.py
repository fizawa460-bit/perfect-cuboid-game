#!/usr/bin/env python3
import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
MAGMA_URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
MAGMA_REFERER = "https://magma.maths.usyd.edu.au/calc/"
EXPECTED_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"

core = json.loads((ROOT / "picard-core.json").read_text(encoding="utf-8"))
if core.get("schema") != "STAGE32_PICARD_CORE_INDLIST_V1":
    raise SystemExit("wrong Picard-core schema")
if core.get("source", {}).get("git_blob_sha1") != EXPECTED_BLOB:
    raise SystemExit("Picard core is not bound to the pinned upstream blob")
if core.get("rank") != 64 or core.get("known_class_count") != 140 or core.get("h2") != 16:
    raise SystemExit("Picard-core invariant mismatch")

gram = core["basis_gram"]
h = core["hyperplane"]
known = core["known_classes"]
if len(gram) != 64 or any(len(r) != 64 for r in gram):
    raise SystemExit("bad 64x64 Gram matrix")
if len(h) != 64 or len(known) != 140 or any(len(r) != 64 for r in known):
    raise SystemExit("bad Picard-core vectors")

flat_gram = ",".join(str(x) for row in gram for x in row)
def vec(v):
    return "[" + ",".join(str(x) for x in v) + "]"
known_text = ",\n".join("PicL!" + vec(v) for v in known)
pilot = (ROOT / "polyhedral_pilot_after_upstream.m").read_text(encoding="utf-8")
code = f'''SetColumns(0);
pmPic := Matrix(Integers(),64,64,[{flat_gram}]);
PicL := RSpace(Integers(),64,pmPic);
HinPicL := PicL!{vec(h)};
gensinPicL := [
{known_text}
];
''' + pilot

data = urllib.parse.urlencode({"input": code}).encode("utf-8")
req = urllib.request.Request(
    MAGMA_URL,
    data=data,
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html, application/xml, application/xhtml+xml",
        "Referer": MAGMA_REFERER,
        "User-Agent": "perfect-cuboid-stage32-poly/1.0",
    },
    method="POST",
)
try:
    with urllib.request.urlopen(req, timeout=75) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        status = resp.status
        headers = dict(resp.headers.items())
except urllib.error.HTTPError as exc:
    diagnostic = exc.read().decode("utf-8", errors="replace")
    payload = {
        "success": False,
        "http_status": exc.code,
        "reason": str(exc.reason),
        "diagnostic": diagnostic,
        "core_sha256": core.get("canonical_sha256_without_this_field"),
        "upstream_blob": EXPECTED_BLOB,
    }
    (ROOT / "polyhedral-pilot-response.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(payload, sort_keys=True))
    raise SystemExit(2)

(ROOT / "polyhedral-pilot-response.xml").write_text(raw, encoding="utf-8")
root = ET.fromstring(raw)
lines = []
for result in root.findall(".//results"):
    for line in result.findall(".//line"):
        lines.append("".join(line.itertext()))
stdout = "\n".join(lines) + ("\n" if lines else "")
(ROOT / "polyhedral-pilot-stdout.txt").write_text(stdout, encoding="utf-8")
completion = "STAGE32_POLYHEDRAL_PILOT_END" in lines
runtime_error = any(x in stdout for x in ("Runtime error", "Internal error", "User error", "Assertion failed"))
compact_line = next((x for x in lines if x.startswith("STAGE32_POLY|LEVEL2_COMPACT|")), None)
compact = None if compact_line is None else compact_line.rsplit("|",1)[1].strip().lower() == "true"
payload = {
    "success": status == 200 and completion and not runtime_error,
    "http_status": status,
    "runtime_error_seen": runtime_error,
    "completion_marker_seen": completion,
    "level2_compact": compact,
    "core_sha256": core.get("canonical_sha256_without_this_field"),
    "upstream_blob": EXPECTED_BLOB,
    "response_headers": headers,
    "stdout": stdout,
}
(ROOT / "polyhedral-pilot-response.json").write_text(
    json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps({k: payload[k] for k in (
    "success","http_status","runtime_error_seen","completion_marker_seen","level2_compact","core_sha256","upstream_blob"
)}, sort_keys=True))
print(stdout)
if not payload["success"]:
    raise SystemExit("Stage32 polyhedral pilot did not finish cleanly")
