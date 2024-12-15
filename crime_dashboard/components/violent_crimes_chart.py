import streamlit as st
import plotly.express as px

def render_violent_crimes_chart(filtered_data):
    st.header("Crimes Violentos ao Longo do Tempo")
    fig_violent = px.line(filtered_data, x='year', y='violent_crime', color='state_name', title="Crimes Violentos por Estado ao Longo do Tempo")
    st.plotly_chart(fig_violent)

