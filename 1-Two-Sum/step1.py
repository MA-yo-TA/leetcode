from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_indices: Dict[int, List[int]] = {}
        for index in range(len(nums)):
            num = nums[index]
            if num in num_to_indices:
                num_to_indices[num].append(index)
            else:
                num_to_indices[num] = [index]

        for index in range(len(nums)):
            num = nums[index]
            pair_indices = num_to_indices.get(target - num)
            if pair_indices is None:
                continue
            pair_indices = [
                pair_index for pair_index in pair_indices if pair_index != index
            ]
            if not pair_indices:
                continue
            return [index, pair_indices[0]]
