class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev_from_begin = nums[0]
        current_from_begin = max(nums[0], nums[1])

        prev_without_begin = 0
        current_without_begin = nums[1]

        for i in range(2, len(nums)):
            next_from_begin = max(
                prev_from_begin + nums[i],
                current_from_begin,
            )
            prev_from_begin = current_from_begin
            current_from_begin = next_from_begin

            next_without_begin = max(
                prev_without_begin + nums[i],
                current_without_begin,
            )
            prev_without_begin = current_without_begin
            current_without_begin = next_without_begin

        return max(current_without_begin, prev_from_begin)
