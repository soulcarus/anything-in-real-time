import streamlit as st
import plotly.express as px

def render_violent_crimes_chart(filtered_data):
    st.header("Violent Crimes Over Time")
    fig_violent = px.line(filtered_data, x='year', y='violent_crime', color='state_name', title="Violent Crimes by State Over Time")
    st.plotly_chart(fig_violent)
