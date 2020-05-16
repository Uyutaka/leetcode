class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		strDigit = ''.join([str(digits[i]) for i in range(len(digits))])
		targetStr = str(int(strDigit) + 1)

		output = []
		for d in targetStr:
			output.append(int(d))
		return output