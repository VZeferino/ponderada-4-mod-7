# Documentação da API e Seu Funcionamento

A API desenvolvida utiliza o framework FastAPI em Python para fazer previsões com base em um modelo de machine learning treinado. A API tem um único endpoint, /prever, que aceita solicitações POST contendo informações sobre a idade (Age), renda anual (Annual_Income_k) e gênero (Gender_Male) de um cliente.

Para fazer uma previsão, o usuário deve enviar uma solicitação HTTP POST com um corpo JSON contendo os valores desses atributos. Por exemplo:

```
{
  "Age": 30,
  "Annual_Income_k": 70,
  "Gender_Male": 1
}
```

A API processará essa solicitação, fará uma previsão com base nos dados fornecidos e retornará uma resposta JSON com a previsão. A previsão é fornecida no campo "previsao" no formato:

```
{
  "previsao": valor_da_previsao
}
```

# Escolha do Modelo de Machine Learning e Justificação

O modelo de machine learning escolhido para este projeto é o Gradient Boosting, mais especificamente o regressor GradientBoostingRegressor da biblioteca scikit-learn. Essa escolha se baseia principalmente no desempenho pois o modelo Gradient Boosting foi o que me deu o melhor resultado.

Foi considerado diversos modelos durante o desenvolvimento, incluindo Regressão Linear, Árvore de Decisão e Random Forest, o Gradient Boosting se destacou em termos de métricas de avaliação, como o Erro Quadrático Médio (MSE) e o coeficiente de determinação (R²)

# Como rodar

Para rodar a apliacação, após clonar o repositório rode

```
docker build -t model:model .
```

depois execute 

```
docker run -p 8000:8000 model:model
```

[Link para o meu contêiner Docker no Docker Hub](https://hub.docker.com/repository/docker/vzeferino/model/general)
