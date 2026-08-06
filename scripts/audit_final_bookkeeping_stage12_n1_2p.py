#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def report() -> dict:
    return {
        "classification": "A_FINAL_BOOKKEEPING_WRITTEN_INDEPENDENT_REVIEW_REQUIRED",
        "reference": {
            "author": "Gerald Tenenbaum",
            "title": "Introduction to Analytic and Probabilistic Number Theory",
            "edition": "Third Edition",
            "series": "Graduate Studies in Mathematics 163",
            "publisher": "American Mathematical Society",
            "year": 2015,
            "chapter": "II.5",
            "theorem": "II.5.2",
        },
        "coefficient_regions": ["R00", "R10", "R01", "R11"],
        "rectangle_error_terms": [
            "RS*E_star(sqrt(R))",
            "RS*E_star(sqrt(S))",
            "R^(1/2+delta)*S",
            "R*S^(1/2+delta)",
        ],
        "final_route": ["2j", "2k", "2l", "2m", "2n", "2o", "2p"],
        "status": "PROVISIONALLY_CLOSED_FINAL_BOOKKEEPING_WRITTEN_REVIEW_PENDING",
    }


def main() -> None:
    data = report()
    assert data["coefficient_regions"] == ["R00", "R10", "R01", "R11"]
    assert data["reference"]["chapter"] == "II.5"
    rendered = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    out = Path("data/final_bookkeeping_stage12_n1_2p_report.json")
    if out.exists():
        assert json.loads(out.read_text(encoding="utf-8")) == data
    print(rendered, end="")


if __name__ == "__main__":
    main()
