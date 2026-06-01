class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ''' get all the border cells in a set and do a DFS from those border cells.
        we are going from outside to inside, that means heights need to increase if water 
        wants to flow downhill.
        if condition passes, add to the set 
        let us do this recursively.'''
        pac, atl = set(),set()

        m,n = len(heights), len(heights[0])
        dir = [[0,1],[0,-1],[1,0],[-1,0]]

        def inB(r, c):
            return 0<= r<m and 0<=c<n
        
        def dfs(st):
            stk = list(st)

            while stk:
                x, y = stk.pop()

                for off_r, off_c in dir:

                    nr, nc = off_r+x, off_c+y
                    if (nr, nc) not in st and inB(nr, nc) and heights[nr][nc] >= heights[x][y]:
                        st.add((nr, nc))
                        stk.append((nr, nc))
        
        for i in range(n):
            pac.add((0, i))
            atl.add((m - 1, i))
        for i in range(m):
            pac.add((i, 0))
            atl.add((i, n-1))
        
        dfs(pac)
        dfs(atl)
        ans = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    ans.append([i,j])
        
        return ans

            


        

                
                


                 
        



        
        