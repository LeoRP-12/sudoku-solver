from .sudo_solver import Sudoko


class TestSudoko:
    def test_level1_solver(self):
        board = '''
        | |4| |9|5|3|1|2| |
        |3|1| | | | |9|5| |
        |6| | |1|8| | |7| |
        | |7| | |4| | | | |
        |5|2|6| | | |4|8|9|
        | | | | |9| | |6| |
        | |8| | |2|4| | |1|
        | |6|9| | | | |4|5|
        | |5|1|7|6|9| |3| |
        '''

        Sudoko(board).solver()
        
        assert Sudoko.solved == ""