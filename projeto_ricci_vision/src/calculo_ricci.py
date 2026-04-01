import numpy as np
import sys

# 1. PATCH DE COMPATIBILIDADE (Fix para NumPy 2.x e MXNet)
if not hasattr(np, "bool"): np.bool = bool
if not hasattr(np, "bool_"): np.bool_ = bool
if not hasattr(np, "float"): np.float = float
if not hasattr(np, "int"): np.int = int

import mxnet as mx
import polars as pl
import networkx as nx
from GraphRicciCurvature.OllivierRicci import OllivierRicci
import cv2
import os

# Garantir estrutura de pastas
os.makedirs('output', exist_ok=True)

def processar_hiperplano_ricci():
    # 2. Carregar Matriz de Onda
    if not os.path.exists('data/onda_pixels.npy'):
        print("Erro: Arquivo 'data/onda_pixels.npy' não encontrado.")
        return

    onda_raw = np.load('data/onda_pixels.npy', allow_pickle=True)
    
    # 3. MXNet: Transformar Brilho em Distribuição de Massa
    # O Softmax enfatiza as diferenças, criando 'montanhas' na imagem
    onda_nd = mx.nd.array(onda_raw).astype('float32')
    onda_prob = mx.nd.softmax(onda_nd / 5.0).asnumpy()
    
    escala = 32
    onda_red = cv2.resize(onda_prob, (escala, escala))

    # 4. Sobel: Criar Relevo Geométrico (Atrito da Onda)
    # Calculamos a inclinação para que o espaço deixe de ser plano
    grad_x = cv2.Sobel(onda_red, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(onda_red, cv2.CV_64F, 0, 1, ksize=3)
    grad_mag = np.sqrt(grad_x**2 + grad_y**2)

    # 5. Polars: Indexação de Massa e Gradiente
    df = pl.DataFrame({
        "id": np.arange(escala * escala),
        "grad": grad_mag.flatten()
    })

    # 6. Grafo Geometrizado
    G = nx.grid_2d_graph(escala, escala)
    nodes = list(G.nodes())
    
    for u, v in G.edges():
        # Buscamos o gradiente no Polars para definir o 'peso' (curvatura)
        g_u = df[nodes.index(u), "grad"]
        g_v = df[nodes.index(v), "grad"]
        
        # Métrica: O peso da aresta é aumentado onde há variação de luz (gradiente)
        # Isso 'dobra' o espaço e gera a Curvatura de Ricci
        G[u][v]['weight'] = 1.0 + (g_u + g_v) * 100.0

    # 7. Cálculo de Ricci via OTD (Transporte Ótimo)
    print("Calculando Ricci sobre Relevo Geométrico...")
    orc = OllivierRicci(G, alpha=0.5, method="OTD", verbose="ERROR")
    orc.compute_ricci_curvature()

    # 8. Reconstrução e Visualização Térmica
    mapa_ricci = np.zeros((escala, escala), dtype=float)
    for n1, n2 in G.edges():
        curv = G[n1][n2].get("ricciCurvature", 0)
        mapa_ricci[n1] += curv

    mapa_abs = np.abs(mapa_ricci)
    if np.max(mapa_abs) > 1e-5:
        # Ganho logarítmico para destacar as dobras da onda
        mapa_log = np.log1p(mapa_abs * 1000)
        mapa_vis = cv2.normalize(mapa_log, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
        # Mapa Térmico JET (Azul=Plano, Vermelho=Curvatura)
        mapa_colorido = cv2.applyColorMap(mapa_vis, cv2.COLORMAP_JET)
        
        cv2.imwrite('output/assinatura_ricci.jpg', mapa_vis)
        print(f"Sucesso! Valor Máximo de Curvatura: {np.max(mapa_abs):.6f}")
        cv2.imshow("Geometria da Onda (Ricci Termico)", mapa_colorido)
    else:
        print("Aviso: Espaço ainda plano. Tentando aumentar o contraste da imagem original.")

    print("Pressione qualquer tecla na janela para encerrar.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    processar_hiperplano_ricci()

