class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = [-1]
        for new in asteroids:
            while new < 0 < ans[-1]:
                if -new < ans[-1] or -new == ans.pop():
                    break
            else:
                ans.append(new)
        return ans[1:]