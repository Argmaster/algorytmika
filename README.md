# algorithms

Implementations of motif search algorithms. Described in

```
Bioinformatics Algorithms:
An Active Learning Approach
2nd Edition, Vol. I

by
Phillip Compeau & Pavel Pevzner
```

-   Exhaustive search algorithm is available in `algorithms.exhaustive `submodule
-   Median search algorithm is available in `algorithms.median` submodule
-   Greedy search algorithm is available in `algorithms.greedy` submodule
-   Randomized search algorithm is available in `algorithms.randomized `submodule

All tests, including benchmarks are contained in `tests/` directory.

# Benchmarks

All benchmarks used same input settings (if possible), they were run on sample data (`tests/data/sample.txt`) with 8-mers and max distance 3, in randomized search 1000 samples were used.
Limited sample size was used to keep runtimes reasonable.

-   Running exhaustive algorithm takes on average 8.4 seconds
-   Running median algorithm takes on average 17.1 seconds
-   Running greedy algorithm takes on average 0.0008 seconds
-   Running randomized algorithm takes on average 8.4 seconds
