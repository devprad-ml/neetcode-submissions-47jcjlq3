class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = set()
        atl = set()
        ans = []
        row, col = len(heights), len(heights[0])
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        def inBounds(r, c):
            return 0 <= r < row and 0 <= c < col
        def dfs(r, c, seen):
            seen.add((r,c))
            for x, y in dir:
                nr, nc = r+x, c+y
                if inBounds(nr, nc):
                    if heights[r][c] <= heights[nr][nc] and (nr, nc) not in seen:
                        dfs(nr, nc, seen)

        
        for i in range(col):
            dfs(0, i, p)
        for i in range(row):
            dfs(i, 0, p)
        
        for i in range(col):
            dfs(row-1, i, atl)
        for i in range(row):
            dfs(i, col-1, atl)
      
        for i in range(row):
            for j in range(col):
                if (i,j) in p and (i, j) in atl:
                    ans.append([i,j])
        return ans

                
                


                 
        



        
        