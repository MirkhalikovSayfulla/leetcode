class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        return len(Counter(map(int, re.sub('[a-z]+', ' ', word).split())))