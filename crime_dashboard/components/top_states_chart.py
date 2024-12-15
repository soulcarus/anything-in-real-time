import streamlit as st
import plotly.express as px

def render_top_states_chart(filtered_data):
    st.header("Top 10 States with the Highest Crime Rates (Last Year)")
    latest_year = filtered_data['year'].max()
    latest_data = filtered_data[filtered_data['year'] == latest_year]
    latest_data['violent_crime_rate'] = latest_data['violent_crime'] / latest_data['population'] * 100000
    top_10_violent = latest_data.nlargest(10, 'violent_crime_rate')
    fig_top10 = px.bar(top_10_violent, x='state_name', y='violent_crime_rate', title="Top 10 States by Violent Crime Rate")
    st.plotly_chart(fig_top10)
