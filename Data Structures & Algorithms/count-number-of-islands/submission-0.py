class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(r, c):
            
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
                return
            
            grid[r][c] = '0'

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

            # directions = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]
            # for dr, dc in directions:
            #     # if grid[dr][dc] == '1':
            #     dfs(dr, dc)
            return          

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count



