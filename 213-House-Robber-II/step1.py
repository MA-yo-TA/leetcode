class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        max_monies_from_begin = [nums[0], max(nums[0], nums[1])]
        max_monies_without_begin = [0, nums[1]]
        for i in range(2, len(nums)):
            max_monies_from_begin.append(
                max(
                    max_monies_from_begin[-1],
                    max_monies_from_begin[-2] + nums[i],
                )
            )
            max_monies_without_begin.append(
                max(
                    max_monies_without_begin[-1],
                    max_monies_without_begin[-2] + nums[i],
                )
            )

        return max(max_monies_from_begin[-2], max_monies_without_begin[-1])
