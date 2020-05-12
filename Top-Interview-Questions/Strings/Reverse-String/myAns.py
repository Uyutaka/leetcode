class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""

		for index, chr in enumerate(s):
			if index == int(len(s) / 2):
				return
			tmp = s[index]
			s[index] = s[len(s) - index - 1]
			s[len(s) - index - 1] = tmp