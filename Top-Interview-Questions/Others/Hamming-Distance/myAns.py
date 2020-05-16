class Solution:
	def hammingDistance(self, x: int, y: int) -> int:
		xStr = str(bin(x))
		yStr = str(bin(y))
		# Remove '0b'
		xStr = xStr[2:]
		yStr = yStr[2:]
		numZeros = abs(len(xStr) - len(yStr))
		if len(xStr) < len(yStr):
			xStr = '0' * numZeros + xStr
		else:
			yStr = '0' * numZeros + yStr

		count = 0
		for i in range(len(xStr)):
			if xStr[i] != yStr[i]:
				count += 1
		return count