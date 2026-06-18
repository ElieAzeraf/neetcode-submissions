class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] in row and board[i][j] != ".":
                    return False
                row.add(board[i][j])
        
        for i in range(9):
            column = set()
            for j in range(9):
                if board[j][i] in column and board[j][i] != ".":
                    return False
                column.add(board[j][i])

        for i in range(9):
            box = set()
            for j in range(9):
                x, y = 3 * (i % 3) + int(j/3), 3 * int(i/3) + j % 3
                e = board[x][y]

                if e in box and e != ".":
                    return False
                box.add(e)

        return True
            
        

        