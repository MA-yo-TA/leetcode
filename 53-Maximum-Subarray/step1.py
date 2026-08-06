class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        length_to_prefix_sum = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            length_to_prefix_sum.append(prefix_sum)

        min_prefix_sum_so_far = 0
        max_subarray_sum = float("-inf")
        for prefix_sum in length_to_prefix_sum:
            if prefix_sum - min_prefix_sum_so_far > max_subarray_sum:
                max_subarray_sum = prefix_sum - min_prefix_sum_so_far

            if prefix_sum < min_prefix_sum_so_far:
                min_prefix_sum_so_far = prefix_sum

        return max_subarray_sum
