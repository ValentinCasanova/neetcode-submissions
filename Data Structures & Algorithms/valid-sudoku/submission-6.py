class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = collections.defaultdict(set)
        col_map = collections.defaultdict(set)
        square_map = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == '.':
                    continue
                if (cur in row_map[row] or
                    cur in col_map[col] or 
                    cur in square_map[(row // 3, col //3)]):
                    return False
                else:
                    row_map[row].add(cur)
                    col_map[col].add(cur)
                    square_map[(row//3,col//3)].add(cur)
        return True