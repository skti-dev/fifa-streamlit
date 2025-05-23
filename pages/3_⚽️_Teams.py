import streamlit as st
from utils import get_data, setup_sidebar

st.set_page_config(
  page_title="Teams",
  page_icon="⚽️",
  layout="wide"
)

df_data = get_data()

clubs = df_data['Club'].unique()
club = st.sidebar.selectbox('Selecione um clube', clubs)

df_clubs = df_data[(df_data['Club'] == club)].set_index('Name')

current_club = df_clubs.iloc[0]

st.title(current_club['Club'])
st.image(current_club['Club Logo'], width=30)

df_clubs['Height(m)'] = (df_clubs['Height(cm.)'] / 100).round(2)
df_clubs['Weight(kg)'] = (df_clubs['Weight(lbs.)'] * 0.453).round(2)

columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 'Height(m)', 'Weight(kg)', 'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_clubs[columns], 
             column_config={
               'Overall': st.column_config.ProgressColumn(
                 'Overall', min_value=0, max_value=100, format='%d'
               ),
               'Value(£)': st.column_config.ProgressColumn('Value(£)', format='£%.2f', min_value=0, max_value=df_clubs['Value(£)'].max()),
               'Wage(£)': st.column_config.ProgressColumn('Weekly Wage(£)', format='£%.2f', min_value=0, max_value=df_clubs['Wage(£)'].max()),
               'Photo': st.column_config.ImageColumn(),
               'Flag': st.column_config.ImageColumn('Country'),
               'Release Clause(£)': st.column_config.ProgressColumn('Release Clause(£)', format='£%.2f', min_value=0, max_value=df_clubs['Release Clause(£)'].max()),
               'Height(m)': st.column_config.NumberColumn('Height (m)', format='%.2f m'),
               'Weight(kg)': st.column_config.NumberColumn('Weight (kg)', format='%.2f kg'),
             })

setup_sidebar()
