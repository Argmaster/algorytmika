from timeit import timeit
from source.lab1.change import CoinSet, exhausting, greedy


COIN_SET = CoinSet(25, 20, 10, 5, 1)
COIN_SET_PL = CoinSet(100, 50, 20, 10, 5, 2, 1)


def test_greedy_40x10():
    print(timeit("greedy(40, COIN_SET)", globals=globals(), number=10))


def test_greedy_pl_40x10():
    print(timeit("greedy(40, COIN_SET)", globals=globals(), number=10))


def test_exhausting_40x10():
    print(timeit("exhausting(40, COIN_SET)", globals=globals(), number=10))


def test_exhausting_pl_40x10():
    print(timeit("exhausting(40, COIN_SET)", globals=globals(), number=10))


# Bigger change


def test_greedy_797x10():
    print(timeit("greedy(40, COIN_SET)", globals=globals(), number=10))


def test_greedy_pl_797x10():
    print(timeit("greedy(40, COIN_SET)", globals=globals(), number=10))


def test_exhausting_797x10():
    print(timeit("exhausting(40, COIN_SET)", globals=globals(), number=10))


def test_exhausting_pl_797x10():
    print(timeit("exhausting(40, COIN_SET)", globals=globals(), number=10))
