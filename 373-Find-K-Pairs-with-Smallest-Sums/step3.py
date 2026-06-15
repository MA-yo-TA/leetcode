from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        candidates = []
        for index1 in range(min(len(nums1), k)):
            heapq.heappush(candidates, (nums1[index1] + nums2[0], index1, 0))

        k_smallest_pairs = []
        while len(k_smallest_pairs) < k:
            _, index1, index2 = heapq.heappop(candidates)
            k_smallest_pairs.append([nums1[index1], nums2[index2]])

            index2 += 1
            if index2 < len(nums2):
                heapq.heappush(
                    candidates, (nums1[index1] + nums2[index2], index1, index2)
                )

        return k_smallest_pairs
