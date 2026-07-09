class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3 , c/3)

        #set up nested for loop to make the grid
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # If the box is empty, continue
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]): 
                    # If there is a number already in board[r][c] within the current row, column, or square, return False
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True