import numpy as np
import networkx as nx
import ot
from GraphRicciCurvature.OllivierRicci import OllivierRicci

def validar_geometria_zeta(token_a, token_b):
    print("\n" + "="*40)
    print(f"🧪 TESTANDO GEOMETRIA: {token_a} + {token_b}")
    print("="*40)
    
    G = nx.Graph()
    for i in range(6):
        G.add_edge(i, (i + 1) % 6, weight=1.0)
    
    if str(token_a) == str(token_b):
        print("🌀 ATIVANDO DOBRA ORTO-PARA (0-3)")
        G.add_edge(0, 3, weight=0.1)
    
    try:
        # Usamos o peso explicitamente para o NetworKit
        orc = OllivierRicci(G, weight="weight", alpha=0.5, verbose="ERROR")
        orc.compute_ricci_curvature()
        
        adj = nx.adjacency_matrix(G, weight='ricciCurvature').todense()
        
        print("\n✅ MATRIZ DE RICCI GERADA (Embedding):")
        print(np.around(adj, decimals=4))
        
        curv_dobra = G[0][3]['ricciCurvature']
        print(f"\n📊 Curvatura na Dobra (Manifold): {curv_dobra:.4f}")
        
        if curv_dobra > 0.5:
            print("💎 STATUS: CARBONO ZETA ESTÁVEL (1+1=0)")
        else:
            print("⚠️ AVISO: A onda pode se dissipar.")
            
    except Exception as e:
        print(f"❌ FALHA: {str(e)}")

if __name__ == "__main__":
    validar_geometria_zeta(1, 1)
