class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        prefix_sum = []
        sum_so_far = 0
        for num in nums:
            sum_so_far += num
            prefix_sum.append(sum_so_far)

        max_subaray_sum = -float("inf")
        min_prefix_sum_so_far = 0
        for i in range(len(prefix_sum)):
            max_subaray_sum = max(
                prefix_sum[i] - min_prefix_sum_so_far,
                max_subaray_sum,
            )
            min_prefix_sum_so_far = min(
                prefix_sum[i],
                min_prefix_sum_so_far,
            )

        return max_subaray_sum
