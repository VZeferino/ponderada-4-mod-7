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

# Como rodar

Abra o EC2 e rode os comandos

```
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip -y
git clone https://github.com/VZeferino/ponderada-4-mod-7.git
cd ponderada-4-mod-7
python3 -m pip install -r requirements.txt
sudo iptables -t nat -I PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 5000
sudo iptables -I INPUT -p tcp --dport 5000 -j ACCEPT
```

para então iniciar o servidor

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

com o servidor rodando deve-se então criar uma nova instância e executar o frontend, seguindo os seguintes comandos:

```
sudo apt update
sudo apt upgrade
sudo apt install python3 python3-pip -y
git clone https://github.com/VZeferino/ponderada-4-mod-7.git
cd ponderada-4-mod-7
python3 -m pip install -r requirements.txt
```

para então iniciar o front

```
streamlit run dash.py
```

Lembrando de estar com as permissões para as portas corretas.
