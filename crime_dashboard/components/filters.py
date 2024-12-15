import streamlit as st

def render_filters(data):
    st.header("Filters")
    col1, col2 = st.columns(2)
    
    with col1:
        selected_states = st.multiselect("Select States", data['state_name'].unique())
    
    with col2:
        selected_years = st.slider("Select Year Range", 
                                   int(data['year'].dt.year.min()), 
                                   int(data['year'].dt.year.max()), 
                                   (int(data['year'].dt.year.min()), int(data['year'].dt.year.max())))
    
    return selected_states, selected_years
