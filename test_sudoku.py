from solver import SudokuSolver


class TestSudoko:
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