import streamlit as st
import requests

# Função para fazer uma solicitação POST para a API
def fazer_solicitacao():
    age = st.slider('Age', 18, 100, 30)
    annual_income = st.slider('Annual Income (k)', 0, 200, 50)
    gender_male = st.radio('Gender', ['Female', 'Male'])

    # Mapear o gênero para 0 (Female) ou 1 (Male)
    gender_mapping = {'Female': 0, 'Male': 1}
    gender_male = gender_mapping[gender_male]

    # Criar os dados de entrada
    data = {
        'Age': age,
        'Annual_Income_k': annual_income,
        'Gender_Male': gender_male
    }

    # Fazer uma solicitação POST para a API
    response = requests.post('http://localhost:8000/prever', json=data)

    if response.status_code == 200:
        resultado = response.json()
        st.write(f'Previsão: {resultado["previsao"]}')
    else:
        st.write('Erro ao fazer a previsão.')

# Configurar a interface do Streamlit
st.title('Dashboard de Previsão')
st.write('Insira os dados abaixo para fazer uma previsão.')

fazer_solicitacao()
