import streamlit as st

def render_overview_stats(filtered_data):
    st.header("Estatísticas Gerais")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Crimes Violentos", f"{filtered_data['violent_crime'].sum():,}")
    col2.metric("Total de Crimes contra a Propriedade", f"{filtered_data['property_crime'].sum():,}")
    col3.metric("Total de Homicídios", f"{filtered_data['homicide'].sum():,}")

