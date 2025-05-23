import streamlit as st
import pandas as pd
from datetime import datetime

@st.cache_data
def load_data():
  df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
  # Filtrar jogadores que não tem contrato válido
  invalid_contracts = df_data[df_data['Contract Valid Until'] < datetime.today().year]
  # Atribuindo um novo clube
  invalid_contracts_copy = invalid_contracts.copy()
  invalid_contracts_copy['Club'] = 'Sem contrato'
  invalid_contracts_copy['Club Logo'] = 'https://cdn-icons-png.flaticon.com/512/512/512605.png'
  # Atualizando dataframe original
  valid_contracts = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
  df_data = pd.concat([valid_contracts, invalid_contracts_copy], ignore_index=True)
  # Excluindo valores que não tem valores registrados
  df_data = df_data[df_data['Value(£)'] > 0]
  # Ordenando por overall
  df_data = df_data.sort_values(by='Overall', ascending=False)
  # Resetando o index
  df_data = df_data.reset_index(drop=True)
  
  return df_data

def get_data():
  if 'data' not in st.session_state:
    st.session_state['data'] = load_data()
  
  return st.session_state['data']

def setup_sidebar(has_divider=True):
  if has_divider:
    st.sidebar.markdown('---')
  st.sidebar.markdown('Desenvolvido por [Asimov Academy](https://www.asimov.academy/)')
  st.sidebar.markdown('Adicionais por [Augusto Seabra](https://github.com/skti-dev)')