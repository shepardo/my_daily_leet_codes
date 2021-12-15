# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt_acc = 0
        if root is None:
            return 0
        left_tilt = self.doFindTilt(root.left) if root.left is not None else 0
        right_tilt = self.doFindTilt(root.right) if root.right is not None else 0
        self.tilt_acc += abs(right_tilt - left_tilt)
        return self.tilt_acc 

    # [3, 3, 1, 1, 7, 2, 2, 14, 21]

    def doFindTilt(self, node: TreeNode) -> int:
        if node is None:
            return 0
        else:
            if node.left is None and node.right is None:
                return node.val
            else:
                tuple_left = self.doFindTilt(node.left) if node.left is not None else 0
                tuple_right = self.doFindTilt(node.right) if node.right is not None else 0
                self.tilt_acc += abs(tuple_left - tuple_right)
                return tuple_left + tuple_right + node.val

# https://leetcode.com/problems/binary-tree-tilt/
#         