#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # digits[-1] = digits[-1] + 1
        # if digits[-1] == 10:
        #     if len(digits) == 1:
        #         digits = [1,0]
        #     else:
        #         digits[-1] = 0
        #         digits[-2] = digits[-2]+1
        # return digits

        # SECOND CODE
        digits[-1] = digits[-1] + 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i]>9:
                digits[i] = 0
                if i-1<0:
                    digits = [1] + digits
                else:
                    digits[i-1] = digits[i-1]+1
        return digits

        
# @lc code=end

