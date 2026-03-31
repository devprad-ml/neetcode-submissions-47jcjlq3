class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ''' we can just take a starting land point and traverse 
        in all the cardinal directions. if we find a 1, we can change it to a 2. 
        we will do a DFS from each cell.
        whenver we get a cell which is a 1 but not visited,
        we increase the number of islands.

        we cannot go out of bounds during the traversal.'''

        isl = 0
        row, col = len(grid), len(grid[0])
        def inBounds(x,y):
            return 0 <= x < row and 0 <= y < col 

        def bfs(r, c):
            if not inBounds(r,c) or grid[r][c] != '1':
                return
            
            grid[r][c] = '2'

            bfs(r+1,c)
            bfs(r-1,c)
            bfs(r,c+1)
            bfs(r,c-1)



        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    isl += 1
                    bfs(i,j)
        return isl
        