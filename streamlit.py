import streamlit as st
import pandas as pd

st.title("Manipulação de Dados com Streamlit")

df = pd.DataFrame({
  'Nome': ["João Carlos", "Maria Marcia", "Jonas Marcio", "José Marcos"],
  'Ocupação': ["professor", "caixa", "pedreiro", "empresário"]
})

df