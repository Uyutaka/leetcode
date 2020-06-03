class Solution:
	def longestPalindrome(self, s: str) -> str:
		maxNum = 0
		output = ''
		for i in range(len(s)):
			subStr = ''
			for j in range(i, len(s)):
				subStr += s[j]
				if subStr == subStr[::-1] and maxNum < len(subStr):
					maxNum = len(subStr)
					output = subStr
		return output
