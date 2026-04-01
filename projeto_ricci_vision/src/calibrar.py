
import numpy as np
import sys
import os

# 1. PATCH DE COMPATIBILIDADE (Essencial para NumPy 2.x + MXNet em 2026)
if not hasattr(np, "bool"): np.bool = bool
if not hasattr(np, "bool_"): np.bool_ = bool
if not hasattr(np, "float"): np.float = float
if not hasattr(np, "int"): np.int = int

import mxnet as mx
import polars as pl
import networkx as nx
from GraphRicciCurvature.OllivierRicci import OllivierRicci
import cv2

# --- CONFIGURAÇÃO DE CAMINHOS ABSOLUTOS (A AMARRA DO DIRETÓRIO) ---
# Define a raiz do projeto: /home/devildev/ESTRUTURA_RESSONANCIA/projeto_ricci_vision
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUT_DIR = os.path.join(BASE_DIR, 'output')

os.makedirs(OUT_DIR, exist_ok=True)

def processar_hiperplano_ricci():
    caminho_npy = os.path.join(DATA_DIR, 'onda_pixels.npy')
    
    # 2. Carregar Matriz de Onda (Massa do Anel Benzênico)
    if not os.path.exists(caminho_npy):
        print(f"❌ Erro: Arquivo não encontrado em {caminho_npy}")
        return

    # allow_pickle=True resolve o erro de carregamento de objetos complexos
    onda_raw = np.load(caminho_npy, allow_pickle=True).astype('float32')
    
    # 3. MXNet: Transformar Brilho em Campo de Massa Zeta
    onda_nd = mx.nd.array(onda_raw)
    onda_prob = mx.nd.softmax(onda_nd / 5.0).asnumpy()
    
    escala = 32
    onda_red = cv2.resize(onda_prob, (escala, escala))

    # 4. Sobel: Relevo Geométrico para o Carbono Zeta
    grad_x = cv2.Sobel(onda_red, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(onda_red, cv2.CV_64F, 0, 1, ksize=3)
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)

    # 5. Polars: Telemetria de Gradiente no Hiperplano
    df = pl.DataFrame({
        "id": np.arange(escala * escala),
        "grad": grad_mag.flatten()
    })

    # 6. Grafo Geometrizado (C6 - Estrutura de Lewis)
    G = nx.grid_2d_graph(escala, escala)
    nodes = list(G.nodes())
    
    for u, v in G.edges():
        g_u = df[nodes.index(u), "grad"]
        g_v = df[nodes.index(v), "grad"]
        # Métrica: Onde a 'nuvem' de elétrons muda, a curvatura nasce
        G[u][v]['weight'] = 1.0 + (g_u + g_v) * 100.0

    # 7. Cálculo de Ricci via OTD (Transporte Ótimo de Massa)
    print(f"⚛️  Calculando Ricci sobre Relevo do Anel Zeta (2026)...")
    orc = OllivierRicci(G, alpha=0.5, method="OTD", verbose="ERROR")
    orc.compute_ricci_curvature()

    # 8. Reconstrução e Visualização (JET Color Map)
    mapa_ricci = np.zeros((escala, escala), dtype=float)
    for n1, n2 in G.edges():
        curv = G[n1][n2].get("ricciCurvature", 0)
        mapa_ricci[n1] += curv

    mapa_abs = np.abs(mapa_ricci)
    if np.max(mapa_abs) > 1e-5:
        mapa_log = np.log1p(mapa_abs * 1000)
        mapa_vis = cv2.normalize(mapa_log, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        mapa_colorido = cv2.applyColorMap(mapa_vis, cv2.COLORMAP_JET)
        
        caminho_out = os.path.join(OUT_DIR, 'assinatura_ricci.jpg')
        cv2.imwrite(caminho_out, mapa_vis)
        
        print(f"✅ SUCESSO! Valor Máximo de Curvatura: {np.max(mapa_abs):.6f}")
        cv2.imshow("Ressonancia Zeta (Campo de Ricci)", mapa_colorido)
    else:
        print("⚠️ AVISO: Espaço plano detectado. Verifique o contraste da molécula.")

    print("Pressione qualquer tecla na janela para encerrar o ciclo.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    processar_hiperplano_ricci()
