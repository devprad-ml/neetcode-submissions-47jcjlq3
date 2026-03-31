class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row, col = len(grid), len(grid[0])
        max_area = -float('inf')

        def inB(r, c):
            return 0 <= r < row and 0 <= c < col
        
        def dfs(x, y):
            area = 0
            stk = [(x, y)]

            while stk:
                r, c = stk.pop()
                if inB(r, c) and grid[r][c] == 1:
                    area += 1
                    grid[r][c] = 2

                    for ofr, ofc in [[0,1],[0,-1],[1,0],[-1,0]]:
                        nr, nc = ofr+r, ofc+c

                        if inB(nr, nc) and grid[nr][nc] == 1:
                            stk.append((nr, nc))
            
            return area
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    max_area = max(dfs(i, j), max_area)
        return max_area if max_area != -float('inf') else 0

        