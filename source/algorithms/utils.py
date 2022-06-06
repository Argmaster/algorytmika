from typing import Iterable, Sequence

__all__ = [
    "NUCLEOTIDES",
    "contains",
    "iter_subsequences",
    "hamming_distance",
    "immediate_neighbors",
    "dna_to_int",
    "int_to_dna",
]


NUCLEOTIDES: str = "ATGC"


def contains(sequence: str, item: str, max_distance: int = 0) -> bool:
    """Check wheather a sequence contains item with at most max_distance
    mismatches.

    Parameters
    ----------
    sequence : str
        Sequence to search in.
    item : str
        Sequence to look for.
    max_distance : int, optional
        Maximal number of mismatches, by default 0

    Returns
    -------
    bool
        True when contains.
    """
    sub_sequences = iter_subsequences(sequence, len(item))
    assert sub_sequences
    if sub_sequences:
        return (
            min(hamming_distance(item, sub) for sub in sub_sequences)
            <= max_distance
        )
    else:
        return False


def iter_subsequences(
    sequence: str,
    mer_length: int,
) -> Iterable[str]:
    """Generates all k-mers for given sequence with given length.

    ```
    >>> for s in iter_subsequences("ATGCATGC", 3):
    ...    print(s)
    ATG
    TGC
    GCA
    CAT
    ATG
    TGC

    ```
    Parameters
    ----------
    sequence : str
        Sequence to sample from.
    mer_length : Optional[int], optional
        Length of subsequences to return (can be also considered a step), by default None,
        then its set to length of sequence

    Yields
    ------
    str
        Subsequence from sequence.
    """
    assert mer_length
    if len(sequence) < mer_length:
        yield sequence
    else:
        for i in range(0, len(sequence) - mer_length + 1):
            yield sequence[i : i + mer_length]
    return


def hamming_distance(first: Sequence, second: Sequence) -> int:
    assert first
    assert second
    return sum(f != s for f, s in zip(first, second))


def immediate_neighbors(pattern: str) -> Iterable[str]:
    for i, char in enumerate(pattern):
        for nucleotide in NUCLEOTIDES:
            if nucleotide != char:
                yield pattern[:i] + nucleotide + pattern[i + 1 :]


_MAP = {
    "A": 0,
    0: "A",
    "C": 1,
    1: "C",
    "G": 2,
    2: "G",
    "T": 3,
    3: "T",
}
_BASE = 4


def dna_to_int(value: str) -> int:
    assert value
    multiplier = 1
    total = 0
    for val in reversed(value):
        total += _MAP[val] * multiplier
        multiplier *= _BASE
    return total


def int_to_dna(value: int, size: int = 0) -> str:
    seq = []
    while value:
        reminder = value % _BASE
        value //= _BASE
        seq.append(_MAP[reminder])
    seq.reverse()
    return f'{"".join(seq):A>{size}}'


if __name__ == "__main__":
    import doctest

    doctest.testmod()
