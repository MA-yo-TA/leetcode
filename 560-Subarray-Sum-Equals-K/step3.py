from collections import defaultdict
from itertools import accumulate


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum_count = defaultdict(int, {0: 1})
        equals_k_count = 0
        for prefix_sum in accumulate(nums):
            equals_k_count += prefix_sum_count[prefix_sum - k]
            prefix_sum_count[prefix_sum] += 1

        return equals_k_count
