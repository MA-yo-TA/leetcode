class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        prevs = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, len(nums)):
            curr = max(prevs[0] + nums[i], prevs[1] + nums[i], prevs[2])
            prevs = [prevs[1], prevs[2], curr]

        return max(prevs)
