class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            row = set()
            for j in range(9):
                e = board[i][j]
                if e in row and e != ".":
                    return False
                row.add(e)
        
        for i in range(9):
            column = set()
            for j in range(9):
                e = board[j][i]
                if e in column and e != ".":
                    return False
                column.add(e)

        for i in range(9):
            box = set()
            for j in range(9):
                x, y = 3 * (i % 3) + int(j/3), 3 * int(i/3) + j % 3
                e = board[x][y]

                if e in box and e != ".":
                    return False
                box.add(e)

        return True
            
        

        