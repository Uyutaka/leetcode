class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		if len(prices) < 2:
			return 0

		minP = max(prices)
		maxProfit = 0
		for i in range(len(prices)):
			if prices[i] < minP:
				minP = prices[i]
			elif prices[i] - minP > maxProfit:
				maxProfit = prices[i] - minP
		return maxProfit