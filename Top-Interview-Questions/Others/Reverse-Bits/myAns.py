class Solution:
	def reverseBits(self, n: int) -> int:
		# Convert to list
		bitList = list("{0:{fill}32b}".format(n, fill='0'))
		# Reverse
		bitList.reverse()
		# Joint and convert it to decimal
		return int(''.join(bitList), 2)

		print(bitList)