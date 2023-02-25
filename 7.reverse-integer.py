#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x[0] == "-":
            if abs(int(x[1:]))<=2**31 and abs(int(x[1:][::-1]))<=2**31:
                return int("-" + x[1:][::-1])
            else:
                return 0
        elif abs(int(x))<=(2**31-1) and abs(int(x[::-1]))<=(2**31-1):
            return int(x[::-1])
        else: 
            return 0
        
# @lc code=end

