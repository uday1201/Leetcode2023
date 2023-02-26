#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        numstr = str(num)
        while len(numstr) > 1:
            sum = 0
            for i in range(len(numstr)):
                sum += int(numstr[i])
            numstr = str(sum)
        return int(numstr)
        
# @lc code=end

