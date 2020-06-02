class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:

		engList = []

		for i in range(len(words)):
			eng = ''
			for c in words[i]:
				eng += chr(97 + order.index(c))
			engList.append(eng)

		originList = []
		originList[:] = engList

		engList.sort()

		return originList == engList
