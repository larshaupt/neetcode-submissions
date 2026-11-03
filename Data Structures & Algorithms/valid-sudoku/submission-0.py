class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n,m = len(board[0]), len(board)

        for row in range(m):
            row_values = board[row]
            row_values = [val for val in row_values if val != "."]
            if len(set(row_values)) != len(row_values):
                return False
        
        for col in range(n):
            col_values = [board[i][col] for i in range(m)]
            col_values = [val for val in col_values if val != "."]
            if len(set(col_values)) != len(col_values):
                return False
            
        for sector_id in range(9):
            sector_coord = (sector_id//3, sector_id%3)
            sector_values = [board[row][col] for row in range(sector_coord[0]*3, sector_coord[0]*3+3) for col in range(sector_coord[1]*3, sector_coord[1]*3+3)]
            sector_values = [val for val in sector_values if val != "."]
            if len(set(sector_values)) != len(sector_values):
                return False
        return True