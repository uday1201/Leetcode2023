#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
import math
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        if numRows == 1:
            return s
        n = len(s)
        sections = math.ceil(n / (2 * numRows - 2.0))
        num_cols = sections * (numRows - 1)
        mat = [['' for c in range(num_cols)] for r in range(numRows)]
        down = True
        row = 0
        col = 0
        for i in range(len(s)):
            if down:
                mat[row][col] = s[i]
                if (row+1)==numRows:
                    if row>0:
                        down = False
                        row -=1
                    col +=1
                else:
                    row +=1
            else:
                mat[row][col] = s[i]
                if (row)==0:
                    down = True
                    if numRows>row+1:
                        row +=1
                else:
                    row -=1
                    col +=1
        result = ''
        for r in mat:
            result = result + ''.join(r)
            
        return result
        """
        if numRows==1:
            return s
        result = ''
        for r in range(numRows):
            step = 2*(numRows-1)
            for i in range(r, len(s),step):
                result += s[i]
                if r>0 and r<numRows-1 and (i+step-2*r)<len(s):
                    result += s[i+step-2*r]
        return result

# @lc code=end

