import copy

class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:

		# Check rows
		for i in range(9):
			row = copy.deepcopy(board[i])
			self.removeDot(row)
			if sorted(list(set(row))) != sorted(row):
				return False

		# Check cols
		for i in range(9):
			col = []
			for j in range(9):
				col.append(board[j][i])
			self.removeDot(col)
			if sorted(list(set(col))) != sorted(col):
				return False

		# Check blocks
		boxes = self.getBoxes(board)
		for i in range(9):
			removed = self.removeDot(boxes[i])
			if sorted(list(set(removed))) != sorted(removed):
				print("box")
				return False

		return True

	def removeDot(self, l):
		while "." in l:
			l.remove(".")
		return l

	def getBoxes(self, board):
		boxes = []
		for i in range(9):
			if i == 0 or i % 3 == 0:
				box_set_1 = board[i][:3] + board[i + 1][:3] + board[i + 2][:3]
				boxes.append(box_set_1)
				box_set_2 = board[i][3:6] + board[i + 1][3:6] + board[i + 2][3:6]
				boxes.append(box_set_2)
				box_set_3 = board[i][6:] + board[i + 1][6:] + board[i + 2][6:]
				boxes.append(box_set_3)
		return boxes