import streamlit as st
from utils.data_loader import load_data
from components.filters import render_filters
from components.overview_stats import render_overview_stats
from components.violent_crimes_chart import render_violent_crimes_chart
from components.crime_type_breakdown import render_crime_type_breakdown
from components.crime_map import render_crime_map
from components.correlation_heatmap import render_correlation_heatmap
from components.top_states_chart import render_top_states_chart
from components.data_table import render_data_table
from components.operations_dashboard import render_operations_dashboard

st.set_page_config(page_title="Real-Time Crime Dashboard", layout="wide")

data = load_data()

st.title("Real-Time Crime Dashboard")

tab1, tab2 = st.tabs(["Visão Geral", "Operações"])

with tab1:
    # Renderizar filtros
    selected_states, selected_years = render_filters(data)

    # Filtrar dados com base na seleção
    filtered_data = data[data['state_name'].isin(selected_states) & (data['year'].dt.year >= selected_years[0]) & (data['year'].dt.year <= selected_years[1])] if selected_states else data[(data['year'].dt.year >= selected_years[0]) & (data['year'].dt.year <= selected_years[1])]

    # Renderizar componentes
    render_overview_stats(filtered_data)
    render_violent_crimes_chart(filtered_data)
    render_crime_type_breakdown(filtered_data)
    render_crime_map(filtered_data)
    render_correlation_heatmap(filtered_data)
    render_top_states_chart(filtered_data)
    render_data_table(filtered_data)
# teste
with tab2:
    render_operations_dashboard(data)

