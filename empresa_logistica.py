import pandas as panda

def achar_outliers_iqr(serie):
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    return serie[(serie < limite_inferior) | (serie > limite_superior)]

colunas = [
    'id_veiculo', 'data_viagem', 'tempo_viagem', 'velocidade_media', 'consumo_combustivel', 'carga_transportada', 'id_motorista', 'feedback_cliente'   
]

data = panda.read_csv('empresa_logistica.csv', header=None, names=colunas)

id_veiculo = data['id_veiculo']
data_viagem = data['data_viagem']
tempo_viagem = data['tempo_viagem']
velocidade_media = data['velocidade_media']
consumo_combustivel = data['consumo_combustivel']
carga_transportada = data['carga_transportada']
id_motorista = data['id_motorista']
feedback_cliente = data['feedback_cliente']

z = (velocidade_media - velocidade_media.mean()) / velocidade_media.std()
outliers_z = velocidade_media[abs(z) > 3]
print(outliers_z)

# for i in range(len(data)):
#     print(
#         "id veiculo: ", id_veiculo[i],", data viagem: ", data_viagem[i], ", tempo viagem: ", tempo_viagem[i],
#         "velocidade media: ", velocidade_media[i], ", consumo combustivel: ", consumo_combustivel[i],
#         "carga transportada: ", carga_transportada[i],", id motorista: ", id_motorista[i], ", feedback cliente", feedback_cliente[i]
#     )
    
print(achar_outliers_iqr(velocidade_media))
# VERIFICAR TODAS AS DISCREPANSEAS COM AS COLUNAS NUMÉRICAS!!