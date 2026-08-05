from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        smallest_end_for_lengths = []
        for i in range(len(nums)):
            length_to_update = bisect_left(smallest_end_for_lengths, nums[i])
            if length_to_update == len(smallest_end_for_lengths):
                smallest_end_for_lengths.append(nums[i])
            else:
                smallest_end_for_lengths[length_to_update] = nums[i]

        return len(smallest_end_for_lengths)
