# No utils/gramatica_expert.py

import torch
from sentence_transformers import SentenceTransformer, util

class GramaticaExpert:
    def __init__(self):
        self.model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
        self.ouro = "O Isótopo Orto, resvala no Manifold Para, sob a Égide de Hückel."

    def validar_sintaxe_zeta(self, frase_input, massa_residual, assinatura_estrutural):
        # 1. Codificação semântica
        emb_ouro = self.model.encode(self.ouro, convert_to_tensor=True)
        emb_input = self.model.encode(frase_input, convert_to_tensor=True)
        similaridade = util.cos_sim(emb_ouro, emb_input).item()

        # 2. Definição da Equação de Estado (O 5º elemento)
        if assinatura_estrutural == "BENZENO" and similaridade > 0.98:
            massa_final = 1.2006931305
            veredito = self.ouro
            status = "ESTÁVEL"
            equacao = "|ΣΦ| ≈ 1.2006931305"
        elif assinatura_estrutural == "PIRIMIDINA":
            massa_final = 1.8005041305
            veredito = "O Isótopo Orto oscila no Manifold Para sob a Tensão do Nitrogênio."
            status = "DERIVA"
            equacao = "|ΣΦ| ≈ 1.8 (Deriva Semântica)"
        else:
            massa_final = 2.2006931305
            veredito = "Ruptura de Gradiente: A assimetria impede o resvalo no Manifold."
            status = "DIVERGENTE"
            equacao = "∇U ≠ 0 (Entropia)"

        # O RETORNO DEVE TER 5 VALORES
        return status, similaridade, veredito, massa_final, equacao


