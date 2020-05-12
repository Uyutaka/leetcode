class Solution:
	def isPalindrome(self, s: str) -> bool:
		s = s.lower()
		alnumStr = ""
		for ch in s:
			if ch.isalnum():
				alnumStr += ch

		for i in range(int(len(alnumStr) / 2)):
			if alnumStr[i] != alnumStr[len(alnumStr) - i - 1]:
				return False
		return True


