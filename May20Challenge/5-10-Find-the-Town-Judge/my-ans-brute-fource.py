class Solution:
	def findJudge(self, N: int, trust: List[List[int]]) -> int:
		if len(trust) == 0 and N == 1:
			return 1

		if len(trust) < N - 1:
			return -1

		hash = dict()

		for s, d in trust:
			if not d in hash.keys():
				hash[d] = list()
			hash[d].append(s)

		print(hash)
		for k in hash.keys():
			print(len(hash[k]))
			if len(hash[k]) == N - 1:
				# return k
				for s, d in trust:
					if s == k:
						return -1
				return k
		return -1