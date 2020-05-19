class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		# https://qiita.com/76b26e64/items/2f9ec0f32ebb4508dc2e

		dp = [0] * len(nums)
		dp[0] = nums[0]
		for i in range(1, len(nums)):
			dp[i] = max(nums[i], dp[i - 1] + nums[i])
		return max(dp)