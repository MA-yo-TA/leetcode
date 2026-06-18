class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) < len(nums2):
            return list(set(nums1).intersection(nums2))
        else:
            return list(set(nums2).intersection(nums1))
