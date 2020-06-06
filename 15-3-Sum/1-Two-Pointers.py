class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		def twoSum(nums, i, res):
			lo, hi = i + 1, len(nums) - 1
			while (lo < hi):
				sum = nums[i] + nums[lo] + nums[hi]
				if sum < 0 or (i + 1 < lo and nums[lo] == nums[lo - 1]):
					lo += 1
				elif 0 < sum or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
					hi -= 1
				else:
					res.append([nums[i], nums[lo], nums[hi]])
					lo += 1
					hi -= 1

		res = []
		nums.sort()
		for i in range(len(nums)):
			if nums[i] > 0:
				break
			if i == 0 or nums[i - 1] != nums[i]:
				twoSum(nums, i, res)

		return res