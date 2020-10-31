from typing import List, Tuple, Union

Matrix = List[List[int]]

"""
    Given a partially filled 9×9 2D array, the objective is to fill a 9×9
    square grid with digits numbered 1 to 9, so that every row, column, and
    and each of the nine 3×3 sub-grids contains all of the digits.

    This can be solved using Backtracking and is similar to n-queens.
    We check to see if a cell is safe or not and recursively call the
    function on the next column to see if it returns True. if yes, we
    have solved the puzzle. else, we backtrack and place another number
    in that cell and repeat this process.
"""
# assigning initial values to the grid
initial_grid = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


initial_not_solvable_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


# a grid with no solution
no_solution = [
    [5, 0, 6, 5, 0, 8, 4, 0, 3],
    [5, 2, 0, 0, 0, 0, 0, 0, 2],
    [1, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]


def is_safe(grid: Matrix, row: int, column: int, n: int) -> bool:
    """
    This function checks the grid to see if each row,
    column, and the 3x3 subgrids contain the digit 'n'.
    It returns False if it is not 'safe' (a duplicate digit
    is found) else returns True if it is 'safe'
    """
    if n == 0:
        return True

    elif n < 0 or n > 9 or (not isinstance(n, int)):
        return False

    for i in range(9):
        if (grid[row][i] == n and i != column) or (grid[i][column] == n and i != row):
            return False

    for i in range(3):
        for j in range(3):
            new_row = (row - row % 3) + i
            new_column = (column - column % 3) + j
            if (
                new_row != row
                and new_column != column
                and grid[new_row][new_column] == n
            ):
                return False

    return True


def is_completed(grid: Matrix) -> bool:
    """
    This function checks if the puzzle is completed or not.
    it is completed when all the cells are assigned with a non-zero number.

    >>> is_completed([[0]])
    False
    >>> is_completed([[1]])
    True
    >>> is_completed([[1, 2], [0, 4]])
    False
    >>> is_completed([[1, 2], [3, 4]])
    True
    >>> is_completed(initial_grid)
    False
    >>> is_completed(no_solution)
    False
    """
    return all(all(cell != 0 for cell in row) for row in grid)


def find_empty_location(grid: Matrix) -> Tuple[int, int]:
    """
    This function finds an empty location so that we can assign a number
    for that particular row and column.
    """
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j


def check_original_solvable(grid) -> bool:
    for original_row in range(9):
        for origin_col in range(9):
            origin_digit = grid[original_row][origin_col]
            if origin_digit:
                if not is_safe(grid, original_row, origin_col, origin_digit):
                    return False
    return True


def sudoku_solve(grid: Matrix) -> Union[Matrix, bool]:
    """
    Takes a partially filled-in grid and attempts to assign values to
    all unassigned locations in such a way to meet the requirements
    for Sudoku solution (non-duplication across rows, columns, and boxes)

    >>> sudoku(initial_grid)  # doctest: +NORMALIZE_WHITESPACE
    [[3, 1, 6, 5, 7, 8, 4, 9, 2],
     [5, 2, 9, 1, 3, 4, 7, 6, 8],
     [4, 8, 7, 6, 2, 9, 5, 3, 1],
     [2, 6, 3, 4, 1, 5, 9, 8, 7],
     [9, 7, 4, 8, 6, 3, 1, 2, 5],
     [8, 5, 1, 7, 9, 2, 6, 4, 3],
     [1, 3, 8, 9, 4, 7, 2, 5, 6],
     [6, 9, 2, 3, 5, 1, 8, 7, 4],
     [7, 4, 5, 2, 8, 6, 3, 1, 9]]
     >>> sudoku(no_solution)
     False
     >>> sudoku(initial_not_solvable_grid)
     False
    """

    if is_completed(grid):
        return grid

    row, column = find_empty_location(grid)

    for digit in range(1, 10):
        if is_safe(grid, row, column, digit):
            grid[row][column] = digit

            if sudoku_solve(grid):
                return grid

            grid[row][column] = 0

    return False


def print_solution(grid: Matrix) -> None:
    """
    A function to print the solution in the form
    of a 9x9 grid
    """
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()


def sudoku(grid: Matrix) -> Union[Matrix, bool]:
    if not check_original_solvable(grid):
        return False
    return sudoku_solve(grid)


if __name__ == "__main__":
    # make a copy of grid so that you can compare with the unmodified grid
    for grid in (
        initial_grid,
        no_solution,
        initial_not_solvable_grid,
    ):
        grid = list(map(list, grid))
        solution = sudoku(grid)
        if solution:
            print("grid after solving:")
            print_solution(solution)
        else:
            print("Cannot find a solution.")
