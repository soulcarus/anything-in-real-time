import streamlit as st
import plotly.express as px

def render_correlation_heatmap(filtered_data):
    st.header("Correlação entre Tipos de Crime")
    crime_types = ['homicide', 'rape_revised', 'robbery', 'aggravated_assault', 'burglary', 'larceny', 'motor_vehicle_theft', 'population']
    correlation_data = filtered_data[crime_types]
    correlation_matrix = correlation_data.corr()
    fig_corr = px.imshow(correlation_matrix, text_auto=True, aspect="auto", title="Mapa de Calor da Correlação entre Tipos de Crime")
    st.plotly_chart(fig_corr)
