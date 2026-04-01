
import polars as pl
import numpy as np

# 1. Carregar o Catálogo de Memória (Parquet)
caminho_db = "data/catalogo_geometrico.parquet"
db = pl.read_parquet(caminho_db)

# 2. Carregar a Telemetria que está no Sensor AGORA (CSV)
atual = pl.read_csv("output/telemetria_imagem.csv")
m_atual = atual["curvatura_ricci"].mean()
d_atual = atual["curvatura_ricci"].std()

print(f"\n--- SENSOR ATUAL ---")
print(f"Média: {m_atual:.6f} | Desvio: {d_atual:.6f}")

# 3. Cruzamento via Polars (Cálculo de Proximidade no Hiperplano)
resultado = db.with_columns([
    ( ((pl.col("media") - m_atual)**2 + (pl.col("desvio") - d_atual)**2).sqrt() ).alias("distancia")
]).sort("distancia")

# 4. Decisão do Sistema (CORRIGIDO)
identidade = resultado[0, "objeto"]
proximidade = resultado[0, "distancia"]

print("\n--- RESULTADO DO RECONHECIMENTO ---")
print(resultado)

# Correção do Nome da Variável aqui:
if proximidade < 0.001:
    print(f"\nSISTEMA: Identidade Confirmada -> '{identidade}' (Precisão: 100%)")
else:
    print(f"\nSISTEMA: O objeto mais provável é '{identidade}' (Distância: {proximidade:.6f})")

# DICA: Para o OpenFrameworks, você pode salvar apenas o 'nome' identificado:
with open("output/identidade_detectada.txt", "w") as f:
    f.write(identidade)
