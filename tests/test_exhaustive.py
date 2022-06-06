from collections import ChainMap
from pathlib import Path
from random import random
from timeit import timeit
from typing import List

import pytest

from algorithms.exhaustive import exhaustive
from algorithms.utils import int_to_dna

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture()
def dna_data():
    return (DATA_DIR / "sample.txt").read_text().strip().upper().split("\n")


def uniform_sample(size: int) -> str:
    return "".join(int_to_dna(int(random() * 4), 1) for _ in range(size))


def generate_sample(dest: Path) -> None:
    dest.write_text("\n".join(uniform_sample(30) for _ in range(8)))


def test_exhaustive(dna_data: List[str]) -> None:
    assert exhaustive(dna_data, 8, 2).consensus() == "AAAAAAAA"


@pytest.mark.skip()
def test_exhaustive_benchmark(dna_data: List[str]) -> None:
    number = 20
    print(
        timeit(
            "exhaustive(dna_data, 8, 3).consensus()",
            globals=dict(ChainMap(locals(), globals())),
            number=number,
        )
        / number
    )
