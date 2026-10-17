class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(list)
        colMap = defaultdict(list)
        groupMap = defaultdict(list)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue 
                
                if board[row][col] in rowMap[row] or board[row][col] in colMap[col] or board[row][col] in groupMap[(row//3, col//3)]:
                    return False
                
                rowMap[row].append(board[row][col])
                colMap[col].append(board[row][col])
                groupMap[(row//3, col//3)].append(board[row][col])
        return True