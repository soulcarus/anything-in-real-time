import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import folium
from folium.plugins import HeatMap

st.set_page_config(page_title="Public Security System", page_icon=":shield:", layout="wide")
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# main 
st.sidebar.title("Public Security System") 
st.sidebar.markdown("---")
page = st.sidebar.radio("", ["Dashboard", "State Operation", "Config", "User"])  

st.sidebar.markdown("---")
st.sidebar.button("Logout")  


if page == "Dashboard":
    # Dropdown
    state = st.selectbox('USA (All States)', ['Texas', 'Florida', 'California'])

    st.markdown("---")


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="metric-card"><div class="metric-title">Total Crimes</div><div class="metric-value">5000</div></div>', unsafe_allow_html=True) #mock data, replace with actual data
    with col2:
        st.markdown('<div class="metric-card"><div class="metric-title">Security Spendings</div><div class="metric-value">$1.2 Billion</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><div class="metric-title">Crimes Per 100k</div><div class="metric-value">450</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><div class="metric-title">Spending Per Capita</div><div class="metric-value">$450</div></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Graphs
    # st.markdown("### Crime Rates and Security Spending Over Time")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Crime Rates Over Time")
        crime_data = pd.DataFrame({
            'Year': [2018, 2019, 2020, 2021, 2022],
            'Crime Rate': [450, 460, 470, 480, 490]
        })        
        st.line_chart(crime_data.set_index('Year'))

    with col2:
        st.markdown("#### Security Spending Over Time")
        spending_data = pd.DataFrame({
            'Year': [2018, 2019, 2020, 2021, 2022],
            'Spending': [1.0, 1.1, 1.3, 1.4, 1.5]  # Billions of dollars
        })
        st.bar_chart(spending_data.set_index('Year'))

    # Map and AI Assistant

    col1, col2 = st.columns(2)

    with col1:
        # Data for map
        data = pd.DataFrame({
            'latitude': [29.76, 30.2672, 34.0522],
            'longitude': [-95.3698, -97.7431, -118.2437],
            'state': ['Texas', 'Florida', 'California'],
            'crime_count': [500, 300, 450]  # Mock data for crime count to vary heat intensity
        })

        # Base map (US center)
        map_center = [37.0902, -95.7129]  
        m = folium.Map(location=map_center, zoom_start=5)

        # heatmap
        heat_data = [[row['latitude'], row['longitude'], row['crime_count']] for index, row in data.iterrows()]
        HeatMap(heat_data).add_to(m)

        # Markers for each location
        for _, row in data.iterrows():
            folium.Marker(
                location=[row['latitude'], row['longitude']],
                popup=f"State: {row['state']}<br>Crime Count: {row['crime_count']}"
            ).add_to(m)

        st.markdown("### Crimes Heatmap")
        st.components.v1.html(m._repr_html_(), width=355, height=300)


    with col2:
        # Grok Assistant 
            st.markdown("### Grok Assistant")
            st.write("Grok is ready to assist!")

        # Simple chatbot input (static response for now)
            user_input = st.text_input("Type your query:")
            if user_input:
                st.write(f"Grok: I'm here to help with {user_input}!")
