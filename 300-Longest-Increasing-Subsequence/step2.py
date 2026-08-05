class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis_length_ending_at = [1 for i in range(len(nums))]

        def max_extendable_lis_length_before(index: int) -> int:
            max_length = 0
            for i in range(index):
                if nums[i] < nums[index]:
                    max_length = max(max_length, lis_length_ending_at[i])

            return max_length

        for i in range(len(nums)):
            lis_length_ending_at[i] = max_extendable_lis_length_before(i) + 1

        return max(lis_length_ending_at)
