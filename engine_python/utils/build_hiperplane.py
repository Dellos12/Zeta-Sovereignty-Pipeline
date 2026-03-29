import pandas as pd
import os

os.makedirs('shared_data', exist_ok=True)

# ESPECIALISTA EM QUÍMICA E METRAGEM (Triade de Valência)
df_quimica = pd.DataFrame({
    'posicao_anel': ['orto', 'meta', 'para', 'meta2', 'meta3', 'meta4'],
    'eletronegatividade': [2.55, 0.0, 2.55, 0.0, 0.0, 0.0],
    'fase_rad': [0.0, 2.0944, 3.1415, 0.0, 0.0, 0.0], # 0, 120, 180 graus
    'assinatura_limite': [1.2006931305] * 6
})

df_quimica.to_parquet('shared_data/silver_quimica.parquet')
print("✅ Camada Silver atualizada com a Triade Orto-Meta-Para.")

