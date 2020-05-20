# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		levels = []

		def helper(node, level):
			if node:

				if len(levels) == level:
					print(len(levels), level, node.val)

					levels.append([])
					print('if')

				else:
					print('else')
					# print(level)
					print(len(levels), level, node.val)

				levels[level].append(node.val)
				# print(level, node.val)

				helper(node.left, level + 1)
				helper(node.right, level + 1)

		level = 0
		helper(root, level)
		return levels