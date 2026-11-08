#!/usr/bin/env python3
"""Verify finite inputs to the class-group functional reduction of delta-star."""
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
HASHES = {
 "four_lift_target384.json":"0eba8c6e2610e463f4252f566c12cdfc0bd153addc393ad6847b41aa6fa0dce0",
 "units381_exact.json":"78136c1f3c1fed53c429d26fc754af33edb0106d6c119fc738f7ea9f24373bd2",
 "row375_results.json":"28794c519ca99152599ccd1ef7a818f0106e2113f8a5b959daa35b6f79985d01",
 "unit_basis_witnesses.json":"d0705fa3cb0b70084fd7f5693b7a418fcb7f226decadce578d2c356ec0cc1b3e",
 "curve_C29.json":"04542e2e37a75ce382ca7921d51aae9e3bcc690b6a03d514dcbc0a511205bd74"
}


def read(name):
    b=(HERE/name).read_bytes()
    if name in HASHES:
        assert sha256(b).hexdigest()==HASHES[name],name
    return json.loads(b)


class BinarySpan:
    def __init__(self, vectors=()):
        self.rows={}
        for v in vectors:
            self.add(v)

    def reduce(self, value, expression=0):
        while value:
            pivot=value.bit_length()-1
            if pivot not in self.rows:
                break
            v,e=self.rows[pivot]
            value^=v
            expression^=e
        return value,expression

    def add(self,value,expression=0):
        value,expression=self.reduce(value,expression)
        if not value:
            return False
        self.rows[value.bit_length()-1]=(value,expression)
        return True

    def rank(self):
        return len(self.rows)


def pairing_equations(radical_rows,dimension):
    pairs=[(i,j) for i in range(dimension) for j in range(i+1,dimension)]
    equations=[]
    for r in radical_rows:
        for j in range(dimension):
            equations.append(sum(1<<k for k,(i,l) in enumerate(pairs)
                                 if (j==l and (r>>i)&1) or (j==i and (r>>l)&1)))
    return pairs,equations


def main():
    data=read("units381_exact.json")
    rational=read("row375_results.json")
    units=read("unit_basis_witnesses.json")
    curve=read("curve_C29.json")
    delta=read("four_lift_target384.json")
    degree=len(curve["F_ascending"])-1
    assert degree==105 and curve["F_ascending"][-1]==1
    genus=(degree-1)//2
    assert genus==52 and 2*(genus-1)==102
    kernel=[int(v,16) for v in data["kernel_basis_local_codes"]]
    assert len(kernel)==9
    basis=BinarySpan()
    for i,v in enumerate(kernel):
        assert basis.add(v,1<<i)
    assert basis.rank()==9
    known=[int(v,16) for v in rational["unit_squareclasses_at_2"]]
    assert len(known)==8
    known_coordinates=[]
    for v in known:
        remainder,e=basis.reduce(v)
        assert remainder==0
        known_coordinates.append(e)
    assert BinarySpan(known_coordinates).rank()==8
    code=int(delta["independent_local_code"],16)
    remainder,delta_coordinates=basis.reduce(code)
    assert remainder==0 and delta_coordinates
    assert BinarySpan(known_coordinates+[delta_coordinates]).rank()==9
    assert code==0x44b88774c94772d6bc5c8f05827
    mask=int(delta["unit_basis_mask"],16)
    assert mask==0x4125e122ae5103
    images=data["basis_images"]
    assert len(images)==len(units)==55 and mask.bit_length()<=55
    computed=0
    for i,w in enumerate(units):
        assert w["unit_code"]==images[i]["unit_local_code"]
        if mask>>i&1:
            computed^=int(w["unit_code"],16)
    assert computed==code
    functionals=[f for f in range(1<<9)
                 if all((f&r).bit_count()%2==0 for r in known_coordinates)
                 and (f&delta_coordinates).bit_count()%2==1]
    assert len(functionals)==1
    corrections=[]
    for m in range(1<<8):
        value=0
        for i,v in enumerate(known_coordinates):
            if m>>i&1:
                value^=v
        if value==(delta_coordinates^(1<<8)):
            corrections.append(m)
    assert corrections==[0x31]
    pairs,equations=pairing_equations(known_coordinates,9)
    assert len(pairs)==36 and BinarySpan(equations).rank()==36

    # The Galois-equivariant odd-degree splitting of the root permutation module.
    full=(1<<degree)-1
    def project(v):
        return v^(full if v.bit_count()%2 else 0)

    vectors=[project(1<<i) for i in range(degree)]
    assert all(v.bit_count()%2==0 and project(v)==v for v in vectors)
    assert project(full)==0 and BinarySpan(vectors).rank()==104
    def swap(v,i):
        a=(v>>i)&1
        b=(v>>(i+1))&1
        return v^(((1<<i)|(1<<(i+1))) if a!=b else 0)

    for i in range(degree-1):
        assert all(project(swap(1<<j,i))==swap(project(1<<j),i) for j in range(degree))

    print(json.dumps({
      "root_degree":degree,"genus":genus,"rational_theta_characteristic_degree":genus-1,
      "canonical_divisor_degree":102,"unit_selmer_dimension":9,
      "known_rational_coordinates_in_unit_selmer":list(map(hex,known_coordinates)),
      "delta_coordinates_in_unit_selmer":hex(delta_coordinates),
      "quotient_unit_selmer_by_known_rationals_dimension":1,
      "unique_unit_quotient_linear_functional":hex(functionals[0]),
      "canonical_unit_selmer_representative_coordinates":"0x100",
      "canonical_unit_basis_mask":data["kernel_basis_as_unit_bitmasks"][8],
      "rational_correction_to_delta":["H","D5b","D7"],
      "alternating_form_variables":36,"independent_radical_equations":36,
      "all_unit_selmer_Cassels_Tate_pairings_zero":True,
      "permutation_module_dimension":degree,"norm_zero_module_dimension":104,
      "equivariant_projection_checked":True,
      "unrestricted_global_H1_J4_lift_exists":True,
      "Sel4_lift_equivalent_to_class_group_functional_being_zero":True,
      "class_group_functional_value":"UNDETERMINED",
      "delta_Sel4_membership":"UNDETERMINED",
      "nonlift_rank_upper_bound":"7+c_Cl",
      "source_and_nonlift_imply_c_Cl_at_least":3,
      "nonlift_without_source_implies_c_Cl_at_least":1
    },indent=2))


if __name__=="__main__":
    main()
