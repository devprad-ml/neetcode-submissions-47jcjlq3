class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()
        n = len(grid)
        m = len(grid[0])
        d = 0
        seen = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    seen.add((i, j))
                    q.append((i,j))
        
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        def inBounds(r, c):
            return 0 <= r < n and 0 <= c < m
        while q:
            
            l = len(q)

            for _ in range(l):
                row, col = q.popleft()
                
                for off_r, off_c in dir:
                    nr, nc = off_r+row, off_c+col

                    if inBounds(nr, nc):
                        if grid[nr][nc] not in seen and grid[nr][nc] == 2147483647:
                            grid[nr][nc] = d+1
                            seen.add((nr, nc))
                            q.append((nr, nc))
            if q:
                d += 1
        

                    

        