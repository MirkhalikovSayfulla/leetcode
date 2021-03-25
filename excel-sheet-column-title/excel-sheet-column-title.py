class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        d = {}
        for i in range(26):
            d[i] = chr(ord("A") + i)
        
        while n > 0:
            n -= 1
            s = d[((n) % 26)] + s
            n //= 26
        return s