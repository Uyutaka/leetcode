class Solution:
	def rob(self, nums: List[int]) -> int:
		prevMax = 0
		currMax = 0

		for val in nums:
			tmp = currMax
			currMax = max(prevMax + val, currMax)
			prevMax = tmp
		return currMax