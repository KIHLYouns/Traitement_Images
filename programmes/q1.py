# Importation des bibliothèques nécessaires
import numpy as np  # numpy pour la manipulation des tableaux
import matplotlib.pyplot as plt  # matplotlib pour l'affichage des images

def create_pbm_image(data, magic_number='P1'):
    """
    Créer une image au format PBM à partir d'un tableau de données
    
    Paramètres:
    - data: tableau numpy contenant les pixels de l'image (0 ou 1)
    - magic_number: type de fichier PBM ('P1' pour binaire ASCII)
    
    Retourne:
    - chaîne de caractères au format PBM
    """
    height, width = data.shape  # Récupération des dimensions de l'image
    header = f"{magic_number}\n{width} {height}\n"  # En-tête PBM avec dimensions
    body = '\n'.join(' '.join(map(str, row)) for row in data)  # Conversion pixels en texte
    return header + body

def read_pbm_image(file_path):
    """
    Lire une image PBM à partir d'un fichier
    
    Paramètres:
    - file_path: chemin du fichier PBM
    
    Retourne:
    - tableau numpy contenant les pixels de l'image (0 ou 1)
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Ignorer les lignes de commentaires
    lines = [line for line in lines if not line.startswith('#')]
    
    # Lire le type de fichier (P1)
    magic_number = lines[0].strip()
    
    # Lire les dimensions de l'image
    width, height = map(int, lines[1].strip().split())
    
    # Lire les pixels de l'image
    data = []
    for line in lines[2:]:
        data.extend(map(int, line.strip().split()))
    
    # Convertir en tableau numpy
    data = np.array(data).reshape((height, width))
    return data

def read_pgm_image(file_path):
    """
    Lire une image PGM à partir d'un fichier
    
    Paramètres:
    - file_path: chemin du fichier PGM
    
    Retourne:
    - tableau numpy contenant les niveaux de gris
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Ignorer les lignes de commentaires
    lines = [line for line in lines if not line.startswith('#')]
    
    # Lire le type de fichier (P2)
    magic_number = lines[0].strip()
    if magic_number != 'P2':
        raise ValueError("Le fichier doit être au format PGM (P2)")
    
    # Lire les dimensions de l'image
    width, height = map(int, lines[1].strip().split())
    
    # Lire les pixels de l'image
    data = []
    for line in lines[3:]:
        data.extend(map(int, line.strip().split()))
    
    # Convertir en tableau numpy
    data = np.array(data).reshape((height, width))
    return data

def display_binary_image(data):
    """
    Affiche une image binaire
    
    Paramètres:
    - data: tableau numpy contenant les pixels (0 ou 1)
    """
    plt.imshow(data, cmap='binary', vmin=0, vmax=1)  # Affichage en noir et blanc
    plt.axis('off')  # Cache les axes
    plt.show()  # Affiche l'image

def display_grayscale_image(data):
    """
    Affiche une image en niveaux de gris
    
    Paramètres:
    - data: tableau numpy contenant les niveaux de gris
    """
    plt.imshow(data, cmap='gray', vmin=0, vmax=15)  # Affichage en niveaux de gris (0-15)
    plt.axis('off')  # Cache les axes
    plt.show()  # Affiche l'image

# Lire les images I1 et I2 à partir des fichiers PBM
I1 = read_pbm_image('images_initiales/I1.pbm')
I2 = read_pbm_image('images_initiales/I2.pbm')

# Opérations arithmétiques sur les images
I_ad = I1 + I2  # Addition pixel par pixel des images
I_s = np.maximum(I1 - I2, 0)  # Soustraction avec seuil à 0 pour éviter les valeurs négatives

# Affichage des résultats dans des fenêtres séparées
plt.figure()  # Nouvelle fenêtre
display_binary_image(I1)  # Affichage I1

plt.figure()
display_binary_image(I2)  # Affichage I2

plt.figure()
display_binary_image(I_ad)  # Affichage addition

plt.figure()
display_binary_image(I_s)  # Affichage soustraction

# Sauvegarde des résultats au format PBM
with open('résultats/I_ad.pbm', 'w') as f:
    f.write(create_pbm_image(I_ad))  # Sauvegarde addition
with open('résultats/I_s.pbm', 'w') as f:
    f.write(create_pbm_image(I_s))  # Sauvegarde soustraction

# Lire l'image de gris codée sur 4 bits à partir d'un fichier
gray_image_path = 'images_initiales/I_g.pgm'
gray_image = read_pgm_image(gray_image_path)

# Convertir l'image en tableau numpy et multiplier par 2
I_p = gray_image * 2

# Affichage de l'image résultante
plt.figure()
display_grayscale_image(I_p)  # Affichage multiplication par 2

print("Les résultats ont été sauvegardés sous les noms I_ad.pbm et I_s.pbm")