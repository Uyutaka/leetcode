class Solution:
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		left = 1
		right = n

		while left < right:
			mid = int((left + right) / 2)

			if isBadVersion(mid):
				right = mid

			else:
				left = mid + 1

		return left