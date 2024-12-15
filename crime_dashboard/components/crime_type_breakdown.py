import streamlit as st
import plotly.express as px

def render_crime_type_breakdown(filtered_data):
    st.header("Distribuição dos Tipos de Crime")
    crime_types = ['homicide', 'rape_revised', 'robbery', 'aggravated_assault', 'burglary', 'larceny', 'motor_vehicle_theft']
    crime_data = filtered_data.groupby('year')[crime_types].sum().reset_index()
    fig_stacked = px.bar(crime_data, x='year', y=crime_types, title="Distribuição dos Tipos de Crime ao Longo do Tempo", labels={'value': 'Número de Crimes', 'variable': 'Tipo de Crime'})
    st.plotly_chart(fig_stacked)

