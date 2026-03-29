import numpy as np

class MemoriaZeta:
    """
    NBR-ZETA-1200: Mapeamento de Fenomenologia Aromática.
    """
    MEMORIAS = {
        "BENZENO": {
            "estado": "Cerne Estável (sp3)",
            "ricci": "Convergente",
            "ressonancia": "Máxima (Hückel)",
            "limite_zeta": 1.2006931305,
            "descricao": "Deslocalização perfeita. O 1+1=0 soberano."
        },
        "PIRIMIDINA": {
            "estado": "Deriva Heterocíclica",
            "ricci": "Assimétrica (N)",
            "ressonancia": "Perturbada",
            "limite_zeta": 1.8005041305,
            "descricao": "Injeção de Nitrogênio. O Isótopo oscila sob tensão."
        },
        "FENANTRENO": {
            "estado": "Ruptura de Gradiente",
            "ricci": "Divergente",
            "ressonancia": "Nula",
            "limite_zeta": 2.2006931305,
            "descricao": "Tensão térmica supera a estabilidade. IA Proto detectada."
        }
    }

    @staticmethod
    def evocar_memoria(massa_residual):
        """
        Busca a memória estrutural baseada no limite Zeta.
        Se o valor estiver próximo de um dos limites, evoca a molécula correspondente.
        """
        for nome, dados in MemoriaZeta.MEMORIAS.items():
            # Tolerância de 0.1 para capturar pequenas variações
            if abs(massa_residual - dados["limite_zeta"]) < 0.1:
                return nome, dados
        
        # Fallback de segurança
        return "VÁCUO", {
            "estado": "Instável",
            "ressonancia": "Nula",
            "descricao": "Dissipação total."
        }

