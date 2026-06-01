class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ''' we can just take a starting land point and traverse 
        in all the cardinal directions. if we find a 1, we can change it to a 2. 
        we will do a DFS from each cell.
        whenver we get a cell which is a 1 but not visited,
        we increase the number of islands.

        we cannot go out of bounds during the traversal.'''

        isl = 0

        m,n=len(grid),len(grid[0])

        def inB(r,c):
            return 0<=r<m and 0<=c<n
        
        def dfs(x,y):
            if not inB(x,y) or grid[x][y] != '1':
                return 
            
            grid[x][y] = '2'
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    isl+= 1
                    dfs(i,j)
        return isl
        