class Solution:
    def isPathCrossing(self, path: str) -> bool:
            x, y = 0, 0
            seen = {(x, y)}
            for move in path: 
                if   move == "N": y += 1
                elif move == "S": y -= 1
                elif move == "E": x += 1
                else: x -= 1
                if (x, y) in seen: return True
                seen.add((x, y))
            return False 