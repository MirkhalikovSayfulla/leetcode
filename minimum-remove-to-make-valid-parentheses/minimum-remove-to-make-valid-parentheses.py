class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        a = []
        for i, x in enumerate(s):
            if x not in '()':
                continue
            if a and x == ')' and a[-1][0] == '(':
                a.pop()
            else:
                a.append((x, i))
                
        ans = ''
        now = 0
        for i in range(len(s)):
            if now < len(a) and a[now][1] == i:
                now += 1
            else:
                ans += s[i]
                
        return ans