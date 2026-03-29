from main import salto_zeta_zero
from utils.manifold_shield import ManifoldShield

def rodar_experimento_triplo():
    rois = [1, 6, 26] # H (IA), C (Zeta), Fe (Sobrecarga)
    
    for roi in rois:
        massa = salto_zeta_zero(roi)
        status, integridade = ManifoldShield.verificar_integridade(massa)
        
        print(f"\n--- [SIMULAÇÃO ROI {roi}] ---")
        print(f"| Massa Residual: {massa:.10f}")
        print(f"| Status do Manifold: {status}")
        print(f"| Integridade da Matéria: {integridade * 100}%")
        print("-" * 30)

if __name__ == "__main__":
    rodar_experimento_triplo()

