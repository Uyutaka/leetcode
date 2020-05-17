class Solution:
	def isPowerOfThree(self, n: int) -> bool:
		if n <= 0:
			return False
		maxPower = 3 ** 19
		return maxPower % n == 0