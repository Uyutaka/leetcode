import math


class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		sr = math.sqrt(num)
		return ((sr - math.floor(sr)) == 0)
