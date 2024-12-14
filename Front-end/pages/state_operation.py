import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Public Security System", page_icon=":shield:", layout="wide")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# sidebar 
st.sidebar.title("Public Security System") 
st.sidebar.markdown("---")
page = st.sidebar.radio("", ["Dashboard", "State Operation", "Config", "User"])  

st.sidebar.markdown("---")
st.sidebar.button("Logout")  


# Title of the page
st.title("State Operation")
st.markdown("---")
# Display metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="metric-card"><h4>Current Crime Rate</h4><p>450</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><h4>Projected Crime Rate</h4><p>470</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><h4>Current Budget</h4><p>$1.2 Billion</p></div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="metric-card"><h4>Suggested Budget</h4><p>$1.5 Billion</p></div>', unsafe_allow_html=True)
st.markdown("---")

# Line graph for crime rate projection
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Crime Rate Projection")
    crime_data = pd.DataFrame({
        'Year': [2023, 2024, 2025, 2026, 2027],
        'Crime Rate': [450, 460, 470, 480, 490]
    })        
    st.line_chart(crime_data.set_index('Year'))

with col2:
# Key Crime Indicators section
    st.markdown("### Key Crime Indicators")
    key_indicators_data = {
       "Violent Crime Rate": "35%",
        "Property Crime Rate": "50%",
        "Clearance Rate": "60%",
        "Recidivism Rate": "20%"
    }
    for indicator, value in key_indicators_data.items():
        st.markdown(f'<div><h5>{indicator}</h5><p>{value}</p></div>', unsafe_allow_html=True)

st.markdown("---")

# AI Recommendations, mock
st.markdown("### AI Recommendations for Texas")
ai_recommendations = """
- Increase security funding in urban areas with rising crime rates.
- Focus on rehabilitation programs for high-risk individuals to reduce recidivism.
- Deploy AI-powered surveillance tools to monitor crime hotspots in real-time.
- Reallocate resources to regions with increasing property crime rates.
"""
st.markdown(f'<div class="ai-recommendations"><p>{ai_recommendations}</p></div>', unsafe_allow_html=True)
