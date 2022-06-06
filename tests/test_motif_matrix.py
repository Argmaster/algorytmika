import pytest

from algorithms.motif_matrix import MotifMatrix


class TestMotifMatrix:
    @pytest.fixture()
    def mm(self) -> MotifMatrix:
        return MotifMatrix(
            [
                "AAAAC",
                "AAATA",
                "AGAAA",
                "CAACA",
            ]
        )

    def test_count(self, mm: MotifMatrix) -> None:
        assert mm.count() == {
            "A": [3, 3, 4, 2, 3],
            "T": [0, 0, 0, 1, 0],
            "G": [0, 1, 0, 0, 0],
            "C": [1, 0, 0, 1, 1],
        }

    def test_profile(self, mm: MotifMatrix) -> None:
        assert mm.profile() == {
            "A": [0.75, 0.75, 1.0, 0.5, 0.75],
            "T": [0, 0, 0, 0.25, 0],
            "G": [0, 0.25, 0, 0, 0],
            "C": [0.25, 0, 0, 0.25, 0.25],
        }

    def test_consensus(self, mm: MotifMatrix) -> None:
        assert mm.consensus() == "AAAAA"

    def test_score(self, mm: MotifMatrix) -> None:
        assert mm.score() == 5

    @pytest.fixture()
    def mm2(self) -> MotifMatrix:
        return MotifMatrix(
            [
                "TCGGGGGTTTTT",
                "CCGGTGACTTAC",
                "ACGGGGATTTTC",
                "TTGGGGACTTTT",
                "AAGGGGACTTCC",
                "TTGGGGACTTCC",
                "TCGGGGATTCAT",
                "TCGGGGATTCCT",
                "TAGGGGAACTAC",
                "TCGGGTATAACC",
            ]
        )

    def test_count_2(self, mm2: MotifMatrix) -> None:
        assert mm2.count() == {
            "A": [2, 2, 0, 0, 0, 0, 9, 1, 1, 1, 3, 0],
            "C": [1, 6, 0, 0, 0, 0, 0, 4, 1, 2, 4, 6],
            "G": [0, 0, 10, 10, 9, 9, 1, 0, 0, 0, 0, 0],
            "T": [7, 2, 0, 0, 1, 1, 0, 5, 8, 7, 3, 4],
        }

    def test_profile_2(self, mm2: MotifMatrix) -> None:
        assert mm2.profile() == {
            "A": [0.2, 0.2, 0, 0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
            "C": [0.1, 0.6, 0, 0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
            "G": [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
            "T": [0.7, 0.2, 0, 0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4],
        }

    def test_consensus_2(self, mm2: MotifMatrix) -> None:
        assert mm2.consensus() == "TCGGGGATTTCC"

    def test_score_2(self, mm2: MotifMatrix) -> None:
        assert mm2.score() == 30
