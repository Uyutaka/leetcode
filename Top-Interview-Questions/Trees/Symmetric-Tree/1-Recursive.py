# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        def helper(leftNode, rightNode):
            if leftNode == None and rightNode == None:
                return True
            if leftNode == None or rightNode == None:
                return False
            return leftNode.val == rightNode.val \
                   and helper(leftNode.left, rightNode.right) \
                   and helper(leftNode.right, rightNode.left)
        return helper(root.left, root.right)