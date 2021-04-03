class Solution:
    def isPrefixOfWord(self, s: str, w: str) -> int:
        l = s.split()
        for i in l:
            if len(i) >= len(w) and i[0:len(w)] == w:
                    return l.index(i)+1
        return -1