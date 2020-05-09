class Solution:
	def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
		if len(coordinates) <= 2:
			return True

		# Remove duplicate elements
		coordinates = list(map(list, set(map(tuple, coordinates))))

		# Sort by x values
		coordinates = sorted(coordinates, key=lambda x: x[0])

		# Check if x constantly increases
		print(coordinates)
		for i in range(1, len(coordinates)):
			if coordinates[i][0] - coordinates[i - 1][0] <= 0:
				return False
		# Check if y constantly increases or decreases

		if coordinates[1][1] - coordinates[0][1] < 0:
			isIncreasing = False
		else:
			isIncreasing = True

		for i in range(1, len(coordinates)):
			if isIncreasing and (coordinates[i][1] - coordinates[i - 1][1] < 0):
				return False
			if (not isIncreasing) and (coordinates[i][1] - coordinates[i - 1][1] > 0):
				return False

		# Check if y is contant
		y = [row[1] for row in coordinates]
		if len(list(set(y))) == 1:
			return True

		# Check slope
		slope = self.getSlope(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1])
		print(slope)
		for i in range(2, len(coordinates)):
			if self.getSlope(coordinates[i - 1][0], coordinates[i - 1][1], coordinates[i][0],
			                 coordinates[i][1]) != slope:
				return False
		return True

	def isIncreasingSlope(self, y1, y2):
		return True if y2 - y1 > 0 else False

	def getSlope(self, x1, y1, x2, y2) -> float:
		return (x2 - x1) / (y2 - y1)

