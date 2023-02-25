#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        amount = []
        closed = False
        for i in range(len(height)):
            for j in range(len(height)):
                amount.append(abs(min(height[i],height[j])*(j-i)))
        return max(amount)
        """
        l = 0
        r = len(height)-1
        area = 0
        while l<r:
            if area<min(height[l],height[r])*(r-l):
                area = min(height[l],height[r])*(r-l)
            if height[l]<=height[r]:
                l +=1
            elif height[r]<height[l]:
                r -=1
            else:
                break
        return area

        
# @lc code=end

