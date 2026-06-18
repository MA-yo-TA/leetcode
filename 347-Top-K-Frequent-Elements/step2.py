from typing import Dict, List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_counter: Dict[int, List[int]] = {}
        for num in nums:
            if frequency_counter.get(num) is None:
                frequency_counter[num] = [1, num]
            else:
                frequency_counter[num][0] += 1

        frequency_counts = list(frequency_counter.values())
        heapq.heapify_max(frequency_counts)
        k_most_frequent_elements = []
        while len(k_most_frequent_elements) < k:
            k_most_frequent_elements.append(heapq.heappop_max(frequency_counts)[1])

        return k_most_frequent_elements
