import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    data = pd.read_csv("data/estimated_crimes_series.csv")
    
    data['year'] = pd.to_datetime(data['year'], format='%Y')
    numeric_columns = ['population', 'violent_crime', 'homicide', 'rape_legacy', 'rape_revised', 
                       'robbery', 'aggravated_assault', 'property_crime', 'burglary', 'larceny', 'motor_vehicle_theft']
    for col in numeric_columns:
        data[col] = pd.to_numeric(data[col], errors='coerce')
    
    return data
