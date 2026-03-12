class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)
        
        for i in range(9):
            for c in range(9):
                if(board[i][c] == ".")
                    continue
                if(board[i][c] in rows[i] or board[i][c] in cols[c] or board[i][c] in 
                square[( i // 3, c // 3)]):
                    return False
                cols[c].add(board[i][c])
                rows[i].add(board[i][c])
                square[(i // 3, c // 3)].add(board[i][c])
        return False
                