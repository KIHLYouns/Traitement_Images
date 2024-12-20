import numpy as np
import matplotlib.pyplot as plt

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
    
    magic_number = lines[0].strip()  # Lit le type de fichier (doit être 'P1' pour PBM ASCII)
    if magic_number != 'P1':
        raise ValueError("Seul le format P1 PBM est supporté.")
    
    width, height = map(int, lines[1].strip().split())  # Lit les dimensions de l'image (largeur et hauteur)
    
    data = []
    for line in lines[2:]:
        data.extend([int(pixel) for pixel in line.strip().split()])  # Lit les pixels et les convertit en entiers
    
    data = np.array(data).reshape((height, width))  # Formate les données en un tableau 2D (hauteur x largeur)
    return data

def create_pbm_image(data, magic_number='P1'):
    """
    Crée une image au format PBM (Portable Bitmap) à partir des données fournies.
    
    Paramètres:
    - data : tableau numpy contenant les pixels de l'image (0 ou 1)
    - magic_number : type de fichier PBM ('P1' pour binaire ASCII)
    
    Retourne:
    - chaîne de caractères au format PBM prête à être écrite dans un fichier
    """
    height, width = data.shape  # Récupère les dimensions de l'image
    header = f"{magic_number}\n{width} {height}\n"  # Crée l'en-tête PBM avec le type et les dimensions
    body = '\n'.join(' '.join(map(str, row)) for row in data)  # Convertit les pixels en chaîne de caractères
    return header + body

def read_pgm_image(file_path):
    """
    Lit une image PGM à partir d'un fichier.
    
    Paramètres:
    - file_path : chemin du fichier PGM
    
    Retourne:
    - data : tableau numpy des pixels de l'image
    - max_val : valeur maximale de pixel
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Ignore les lignes de commentaires et supprime les espaces en début et fin de ligne
    lines = [line.strip() for line in lines if not line.startswith('#')]

    magic_number = lines[0]  # Lit le type de fichier (doit être 'P2' pour PGM ASCII)
    if magic_number != 'P2':
        raise ValueError("Seul le format P2 PGM est supporté.")

    width, height = map(int, lines[1].split())  # Lit les dimensions de l'image
    max_val = int(lines[2])  # Lit la valeur maximale des pixels

    data = []
    for line in lines[3:]:
        data.extend([int(pixel) for pixel in line.split()])  # Lit les pixels et les convertit en entiers

    data = np.array(data).reshape((height, width))  # Formate les données en un tableau 2D
    return data, max_val

def create_pgm_image(data, max_val=15, magic_number='P2'):
    """
    Crée une image au format PGM à partir des données fournies.
    
    Paramètres:
    - data : tableau numpy des pixels de l'image
    - max_val : valeur maximale de pixel
    - magic_number : type de fichier PGM ('P2' pour binaire ASCII)
    
    Retourne:
    - chaîne de caractères au format PGM prête à être écrite dans un fichier
    """
    height, width = data.shape  # Récupère les dimensions de l'image
    header = f"{magic_number}\n{width} {height}\n{max_val}\n"  # Crée l'en-tête PGM
    body = '\n'.join(' '.join(map(str, row)) for row in data)  # Convertit les pixels en chaîne de caractères
    return header + body    

if __name__ == "__main__":
    # Lit les deux images PBM I1 et I2
    I1 = read_pbm_image('images_initiales/I1.pbm')
    I2 = read_pbm_image('images_initiales/I2.pbm')
    
    # Lecture de l'image PGM I_g.pgm
    I_g, max_val = read_pgm_image('images_initiales/I_g.pgm')
    
    # Additionne les deux images pixel par pixel et limite les valeurs à 0 ou 1
    I_ad = np.clip(I1 + I2, 0, 1)
    
    # Soustrait les deux images pixel par pixel et limite les valeurs à 0 ou 1
    I_s = np.clip(I1 - I2, 0, 1)

    # Multiplication de l'image I_g par 2 et limitation à max_val
    I_g_mult2 = np.clip(I_g * 2, 0, max_val)
    
    # Affiche toutes les images dans une fenêtre
    plt.figure(figsize=(12, 10))
    
    # Affiche l'image I1 en noir et blanc
    plt.subplot(3, 2, 1)
    plt.imshow(I1, cmap='binary')
    plt.title('Image I1')
    plt.axis('off')
    
    # Affiche l'image I2 en noir et blanc
    plt.subplot(3, 2, 2)
    plt.imshow(I2, cmap='binary')
    plt.title('Image I2')
    plt.axis('off')
    
    # Affiche l'image résultante de l'addition de I1 et I2
    plt.subplot(3, 2, 3)
    plt.imshow(I_ad, cmap='binary')
    plt.title('I_ad = I1 + I2')
    plt.axis('off')
    
    # Affiche l'image résultante de la soustraction de I1 et I2
    plt.subplot(3, 2, 4)
    plt.imshow(I_s, cmap='binary')
    plt.title('I_s = I1 - I2')
    plt.axis('off')
    
    # Affiche l'image PGM originale en niveaux de gris
    plt.subplot(3, 2, 5)
    plt.imshow(I_g, cmap='gray', vmin=0, vmax=max_val)
    plt.title('Image I_g')
    plt.axis('off')
    
    # Affiche l'image PGM multipliée par 2 en niveaux de gris
    plt.subplot(3, 2, 6)
    plt.imshow(I_g_mult2, cmap='gray', vmin=0, vmax=max_val)
    plt.title('I_g * 2')
    plt.axis('off')
    
    plt.tight_layout()  # Ajuste les espacements entre les sous-graphiques
    plt.show()  # Affiche toutes les figures

    # Sauvegarde des résultats dans des fichiers
    with open("résultats/I_ad.pbm", "w") as f:
        f.write(create_pbm_image(I_ad))
    with open("résultats/I_s.pbm", "w") as f:
        f.write(create_pbm_image(I_s))
    with open("résultats/I_g_mult2.pgm", "w") as f:
        f.write(create_pgm_image(I_g_mult2, max_val))

    print("Résultats sauvegardés : I_ad.pbm, I_s.pbm, I_g_mult2.pgm")