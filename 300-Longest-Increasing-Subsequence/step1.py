class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        length_from_begin = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    length_from_begin[i] = max(
                        length_from_begin[i], length_from_begin[j] + 1
                    )

        return max(length_from_begin)
