class Solution:
	def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
		nRooms = len(rooms)
		isVisited = [False] * nRooms
		isVisited[0] = True

		stack = [0]
		while stack:
			nextRoom = stack.pop()
			isVisited[nextRoom] = True
			for num in rooms[nextRoom]:
				if not isVisited[num]:
					stack.append(num)

		return all(isVisited)