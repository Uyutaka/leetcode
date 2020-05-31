class Solution:
	def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
		distList = []
		for i in range(len(points)):
			dist = points[i][0] ** 2 + points[i][1] ** 2
			distList.append([dist, i])
		distList.sort()
		output = []
		for i in range(K):
			output.append(points[distList[i][1]])
		return output
