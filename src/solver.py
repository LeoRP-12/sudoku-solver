from typing import List, Dict, Tuple
import copy

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
    

    def apply_locked_candidates(self) -> bool:
        """
        Apply the 'Locked Candidates' heuristic (both Pointing and Claiming).
        
        Returns
        -------
        bool
            True if any candidate was eliminated, False otherwise.
        """
        updated = False

        # Check each digit from 1 to 9
        for digit in range(1, 10):

            # Analyze all 3x3 blocks
            for block_row in range(0, 9, 3):
                for block_col in range(1, 19, 6):
                    positions = []

                    # Find all positions in block that can hold the digit
                    for i in range(block_row, block_row + 3):
                        for j in range(block_col, block_col + 6, 2):
                            key = f"{i}:{j}"
                            if key in self.possibilities and digit in self.possibilities[key]:
                                positions.append((i, j))

                    if not positions:
                        continue

                    # Pointing: all candidates in the block are in the same row
                    rows = {i for i, _ in positions}
                    if len(rows) == 1:
                        row = rows.pop()
                        for col in range(1, 19, 2):
                            if not (block_col <= col < block_col + 6):
                                key = f"{row}:{col}"
                                if key in self.possibilities and digit in self.possibilities[key]:
                                    self.possibilities[key].remove(digit)
                                    updated = True

                    # Pointing: all candidates in the block are in the same column
                    cols = {j for _, j in positions}
                    if len(cols) == 1:
                        col = cols.pop()
                        for row in range(9):
                            if not (block_row <= row < block_row + 3):
                                key = f"{row}:{col}"
                                if key in self.possibilities and digit in self.possibilities[key]:
                                    self.possibilities[key].remove(digit)
                                    updated = True

            # Claiming: analyze rows
            for row in range(9):
                positions = []
                for col in range(1, 19, 2):
                    key = f"{row}:{col}"
                    if key in self.possibilities and digit in self.possibilities[key]:
                        positions.append((row, col))
                if not positions:
                    continue

                block_cols = {((col - 1) // 6) for _, col in positions}
                if len(block_cols) == 1:
                    block_col_start = list(block_cols)[0] * 6 + 1
                    block_row_start = (row // 3) * 3
                    for i in range(block_row_start, block_row_start + 3):
                        for j in range(block_col_start, block_col_start + 6, 2):
                            if i == row:
                                continue
                            key = f"{i}:{j}"
                            if key in self.possibilities and digit in self.possibilities[key]:
                                self.possibilities[key].remove(digit)
                                updated = True

            # Claiming: analyze columns
            for col in range(1, 19, 2):
                positions = []
                for row in range(9):
                    key = f"{row}:{col}"
                    if key in self.possibilities and digit in self.possibilities[key]:
                        positions.append((row, col))
                if not positions:
                    continue

                block_rows = {(row // 3) for row, _ in positions}
                if len(block_rows) == 1:
                    block_row_start = list(block_rows)[0] * 3
                    block_col_start = ((col - 1) // 6) * 6 + 1
                    for i in range(block_row_start, block_row_start + 3):
                        for j in range(block_col_start, block_col_start + 6, 2):
                            if j == col:
                                continue
                            key = f"{i}:{j}"
                            if key in self.possibilities and digit in self.possibilities[key]:
                                self.possibilities[key].remove(digit)
                                updated = True

        return updated
    
    def apply_naked_pairs(self) -> bool:
        """
        Apply the Naked Pairs heuristic to all units (rows, columns, blocks).

        Returns
        -------
        bool
            True if any candidates were eliminated, False otherwise.
        """
        updated = False

        def find_naked_pairs(unit_keys: List[str]):
            nonlocal updated
            # Map pairs -> where they appear
            pairs_locations: Dict[Tuple[int, int], List[str]] = {}
            for key in unit_keys:
                if key in self.possibilities and len(self.possibilities[key]) == 2:
                    pair = tuple(sorted(self.possibilities[key]))
                    pairs_locations.setdefault(pair, []).append(key)

            # For each pair, check that it appears in exactly 2 cells
            for pair, keys in pairs_locations.items():
                if len(keys) == 2:
                    # Remove the two numbers from the other cells
                    for key in unit_keys:
                        if key in self.possibilities and key not in keys:
                            for val in pair:
                                if val in self.possibilities[key]:
                                    self.possibilities[key].remove(val)
                                    updated = True

        # check all rows
        for row in range(9):
            unit_keys = [f"{row}:{col}" for col in range(1, 19, 2)]
            find_naked_pairs(unit_keys)

        # check all columns
        for col in range(1, 19, 2):
            unit_keys = [f"{row}:{col}" for row in range(9)]
            find_naked_pairs(unit_keys)

        # check all 3x3 blocks
        for block_row in range(0, 9, 3):
            for block_col in range(1, 19, 6):
                unit_keys = []
                for i in range(block_row, block_row + 3):
                    for j in range(block_col, block_col + 6, 2):
                        unit_keys.append(f"{i}:{j}")
                find_naked_pairs(unit_keys)

        return updated
    

    def apply_hidden_pairs(self) -> bool:
        """
        Apply the Hidden Pairs heuristic to all units (rows, columns, blocks).

        Returns
        -------
        bool
            True if any candidates were eliminated, False otherwise.
        """
        updated = False

        def find_hidden_pairs(unit_keys: List[str]):
            nonlocal updated
            number_positions: Dict[int, List[str]] = {n: [] for n in range(1, 10)}
            for key in unit_keys:
                if key in self.possibilities:
                    for n in self.possibilities[key]:
                        number_positions[n].append(key)

            # Searches for pairs of numbers that occur in exactly the same two cells
            numbers = list(range(1, 10))
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    n1, n2 = numbers[i], numbers[j]
                    if (set(number_positions[n1]) == set(number_positions[n2]) and
                            len(number_positions[n1]) == 2):
                        # N1 and N2 only appear in two cells, and they are the same
                        for key in number_positions[n1]:
                            if key in self.possibilities:
                                original = set(self.possibilities[key])
                                self.possibilities[key] = [val for val in self.possibilities[key] if val in (n1, n2)]
                                if set(self.possibilities[key]) != original:
                                    updated = True

        # Applies to all rows, columns and blocks
        for row in range(9):
            unit_keys = [f"{row}:{col}" for col in range(1, 19, 2)]
            find_hidden_pairs(unit_keys)

        for col in range(1, 19, 2):
            unit_keys = [f"{row}:{col}" for row in range(9)]
            find_hidden_pairs(unit_keys)

        for block_row in range(0, 9, 3):
            for block_col in range(1, 19, 6):
                unit_keys = []
                for i in range(block_row, block_row + 3):
                    for j in range(block_col, block_col + 6, 2):
                        unit_keys.append(f"{i}:{j}")
                find_hidden_pairs(unit_keys)

        return updated

    def solve_with_backtracking(self) -> bool:
        """
        Solve the Sudoku puzzle using recursive backtracking with the
        Minimum Remaining Values (MRV) heuristic.

        This method selects the empty cell with the fewest possible values,
        tries each possibility, and recursively continues solving.
        If it reaches a contradiction (i.e., a cell has no possible values),
        it backtracks and tries a different value.

        Returns
        -------
        bool
            True if a solution is found, False otherwise.
        """
        if not self.possibilities:
            # No more cells to fill; puzzle is solved
            return True

        # Choose cell with the fewest possibilities (MRV heuristic)
        key = min(self.possibilities, key=lambda k: len(self.possibilities[k]))
        i, j = map(int, key.split(":"))

        for num in self.possibilities[key]:
            # Save current state
            original_board = self.board[:]
            original_possibilities = copy.deepcopy(self.possibilities)

            # Place the value on the board
            self.board[i] = self.board[i][:j] + str(num) + self.board[i][j+1:]

            # Remove this key and re-eliminate possibilities
            del self.possibilities[key]
            self.eliminate_possibilities()
            # Constraint propagation
            self.apply_heuristic()

            # Check if any cell has no possibilities left → invalid board
            if any(len(v) == 0 for v in self.possibilities.values()):
                # Backtrack
                self.board = original_board
                self.possibilities = original_possibilities
                continue

            # Recurse
            if self.solve_with_backtracking():
                return True

            # Backtrack on failure
            self.board = original_board
            self.possibilities = original_possibilities

        return False  # No valid number worked for this cell → backtrack
    
    def apply_heuristic(self) -> bool:
        """
        Apply Sudoku solving heuristics and verify if the board was updated.

        Returns
        -------
        bool
            True if the board was updated, False otherwise.
        """
        changed = (
                self.apply_single_possibilities() or
                self.apply_hidden_singles_in_rows() or
                self.apply_hidden_singles_in_columns() or
                self.apply_hidden_singles_in_blocks() or
                self.apply_locked_candidates() or
                self.apply_naked_pairs() or
                self.apply_hidden_pairs()
            )

        return changed
    
    def solve(self) -> bool:
        """
        Solve the Sudoku puzzle using logical strategies and backtracking.

        Returns
        -------
        bool
            True if a solution was found, False otherwise.
        """
        while True:
            self.eliminate_possibilities()
            changed = self.apply_heuristic()
            if not changed:
                break

        if self.possibilities:
            solved = self.solve_with_backtracking()
        else:
            solved = True

        if solved:
            print("\nFinal board:")
            self.print_board()
        else:
            print("No solution found.")

        return solved

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
    result = solver.solve()