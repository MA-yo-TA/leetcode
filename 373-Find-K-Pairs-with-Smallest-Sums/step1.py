from typing import List
import heapq


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        k_smallest_pairs = []
        next_smallest_candidates = []
        for i in range(min(k, len(nums1))):
            num1 = nums1[i]
            num2 = nums2[0]
            sum = num1 + num2
            heapq.heappush(next_smallest_candidates, (sum, (i, 0)))

        while len(k_smallest_pairs) < k:
            _, smallest_pair_index = heapq.heappop(next_smallest_candidates)
            k_smallest_pairs.append(
                [nums1[smallest_pair_index[0]], nums2[smallest_pair_index[1]]]
            )

            nums2_candidate_index = smallest_pair_index[1] + 1
            if nums2_candidate_index < len(nums2):
                candidate_sum = (
                    nums1[smallest_pair_index[0]] + nums2[nums2_candidate_index]
                )
                heapq.heappush(
                    next_smallest_candidates,
                    (candidate_sum, (smallest_pair_index[0], nums2_candidate_index)),
                )

        return k_smallest_pairs
