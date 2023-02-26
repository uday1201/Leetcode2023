#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) > 1:
            comp = nums[0]
        else:
            return nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == comp:
                count +=1
            else:
                comp = nums[i]
            if count > len(nums)/2:
                return comp
# @lc code=end

