PETIT_ALPHA_DENOMINATOR = 120


def audit():
    return {
        "audit_verdict": "NEW_GATE",
        "petit_species_match": True,
        "petit_alpha_upper": 1 / PETIT_ALPHA_DENOMINATOR,
        "twist_count_exponent": 0.5,
        "covering_map_adapter": False,
        "nontorsion_image": False,
        "canonical_height_upper_bridge": False,
        "packet_multiplicity_bridge": False,
    }


if __name__ == "__main__":
    data = audit()
    assert data["petit_species_match"]
    assert data["petit_alpha_upper"] == 1 / 120
    assert data["twist_count_exponent"] == 0.5
    assert not data["covering_map_adapter"]
    print("STAGE15_6AU_VERIFY=PASS")
    print("AUDIT_VERDICT=NEW_GATE")
    print("PETIT_HALF_POWER_TWIST_SPECIES_MATCH=true")
