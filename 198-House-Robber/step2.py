class Solution:
    def rob(self, nums: list[int]) -> int:
        prevprev_max = 0
        prev_max = 0
        current_max = 0
        for i in range(len(nums)):
            current_max = max(prevprev_max + nums[i], prev_max)
            prevprev_max = prev_max
            prev_max = current_max

        return current_max
