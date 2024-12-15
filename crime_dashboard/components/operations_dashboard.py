import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def render_operations_dashboard(data: pd.DataFrame):
    st.header("Painel de Operações")
    data.dropna(subset=['violent_crime'], inplace=True)
    data = data.iloc[1:]

    # Preparar dados para o ano mais recente
    latest_year = data['year'].max()
    latest_data = data[data['year'] == latest_year]

    # Calcular custo por capita (estimativa simplificada)
    latest_data['cost_per_capita'] = (latest_data['violent_crime'] * 150000 + latest_data['property_crime'] * 3500) / latest_data['population']

    # Top 10 estados por custo per capita
    top_cost_states = latest_data.nlargest(10, 'cost_per_capita')
    fig_cost = px.bar(top_cost_states, x='state_name', y='cost_per_capita', 
                      title="Top 10 Estados - Custo Estimado por Capita (USD)")
    st.plotly_chart(fig_cost)

    # Top 10 estados por taxa de crimes violentos
    latest_data['violent_crime_rate'] = latest_data['violent_crime'] / latest_data['population'] * 100000
    top_violent_states = latest_data.nlargest(10, 'violent_crime_rate')
    fig_violent = px.bar(top_violent_states, x='state_name', y='violent_crime_rate', 
                         title="Top 10 Estados - Taxa de Crimes Violentos (por 100.000 habitantes)")
    st.plotly_chart(fig_violent)

    # Previsão de taxa de crimes violentos para o próximo ano
    st.subheader("Previsão de Taxa de Crimes Violentos para o Próximo Ano")

    # Preparar dados para o modelo
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

    # Calcular métricas de avaliação
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))

    # Exibir métricas de avaliação
    st.subheader("Avaliação do Modelo")
    col1, col2, col3 = st.columns(3)
    col1.metric("R² Score", f"{r2:.3f}")
    col2.metric("Mean Absolute Error", f"{mae:.2f}")
    col3.metric("Root Mean Squared Error", f"{rmse:.2f}")

    # Gráfico de dispersão: Valores Previstos vs. Reais
    fig_scatter = px.scatter(x=y_test, y=y_pred, 
                             labels={'x': 'Valores Reais', 'y': 'Valores Previstos'},
                             title="Valores Previstos vs. Reais")
    fig_scatter.add_trace(go.Scatter(x=[y_test.min(), y_test.max()], 
                                     y=[y_test.min(), y_test.max()],
                                     mode='lines', name='Linha de Referência'))
    st.plotly_chart(fig_scatter)

    # Gráfico de Importância das Features
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': rf_model.feature_importances_
    }).sort_values('importance', ascending=False)

    fig_importance = px.bar(feature_importance, x='feature', y='importance',
                            title="Importância das Features")
    st.plotly_chart(fig_importance)

    # Fazer previsões para o próximo ano
    next_year = latest_year.year + 1
    next_year_data = latest_data[features].copy()
    next_year_data['year'] = next_year
    next_year_data_scaled = scaler.transform(next_year_data)
    predictions = rf_model.predict(next_year_data_scaled)

    # Adicionar previsões ao dataframe
    next_year_data['predicted_violent_crime_rate'] = predictions
    next_year_data['state_name'] = latest_data['state_name']

    # Visualizar previsões
    fig_prediction = px.scatter(next_year_data, x='state_name', y='predicted_violent_crime_rate',
                                size='population', hover_data=['property_crime'],
                                title=f"Previsão de Taxa de Crimes Violentos para {next_year}")
    st.plotly_chart(fig_prediction)

    # Mostrar estados com maior aumento previsto
    next_year_data['increase'] = next_year_data['predicted_violent_crime_rate'] - latest_data['violent_crime_rate']
    top_increase = next_year_data.nlargest(5, 'increase')
    st.write("Top 5 Estados com Maior Aumento Previsto na Taxa de Crimes Violentos:")
    st.table(top_increase[['state_name', 'increase']])

    # Assistente de Análise de Dados
    st.subheader("Assistente de Análise de Dados")
    
    predefined_questions = [
        "Quais estados têm o maior potencial para redução de custos?",
        "Onde devemos focar nossos esforços para reduzir crimes violentos?",
        "Qual é a relação entre investimento em segurança e taxas de criminalidade?",
        "Como podemos otimizar a alocação de recursos para maximizar a segurança?",
        "Quais estados precisam de mais atenção com base nas previsões para o próximo ano?",
        "Como a precisão do modelo afeta nossas decisões de alocação de recursos?",
        "Quais fatores têm maior influência na taxa de crimes violentos, segundo o modelo?"
    ]

    selected_question = st.selectbox("Selecione uma pergunta predefinida ou digite sua própria:", 
                                     [""] + predefined_questions)
    
    user_question = st.text_input("Sua pergunta:", value=selected_question)

    if st.button("Enviar Pergunta"):
        if user_question:
            st.write("Resposta simulada do LLM:")
            st.write("Analisando sua pergunta... (Esta é uma resposta simulada do assistente de IA)")
            st.write(f"Pergunta recebida: {user_question}")
            st.write("Para uma implementação real, você precisaria integrar com um serviço de LLM como OpenAI GPT ou similar.")
        else:
            st.warning("Por favor, selecione ou digite uma pergunta.")