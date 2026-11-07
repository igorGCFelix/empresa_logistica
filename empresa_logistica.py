import pandas as panda

def achar_outliers_iqr(serie):
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - 1.5 * iqr
    limite_superior = q3 + 1.5 * iqr
    return serie[(serie < limite_inferior) | (serie > limite_superior)]


def achar_outliers_z(serie):
    z = (serie - serie.mean()) / serie.std()
    return serie[abs(z) > 3]

def achar_media(serie):
    media = serie.mean()
    return media

def achar_mediana(serie):
    mediana = serie.median()
    return mediana



colunas = [
    'id_veiculo', 'data_viagem', 'tempo_viagem', 'velocidade_media',
    'consumo_combustivel', 'carga_transportada', 'id_motorista',
    'feedback_cliente'
]

data = panda.read_csv('empresa_logistica.csv', header=None, names=colunas)
data['data_viagem'] = panda.to_datetime(data['data_viagem'])

id_veiculo = data['id_veiculo']
data_viagem = data['data_viagem']
tempo_viagem = data['tempo_viagem']
velocidade_media = data['velocidade_media']
consumo_combustivel = data['consumo_combustivel']
carga_transportada = data['carga_transportada']
id_motorista = data['id_motorista']
feedback_cliente = data['feedback_cliente']

colunas_numericas = {
    'tempo_viagem': tempo_viagem,
    'velocidade_media': velocidade_media,
    'consumo_combustivel': consumo_combustivel,
    'carga_transportada': carga_transportada,
    'feedback_cliente': feedback_cliente,
}

for nome, serie in colunas_numericas.items():
    outliers_iqr = achar_outliers_iqr(serie)
    outliers_z = achar_outliers_z(serie)
    media = achar_media(serie)
    mediana = achar_mediana(serie)

    print(f"\n=== {nome} ===")
    print(f"IQR: {len(outliers_iqr)} outlier(s)")
    print(f"Z-score: {len(outliers_z)} outlier(s)")
    print(f"Media: {media} ")
    print(f"Mediana: {mediana} ")

    if not outliers_iqr.empty:
        print(data.loc[outliers_iqr.index])
    if not outliers_z.empty:
        print(data.loc[outliers_z.index])
        
maximo = data['feedback_cliente'].max()
minimo = data['feedback_cliente'].min()
print("\nNota máxima: ", maximo, "Nota Mínima: ", minimo)


for linha in zip(id_veiculo, data_viagem, tempo_viagem, velocidade_media, consumo_combustivel, carga_transportada, id_motorista, feedback_cliente):
    if linha[7] == maximo:
        print(f"id veiculo: {linha[0]}, data viagem: {linha[1]}, tempo viagem: {linha[2]}, " f"velocidade media: {linha[3]}, consumo combustivel: {linha[4]}, "f"carga transportada: {linha[5]}, id motorista: {linha[6]}, "f"feedback cliente: {linha[7]}")
        
    elif linha[7] == minimo:
            print(f"id veiculo: {linha[0]}, data viagem: {linha[1]}, tempo viagem: {linha[2]}, " f"velocidade media: {linha[3]}, consumo combustivel: {linha[4]}, "f"carga transportada: {linha[5]}, id motorista: {linha[6]}, "f"feedback cliente: {linha[7]}")
    

