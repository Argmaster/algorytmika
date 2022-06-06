from algorithms.utils import (
    contains,
    dna_to_int,
    hamming_distance,
    int_to_dna,
    iter_subsequences,
)


def test_hamming_distance():
    assert hamming_distance("ATTGGA", "ATCGGA") == 1
    assert hamming_distance("GCCTTAGACCCC", "GGGTTAAACCCC") == 3
    assert hamming_distance("ATGCGATAGCGAT", "ATGCGATAGCGAT") == 0
    assert hamming_distance("AAAAAA", "TTTTTT") == 6


def test_iter_subsequences():
    assert tuple(iter_subsequences("AATT", 2)) == ("AA", "AT", "TT")
    assert tuple(iter_subsequences("ATGCA", 2)) == ("AT", "TG", "GC", "CA")


def test_contains():
    assert contains("AATT", "AG", 1) is True
    assert contains("AATT", "AAGT", 1) is True
    assert contains("AATT", "ACGT", 1) is False


def test_dna_to_int():
    assert dna_to_int("ATTGCA") == 996
    assert dna_to_int("GGCAATT") == 10511
    assert dna_to_int("AC") == 1


def test_int_to_dna():
    assert int_to_dna(996, 6) == "ATTGCA"
    assert int_to_dna(10511, 7) == "GGCAATT"
    assert int_to_dna(1, 2) == "AC"
