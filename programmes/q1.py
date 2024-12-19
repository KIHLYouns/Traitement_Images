import numpy as np
import matplotlib.pyplot as plt

def create_pbm_image(data, magic_number='P1'):
    """
    Crée une image au format PBM (Portable Bitmap) à partir d'un tableau de données.
    
    Paramètres:
    - data : tableau numpy contenant les pixels de l'image (0 ou 1)
    - magic_number : type de fichier PBM ('P1' pour binaire ASCII)
    
    Retourne:
    - chaîne de caractères au format PBM
    """
    height, width = data.shape  # Récupération des dimensions de l'image
    header = f"{magic_number}\n{width} {height}\n"  # En-tête PBM avec dimensions
    body = '\n'.join(' '.join(map(str, row)) for row in data)  # Conversion des pixels en texte
    return header + body

def read_pbm_image(file_path):
    """
    Lit une image PBM à partir d'un fichier.
    
    Paramètres:
    - file_path : chemin du fichier PBM
    
    Retourne:
    - tableau numpy contenant les pixels de l'image (0 ou 1)
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Ignorer les lignes de commentaires
    lines = [line for line in lines if not line.startswith('#')]
    
    # Lire le type de fichier (P1)
    magic_number = lines[0].strip()
    if magic_number != 'P1':
        raise ValueError("Ce script ne supporte que le format P1 PBM.")
    
    # Lire les dimensions de l'image
    width, height = map(int, lines[1].strip().split())
    
    # Lire les pixels de l'image
    data = []
    for line in lines[2:]:
        data.extend([int(pixel) for pixel in line.strip().split()])
    
    # Convertir en tableau numpy
    data = np.array(data).reshape((height, width))
    return data

def display_binary_image(data, title='Image Binaire'):
    """
    Affiche une image binaire.
    
    Paramètres:
    - data : tableau numpy contenant les pixels (0 ou 1)
    - title : titre de l'image affichée
    """
    plt.imshow(data, cmap='binary', vmin=0, vmax=1)  # Affichage en noir et blanc
    plt.title(title)
    plt.axis('off')  # Cache les axes
    plt.show()

if __name__ == "__main__":
    # Lire les images I1 et I2 à partir des fichiers PBM
    I1 = read_pbm_image('images_initiales/I1.pbm')
    I2 = read_pbm_image('images_initiales/I2.pbm')
    
    # Opérations arithmétiques sur les images
    I_ad = np.clip(I1 + I2, 0, 1)  # Addition pixel par pixel des images avec seuil à 1
    I_s = np.clip(I1 - I2, 0, 1)   # Soustraction pixel par pixel des images avec seuil à 0
    
    # Affichage des images
    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    display_binary_image(I1, title='Image I1')

    plt.subplot(2, 2, 2)
    display_binary_image(I2, title='Image I2')

    plt.subplot(2, 2, 3)
    display_binary_image(I_ad, title='Addition I_ad = I1 + I2')

    plt.subplot(2, 2, 4)
    display_binary_image(I_s, title='Soustraction I_s = I1 - I2')

    plt.tight_layout()
    plt.show()

    # Sauvegarde des résultats au format PBM
    with open('résultats/I_ad.pbm', 'w') as f:
        f.write(create_pbm_image(I_ad))

    with open('résultats/I_s.pbm', 'w') as f:
        f.write(create_pbm_image(I_s))

    print("Les résultats ont été sauvegardés sous les noms I_ad.pbm et I_s.pbm")