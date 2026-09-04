class Solution:
    def rob(self, nums: list[int]) -> int:
        def calculate_max_money(begin: int, end: int) -> int:
            prev_max = 0
            current_max = 0

            for i in range(begin, end):
                next_max = max(prev_max + nums[i], current_max)
                prev_max = current_max
                current_max = next_max

            return current_max

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(
            calculate_max_money(0, len(nums) - 1),
            calculate_max_money(1, len(nums)),
        )
