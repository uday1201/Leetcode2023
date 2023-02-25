#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        for x in numbers:
            if target-x in numbers:
                if target == 2*x:
                    return [i+1 for i, z in enumerate(numbers) if z == x] 
                else:
                    return [numbers.index(x)+1, numbers.index(target-x)+1]
        '''
        start = 0
        end = len(numbers) - 1

        while (start <= end):
            sum = numbers[start] + numbers[end]
            if sum < target:
                start = start + 1
            elif sum > target:
                end = end - 1
            else:
                return [start+1, end+1]

        return []
# @lc code=end

