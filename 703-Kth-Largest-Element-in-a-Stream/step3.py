from typing import List
import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest_elements = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.k_largest_elements) < self.k:
            heapq.heappush(self.k_largest_elements, val)
        elif val > self.k_largest_elements[0]:
            heapq.heappushpop(self.k_largest_elements, val)
        return self.k_largest_elements[0]
