from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.descending_nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        expanded_nums = [float("inf")] + self.descending_nums + [float("-inf")]
        interval_head = 0
        interval_tail = len(expanded_nums) - 1
        interval_center = (interval_tail + interval_head) // 2
        while interval_head != interval_tail:
            if val >= expanded_nums[interval_center]:
                interval_tail = interval_center
                interval_center = (interval_tail + interval_head) // 2
            else:
                interval_head = interval_center + 1
                interval_center = (interval_tail + interval_head) // 2

        self.descending_nums.insert(interval_head - 1, val)

        return self.descending_nums[self.k - 1]
