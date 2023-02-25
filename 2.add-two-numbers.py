#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        d = ListNode(0)
        result = d
        carry = 0

        while l1 or l2 or carry:
            l1val = (l1.val if l1 else 0)
            l2val = (l2.val if l2 else 0)
            value = (l1val + l2val + carry)%10
            carry = (1 if l1val+l2val+carry>=10 else 0)
            d.next = ListNode(value)
            d = d.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        print(result.next)
        return result.next

# @lc code=end

