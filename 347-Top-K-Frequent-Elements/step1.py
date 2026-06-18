from functools import total_ordering
from typing import Dict, List
import heapq


@total_ordering
class Frequency:
    def __init__(self, value: int, count: int):
        self.value = value
        self.count = count

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.count == other.count

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.count < other.count

    def count_up(self):
        self.count += 1


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter: Dict[int, Frequency] = {}
        for num in nums:
            if frequency_counter.get(num) is None:
                frequency_counter[num] = Frequency(num, 1)
            else:
                frequency_counter[num].count_up()

        frequency_counts = list(frequency_counter.values())
        heapq.heapify_max(frequency_counts)
        k_most_frequent_elements = []
        while len(k_most_frequent_elements) < k:
            k_most_frequent_elements.append(heapq.heappop_max(frequency_counts).value)

        return k_most_frequent_elements
