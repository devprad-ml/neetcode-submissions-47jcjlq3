class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = set()
        atl = set()
        ans = []
        row, col = len(heights), len(heights[0])
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        def inBounds(r, c):
            return 0 <= r < row and 0 <= c < col
        def dfs(starts):
            stk = list(starts)
            while stk:
                x, y = stk.pop()

                for off_r, off_c in dir:
                    nr, nc = off_r+x, off_c+y

                    if inBounds(nr, nc):
                        if (nr, nc) not in starts and heights[nr][nc] >= heights[x][y]:
                            starts.add((nr, nc))
                            stk.append((nr, nc))


        
        for i in range(col):
            p.add((0, i))
        for i in range(row):
            p.add((i, 0))
        
        for i in range(col):
            atl.add((row-1, i))
        for i in range(row):
            atl.add((i, col-1))
        
        dfs(p)
        dfs(atl)
      
        for i in range(row):
            for j in range(col):
                if (i,j) in p and (i, j) in atl:
                    ans.append([i,j])
        return ans

                
                


                 
        



        
        