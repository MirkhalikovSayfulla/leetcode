class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting = set([a[0] for a in paths])
        for p in paths:
            if p[1] not in starting: 
                return p[1]