class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		nS1 = len(s1)
		nS2 = len(s2)

		keyMap = {}
		for i in range(nS1):
			if s1[i] in keyMap:
				keyMap[s1[i]] += 1
			else:
				keyMap[s1[i]] = 1

		s2Map = {}
		for i in range(nS2):
			if s2[i] in s2Map:
				s2Map[s2[i]] += 1
			else:
				s2Map[s2[i]] = 1

			if nS1 <= i:
				s2Map[s2[i - nS1]] -= 1
				if s2Map[s2[i - nS1]] == 0:
					del s2Map[s2[i - nS1]]

			if keyMap == s2Map:
				return True

		return False