import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import base64;

from utils.grok import interact_with_data

def render_operations_dashboard(data: pd.DataFrame):
    st.header("Operations Dashboard")
    data.dropna(subset=['violent_crime'], inplace=True)
    estados_interesse = ['Maryland', 'Idaho', 'Massachusetts']
    data = data[data['state_name'].isin(estados_interesse)]


    data = data.iloc[1:]

    latest_year = data['year'].max()
    latest_data = data[data['year'] == latest_year]

    # Calculate cost per capita (simplified estimate)
    latest_data['cost_per_capita'] = (latest_data['violent_crime'] * 150000 + latest_data['property_crime'] * 3500) / latest_data['population']

    # Top 10 states by cost per capita
    top_cost_states = latest_data.nlargest(10, 'cost_per_capita')
    fig_cost = px.bar(top_cost_states, x='state_name', y='cost_per_capita', 
                      title="Top 10 States - Estimated Cost per Capita (USD)")
    st.plotly_chart(fig_cost)

    # Top 10 states by violent crime rate
    latest_data['violent_crime_rate'] = latest_data['violent_crime'] / latest_data['population'] * 100000
    top_violent_states = latest_data.nlargest(10, 'violent_crime_rate')
    fig_violent = px.bar(top_violent_states, x='state_name', y='violent_crime_rate', 
                         title="Top 10 States - Violent Crime Rate (per 100,000 inhabitants)")
    st.plotly_chart(fig_violent)

    st.subheader("Forecast of Violent Crime Rate for Next Year")

    data['year'] = pd.to_datetime(data['year']).dt.year
    data['violent_crime_rate'] = data['violent_crime'] / data['population'] * 100000

    features = ['year', 'population', 'property_crime']
    X = data[features]
    y = data['violent_crime_rate']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train_scaled, y_train)

    y_pred = rf_model.predict(X_test_scaled)

    # Calculate evaluation metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    # Display evaluation metrics
    st.subheader("Model Evaluation")
    col1, col2, col3 = st.columns(3)
    col1.metric("R² Score", f"{r2:.3f}")
    col2.metric("Mean Absolute Error", f"{mae:.2f}")
    col3.metric("Root Mean Squared Error", f"{rmse:.2f}")

    # Scatter plot: Predicted vs. Actual Values
    fig_scatter = px.scatter(x=y_test, y=y_pred, 
                             labels={'x': 'Actual Values', 'y': 'Predicted Values'},
                             title="Predicted vs. Actual Values")
    fig_scatter.add_trace(go.Scatter(x=[y_test.min(), y_test.max()], 
                                     y=[y_test.min(), y_test.max()],
                                     mode='lines', name='Reference Line'))
    st.plotly_chart(fig_scatter)

    # Feature Importance Graph
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)

    fig_importance = px.bar(feature_importance, x='feature', y='importance',
                            title="Feature Importance")
    st.plotly_chart(fig_importance)

    # Make predictions for next year
    next_year = latest_year.year + 1
    next_year_data = latest_data[features].copy()
    next_year_data['year'] = next_year
    next_year_data_scaled = scaler.transform(next_year_data)
    predictions = rf_model.predict(next_year_data_scaled)

    next_year_data['predicted_violent_crime_rate'] = predictions
    next_year_data['state_name'] = latest_data['state_name']

    fig_prediction = px.scatter(next_year_data, x='state_name', y='predicted_violent_crime_rate',
                                size='population', hover_data=['property_crime'],
                                title=f"Forecast of Violent Crime Rate for {next_year}")
    st.plotly_chart(fig_prediction)

    next_year_data['increase'] = next_year_data['predicted_violent_crime_rate'] - latest_data['violent_crime_rate']
    top_increase = next_year_data.nlargest(5, 'increase')
    st.write("Top 5 States with the Highest Predicted Increase in Violent Crime Rate:")
    st.table(top_increase[['state_name', 'increase']])

    st.subheader("Data Analysis Assistant")
    
    predefined_questions = [
        "Which states have the highest potential for cost reduction?",
        "Where should we focus our efforts to reduce violent crimes?",
        "What is the relationship between investment in security and crime rates?",
        "How can we optimize resource allocation to maximize security?",
        "Which states need more attention based on predictions for next year?",
        "How does the model's accuracy affect our resource allocation decisions?",
        "What factors have the greatest influence on the violent crime rate, according to the model?"
    ]

    selected_question = st.selectbox("Select a predefined question or type your own:", 
                                     [""] + predefined_questions)
    
    user_question = st.text_input("Your question:", value=selected_question)

    if st.button("Submit Question"):
        if user_question:
            st.write("Communicating with Grok...")
            st.write(f"Question received: {user_question}")
            
            # swap with getting images that Ale added
            base64_image = base64.b64encode(open("program.png", "rb").read()).decode("utf-8")
            images = [base64_image]

            res = interact_with_data(data.describe().to_string(), images, user_question)
            st.write(res.content)
        else:
            st.warning("Please select or type a question.")
