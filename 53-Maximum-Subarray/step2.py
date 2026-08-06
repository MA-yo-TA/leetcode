class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not nums:
            return 0

        prefix_sum = []
        sum_so_far = 0
        for num in nums:
            sum_so_far += num
            prefix_sum.append(sum_so_far)

        min_prefix_sum_so_far = 0
        max_subarray_sum = float("-inf")
        for i in range(len(prefix_sum)):
            if prefix_sum[i] - min_prefix_sum_so_far > max_subarray_sum:
                max_subarray_sum = prefix_sum[i] - min_prefix_sum_so_far

            if prefix_sum[i] < min_prefix_sum_so_far:
                min_prefix_sum_so_far = prefix_sum[i]

        return max_subarray_sum
