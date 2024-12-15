import streamlit as st

def render_filters(data):
    st.header("Filtros")
    col1, col2 = st.columns(2)
    
    with col1:
        selected_states = st.multiselect("Selecione os Estados", data['state_name'].unique())
    
    with col2:
        selected_years = st.slider("Selecione o Intervalo de Anos", 
                                   int(data['year'].dt.year.min()), 
                                   int(data['year'].dt.year.max()), 
                                   (int(data['year'].dt.year.min()), int(data['year'].dt.year.max())))
    
    return selected_states, selected_years

