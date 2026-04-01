
import cv2
import numpy as np
import urllib.request
import os

def baixar_imagem(url, nome_arquivo):
    if not os.path.exists(nome_arquivo):
        print(f"Baixando imagem de: {url}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response, open(nome_arquivo, 'wb') as out_file:
                out_file.write(response.read())
            print(f"Imagem salva com sucesso em: {nome_arquivo}")
        except Exception as e:
            print(f"Erro ao baixar a imagem: {e}")
            return None
    return nome_arquivo

# URL direta da imagem (não a página do Unsplash)
url_imagem = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=60"
caminho_local = "data/imagem_onda.jpg"

os.makedirs('data', exist_ok=True)
arquivo = baixar_imagem(url_imagem, caminho_local)

if arquivo and os.path.exists(arquivo):
    img_bgr = cv2.imread(arquivo)
    
    if img_bgr is None:
        print("Erro: O OpenCV não conseguiu ler o arquivo de imagem.")
    else:
        gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
        camada_pontos = cv2.Laplacian(gray, cv2.CV_64F)
        silhueta = cv2.GaussianBlur(gray, (15, 15), 0)

        pontos_vis = np.absolute(camada_pontos).astype(np.uint8)
        
        cv2.imshow("Camada 1: Pontos (Onda)", pontos_vis)
        cv2.imshow("Camada 2: Silhueta (Geometria)", silhueta)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        np.save('data/onda_pixels.npy', gray)
        print("Matriz de pontos salva em data/onda_pixels.npy")
else:
    print("Falha ao processar: Arquivo de imagem não encontrado.")
