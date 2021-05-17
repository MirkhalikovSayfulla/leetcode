class Solution:
    def trailingZeroes(self, n: int) -> int:
        temp = 5
        ans = 0
        while temp <= n:
            ans += n// temp
            temp = temp * 5
        return ans