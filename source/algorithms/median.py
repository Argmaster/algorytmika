import math
from typing import Sequence

from rich.progress import Progress

from .utils import hamming_distance, int_to_dna, iter_subsequences

__all__ = ["median"]


def median(sequences: Sequence[str], mer_length: int) -> str:
    """Calculate median string from given collection of sequences.

    Parameters
    ----------
    sequences : Sequence[str]
        List of sequences to look for k-mer in.
    mer_length : int
        Expected length of k-mer.

    Returns
    -------
    Optional[str]
        _description_
    """
    assert mer_length > 0
    assert sequences
    assert all(sequences)
    min_distance = math.inf
    median = None
    with Progress() as progress:
        task = progress.add_task(
            f"Finding motifs for {mer_length}-mers", total=4**mer_length - 1
        )
        for k_mer_int in range(4**mer_length - 1):
            k_mer = int_to_dna(k_mer_int, mer_length)
            current_distance = _hamming_total_distance(sequences, k_mer)
            if current_distance < min_distance:
                min_distance = current_distance
                median = k_mer
                assert isinstance(median, str)
            progress.advance(task, 1)
    assert median is not None
    return median


def _hamming_total_distance(sequences: Sequence[str], mer: str) -> int:
    assert all(len(s) >= len(mer) for s in sequences)
    total_distance = 0
    for sub_seq in sequences:
        min_distance = min(
            hamming_distance(mer, k_mer)
            for k_mer in iter_subsequences(sub_seq, len(mer))
        )
        total_distance += min_distance

    return total_distance
