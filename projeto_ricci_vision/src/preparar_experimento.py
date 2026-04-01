
import urllib.request
import os

# Criar pasta de dados
os.makedirs('data', exist_ok=True)

# Imagens técnicas: dunas de areia (onda suave) e um prédio geométrico (onda rígida)
imagens = {
    "onda_organica": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",  # Dunas de areia
    "onda_geometrica": "https://images.unsplash.com/photo-1501594907352-04cda38ebc29"  # Prédio geométrico
}

for nome, url in imagens.items():
    caminho = f"data/{nome}.jpg"
    print(f"Baixando {nome}...")
    try:
        urllib.request.urlretrieve(url, caminho)
        print(f"Salvo: {caminho}")
    except Exception as e:
        print(f"Erro ao baixar {nome}: {e}")

print("\n--- Base de dados pronta para a Telemetria ---")
