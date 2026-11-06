# restart from scratch
# the input is a nested list
# a list of lists, in which that nested list holds strings
# the outer list will represent rows, while inner list's strs represent columns
# return is a bool, such that the grid is valid or not

# we're supposed to determine if a 9x9 sudoku grid is valid
# in order to determine if its valid needs the following:
# - each row must contain digits of 1-9 w/o repitition
# - each column must contain digits of 1-9 w/o repitition
# - each of the nine sub-boxes (3x3 grids) contain digits 1-9 w/o repitition
# - note: they dont NEED digits 1-9, just those possible digits and no repititions

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        digits = ["1","2","3","4","5","6","7","8","9"]

        # to break it down we can assert each rule at a time:
        # check if each row contains digits 1-9
        for r in range(len(board)):
            row_set = set()
            for c in range(len(board[r])):
                if board[r][c] in digits:
                    if board[r][c] in row_set:
                        return False
                    row_set.add(board[r][c])

        # check if each column contains digits 1-9
        for c in range(9):
            column_set = set()
            for r in range(9):
                if board[r][c] in digits:
                    if board[r][c] in column_set:
                        return False
                    column_set.add(board[r][c])

        # check if each box (3x3) contains digits 1-9
            for br in range(3):
                for bc in range(3):
                    box_set = set()
                    for r_offset in range(3):
                        for c_offset in range(3):
                            r = (br * 3) + r_offset
                            c = (bc * 3) + c_offset

                            if board[r][c] in digits:
                                if board[r][c]in box_set:
                                    return False
                                box_set.add(board[r][c])
        return True