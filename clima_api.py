import requests

#Consulta gratuita de API do IBGE para listar o estados do Brasil
url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados"
resposta = requests.get(url)

if resposta.status_code ==200:
    estados = resposta.json()
    print(f"Conexão ok! Total de estados encontrados: {len(estados)}")
    for estado in estados [:5]:  # Exibe apenas os 5 primeiros estados
        print(f"{estado['sigla']} - {estado['nome']}")

else:
    print("Erro ao conectar na API.")
    