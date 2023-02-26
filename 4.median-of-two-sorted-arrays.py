#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
import math
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        median = 0.0
        if len(nums)%2 == 0:
            median = (nums[int(len(nums)/2-1)] + nums[int(len(nums)/2)])/2
        else:
            median = nums[math.floor(len(nums)/2)]
        return median
# @lc code=end

