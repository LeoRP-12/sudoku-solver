import pytest
from src.solver import SudokuSolver
from typing import List


def load_sudoku_puzzles(path: str) -> List[List[str]]:
    """
    Load Sudoku puzzles from a text file, each puzzle consists of 9 lines in visual format,
    separated by lines containing '========'.

    Parameters
    ----------
    path : str
        Path to the text file containing the Sudoku puzzles.

    Returns
    -------
    List[List[str]]
        A list of Sudoku puzzles, each puzzle is a list of 9 visual-format strings.
    """
    with open(path, "r") as f:
        raw = f.read().strip()

    blocks = raw.split("========")
    puzzles = []
    for block in blocks:
        lines = [line.strip() for line in block.strip().splitlines()]
        # Accept only puzzles with 9 lines, each line in visual format (with pipes)
        if len(lines) == 9 and all(line.startswith("|") and line.endswith("|") for line in lines):
            puzzles.append(lines)

    return puzzles

def is_board_filled(board: List[str]) -> bool:
    """
    Check if all cells in the board are filled with digits 1–9.

    Parameters
    ----------
    board : list of str
        A Sudoku board in visual format (with pipes and spaces).

    Returns
    -------
    bool
        True if all cells are filled, False if any empty (" ") cell exists.
    """
    for row in board:
        for col in range(1, 19, 2):
            if row[col] not in "123456789":
                return False
    return True



