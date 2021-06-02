class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) == 1: 
            if s[0] == '?':
                return 'a'
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                for c in 'abc':
                    if i == 0 and s[i+1] != c:
                        s[i] = c
                        break
                    if i == len(s)-1 and s[i-1] != c: 
                        s[i] = c
                        break
                    if (i > 0 and i < len(s) - 1) and s[i-1] != c and s[i+1] != c: 
                        s[i] = c
                        break
        return ''.join(s)