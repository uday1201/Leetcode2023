#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapd = {'2':['a','b','c'],
            '3' : ['d','e','f'],
            '4' : ['g','h','i'],
            '5' : ['j','k','l'],
            '6' : ['m','n','o'],
            '7' : ['p','q','r','s'],
            '8' : ['t','u','v'],
            '9' : ['w','x','y','z']}
        res = []
        if len(digits) > 0:
            res = mapd[digits[0]]
        else:
            return res
        print(res)
        for i in range(1,len(digits)):
            tempres = []
            for d in mapd[digits[i]]:
                [tempres.append(x+d) for x in res]
            res = tempres
        return res

        
# @lc code=end

