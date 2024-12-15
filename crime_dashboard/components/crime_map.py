import streamlit as st
import plotly.express as px

def render_crime_map(filtered_data):
    st.header("Taxas de Crime Violento por Estado (Último Ano)")
    latest_year = filtered_data['year'].max()
    latest_data = filtered_data[filtered_data['year'] == latest_year]
    latest_data['violent_crime_rate'] = latest_data['violent_crime'] / latest_data['population'] * 100000

    fig_map = px.choropleth(latest_data, 
                            locations='state_abbr', 
                            locationmode="USA-states", 
                            color='violent_crime_rate',
                            scope="usa",
                            title=f"Taxa de Crime Violento por 100.000 Habitantes ({latest_year.year})",
                            color_continuous_scale="Viridis")
    st.plotly_chart(fig_map)

