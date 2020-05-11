class Solution:
	def findJudge(self, N: int, trust: List[List[int]]) -> int:

		if len(trust) < N - 1:
			return -1

		outDegree = [0] * (N + 1)
		inDegree = [0] * (N + 1)

		for i, o in trust:
			inDegree[o] += 1
			outDegree[i] += 1

		for i in range(1, N + 1):
			if inDegree[i] == N - 1 and outDegree[i] == 0:
				return i
		return -1