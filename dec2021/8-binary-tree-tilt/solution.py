# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        right = self.doFindTilt(0, root.right)
        left = self.doFindTilt(0, root.left)
        q = []
        q.append(1)
        q.pop(0)
        return right - left
    
    def travel(self, node):
        self.travel(node.left)
        self.travel(node.right)
        q.append(node.val)
        # [3, 3, 1, 1, 7, 2, 2, 14, 21] 
    
    def doFindTilt(self, result, node: TreeNode) -> int:
        if node is None:
            return result
        else:
            result += self.doFindTilt(result + node.val, node.left)
            result += self.doFindTilt(result, node.right)
            return result


# https://leetcode.com/problems/binary-tree-tilt/
#         