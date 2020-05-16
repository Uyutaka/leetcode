class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		zeros = []
		count = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				zeros.append(i + count)
				count -= 1
		for i in range(len(zeros)):
			nums[:] = nums[:zeros[i]] + nums[zeros[i] + 1:] + [0]