from itertools import combinations_with_replacement
from typing import List


class CoinSet:
    face_values: List[int]
    coin_counts: List[int]

    def __init__(self, *face_values, coin_counts: List[int] = None):
        self.face_values = face_values
        self.coin_counts = [] if coin_counts is None else coin_counts

    def coin_count(self):
        return sum(self.coin_counts)

    def coin_value(self):
        return sum(
            face * count
            for face, count in zip(self.face_values, self.coin_counts)
        )

    def min(self):
        return min(self.face_values)

    def push(self, value: int):
        self.coin_counts.append(value)

    def __iter__(self):
        return iter(self.face_values)

    def __str__(self) -> str:
        coins = ", ".join(
            f"{count}x{face}"
            for face, count in zip(self.face_values, self.coin_counts)
            if count
        )
        return f"CoinSet({coins})"

    def combination(self, max_no: int) -> "CoinSet":
        for comb in combinations_with_replacement(self.face_values, max_no):
            coin_counts = [comb.count(face) for face in self.face_values]
            yield CoinSet(*self.face_values, coin_counts=coin_counts)
