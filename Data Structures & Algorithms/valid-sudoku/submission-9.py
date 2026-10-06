class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set)
        for row in range(9):
            for col in range(9):
                cur_square = board[row][col]
                if cur_square == '.':
                    continue
                    
                if (cur_square in row_map[row]
                    or cur_square in col_map[col]
                    or cur_square in square_map[(row // 3, col // 3)]):
                    return False
                row_map[row].add(cur_square)
                col_map[col].add(cur_square)
                square_map[(row // 3, col // 3)].add(cur_square)
        return True

