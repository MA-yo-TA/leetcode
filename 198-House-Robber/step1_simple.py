class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_moneies = [0] * len(nums)
        max_moneies[0] = nums[0]
        max_moneies[1] = nums[1]
        for i in range(2, len(nums)):
            max_moneies[i] = max(max_moneies[: i - 1]) + nums[i]

        return max(max_moneies)
