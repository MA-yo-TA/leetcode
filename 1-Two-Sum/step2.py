class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            pair_index = num_to_index.get(target - num)
            if pair_index is None:
                num_to_index[num] = index
                continue
            return [index, pair_index]
