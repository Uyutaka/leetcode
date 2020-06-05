import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        paragraph = paragraph.lower()
        print(paragraph)
        words = list(paragraph.split())
        wordCounter = collections.Counter(words)
        for val, freq in wordCounter.most_common():
            if not val in banned:
                return val
