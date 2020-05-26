class Solution:
	def findJudge(self, N: int, trust: List[List[int]]) -> int:

		judge = [[False for i in range(N)] for j in range(N)]
		for i in range(len(trust)):
			judge[trust[i][0] - 1][trust[i][1] - 1] = True

		candidates = []
		for row in range(N):
			if judge[row].count(False) == N:
				candidates.append(row)
				judge[row][row] = True

		for c in candidates:
			cols = [judge[i][c] for i in range(N)]

			if cols.count(True) == N:
				return c + 1
		return -1