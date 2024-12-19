import numpy as np
import matplotlib.pyplot as plt

def create_pbm_image(data, magic_number='P1'):
    """
    Crée une image au format PBM (Portable Bitmap) à partir des données fournies.
    
    Paramètres:
    - data : tableau numpy contenant les pixels de l'image (0 ou 1)
    - magic_number : type de fichier PBM ('P1' pour binaire ASCII)
    
    Retourne:
    - chaîne de caractères au format PBM
    """
    height, width = data.shape  # Récupère les dimensions de l'image
    header = f"{magic_number}\n{width} {height}\n"  # Crée l'en-tête PBM
    body = '\n'.join(' '.join(map(str, row)) for row in data)  # Convertit les pixels en chaîne de caractères
    return header + body

def read_pbm_image(file_path):
    """
    Lit une image PBM à partir d'un fichier.
    
    Paramètres:
    - file_path : chemin du fichier PBM
    
    Retourne:
    - tableau numpy avec les pixels de l'image (0 ou 1)
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Ignore les lignes de commentaires
    lines = [line for line in lines if not line.startswith('#')]
    
    magic_number = lines[0].strip()  # Lit le type de fichier
    if magic_number != 'P1':
        raise ValueError("Seul le format P1 PBM est supporté.")
    
    width, height = map(int, lines[1].strip().split())  # Lit les dimensions de l'image
    
    data = []
    for line in lines[2:]:
        data.extend([int(pixel) for pixel in line.strip().split()])
    
    data = np.array(data).reshape((height, width))  # Formate les données en tableau 2D
    return data

def display_binary_image(data, title='Image Binaire'):
    """
    Affiche une image binaire.
    
    Paramètres:
    - data : tableau numpy contenant les pixels (0 ou 1)
    - title : titre de l'image affichée
    """
    plt.imshow(data, cmap='binary', vmin=0, vmax=1)  # Affiche l'image en noir et blanc
    plt.title(title)
    plt.axis('off')  # Ne montre pas les axes
    # plt.show()  # Retiré pour éviter l'affichage multiple

if __name__ == "__main__":
    # Lit les deux images PBM
    I1 = read_pbm_image('images_initiales/I1.pbm')
    I2 = read_pbm_image('images_initiales/I2.pbm')
    
    # Additionne les deux images pixel par pixel et limite les valeurs à 0 ou 1
    I_ad = np.clip(I1 + I2, 0, 1)
    
    # Soustrait les deux images pixel par pixel et limite les valeurs à 0 ou 1
    I_s = np.clip(I1 - I2, 0, 1)
    
    # Affiche les images originales et les résultats des opérations dans une seule figure
    plt.figure(figsize=(12, 10))  # Ajuste la taille de la figure si nécessaire
    
    plt.subplot(2, 2, 1)
    plt.imshow(I1, cmap='binary', vmin=0, vmax=1)
    plt.title('Image I1')
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.imshow(I2, cmap='binary', vmin=0, vmax=1)
    plt.title('Image I2')
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.imshow(I_ad, cmap='binary', vmin=0, vmax=1)
    plt.title('Addition I_ad = I1 + I2')
    plt.axis('off')
    
    plt.subplot(2, 2, 4)
    plt.imshow(I_s, cmap='binary', vmin=0, vmax=1)
    plt.title('Soustraction I_s = I1 - I2')
    plt.axis('off')
    
    plt.tight_layout()  # Ajuste les espaces pour éviter le chevauchement
    plt.show()
    
    # Sauvegarde les résultats dans le dossier résultats
    with open('résultats/I_ad.pbm', 'w') as f:
        f.write(create_pbm_image(I_ad))

    with open('résultats/I_s.pbm', 'w') as f:
        f.write(create_pbm_image(I_s))

    print("Les résultats ont été sauvegardés sous les noms I_ad.pbm et I_s.pbm")