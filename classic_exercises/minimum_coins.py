from typing import List


class MinimumCoinsforPrice:
    def __init__(self, coin_types: List[int]) -> None:
        self._coin_types: List[int] = coin_types
        self._memo: dict[int, int] = {0: 0}

    def _min_ignore_none(self, a, b) -> int:
        if a is None:
            return b
        if b is None:
            return a
        return min(a, b)

    def calculate(self, price: int) -> int:
        for i in range(1, price + 1):
            for coin in self._coin_types:
                number_of_coins: int = i - coin

                if number_of_coins < 0:
                    continue  # We can't use this coin

                self._memo[i] = self._min_ignore_none(
                    self._memo.get(i),
                    (lambda x: x + 1 if x is not None else None)(
                        self._memo.get(number_of_coins)
                    ),
                )

        return self._memo[price]
