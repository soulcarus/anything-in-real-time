import streamlit as st

def render_data_table(filtered_data):
    st.header("Dados Brutos")
    st.dataframe(filtered_data)

