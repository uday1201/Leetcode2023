#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
import math
# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        targetsum = -math.inf
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            newtarget = target - nums[i]
            newtargetsum = -math.inf
            while l<r:
                sum = nums[l]+nums[r]
                if abs(sum-newtarget)<abs(newtargetsum-newtarget):
                    newtargetsum = sum
                if newtarget < sum:
                    r -=1
                elif newtarget > sum:
                    l +=1
                else:
                    return target
                
            if abs(newtargetsum + nums[i] -target)<abs(targetsum-target):
                targetsum = newtargetsum + nums[i]
        return targetsum

                
        
# @lc code=end

