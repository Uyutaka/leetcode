class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if (not grid) or (len(grid) == 0):
			return 0

		nr = len(grid)
		nc = len(grid[0])
		numOfIslands = 0

		for r in range(nr):
			for c in range(nc):
				if grid[r][c] == '1':
					numOfIslands += 1
					self.dfs(grid, r, c)
		return numOfIslands

	def dfs(self, grid: List[List[str]], r: int, c: int):
		nr = len(grid)
		nc = len(grid[0])
		if r < 0 or c < 0 or nr <= r or nc <= c or grid[r][c] == '0':
			return
		print(r, c)

		grid[r][c] = '0'
		self.dfs(grid, r - 1, c)
		self.dfs(grid, r + 1, c)
		self.dfs(grid, r, c - 1)
		self.dfs(grid, r, c + 1)