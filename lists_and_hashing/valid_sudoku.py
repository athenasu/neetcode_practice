from typing import List
import collections


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        """
            Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
                1. Each row must contain the digits 1-9 without repetition.
                2. Each column must contain the digits 1-9 without repetition.
                3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        """
        pass



board1 = [["5","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]
# Output: True

board2 = [["8","3",".",".","7",".",".",".","."]
         ,["6",".",".","1","9","5",".",".","."]
         ,[".","9","8",".",".",".",".","6","."]
         ,["8",".",".",".","6",".",".",".","3"]
         ,["4",".",".","8",".","3",".",".","1"]
         ,["7",".",".",".","2",".",".",".","6"]
         ,[".","6",".",".",".",".","2","8","."]
         ,[".",".",".","4","1","9",".",".","5"]
         ,[".",".",".",".","8",".",".","7","9"]]
# Output: False


my_solution = Solution()
print(my_solution.is_valid_sudoku(board1))



# Solution
# columns = collections.defaultdict(set)
# rows = collections.defaultdict(set)
# square = collections.defaultdict(set)
# length = len(board)

# for row in range(length):
#     for column in range(length):
#         if board[row][column] == '.':
#             continue
#         if (board[row][column] in rows[row] or
#             board[row][column] in columns[column] or
#             board[row][column] in square[(row // 3, column // 3)]):
#             return False
#         columns[column].add(board[row][column])
#         rows[row].add(board[row][column])
#         square[(row // 3, column // 3)].add(board[row][column])
# return True