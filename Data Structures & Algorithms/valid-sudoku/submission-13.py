class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == '.':
                    continue
                if (cur in rows[r]
                    or cur in cols[c]
                    or cur in square[(r//3, c//3)]):
                    
                    return False

                cols[c].add(cur)
                rows[r].add(cur)
                square[(r//3, c//3)].add(cur)
        return True


        
