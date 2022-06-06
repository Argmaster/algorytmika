from typing import List

from .motif_matrix import MotifMatrix
from .utils import iter_subsequences

__all__ = ["greedy"]


def greedy(sequences: List[str], mer_length: int) -> MotifMatrix:
    """Calculates motif matrix which contains k-mers that are similar to
    repeating k-mer in all `sequences`.

    Parameters
    ----------
    sequences : List[str]
        List of sequences to look for k-mer in.
    mer_length : int
        Expected length of k-mer.

    Returns
    -------
    MotifMatrix
        Matrix with total of len(sequences) rows.
    """
    assert sequences
    assert len(sequences) > 1
    assert all(sequences)
    assert (_len_0 := len(sequences[0])) and all(  # noqa: PT018
        len(s) == _len_0 for s in sequences
    )
    best_motifs: MotifMatrix = MotifMatrix(
        [row[:mer_length] for row in sequences]
    )
    for column_index, first_kmer in enumerate(
        iter_subsequences(sequences[0], mer_length)
    ):
        motifs: MotifMatrix = MotifMatrix(
            [
                first_kmer,
                *(
                    row[column_index : column_index + mer_length]
                    for row in sequences[1:]
                ),
            ]
        )
        if motifs.score() < best_motifs.score():
            best_motifs = motifs

    return best_motifs
