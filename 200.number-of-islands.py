#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        numberofislands = 0
        if rows == 0:
            return 0
        cols = len(grid[0])

        def markit(grid,r,c,rows,cols):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c] != '1':
                return
            grid[r][c] = '-1'
            directions = [[0,1],[1,0],[0,-1],[-1,0]]
            for dir in directions:
                markit(grid, r+dir[0], c+dir[1], rows, cols)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    markit(grid,r,c,rows,cols)
                    numberofislands += 1

        return numberofislands
# @lc code=end

