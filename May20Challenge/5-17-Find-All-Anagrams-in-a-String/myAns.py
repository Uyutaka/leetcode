class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:

		output = []
		element = list(p)
		element.sort()
		for i in range(len(s) - len(p) + 1):
			# element = list(p)
			target = list(s[i:i + len(p)])
			target.sort()
			if target == element:
				output.append(i)

		return output