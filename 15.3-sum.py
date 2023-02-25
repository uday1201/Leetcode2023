#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        print(nums)
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            start = i+1
            end = len(nums)-1
            while start < end:
                sum = nums[start] + nums[end]
                if sum < target:
                    start = start + 1
                elif sum > target:
                    end = end - 1
                else:
                    result.append([nums[i],nums[start], nums[end]])
                    start = start + 1
                    while nums[start] == nums[start-1] and start < end:
                        start = start + 1
        return result
            

# @lc code=end

