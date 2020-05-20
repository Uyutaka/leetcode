class Solution:
	def myAtoi(self, str: str) -> int:
		INT_MAX = 2 ** 31 - 1
		INT_MIN = -2 ** 31

		str = str.lstrip()
		if len(str) == 0:
			return 0

		isNegative = False
		i = 0
		if str[0] == '-':
			isNegative = True
			i = 1
		elif str[0] == '+':
			i = 1

		val = 0
		while i < len(str) and str[i].isdigit():
			val *= 10
			val += int(str[i])
			i += 1

		if isNegative:
			val = max(-val, INT_MIN)
		else:
			val = min(val, INT_MAX)
		return val