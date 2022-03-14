from math import floor
from .coin_set import CoinSet


def greedy(change: int, coins: CoinSet):
    for face_value in coins:
        no_coin_of_type = floor(change / face_value)
        coins.push(no_coin_of_type)
        change = change - face_value * no_coin_of_type
    return coins


def exhausting(change: int, coins: CoinSet):
    max_no_of_coins = floor(change / coins.min())
    best = max_no_of_coins
    for i in range(max_no_of_coins):
        for coin_set in coins.combination(i):
            if coin_set.coin_value() == change:
                if best > coin_set.coin_count():
                    best = coin_set.coin_count()
    return best
