
import polars as pl
import numpy as np

# 1. Carregar a telemetria gerada no passo anterior
try:
    df_atual = pl.read_csv("output/telemetria_imagem.csv")
except FileNotFoundError:
    print("Erro: Arquivo de telemetria não encontrado. Rode o script de telemetria primeiro.")
    exit()

# 2. Extrair a "Impressão Digital" com nomes únicos (Alias)
# Isso resolve o DuplicateError
stats_df = df_atual.select([
    pl.col("curvatura_ricci").mean().alias("media"),
    pl.col("curvatura_ricci").std().alias("desvio")
])

# Converter para vetor numérico para o cálculo de distância no hiperplano
stats_vetor = stats_df.to_numpy()[0]
print(f"Telemetria Capturada -> Média: {stats_vetor[0]:.6f}, Desvio: {stats_vetor[1]:.6f}")

# 3. Lógica de Identificação por Proximidade Geométrica
def identificar(stats_referencia, limiar=0.005):
    # Cálculo da distância Euclidiana no espaço de fase da telemetria
    distancia = np.linalg.norm(stats_vetor - stats_referencia)
    
    print(f"Distância Euclidiana no Hiperplano: {distancia:.6f}")
    
    if distancia < limiar:
        return "SISTEMA: Identidade Geométrica Confirmada. (A onda coincide)"
    else:
        return "SISTEMA: Identidade Desconhecida. (Geometria divergente)"

# 4. Teste de Identificação (Usando os valores que você obteve no terminal)
# Referência baseada nos seus dados anteriores: media=0.066, desvio=0.081
referencia_alvo = np.array([0.066374, 0.081518])
resultado = identificar(referencia_alvo)

print("-" * 40)
print(resultado)
print("-" * 40)
