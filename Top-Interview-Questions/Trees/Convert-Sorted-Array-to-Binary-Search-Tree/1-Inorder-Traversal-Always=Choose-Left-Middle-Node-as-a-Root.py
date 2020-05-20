# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
		def helper(left, right):
			if left > right:
				return None

			i = (left + right) // 2
			root = TreeNode(nums[i])
			root.left = helper(left, i - 1)
			root.right = helper(i + 1, right)
			return root

		return helper(0, len(nums) - 1)