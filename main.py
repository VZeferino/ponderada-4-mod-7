from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

# Inicialize o aplicativo FastAPI
app = FastAPI() 

modelo_gb = load('modelo_gb.joblib')

# Crie uma classe Pydantic para definir a estrutura das entradas da API
class EntradaDaAPI(BaseModel):
    Age: int
    Annual_Income_k: int
    Gender_Male: int  # Use 0 para Female e 1 para Male

@app.post("/prever")
async def prever_valores(entrada: EntradaDaAPI):
    age = entrada.Age
    annual_income = entrada.Annual_Income_k
    gender_male = entrada.Gender_Male

    # Faça uma previsão usando o modelo Gradient Boosting
    previsao = modelo_gb.predict([[age, annual_income, gender_male]])[0]

    return {"previsao": previsao}
