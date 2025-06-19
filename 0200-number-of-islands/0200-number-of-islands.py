class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        coords = set()
        rows, cols = len(grid), len(grid[0]) if grid else 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    coords.add((i, j))
        
        count = 0
        while coords:
            island = [coords.pop()]
            idx = 0
            while idx < len(island):
                x, y = island[idx]
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) in coords:
                        island.append((nx, ny))
                        coords.remove((nx, ny))
                idx += 1
            count += 1
        
        return count
