import streamlit as st

def render_overview_stats(filtered_data):
    st.header("General Statistics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Violent Crimes", f"{filtered_data['violent_crime'].sum():,}")
    col2.metric("Total Property Crimes", f"{filtered_data['property_crime'].sum():,}")
    col3.metric("Total Homicides", f"{filtered_data['homicide'].sum():,}")
