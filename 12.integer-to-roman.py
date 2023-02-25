#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
import math
# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        while num/1000 >= 1:
            roman += 'M'*math.floor(num/1000)
            num = num%1000
        while num/500 >= 1:
            if num/900 >=1:
                roman += 'CM'*math.floor(num/900)
                num = num%900
            else:
                roman += 'D'*math.floor(num/500)
                num = num%500
        while num/100 >= 1:
            if num/400 >=1:
                roman += 'CD'*math.floor(num/400)
                num = num%400
            else:
                roman += 'C'*math.floor(num/100)
                num = num%100
        while num/50 >= 1:
            if num/90 >=1:
                roman += 'XC'*math.floor(num/90)
                num = num%90
            else:
                roman += 'L'*math.floor(num/50)
                num = num%50
        while num/10 >= 1:
            if num/40 >=1:
                roman += 'XL'*math.floor(num/40)
                num = num%40
            else:
                roman += 'X'*math.floor(num/10)
                num = num%10
        while num/5 >= 1:
            if num/9 >=1:
                roman += 'IX'*math.floor(num/9)
                num = num%9
            else:
                roman += 'V'*math.floor(num/5)
                num = num%5
        while num >= 1:
            if num/4 >=1:
                roman += 'IV'*math.floor(num/4)
                num = num%4
            else:
                roman += 'I'*math.floor(num)
                num = -1
        return roman
# @lc code=end

