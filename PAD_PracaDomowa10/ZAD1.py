import streamlit as st
import pandas as pd
import plotly.express as px
import streamlit as st
import time

from streamlit_option_menu import option_menu

if 'first_attempt' not in st.session_state:
    st.session_state.first_attempt = True
if 'data' not in st.session_state:
    st.session_state.data = None

with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options=['Ankieta', 'Staty'],
        icons = ['clipboard-check', 'file-earmark-bar-graph'],
        menu_icon = 'cast',
        default_index = 0
    )

if selected == 'Ankieta':
    firstname = st.text_input("Wpisz imie...")
    if st.button("Zapisz"):
        result = firstname.title()
        st.success(f'Poprawnie zapisano imie. Twoje imie to {result}.')

if selected == "Staty":
    data = st.file_uploader("Wczytaj dane", type=['csv'])
    
    if data is not None:
        if data != st.session_state.data:
            with st.spinner("Nie pędz tak..."):
                time.sleep(2)
            st.session_state.data = data
            
        df = pd.read_csv(data) 
        my_table =  st.dataframe(df.head(10))

        type_of_plot = st.selectbox("Jaki wykres...", ("pudełkowy", "histogram"))
        if type_of_plot == 'pudełkowy':
            which_data = st.selectbox('Ktore dane pokazac', df.columns)
            fig = px.box(df[which_data])
            st.write(fig)
        if type_of_plot == 'histogram':
            which_data = st.selectbox('Ktore dane pokazac', df.columns)
            fig = px.histogram(df, x= df[which_data])
            st.write(fig) 