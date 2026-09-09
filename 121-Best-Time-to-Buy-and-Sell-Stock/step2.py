import itertools
from operator import sub


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return max(
            map(
                sub,
                prices,
                itertools.accumulate(prices, min),
            )
        )
