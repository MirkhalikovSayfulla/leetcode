class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        N, p = sorted(str(N)), 1
        while len(str(p)) <= len(N):
            if sorted(str(p)) == N:
                return True
            p*=2
            
        return False