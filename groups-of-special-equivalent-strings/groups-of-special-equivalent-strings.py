class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len({''.join(sorted(a[::2]) + sorted(a[1::2])) for a in A})