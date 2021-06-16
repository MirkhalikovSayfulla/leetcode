class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    continue
                grid[i][j] = 201
                
                if i > 0:
                    grid[i][j] = min(grid[i][j], grid[i-1][j] + 1)
                
                if j > 0:
                    grid[i][j] = min(grid[i][j], grid[i][j-1] + 1)
                    
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if grid[i][j] == 1: 
                    continue
                    
                if i < n-1:
                    grid[i][j] = min(grid[i][j], grid[i+1][j] + 1)
                if j < m-1:
                    grid[i][j] = min(grid[i][j], grid[i][j+1] + 1)
                
                res = max(res, grid[i][j])
                
        if res == 201:
            return -1  
        
        return res - 1