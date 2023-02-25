#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = list(s)
        result = 0
        for i in range(len(arr)):
            check = []
            start = i
            end = i
            while arr[end] not in check:
                if end == len(arr)-1:
                    check.append(arr[end])
                    break
                check.append(arr[end])
                end = end + 1
                #print(check, marker)
            result = max(result,len(check))
        return result

# @lc code=end

