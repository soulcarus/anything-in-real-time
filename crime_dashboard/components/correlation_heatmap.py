import streamlit as st
import plotly.express as px

def render_correlation_heatmap(filtered_data):
    st.header("Types of Crime Correlation")
    crime_types = ['homicide', 'rape_revised', 'robbery', 'aggravated_assault', 'burglary', 'larceny', 'motor_vehicle_theft', 'population']
    correlation_data = filtered_data[crime_types]
    correlation_matrix = correlation_data.corr()
    fig_corr = px.imshow(correlation_matrix, text_auto=True, aspect="auto", title="Correlation Heatmap")
    st.plotly_chart(fig_corr)
