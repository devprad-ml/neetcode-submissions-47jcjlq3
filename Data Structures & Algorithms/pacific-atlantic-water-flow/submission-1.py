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
            stk = [(r, c)]
            seen.add((r,c))

            while stk:
                x, y = stk.pop()

                for off_r, off_c in dir:
                    nr, nc = off_r+x, off_c+y

                    if inBounds(nr, nc):
                        if (nr, nc) not in seen and heights[nr][nc] >= heights[x][y]:
                            seen.add((nr, nc))
                            stk.append((nr, nc))


        
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

                
                


                 
        



        
        