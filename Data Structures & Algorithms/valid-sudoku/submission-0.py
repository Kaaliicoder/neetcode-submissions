class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        compare = []
        for i in range(0,9):
            for j in range(1,9):
                compare.append(board[i][j-1])
                num = board[i][j-1]
                if num == board[i][j]:
                    return False
                
