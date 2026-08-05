from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        smallest_end_for_lis_lentgh: list[int] = []
        for i in range(len(nums)):
            length_to_update = bisect_left(smallest_end_for_lis_lentgh, nums[i])
            if length_to_update == len(smallest_end_for_lis_lentgh):
                smallest_end_for_lis_lentgh.append(nums[i])
            else:
                smallest_end_for_lis_lentgh[length_to_update] = nums[i]

        return len(smallest_end_for_lis_lentgh)
