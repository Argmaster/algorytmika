from random import random
from typing import Callable, Dict, List, Union

from algorithms.utils import iter_subsequences

from .motif_matrix import MotifMatrix, probability

__all__ = ["randomized_consensus", "randomized"]


def randomized_consensus(
    sequences: List[str], mer_length: int, repeats: int = 10_000
) -> str:
    """Repeat randomized(sequences, mer_length) `repeatrs` times and return
    resulting consensus sequence.

    Parameters
    ----------
    sequences : List[str]
        List of sequences to look for k-mer in.
    mer_length : int
        Expected length of k-mer.
    repeats : int, optional
        Number of repeats, by default 10_000

    Returns
    -------
    str
        Consensus sequence as a result from all repeats.
    """
    return MotifMatrix(
        [randomized(sequences, mer_length).consensus() for _ in range(repeats)]
    ).consensus()


def randomized(sequences: List[str], mer_length: int) -> MotifMatrix:
    """Performs randomized search implemented according to
    RandomizedMotifSearch() described in ``` Bioinformatics Algorithms: An
    Active Learning Approach 2nd Edition, Vol. I.

    Phillip Compeau & Pavel Pevzner
    ```

    Parameters
    ----------
    sequences : List[str]
        List of sequences to look for k-mer in.
    mer_length : int
        Expected length of k-mer.

    Returns
    -------
    MotifMatrix
        Matrix containing best k-mers found.
    """
    sequences = [s.upper() for s in sequences]
    best_motifs = MotifMatrix([_random_mer(s, mer_length) for s in sequences])
    while True:
        profile = best_motifs.profile()
        new_motifs = MotifMatrix(
            [_most_probable(profile, seq, mer_length) for seq in sequences]
        )
        if new_motifs.score() < best_motifs.score():
            best_motifs = new_motifs
        else:
            return best_motifs


def _random_mer(
    sequence: str,
    mer_length: int,
    random_function: Callable[[], Union[float, int]] = random,
):
    assert len(sequence) >= mer_length
    i = int(random_function() * (len(sequence) - mer_length + 1))
    return sequence[i : i + mer_length]


def _most_probable(profile: Dict[str, List[int]], seq: str, mer_length: int):
    return max(
        iter_subsequences(seq, mer_length),
        key=lambda s: probability(profile, s),
    )
