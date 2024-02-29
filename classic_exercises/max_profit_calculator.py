from typing import List


class MaxProfitCalculator:
    def __init__(self, prices: List[int]) -> None:
        self._prices = prices

    def calculate(self) -> int:
        l: int = 0  # Day to buy
        r: int = 0  # Day to sell
        maxp: int = 0  # Max profit

        while r < len(self._prices):
            # Is this profitable transaction?
            if self._prices[l] < self._prices[r]:
                profit: int = self._prices[r] - self._prices[l]
                maxp = max(maxp, profit)
            else:
                l = r

            r += 1

        return maxp
