class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        stack = [[], []]
        latest = int(s[0])
        stack[latest].append(latest)
        result = 0
        for i in range(1,len(s)):
            v = int(s[i])
            if v != latest:
                stack[v].clear()
                latest = v
            stack[v].append(v)
            if len(stack[1-v]) > 0:
                stack[1-v].pop()
                result += 1
        return result