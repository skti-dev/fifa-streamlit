import streamlit as st
from utils import get_data, setup_sidebar

st.set_page_config(
  page_title="Players",
  page_icon="🏃🏼",
  layout="wide"
)

df_data = get_data()

clubs = df_data['Club'].unique()
club = st.sidebar.selectbox('Selecione um clube', clubs)

df_players = df_data[(df_data['Club'] == club)]

players = df_players['Name'].unique()
player = st.sidebar.selectbox('Selecione um jogador', players)

player_stats = df_data[df_data['Name'] == player].iloc[0]

st.image(player_stats['Photo'], width=75)

st.title(player_stats['Name'])
st.image(player_stats['Flag'], width=30)
st.markdown(f'**Posição:** {player_stats["Position"]}')
st.markdown(f'**Clube:** {player_stats["Club"]}')

statsCol1, statsCol2, statsCol3, _ = st.columns(4)

statsCol1.markdown(f'**Idade:** {player_stats["Age"]} anos')
statsCol2.markdown(f'**Altura:** {player_stats["Height(cm.)"] / 100:.2f} m')
statsCol3.markdown(f'**Peso:** {player_stats["Weight(lbs.)"] * 0.453:.2f} kg')

st.divider()

st.subheader(f'Overall {player_stats["Overall"]}')
st.progress(int(player_stats['Overall']))

metricCol1, metricCol2, metricCol3, _ = st.columns(4)

metricCol1.metric(label='Valor de mercado', value=f'£ {player_stats["Value(£)"]:,}')
metricCol2.metric(label='Remuneração semanal', value=f'£ {player_stats["Wage(£)"]:,}')
metricCol3.metric(label='Cláusula de rescisão', value=f'£ {player_stats["Release Clause(£)"]:,}')

st.divider()

setup_sidebar()
