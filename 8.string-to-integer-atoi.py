#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        num = ''
        digits = ['0','1','2','3','4','5','6','7','8','9']
        sign = 1
        i = 0
        while i<len(s):
            if s[i] == " ":
                i +=1
            else:
                break
        if i<len(s):
            if s[i] == "-":
                sign = -1
                i+=1
            elif s[i] == "+":
                i+=1
        while i<len(s):
            if s[i] in digits:
                num += s[i]
                i +=1
            else:
                break
        
        if len(num)>0:
            numeric = sign*int(num)
            if numeric<-2**31:
                return -2**31
            elif numeric>(2**31-1):
                return 2**31-1
            else:
                return numeric
        else:
            return 0


        
# @lc code=end

