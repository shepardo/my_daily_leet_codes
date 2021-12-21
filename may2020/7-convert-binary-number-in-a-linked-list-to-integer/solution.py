# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        node = head
        while node is not None:
            result = result * 2
            result = result + node.val
            node = node.next
        return result
        
# from https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Input: [1, 0, 1]
# Output: 5
# Expected: 5

