#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        """ TLE
        substring = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and len(substring)<(j-i+1):
                    substring = s[i:j+1]
                else: 
                    pass
        return substring
    """
        substring = ''

        for i in range(len(s)):
            # odd len
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)> len(substring):
                    substring = s[l:r+1]
                l -=1
                r +=1
            # even len 
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)> len(substring):
                    substring = s[l:r+1]
                l -=1
                r +=1
        return substring


# @lc code=end

