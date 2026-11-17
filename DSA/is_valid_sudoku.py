# Time: O(1) Space: O(1)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_present_n = [[False]*9 for _ in range(9)]
        row_present_n = [[False]*9 for _ in range(9)]
        box_present_n = [[False]*9 for _ in range(9)]

        for i, r in enumerate(board):
            for j, n in enumerate(r):
                if n != ".":
                    n_int = int(n)
                    if col_present_n[j][n_int-1]:
                        return False
                    col_present_n[j][n_int-1] = True

                    if row_present_n[i][n_int-1]:
                        return False
                    row_present_n[i][n_int-1] = True

                    box_int = (i//3)*3 + j//3
                    if box_present_n[box_int][n_int-1]:
                        return False
                    box_present_n[box_int][n_int-1] = True
        return True
