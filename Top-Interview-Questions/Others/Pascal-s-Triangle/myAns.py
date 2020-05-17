class Solution:
	def generate(self, numRows: int) -> List[List[int]]:
		if numRows == 0:
			return []
		output = [[1]]

		for i in range(1, numRows):
			prevRow = output[i - 1]
			row = [1]
			for j in range(1, i):
				row.append(prevRow[j - 1] + prevRow[j])
			row.append(1)
			output.append(row)
		return output