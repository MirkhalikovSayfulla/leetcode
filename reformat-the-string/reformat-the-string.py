class Solution:
    def reformat(self, s: str) -> str:
        a = [c for c in s if c.isalpha()]
        b = [c for c in s if c.isdigit()]
        if len(a) < len(b): a, b = b, a
        if len(a) - len(b) > 1: return ""
        
        rv = []
        while a:
            rv.append(a.pop())
            if b: rv.append(b.pop())
        return rv