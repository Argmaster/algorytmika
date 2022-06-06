from collections import ChainMap
from pathlib import Path
from timeit import timeit
from typing import List

import pytest

from algorithms.median import median

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture()
def dna_data():
    return (DATA_DIR / "sample.txt").read_text().strip().upper().split("\n")


def test_median(dna_data: List[str]) -> None:
    assert median(dna_data, 8) == "AAAAAAGT"


@pytest.mark.skip()
def test_median_benchmark(dna_data: List[str]) -> None:
    number = 10
    print(
        timeit(
            "median(dna_data, 8)",
            globals=dict(ChainMap(locals(), globals())),
            number=number,
        )
        / number
    )
