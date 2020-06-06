class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		if len(nums) == 0:
			return 0
		dp = [0] * len(nums)
		dp[0] = 1

		for i in range(1, len(nums)):
			maxV = 0
			for j in range(i):
				if nums[j] < nums[i]:
					maxV = max(dp[j], maxV)
			dp[i] = maxV + 1
		return max(dp)