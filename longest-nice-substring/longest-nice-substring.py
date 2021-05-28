class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = ""
        for j in range(len(s)):
            for i in range(j):
                t = s[i : j+1]
                if set(t) == set(t.swapcase()):
                    ans = max(ans, t, key=len)
        return ans 