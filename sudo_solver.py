import numpy as np
from itertools import islice
from collections.abc import Iterable


class Sudoko:
    def __init__(self, board=None):
        self.board = board or [input() for i in range(9)]
        self.numpy_board = np.array([i for i in self.batched(
            [int(self.board[i][j]) if self.board[i][j].isdigit() else 0 for i in range(9) for j in range(1, 19, 2)],
            9)])
        self.target = {f"{i}:{j}": [1, 2, 3, 4, 5, 6, 7, 8, 9] for i in range(9) for j in range(0, 9) if self.numpy_board[i,j] == 0}

    def get_squares(self):
        return {1: [self.numpy_board[i, j] for i in range(3) for j in range(3)],
                2: [self.numpy_board[i, j] for i in range(3) for j in range(3, 6)],
                3: [self.numpy_board[i, j] for i in range(3) for j in range(6, 9)],
                4: [self.numpy_board[i, j] for i in range(3, 6) for j in range(3)],
                5: [self.numpy_board[i, j] for i in range(3, 6) for j in range(3, 6)],
                6: [self.numpy_board[i, j] for i in range(3, 6) for j in range(6, 9)],
                7: [self.numpy_board[i, j] for i in range(6, 9) for j in range(3)],
                8: [self.numpy_board[i, j] for i in range(6, 9) for j in range(3, 6)],
                9: [self.numpy_board[i, j] for i in range(6, 9) for j in range(6, 9)],

                }



    def solver(self):
        self.check_row()
        self.check_col()
        self.check_squares()
        self.uniqueness_criteria()
        self.rows_criteria()   # cagado
        self.cols_criteria()   # cagado
        if self.check_if_solved():
            self.print_board()
        else: self.solver()

    def check_row(self):
        for i in self.target:
            for n in self.target[i].copy():
                for j in range(0, 9):
                    if self.numpy_board[int(i[0]),j] == n:
                        self.remove_guess_from_target(index= i, value=n)
                        continue

    def check_col(self):
        for i in self.target:
            for n in self.target[i].copy():
                for j in range(0, 9):
                    if self.numpy_board[j,int(i[2:])] == n:
                        self.remove_guess_from_target(index= i, value=n)
                        continue

    def check_squares(self):
        square = self.get_squares()
        for i in self.target:
            row_index = int(i[0])
            column_index = int(i[2:])
            for n in self.target[i].copy():
                if row_index < 3 and column_index < 3:
                    if n in square[1]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue
                
                if (row_index <3) and (column_index > 2 and column_index< 6 ):
                    if n in square[2]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue
                if (row_index < 3) and (column_index > 5 and column_index <9):
                    if n in square[3]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue
                if (row_index > 2 and row_index <6) and column_index < 3:
                    if n in square[4]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue
                if (row_index > 2 and row_index <6) and (column_index > 2 and column_index < 6):
                    if n in square[5]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue
                
                if (row_index > 2 and row_index <6) and (column_index > 5 and column_index < 9):
                    if n in square[6]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue

                if (row_index > 5 and row_index <9) and (column_index < 3):
                    if n in square[7]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue
                
                if (row_index > 5 and row_index <9) and (column_index > 2 and column_index < 6):
                    if n in square[8]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue

                if (row_index > 5 and row_index <9) and (column_index > 5 and column_index < 9):
                    if n in square[9]:
                        self.remove_guess_from_target(index= i, value=n)
                        continue


    def uniqueness_criteria(self):
        #execute esse método após para cada elemento do tabuleiro
            #verifica se existe um número que só pode ser colocado em uma casa
            #se sim, coloca o número na casa
            #executa o solver novamente

        for i in self.target.copy():
            if len(self.target[i]) == 1:
                self.numpy_board[int(i[0]),int(i[2:])] = self.target[i][0]
                self.target.pop(i)

    def rows_criteria(self):
        # verifica se dado uma linha, há uma casa que só pode ser preenchida com um número
        linha = {}
        for n in range(0, 9):
            linha[str(n)] = []
            for i in self.target:
                if n == int(i[0]):
                    for t in self.target[i]:
                        linha[str(n)].append(t)
        for i in linha:
            for n in range(0, 10):
                cont = 0
                for t in linha[i]:
                    if n == int(t):
                        cont = cont + 1
                if cont == 1:
                    for k in self.target.copy():
                        if i == k[0]:
                            for h in self.target.copy()[k]:
                                if int(h) == n:
                                    self.numpy_board[int(k[0]), int(k[2:])] = n
                                    self.target.pop(k)

    def cols_criteria(self):
        # verifica se dado uma coluna, há uma casa que só pode ser preenchida com um número
        coluna = {}
        for n in range(1, 19, 2):
            coluna[str(n)] = []
            for i in self.target:
                if n == int(i[2:]):
                    for t in self.target[i]:
                        coluna[str(n)].append(t)
        for i in coluna:
            for n in range(0, 10):
                cont = 0
                for t in coluna[i]:
                    if n == int(t):
                        cont = cont + 1
                if cont == 1:
                    for k in self.target.copy():
                        if i == k[2:]:
                            for h in self.target.copy()[k]:
                                if int(h) == n:
                                    self.numpy_board[int(k[0]), int(k[2:])] = n
                                    self.target.pop(k)

    def squares_criteria(self):
        # verifica se dado um quadrado, há uma casa que só pode ser preenchida com um número
        pass

    def print_board(self):
        print(self.numpy_board)

    def check_if_solved(self):
        return np.all(self.numpy_board)

    def remove_guess_from_target(self, index: str, value):
        self.target[index].remove(value)



    @staticmethod
    def batched(iterable: Iterable, size: int):
        """
        Inspired by: https://docs.python.org/3/library/itertools.html#itertools.batched, itertools function in Python 3.12
        Batch data from the iterable into tuples of length n. The last batch may be shorter than n.
        Loops over the input iterable and accumulates data into lists up to size n. The input is consumed lazily, just enough to fill a batch. The result is yielded as soon as the batch is full or when the input iterable is exhausted
        e.g:
        flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar', 'sweet']
        unflattened = list(batched(flattened_data, 2))
        unflattened
        >> [['roses', 'red'], ['violets', 'blue'], ['sugar', 'sweet']]

        :param iterable: An iterable to be batched
        :type iterable: Iterable

        :param size: The size of the batches to be yielded
        :type size: int
        """
        if size < 1:
            raise ValueError('size must be at least one')
        iterator = iter(iterable)
        while batch := list(islice(iterator, size)):
            yield batch


if __name__ == "__main__":
    Sudoko().solver()