import streamlit as st
import plotly.express as px

def render_crime_map(filtered_data):
    st.header("Violent Crime Rates by State (Last Year)")
    latest_year = filtered_data['year'].max()
    latest_data = filtered_data[filtered_data['year'] == latest_year]
    latest_data['violent_crime_rate'] = latest_data['violent_crime'] / latest_data['population'] * 100000

    fig_map = px.choropleth(latest_data, 
                            locations='state_abbr', 
                            locationmode="USA-states", 
                            color='violent_crime_rate',
                            scope="usa",
                            title=f"Violent Crime Rate per 100,000 People ({latest_year.year})",
                            color_continuous_scale="Viridis")
    fig_map.update_layout(
        autosize=True,
        width=1000,
        height=700,
        margin={"r":0,"t":40,"l":0,"b":0}
    )
    
    st.plotly_chart(fig_map, use_container_width=True)
