import os
import sys
import polars as pl
import numpy as np
from sqlalchemy import create_engine, text

# Adiciona /app ao path para encontrar a pasta utils
sys.path.append("/app")

from utils.gramatica_expert import GramaticaExpert
from utils.compliance import NormaABNT
from utils.manifold_shield import ManifoldShield


def persistir_auditoria_zeta(massa, sim, pico, status):
    # Conexão com o pgvector definido no seu docker-compose
    engine = create_engine('postgresql://postgres:password@db_vector:5432/manifold_development')
    
    query = text("""
        INSERT INTO auditoria_zeta 
        (equacao_estado, similaridade_fase, gradiente_ricci_observado, status_compliance, soberania_veredito, created_at, updated_at)
        VALUES (:eq, :sim, :ricci, :status, :veredito, NOW(), NOW())
    """)
    
    with engine.connect() as conn:
        conn.execute(query, {
            "eq": "|ΣΦ| ≈ 1.2006",
            "sim": sim,
            "ricci": pico,
            "status": "CONFORME",
            "veredito": status
        })
        conn.commit()
    print("🗄️  AUDITORIA PERSISTIDA NO PGVECTOR: SOBERANIA REGISTRADA.")


def executar_salto_zeta_docker():
    print("⚛️  MOTOR ZETA ATIVADO NO CONTAINER [REF: 2026-03-31]")
    
    # 1. CAMINHO DO VOLUME (Mapeado via Docker Compose)
    caminho_telemetria = "/app/shared_data/sensor_input/telemetria_imagem.csv"
    
    if not os.path.exists(caminho_telemetria):
        print(f"❌ ERRO: Sensor não detectado em {caminho_telemetria}")
        return

    # 2. CAPTURA DOS VETORES (PICO 3.34 / DESVIO 0.61)
    df_sensor = pl.read_csv(caminho_telemetria)
    m_sensor = df_sensor["curvatura_ricci"].mean()
    pico_sensor = df_sensor["curvatura_ricci"].max()
    d_sensor = df_sensor["curvatura_ricci"].std()

    print(f"| SENSOR LIDO -> Pico Geométrico: {pico_sensor:.6f}")

    # 3. COLAPSO COM A GRAMÁTICA (O 1+1=0)
    expert_gram = GramaticaExpert()
    frase = "O Isótopo Orto, resvala no Manifold Para, sob a Égide de Hückel."
    
    status, sim, veredito, massa_final, equacao = expert_gram.validar_sintaxe_zeta(
        frase, m_sensor, "BENZENO"
    )

    # 4. VEREDITO DE SOBERANIA (ABNT-ZETA-1200)
    conforme, msg_abnt = NormaABNT.auditar_conformidade_tecnica(massa_final)
    shield_status, integridade = ManifoldShield.verificar_integridade(massa_final)

    print("\n" + "="*50)
    print(f" EXIBIÇÃO DO HIPERPLANO (RESULTADO 2026) ")
    print("="*50)
    print(f"| Massa Residual: {massa_final:.10f}")
    print(f"| Shield: {shield_status} ({integridade*100}% Soberano)")
    print(f"| Norma ABNT: {msg_abnt}")
    print(f"| Equação: {equacao}")
    print("="*50)

    if shield_status == "ESTÁVEL":
        print("✅ PROJEÇÃO AUTORIZADA NO DOCKER.")
    else:
        print("❌ RUPTURA: O gradiente de Ricci excedeu o limite Zeta.")

    # 5. Persistência da auditoria no banco
    persistir_auditoria_zeta(massa_final, sim, pico_sensor, veredito)


if __name__ == "__main__":
    executar_salto_zeta_docker()

