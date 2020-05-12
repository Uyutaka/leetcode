class Solution:
	def climbStairs(self, n: int) -> int:
		count = n - 2
		fibo = [1, 2]

		prevprev = 0
		prev = 1

		for i in range(count):
			fibo.append(fibo[prevprev] + fibo[prev])
			prevprev += 1
			prev += 1

		print(fibo)
		return fibo[n - 1]