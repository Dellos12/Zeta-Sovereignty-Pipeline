
import numpy as np
import sys

# 1. PATCH DE COMPATIBILIDADE (Fix para NumPy 2.x e MXNet)
if not hasattr(np, "bool"): np.bool = bool
if not hasattr(np, "bool_"): np.bool_ = bool
if not hasattr(np, "float"): np.float = float
if not hasattr(np, "int"): np.int = int
import polars as pl
import mxnet as mx
import cv2

# 1. Carregar a onda original (A base da telemetria)
onda_raw = np.load('data/onda_pixels.npy')
escala = 32
onda_red = cv2.resize(onda_raw, (escala, escala)).astype(float)

# 2. MXNet: Normalização para Telemetria
# Transformamos em log-espaço para evitar o 'branco' (estouro de valor)
onda_log = mx.nd.log(mx.nd.array(onda_red) + 1.0).asnumpy()

# 3. Cálculo de Ricci (Simplificado para Telemetria Local)
# Vamos calcular a 'Variação Geométrica Local' (VGL)
# que é a base da curvatura de Ricci nas arestas
v_grad = np.gradient(onda_log)
curvatura_local = np.sqrt(v_grad[0]**2 + v_grad[1]**2)

# 4. Amarra com Polars: O Log de Telemetria
# Aqui transformamos a geometria em dados de navegação
telemetria = pl.DataFrame({
    "pixel_id": np.arange(escala * escala),
    "latitude_x": np.repeat(np.arange(escala), escala),
    "longitude_y": np.tile(np.arange(escala), escala),
    "amplitude_onda": onda_red.flatten(),
    "curvatura_ricci": curvatura_local.flatten()
})

# 5. Análise da Telemetria (Por que a tela está branca?)
stats = telemetria.select([
    pl.col("curvatura_ricci").mean().alias("media"),
    pl.col("curvatura_ricci").max().alias("pico_onda"),
    pl.col("curvatura_ricci").std().alias("desvio_padrao")
])

print("--- TELEMETRIA DO HIPERPLANO ---")
print(stats)

# Salvar telemetria para o Reconhecimento
telemetria.write_csv("output/telemetria_imagem.csv")
print("\nTelemetria salva em output/telemetria_imagem.csv")

