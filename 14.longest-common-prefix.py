#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        substring = ""
        for i in range(len(min(strs, key=len))):
            for x in strs:
                if x[i] != strs[0][i]:
                    return substring
            substring = substring + strs[0][i]
        return substring
        '''
        
        
# @lc code=end

