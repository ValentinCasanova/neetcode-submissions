import math
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted([*nums1, *nums2])
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) % 2 == 0:
            half = int(len(nums) / 2)
            return (nums[half] + nums[half - 1]) / 2
        return nums[math.floor(len(nums) / 2)]
        