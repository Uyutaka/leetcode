from collections import OrderedDict
class Solution:
	def firstUniqChar(self, s: str) -> int:

		hash = OrderedDict()
		for i in range(len(s)):
			if not s[i] in hash.keys():
				hash[s[i]] = 0
			else:
				hash[s[i]] += 1
		print(hash)

		for k, v in hash.items():
			if v == 0:
				return s.index(k)

		return -1