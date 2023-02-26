#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
import itertools
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        result = 1 # all are ones
        arr = [1 for i in range(n)]
        while (1 in arr) and len(arr)>1:
            arr = arr[2:]
            arr.append(2)
            if sum(arr) == n:
                print(arr)
                c = list(itertools.permutations(arr, len(arr)))
                print(c)
                result += len(set(c))
        return result
        """
        onestep = 1
        twostep = 1
        result = 1
        for i in range(n-1):
            result = onestep + twostep
            twostep = onestep
            onestep = result
        return result

# @lc code=end

