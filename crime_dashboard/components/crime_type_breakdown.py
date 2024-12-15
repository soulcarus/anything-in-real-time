import streamlit as st
import plotly.express as px

def render_crime_type_breakdown(filtered_data):
    st.header("Crime Type Distribution")
    crime_types = ['homicide', 'rape_revised', 'robbery', 'aggravated_assault', 'burglary', 'larceny', 'motor_vehicle_theft']
    crime_data = filtered_data.groupby('year')[crime_types].sum().reset_index()
    fig_stacked = px.bar(crime_data, x='year', y=crime_types, title="Crime Type Distribution Over Time", labels={'value': 'Number of Crimes', 'variable': 'Crime Type'})
    st.plotly_chart(fig_stacked)
