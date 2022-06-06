from functools import reduce
from operator import mul
from typing import Dict, Iterable, Iterator, List, Sequence

from .utils import NUCLEOTIDES

__all__ = ["MotifMatrix", "probability"]


class MotifMatrix:
    matrix: Sequence[str]

    def __init__(self, __matrix: Iterable[str]) -> None:
        assert __matrix
        assert all(__matrix)
        self.matrix = [s.upper() for s in __matrix]

    @property
    def width(self) -> int:
        return len(self.matrix[0])

    @property
    def height(self) -> int:
        return len(self.matrix)

    def count(self) -> Dict[str, List[int]]:
        counts = {k: [0 for i in range(self.width)] for k in NUCLEOTIDES}
        for col_i in range(self.width):
            for row in self:
                counts[row[col_i]][col_i] += 1

        return counts

    def profile(self) -> Dict[str, List[int]]:
        counts = self.count()
        for key in NUCLEOTIDES:
            for col_i in range(self.width):
                counts[key][col_i] /= self.height  # type: ignore
        return counts

    def consensus(self) -> str:
        profile = self.profile()
        assert profile
        consensus = []
        for col_i in range(self.width):
            most_common = NUCLEOTIDES[0]
            common_weight = 0.0
            for row_i in NUCLEOTIDES:
                profile_weight = profile[row_i][col_i]
                if profile_weight > common_weight:
                    common_weight = profile_weight
                    most_common = row_i
            consensus.append(most_common)
        return "".join(consensus)

    def score(self) -> int:
        counts = self.count()
        assert counts
        total_score = 0
        for col_i in range(self.width):
            column_score = self.height - max(
                counts[key][col_i] for key in NUCLEOTIDES
            )
            total_score += column_score
        return total_score

    def __iter__(self) -> Iterator[Sequence[str]]:
        return iter(self.matrix)

    def __getitem__(self, index: int) -> str:
        return self.matrix[index]

    def __str__(self) -> str:
        return "\n".join(f"[ {s} ]" for s in self.matrix)

    __repr__ = __str__


def probability(profile: Dict[str, List[int]], seq: str) -> float:
    assert seq
    assert len(seq) == len(profile["A"])
    return reduce(mul, (profile[s][i] for i, s in enumerate(seq)))
