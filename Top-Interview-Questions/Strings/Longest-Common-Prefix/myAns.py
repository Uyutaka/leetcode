class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		prefix = ""

		if len(strs) == 0:
			return prefix

		# Check maximum len of prefix
		sizeList = []
		for s in strs:
			sizeList.append(len(s))
		maxPrefixSize = min(sizeList)

		for i in range(maxPrefixSize):
			prefix += strs[0][i]
			for s in strs:
				if s[i] != prefix[i]:
					return prefix[:-1]
		return prefix        