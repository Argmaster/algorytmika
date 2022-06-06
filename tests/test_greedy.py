from collections import ChainMap
from pathlib import Path
from timeit import timeit
from typing import List

import pytest

from algorithms.greedy import greedy

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture()
def dna_data():
    return (DATA_DIR / "sample.txt").read_text().strip().upper().split("\n")


def test_greedy_2(dna_data):
    assert greedy(dna_data, 8).consensus() == "ATGAAAAA"


@pytest.mark.skip()
def test_greedy_benchmark(dna_data: List[str]) -> None:
    number = 20
    print(
        timeit(
            "greedy(dna_data, 8).consensus()",
            globals=dict(ChainMap(locals(), globals())),
            number=number,
        )
        / number
    )
