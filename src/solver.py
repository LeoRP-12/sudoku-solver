from typing import List, Dict

class SudokuSolver:
    """
    A class to solve Sudoku puzzles using logical techniques and backtracking.

    Parameters
    ----------
    board : list of str
        The initial state of the Sudoku board as a list of 9 strings.

    Attributes
    ----------
    board : list of str
        The current state of the Sudoku board.
    possibilities : dict
        A dictionary mapping empty cells to a list of possible numbers.
    """

    def __init__(self, board: List[str]):
        self.board: List[str] = board
        self.possibilities: Dict[str, List[int]] = self._initialize_possibilities()

    def _initialize_possibilities(self) -> Dict[str, List[int]]:
        """
        Initialize possible values for each empty cell on the board.

        Returns
        -------
        dict
            Dictionary with keys as "row:column" and values as lists of possible numbers.
        """
        possibilities: Dict[str, List[int]] = {}
        for i in range(9):
            for j in range(1, 19, 2):
                if self.board[i][j] == " ":
                    key = f"{i}:{j}"
                    possibilities[key] = list(range(1, 10))
        return possibilities

    def eliminate_possibilities(self) -> Dict[str, List[int]]:
        """
        Eliminate impossible values based on Sudoku rules.

        Returns
        -------
        dict
            Updated possibilities after elimination.
        """
        for key in self.possibilities:
            i, j = map(int, key.split(":"))
            for n in self.possibilities[key][:]:
                n_str = str(n)

                for col in range(1, 19, 2):
                    if self.board[i][col] == n_str:
                        self.possibilities[key].remove(n)
                        break

                for row in range(9):
                    if self.board[row][j] == n_str and n in self.possibilities[key]:
                        self.possibilities[key].remove(n)
                        break

                block_row_start = (i // 3) * 3
                block_col_start = ((j - 1) // 6) * 6 + 1
                for bi in range(block_row_start, block_row_start + 3):
                    for bj in range(block_col_start, block_col_start + 6, 2):
                        if self.board[bi][bj] == n_str and n in self.possibilities[key]:
                            self.possibilities[key].remove(n)
                            break
        return self.possibilities

    def apply_single_possibilities(self) -> bool:
        """
        Apply values where only one possibility exists.

        Returns
        -------
        bool
            True if the board was updated, False otherwise.
        """
        updated = False
        for key in list(self.possibilities.keys()):
            if len(self.possibilities[key]) == 1:
                i, j = map(int, key.split(":"))
                num = str(self.possibilities[key][0])
                self.board[i] = self.board[i][:j] + num + self.board[i][j+1:]
                del self.possibilities[key]
                updated = True
        return updated

    def apply_hidden_singles_in_rows(self) -> bool:
        """
        Apply hidden singles logic in each row.

        Returns
        -------
        bool
            True if the board was updated, False otherwise.
        """
        updated = False
        for row in range(9):
            num_positions = {n: [] for n in range(1, 10)}
            for col in range(1, 19, 2):
                key = f"{row}:{col}"
                if key in self.possibilities:
                    for n in self.possibilities[key]:
                        num_positions[n].append((row, col))

            for n, positions in num_positions.items():
                if len(positions) == 1:
                    i, j = positions[0]
                    key = f"{i}:{j}"
                    if key in self.possibilities:
                        self.board[i] = self.board[i][:j] + str(n) + self.board[i][j+1:]
                        del self.possibilities[key]
                        updated = True
        return updated

    def apply_hidden_singles_in_columns(self) -> bool:
        """
        Apply hidden singles logic in each column.

        Returns
        -------
        bool
            True if the board was updated, False otherwise.
        """
        updated = False
        for col in range(1, 19, 2):
            num_positions = {n: [] for n in range(1, 10)}
            for row in range(9):
                key = f"{row}:{col}"
                if key in self.possibilities:
                    for n in self.possibilities[key]:
                        num_positions[n].append((row, col))

            for n, positions in num_positions.items():
                if len(positions) == 1:
                    i, j = positions[0]
                    key = f"{i}:{j}"
                    if key in self.possibilities:
                        self.board[i] = self.board[i][:j] + str(n) + self.board[i][j+1:]
                        del self.possibilities[key]
                        updated = True
        return updated

    def apply_hidden_singles_in_blocks(self) -> bool:
        """
        Apply hidden singles logic in each 3x3 block.

        Returns
        -------
        bool
            True if the board was updated, False otherwise.
        """
        updated = False
        for block_row in range(0, 9, 3):
            for block_col in range(1, 19, 6):
                num_positions = {n: [] for n in range(1, 10)}
                for i in range(block_row, block_row + 3):
                    for j in range(block_col, block_col + 6, 2):
                        key = f"{i}:{j}"
                        if key in self.possibilities:
                            for n in self.possibilities[key]:
                                num_positions[n].append((i, j))

                for n, positions in num_positions.items():
                    if len(positions) == 1:
                        i, j = positions[0]
                        key = f"{i}:{j}"
                        if key in self.possibilities:
                            self.board[i] = self.board[i][:j] + str(n) + self.board[i][j+1:]
                            del self.possibilities[key]
                            updated = True
        return updated

    def print_possibilities(self) -> None:
        """Print all current possibilities."""
        for key in sorted(self.possibilities):
            print(f"{key}: {self.possibilities[key]}")

    def print_board(self) -> None:
        """Print the current state of the Sudoku board."""
        for line in self.board:
            print(line)


    def _check_col(self, row: int, col: int, num: str) -> bool:
        """Check if a number can be placed in the specified column."""
        for i in range(9):
            if self.board[i][col] == num:
                return False
        return True
    
    def _check_row(self, row: int, col: int, num: str) -> bool:
        """Check if a number can be placed in the specified row."""
        for j in range(1, 19, 2):
            if self.board[row][j] == num:
                return False
        return True
    
    def _check_block(self, row: int, col: int, num: str) -> bool:
        """Check if a number can be placed in the 3x3 block."""
        block_row_start = (row // 3) * 3
        block_col_start = ((col - 1) // 6) * 6 + 1
        for i in range(block_row_start, block_row_start + 3):
            for j in range(block_col_start, block_col_start + 6, 2):
                if self.board[i][j] == num:
                    return False
        return True
    
    def is_valid(self, row: int, col: int, num: str) -> bool:
        """
        Check if placing a number in the specified cell is valid.

        Parameters
        ----------
        row : int
            The row index (0-8).
        col : int
            The column index (1, 3, 5, ..., 17).
        num : str
            The number to check (as a string).

        Returns
        -------
        bool
            True if valid, False otherwise.
        """
        return (
            self._check_row(row, col, num) and
            self._check_col(row, col, num) and
            self._check_block(row, col, num)
        )

    
    def solve_with_backtracking(self) -> bool:
        """
        Solve the Sudoku puzzle using backtracking algorithm.

        Returns
        -------
        bool
            True if the puzzle is solved, False otherwise.
        """
        # Find the next empty cell
        for i in range(9):
            for j in range(1, 19, 2):
                if self.board[i][j] == " ":
                    for num in map(str, range(1, 10)):
                        if self.is_valid(i, j, num):
                            # Try this number
                            self.board[i] = self.board[i][:j] + num + self.board[i][j+1:]
                            if self.solve_with_backtracking():
                                return True
                            # Undo move
                            self.board[i] = self.board[i][:j] + " " + self.board[i][j+1:]
                    return False  # No valid number found, trigger backtracking
        print("\nFinal board:")
        self.print_board()
        return True

    
    def solve(self) -> None:
        """Solve the Sudoku puzzle using logical strategies.
        Fills as much as possible without guessing."""

        while True:
            self.eliminate_possibilities()
            changed = (
                self.apply_single_possibilities() or
                self.apply_hidden_singles_in_rows() or
                self.apply_hidden_singles_in_columns() or
                self.apply_hidden_singles_in_blocks()
            )
            if not changed:
                break
        if self.possibilities:
            return self.solve_with_backtracking()
        
        print("\nFinal board:")
        self.print_board()
        return True
    
    def get_board(self) -> List[str]:
        """
        Get the current state of the board.

        Returns
        -------
        list of str
            The board as a list of 9 formatted strings.
        """
        return self.board


if __name__ == "__main__":
    print("Enter the Sudoku board line by line:")
    board: List[str] = [input() for _ in range(9)]

    solver = SudokuSolver(board)
    solver.solve()
