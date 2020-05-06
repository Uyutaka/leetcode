class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		if not grid or len(grid) == 0:
			return 0

		nr = len(grid)
		nc = len(grid[0])
		numOfIslands = 0

		for r in range(nr):
			for c in range(nc):
				if grid[r][c] == '1':
					numOfIslands += 1
					grid[r][c] = '0'
					neighbors = list()
					neighbors.append([r, c])

					while len(neighbors) != 0:
						row, col = neighbors.pop(0)
						# row = int(id / nc)
						# col = int(id % nc)

						print(row, col)

						if 0 <= row - 1 and grid[row - 1][col] == '1':
							neighbors.append([row-1, col])
							grid[row - 1][col] = '0'

						if row + 1 < nr and grid[row + 1][col] == '1':
							neighbors.append([row+1, col])
							grid[row + 1][col] = '0'

						if 0 <= col - 1 and grid[row][col - 1] == '1':
							neighbors.append([row, col-1])
							grid[row][col - 1] = '0'

						if col + 1 < nc and grid[row][col + 1] == '1':
							neighbors.append([row, col+1])
							grid[row][col + 1] = '0'
		return numOfIslands