class TestSudokuSolver:
    def test_level1_solver(self):
        board = """
        | |4| |9|5|3|1|2| |
        |3|1| | | | |9|5| |
        |6| | |1|8| | |7| |
        | |7| | |4| | | | |
        |5|2|6| | | |4|8|9|
        | | | | |9| | |6| |
        | |8| | |2|4| | |1|
        | |6|9| | | | |4|5|
        | |5|1|7|6|9| |3| |
        """

        board_lines = [line.strip() for line in board.strip().splitlines()]

        solver = SudokuSolver(board_lines)
        solver.solve()

        expected_solution = """
        |8|4|7|9|5|3|1|2|6|
        |3|1|2|4|7|6|9|5|8|
        |6|9|5|1|8|2|3|7|4|
        |9|7|8|6|4|5|2|1|3|
        |5|2|6|3|1|7|4|8|9|
        |1|3|4|2|9|8|5|6|7|
        |7|8|3|5|2|4|6|9|1|
        |2|6|9|8|3|1|7|4|5|
        |4|5|1|7|6|9|8|3|2|
        """

        expected_solution_lines = [line.strip() for line in expected_solution.strip().splitlines()]
        assert solver.board == expected_solution_lines


    def test_level2_solver(self):

        board = """
        |1| | |6| | | |8|4|
        | |2| | | |9| | | |
        | |4|6|8| | | | |7|
        |2| | | |1|5|3|7|8|
        | | | | | |3| | | |
        |4| |3|9| |8|5|6| |
        | | | | | | | | | |
        |3| |7| | | | | |6|
        |6| |4| | | |8|3| |
        """

        board_lines = [line.strip() for line in board.strip().splitlines()]

        solver = SudokuSolver(board_lines)
        solver.solve()

        expected_solution = """
        |1|3|5|6|7|2|9|8|4|
        |7|2|8|5|4|9|6|1|3|
        |9|4|6|8|3|1|2|5|7|
        |2|6|9|4|1|5|3|7|8|
        |5|8|1|7|6|3|4|2|9|
        |4|7|3|9|2|8|5|6|1|
        |8|1|2|3|9|6|7|4|5|
        |3|5|7|2|8|4|1|9|6|
        |6|9|4|1|5|7|8|3|2|
        """

        expected_solution_lines = [line.strip() for line in expected_solution.strip().splitlines()]
        assert solver.board == expected_solution_lines


    def test_level3_solver(self):
        board = """
        | |4| |9|5|3|1|2| |
        |3|1| | | | |9|5| |
        |6| | |1|8| | |7| |
        | |7| | |4| | | | |
        |5|2|6| | | |4|8|9|
        | | | | |9| | |6| |
        | |8| | |2|4| | |1|
        | |6|9| | | | |4|5|
        | |5|1|7|6|9| |3| |
        """

        board_lines = [line.strip() for line in board.strip().splitlines()]

        solver = SudokuSolver(board_lines)
        solver.solve()

        expected_solution = """
        |8|4|7|9|5|3|1|2|6|
        |3|1|2|4|7|6|9|5|8|
        |6|9|5|1|8|2|3|7|4|
        |9|7|8|6|4|5|2|1|3|
        |5|2|6|3|1|7|4|8|9|
        |1|3|4|2|9|8|5|6|7|
        |7|8|3|5|2|4|6|9|1|
        |2|6|9|8|3|1|7|4|5|
        |4|5|1|7|6|9|8|3|2|
        """

        expected_solution_lines = [line.strip() for line in expected_solution.strip().splitlines()]
        assert solver.board == expected_solution_lines


    def test_level4_solver(self):
        board = """
        |1| | |9|2| | | | |
        |5|2|4| |1| | | | |
        | | | | | | | |7| |
        | |5| | | |8|1| |2|
        | | | | | | | | | |
        |4| |2|7| | | |9| |
        | |6| | | | | | | |
        | | | | |3| |9|4|5|
        | | | | |7|1| | |6|
        """

        board_lines = [line.strip() for line in board.strip().splitlines()]

        solver = SudokuSolver(board_lines)
        solver.solve()

        expected_solution = """
        |1|7|6|9|2|3|5|8|4|
        |5|2|4|8|1|7|6|3|9|
        |8|9|3|6|5|4|2|7|1|
        |9|5|7|3|4|8|1|6|2|
        |6|3|8|1|9|2|4|5|7|
        |4|1|2|7|6|5|3|9|8|
        |2|6|5|4|8|9|7|1|3|
        |7|8|1|2|3|6|9|4|5|
        |3|4|9|5|7|1|8|2|6|
        """

        expected_solution_lines = [line.strip() for line in expected_solution.strip().splitlines()]
        assert solver.board == expected_solution_lines


    def test_project_euler_sudoku_sum(self):
        """
        Test solving 50 Sudoku puzzles and calculating the sum of the
        top-left 3-digit numbers in each solved puzzle.
        """
        puzzles = load_sudoku_puzzles("tests/project_euler_sudoku.txt")
        total = 0

        for puzzle in puzzles:
            solver = SudokuSolver(puzzle)
            solver.solve()
            top_row = solver.board[0]
            digits = [top_row[i] for i in [1, 3, 5]]
            number = int("".join(digits))
            total += number

        assert total == 24702, f"Expected total to be 24702, but got {total}"


    def test_solver_can_solve_all_50(self):
        puzzles = load_sudoku_puzzles("tests/project_euler_sudoku.txt")
        assert len(puzzles) == 50, f"Expected 50 puzzles, but got {len(puzzles)}"

        unsolved_indices = []
        for idx, puzzle in enumerate(puzzles):
            solver = SudokuSolver(puzzle)
            solver.solve()
            if not is_board_filled(solver.board):
                unsolved_indices.append(idx + 1)

        assert not unsolved_indices, f"Solver failed to fully solve the following puzzles: {unsolved_indices}"

    def test_hardest_puzzles_solver(self):
        puzzles = load_sudoku_puzzles("tests/hardest_puzzles.txt")

        for idx, puzzle in enumerate(puzzles):
            solver = SudokuSolver(puzzle)
            solver.solve()
            assert is_board_filled(solver.board), f"Puzzle {idx + 1} was not fully solved."

    # def test_solver_can_solve_all_hard_puzzles(self):
    #     puzzles = load_sudoku_puzzles("tests/hard_puzzles.txt")

    #     unsolved_indices = []
    #     for idx, puzzle in enumerate(puzzles):
    #         solver = SudokuSolver(puzzle)
    #         solver.solve()
    #         if not is_board_filled(solver.board):
    #             unsolved_indices.append(idx + 1)

    #     assert not unsolved_indices, f"Solver failed to fully solve the following hardest puzzles: {unsolved_indices}"