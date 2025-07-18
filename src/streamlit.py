import streamlit as st
import time
from solver import SudokuSolver

st.title("Resolvedor de Sudoku")

st.markdown("Insira o tabuleiro abaixo, com o formato visual (ex: `|9| |7| | | | | | |`). Use espaços em branco para células vazias.")

default_board = """
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

text_input = st.text_area("Tabuleiro (9 linhas)", value=default_board, height=250)

if st.button("Resolver Sudoku"):
    lines = text_input.strip().split("\n")
    print(lines)
    print(type(lines))
    if len(lines) != 9:
        st.error("Você deve inserir exatamente 9 linhas.")
    else:
        try:
            solver = SudokuSolver(lines)
            start_time = time.perf_counter()
            result = solver.solve()
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            if result:
                st.success("Sudoku resolvido com sucesso!")
                st.text("\n".join(solver.get_board()))
                st.text(f"Tempo de resolução: {elapsed_time*1000:.1f} milisegundos")
            else:
                st.error("Não foi possível resolver o Sudoku.")
        except Exception as e:
            st.error(f"Erro ao processar o tabuleiro: {e}")
