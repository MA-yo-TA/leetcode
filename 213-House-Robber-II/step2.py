class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prevprev_from_begin = nums[0]
        prev_from_begin = max(nums[0], nums[1])
        current_from_begin = 0

        prevprev_without_begin = 0
        prev_without_begin = nums[1]
        current_without_bein = 0

        for i in range(2, len(nums)):
            current_from_begin = max(
                prev_from_begin,
                prevprev_from_begin + nums[i],
            )
            prevprev_from_begin = prev_from_begin
            prev_from_begin = current_from_begin

            current_without_bein = max(
                prev_without_begin,
                prevprev_without_begin + nums[i],
            )
            prevprev_without_begin = prev_without_begin
            prev_without_begin = current_without_bein

        return max(prevprev_from_begin, current_without_bein)
