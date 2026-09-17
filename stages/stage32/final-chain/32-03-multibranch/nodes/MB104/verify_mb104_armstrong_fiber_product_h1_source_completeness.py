#!/usr/bin/env python3
import hashlib, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
LOCK="ff1581420337745b1718a0b55b2d8049244277de"
def blob(p):
 d=p.read_bytes(); return hashlib.sha1(f"blob {len(d)}\0".encode()+d).hexdigest()
def req(x,m):
 if not x: raise SystemExit("FAIL: "+m)
source=HERE/"ARMSTRONG-FIBER-PRODUCT-H1-SOURCE-NOTE.md"
cert=json.loads((HERE/"ARMSTRONG-FIBER-PRODUCT-H1-SOURCE-COMPLETENESS-CERTIFICATE.json").read_text())
req(blob(source)==LOCK,"SOURCE_LOCK_FAIL")
c=cert["classification"]; m=cert["matrix_consequence"]
req(c["identity_component_excluded"] and c["conjugation_by_F_reduces_first_conjugator"] and c["kernel_conjugation_reduces_second_conjugator"],"conjugation reduction")
req(c["remaining_parameter"]=="relative H coset delta" and c["representatives"]==2*4*4*4==128,"representatives")
req(c["normal_closure_complete"] and c["abelianization_relations_complete"],"completeness")
req(m["preexisting_fixed_relations"]==128 and m["preexisting_matrix_shape"]==[459,64] and m["unimodular_witness_determinant"]==1,"matrix binding")
req(not any(cert["firewall"].values()),"credit firewall")
print("PASS STAGE32_MB104_ARMSTRONG_FIBER_PRODUCT_H1_SOURCE_COMPLETENESS_V1")
