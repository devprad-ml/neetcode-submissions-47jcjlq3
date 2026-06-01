class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ''' so we need to get the O's from the edge of the matrix.
        then we do a DFS/BFS and mark all the connected O's as anything other
        than O and X as they are also unsurrounded regions. 
        then at last we go over the matrix and change the S's to O's 
        and O's to X's as these untouched O's are surrounded O's'''

        

        def inB(r, c):
            return 0 <= r < m and 0 <= c < n

        m,n = len(board),len(board[0])
        q = deque()

        for i in range(m):
            if board[i][0] == 'O':
                q.append((i,0))
            if board[i][n-1] == 'O':
                q.append((i, n-1))

        for i in range(n):
            if board[0][i] == 'O':
                q.append((0,i))
            if board[m-1][i] == 'O':
                q.append((m-1,i))
        
        while q:
            x, y = q.popleft()

            dir = [[0,1],[0,-1],[1,0],[-1,0]]

            board[x][y] = 'U'

            for off_r, off_c in dir:
                nr, nc = off_r+x, off_c+y
                if inB(nr, nc) and board[nr][nc] == 'O':
                    q.append((nr, nc))
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'U':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
            





        






    
                



        