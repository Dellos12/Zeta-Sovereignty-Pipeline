import pandas as pd
import numpy as np
import os

# Garante que a pasta shared_data existe
os.makedirs('shared_data', exist_ok=True)

print("⚛️  Gerando Camada Silver: Especialistas do Carbono Zeta...")

# --- 1. Especialista em Eletronegatividade (Química) ---
# Define a força de atração dos '1s' no anel
df_quimica = pd.DataFrame({
    'posicao_anel': ['orto', 'meta', 'para', 'meta_2', 'meta_3', 'meta_4'],
    'eletronegatividade': [2.55, 0.0, 2.55, 0.0, 0.0, 0.0],
    'spin_valencia': [0.5, 0.0, -0.5, 0.0, 0.0, 0.0], # Soma 0.5 + (-0.5) = 0
    'hibridizacao': ['sp3', 'sp3', 'sp3', 'sp3', 'sp3', 'sp3']
})

# --- 2. Especialista em Termodinâmica (Física) ---
# Define a estabilidade da dobra (Entropia vs Entalpia)
df_termica = pd.DataFrame({
    'posicao_anel': ['orto', 'meta', 'para', 'meta_2', 'meta_3', 'meta_4'],
    'energia_livre_gibbs': [-1.2, -0.1, -1.2, -0.1, -0.1, -0.1],
    'ressonancia_huckel': [1, 1, 1, 1, 1, 1] # 4n+2 ativa
})

# --- 3. Especialista em Gramática (Linguística) ---
# Mapeia o diálogo 'Isso' e 'Aquilo'
df_gramatica = pd.DataFrame({
    'token': ['um', 'mais', 'um', 'zero', 'zeta', 'dobra'],
    'classe_quimica': ['orto', 'giro', 'para', 'resultado', 'vácuo', 'buraco'],
    'massa_critica': [1.0, 0.0, 1.0, 0.0, 0.0, 0.0]
})

# Salvando os especialistas no Hiperplano (Medallion Silver)
df_quimica.to_parquet('shared_data/silver_quimica.parquet')
df_termica.to_parquet('shared_data/silver_termodinamica.parquet')
df_gramatica.to_parquet('shared_data/silver_gramatica.parquet')

print("✅ Arquivos Parquet Gerados. O Buraco de Minhoca tem massa agora.")

