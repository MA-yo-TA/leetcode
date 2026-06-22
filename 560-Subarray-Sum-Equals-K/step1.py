from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cumulative_sum_to_tail = defaultdict(list)
        # 先頭から始まるサブアレイ自体も考慮するために和が0の空アレイを想定
        cumulative_sum_to_tail[0].append(-1)
        cumulative_sum = 0
        for i, num in enumerate(nums):
            cumulative_sum += num
            cumulative_sum_to_tail[cumulative_sum].append(i)

        num_sum_equals_k = 0
        for sum in cumulative_sum_to_tail:
            complement = sum - k
            if complement not in cumulative_sum_to_tail:
                continue
            for i in cumulative_sum_to_tail[sum]:
                for j in cumulative_sum_to_tail[complement]:
                    if i > j:
                        num_sum_equals_k += 1

        return num_sum_equals_k
