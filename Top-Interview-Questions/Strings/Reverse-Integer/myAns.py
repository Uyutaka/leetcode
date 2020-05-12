class Solution:
	def reverse(self, x: int) -> int:
		strX = str(x)
		reversedX = 0
		if '-' in strX:
			strX = strX[1:]
			reversedX = int('-' + strX[::-1])
		else:
			reversedX = int(strX[::-1])

		if reversedX < -2 ** 31 or 2 ** 31 - 1 < reversedX:
			return 0
		else:
			return reversedX

