from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.max_heap_nums = self.max_heapify(nums)

    def max_heapify_root(self, nums: List[int], parent: int, tail: int):
        while True:
            left_child = parent * 2 + 1
            right_child = (parent + 1) * 2
            largest = parent
            if left_child <= tail and nums[largest] < nums[left_child]:
                largest = left_child
            if right_child <= tail and nums[largest] < nums[right_child]:
                largest = right_child

            if largest != parent:
                nums[parent], nums[largest] = nums[largest], nums[parent]
                parent = largest
            else:
                return

    def max_heapify(self, nums: List[int]):

        tail = len(nums) - 1
        for parent in range(len(nums) // 2, -1, -1):
            self.max_heapify_root(nums, parent, tail)

        return nums

    def add(self, val: int) -> int:
        self.max_heap_nums = [val] + self.max_heap_nums
        self.max_heapify_root(self.max_heap_nums, 0, len(self.max_heap_nums) - 1)
        rest = self.max_heap_nums
        for _ in range(self.k):
            rest_largest = rest[0]
            rest = self.max_heapify(rest[1:])

        return rest_largest
