class Solution:
	def hammingWeight(self, n: int) -> int:
		strBit = str(bin(n))
		count = 0
		for b in strBit:
			if b == '1':
				count += 1
		return count