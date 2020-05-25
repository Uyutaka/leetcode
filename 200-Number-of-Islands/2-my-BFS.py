class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		nRow = len(grid)
		if nRow == 0:
			return 0
		nCol = len(grid[0])

		numIslands = 0
		for r in range(nRow):
			for c in range(nCol):
				if grid[r][c] == '1':
					numIslands += 1
					self.convert2Zero(grid, r, c)
		return numIslands

	def convert2Zero(self, grid, row, col):
		nRow = len(grid)
		nCol = len(grid[0])

		stack = [[row, col]]

		while stack:
			r, c = stack.pop()
			if r + 1 < nRow and grid[r + 1][c] == '1':
				stack.append([r + 1, c])
			if c + 1 < nCol and grid[r][c + 1] == '1':
				stack.append([r, c + 1])
			if 0 <= c - 1 and grid[r][c - 1] == '1':
				stack.append([r, c - 1])
			if 0 <= r - 1 and grid[r - 1][c] == '1':
				stack.append([r - 1, c])
			grid[r][c] = '0'