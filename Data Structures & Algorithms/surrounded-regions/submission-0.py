class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ''' so we need to get the O's from the edge of the matrix.
        then we do a DFS/BFS and mark all the connected O's as anything other
        than O and X as they are also unsurrounded regions. 
        then at last we go over the matrix and change the S's to O's 
        and O's to X's as these untouched O's are surrounded O's'''

        row, col = len(board), len(board[0])
        q = []
        def inB(r, c):
            return 0 <= r < row and 0 <= c < col
            

        for i in range(row):
            if board[i][0] == 'O':
                q.append((i, 0))
            if board[i][col-1] == 'O':
                q.append((i, col-1))
        
        for i in range(col):
            if board[0][i] == 'O':
                q.append((0, i))
            if board[row-1][i] == 'O':
                q.append((row-1, i))
        
        while q:
            r, c = q.pop()

            board[r][c] = 'U'

            for ofr, ofc in [[0,1],[0,-1],[1,0],[-1,0]]:
                nr, nc = ofr+r, ofc+c

                if inB(nr, nc) and board[nr][nc] == 'O':
                    q.append((nr, nc))
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'U':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
    
                



        