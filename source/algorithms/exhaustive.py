from concurrent.futures import ProcessPoolExecutor
from itertools import chain
from typing import Iterable, List, Set

from rich.progress import Progress

from .motif_matrix import MotifMatrix
from .utils import contains, immediate_neighbors, iter_subsequences

__all__ = ["exhaustive"]


def exhaustive(
    sequences: List[str],
    mer_length: int,
    max_distance: int,
) -> MotifMatrix:
    """Find all motifs from sequence.

    Parameters
    ----------
    sequences : SequenceLike
        sequences to search in. Only DNA (ATGC) is supported.
    mer_length : int
        Expected length of k-mer.
    max_distance : int
        maximal distance for pattern to be considered matching.
    sector_length : int
        length of a sector in sequence that must contain pattern.

    Returns
    -------
    Set[str]
        set containing all possible matching motifs.
    """
    assert mer_length >= max_distance
    matched_sequences: Set[str] = set()
    # progress object is used for pretty signalizing progress of searching
    with Progress() as progress:
        all_k_mers = set(
            chain(*(iter_subsequences(seq, mer_length) for seq in sequences))
        )
        assert all_k_mers
        task = progress.add_task(
            f"Finding motifs for {mer_length}-mers", total=len(all_k_mers)
        )
        # multiprocessing is used to speed up searching process
        with ProcessPoolExecutor() as executor:
            # runs find_motifs_for_k_mer for each (max_distance, sectionized,
            # all_k_mers) then iterates over results
            for k_mer_motifs in executor.map(
                _find_motifs_for_k_mer,
                [max_distance] * len(all_k_mers),
                [sequences] * len(all_k_mers),
                all_k_mers,
            ):
                # updating set removes all repetitions
                matched_sequences.update(k_mer_motifs)
                progress.advance(task, 1)
    return MotifMatrix(matched_sequences)


def _find_motifs_for_k_mer(
    max_distance: int,
    sequences: Iterable[str],
    k_mer: str,
) -> Set[str]:
    k_mers = set()
    for pattern in _neighbors(k_mer, max_distance):
        for sector in sequences:
            if not contains(sector, pattern, max_distance):
                break
        else:
            k_mers.add(pattern)
    return k_mers


def _neighbors(pattern: str, max_mismatches: int) -> Set[str]:
    neighborhood = {pattern}
    for _ in range(max_mismatches):
        extra = set()
        for sub_pattern in neighborhood:
            extra.update(immediate_neighbors(sub_pattern))
        neighborhood.update(extra)
    return neighborhood
