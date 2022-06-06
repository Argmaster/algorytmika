from collections import ChainMap
from pathlib import Path
from timeit import timeit
from typing import List

import pytest

from algorithms.randomized import randomized_consensus

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture()
def dna_data():
    return (DATA_DIR / "sample.txt").read_text().strip().upper().split("\n")


def test_randomized(dna_data: List[str]):
    assert randomized_consensus(dna_data, 8, 1000) == "AAAAAAAA"


@pytest.mark.skip()
def test_randomized_benchmark(dna_data: List[str]) -> None:
    number = 20
    print(
        timeit(
            "randomized_consensus(dna_data, 8, 1000)",
            globals=dict(ChainMap(locals(), globals())),
            number=number,
        )
        / number
    )
