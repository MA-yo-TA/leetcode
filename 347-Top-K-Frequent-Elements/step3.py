from typing import Dict, List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter の value は [回数, 値]のリスト
        counter: Dict[int, List[int]] = {}
        for num in nums:
            if counter.get(num) is None:
                counter[num] = [1, num]
            else:
                counter[num][0] += 1

        count_and_num = list(counter.values())
        heapq.heapify_max(count_and_num)
        top_k = []
        while len(top_k) < k:
            top_k.append(heapq.heappop_max(count_and_num)[1])
        return top_k
