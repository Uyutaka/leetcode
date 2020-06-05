class Solution:
	def orangesRotting(self, grid: List[List[int]]) -> int:
		queue = []

		# Step 1 Built the initial set of rotten oranges
		freshOrg = 0
		ROWS, COLS = len(grid), len(grid[0])

		for r in range(ROWS):
			for c in range(COLS):
				if grid[r][c] == 2:
					queue.append([r, c])
				elif grid[r][c] == 1:
					freshOrg += 1

		# Mark the round / level, ticker
		queue.append([-1, -1])

		# Step 2 start the rotting process via BFS

		minutes = -1
		directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
		while queue:
			row, col = queue.pop(0)

			if row == -1:
				# finish one round
				minutes += 1
				if queue:
					queue.append([-1, -1])
			else:
				# this is a rotten orange, then it would contaminate its neighbors
				for d in directions:
					neighborRow, neighborCol = row + d[0], col + d[1]
					if ROWS > neighborRow >= 0 and COLS > neighborCol >= 0:
						if grid[neighborRow][neighborCol] == 1:
							grid[neighborRow][neighborCol] = 2
							freshOrg -= 1
							queue.append([neighborRow, neighborCol])
		return minutes if freshOrg == 0 else -1

