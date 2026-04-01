import polars as pl
import os

def registrar_identidade(nome_do_objeto):
    caminho_csv = "output/telemetria_imagem.csv"
    caminho_db = "data/catalogo_geometrico.parquet"
    
    # 1. Ler a telemetria do sensor (pixels brutos)
    if not os.path.exists(caminho_csv):
        print("Erro: Gere a telemetria primeiro!")
        return
        
    df_sensor = pl.read_csv(caminho_csv)
    
    # 2. Criar a nova linha CALCULANDO as estatísticas da coluna 'curvatura_ricci'
    nova_linha = df_sensor.select([
        pl.lit(nome_do_objeto).alias("objeto"),
        pl.col("curvatura_ricci").mean().alias("media"),
        pl.col("curvatura_ricci").std().alias("desvio")
    ])

    # 3. Lógica de MEMÓRIA (Acumular no Parquet)
    if os.path.exists(caminho_db):
        db_antigo = pl.read_parquet(caminho_db)
        # Remove se o objeto já existir para atualizar os valores
        db_filtrado = db_antigo.filter(pl.col("objeto") != nome_do_objeto)
        db_final = pl.concat([db_filtrado, nova_linha])
    else:
        db_final = nova_linha

    # 4. Salvar o Catálogo Geométrico
    db_final.write_parquet(caminho_db)
    
    print("\n--- CATÁLOGO NO HIPERPLANO (MEMÓRIA ATIVA) ---")
    print(db_final.sort("objeto"))

if __name__ == "__main__":
    # --- TESTE AGORA COM A ONDA ORGÂNICA ---
    registrar_identidade("Onda_Geometrica")

