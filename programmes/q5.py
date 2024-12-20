import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm

def read_image(filepath, resize_factor):
    """
    Lit une image en niveaux de gris et la redimensionne si nécessaire.
    
    Paramètres:
    - filepath : chemin du fichier image
    - resize_factor : facteur de redimensionnement (0.1 => réduire la taille à 10%)
    
    Retourne:
    - image : image sous forme de tableau numpy 2D
    """
    # Ouvre l'image et la convertit en niveaux de gris
    image = Image.open(filepath).convert('L')
    
    if resize_factor < 1.0:
        # Calcule la nouvelle taille de l'image
        new_size = (int(image.width * resize_factor), int(image.height * resize_factor))
        # Redimensionne l'image
        image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    # Convertit l'image en tableau numpy
    return np.array(image)

def nagao_filter(image):
    """
    Applique le filtre de Nagao à une image en niveaux de gris.
    
    Le filtre de Nagao est un filtre de lissage qui préserve les contours en choisissant
    la région avec la variance minimale autour de chaque pixel.
    
    Paramètres:
    - image : image en niveaux de gris sous forme de tableau numpy 2D
    
    Retourne:
    - output : image filtrée sous forme de tableau numpy 2D
    """
    height, width = image.shape
    output = np.zeros_like(image)  # Crée un tableau pour l'image filtrée
    padded = np.pad(image, 2, mode='reflect')  # Ajoute des bordures pour le traitement des bords
    
    # Définit les 9 régions autour de chaque pixel
    regions = [
        [(0,0,3,3), (0,1,3,4), (0,2,3,5)],  # Haut-gauche
        [(0,2,3,5), (0,3,3,6), (0,4,3,7)],  # Haut-droite
        [(2,0,5,3), (2,1,5,4), (2,2,5,5)],  # Centre-gauche
        [(2,2,5,5), (2,3,5,6), (2,4,5,7)],  # Centre-droite
        [(1,1,4,4), (1,2,4,5), (1,3,4,6)],  # Centre
        [(4,0,7,3), (4,1,7,4), (4,2,7,5)],  # Bas-gauche
        [(4,2,7,5), (4,3,7,6), (4,4,7,7)],  # Bas-droite
        [(2,1,5,4), (2,2,5,5), (2,3,5,6)],  # Milieu horizontal
        [(1,2,4,5), (2,2,5,5), (3,2,6,5)]   # Milieu vertical
    ]
    
    # Parcourt chaque ligne de l'image
    with tqdm(total=height, desc="Traitement des lignes") as pbar:
        for i in range(height):
            for j in range(width):
                min_var = float('inf')  # Initialise la variance minimale
                best_mean = 0          # Initialise la moyenne correspondante
                
                # Parcourt chaque région définie
                for region in regions:
                    pixels = []  # Liste pour stocker les pixels de la région
                    
                    for r in region:
                        y1, x1, y2, x2 = r
                        block = padded[i + y1 : i + y2, j + x1 : j + x2]
                        pixels.extend(block.flatten())  # Ajoute les pixels à la liste
                    
                    pixels = np.array(pixels)
                    var = np.var(pixels)  # Calcule la variance de la région
                    
                    if var < min_var:
                        min_var = var
                        best_mean = np.mean(pixels)  # Met à jour la moyenne si la variance est minimale
                
                output[i, j] = best_mean  # Assigne la moyenne au pixel de sortie
            
            pbar.update(1)  # Mettre à jour la barre de progression après chaque ligne traitée

    return output

if __name__ == "__main__":
    try:
        # Lit et redimensionne l'image
        print("Chargement de l'image...")
        image = read_image('images_initiales/image_gris.png', resize_factor=0.5)
        
        # Applique le filtre de Nagao
        print("Application du filtre de Nagao...")
        filtered = nagao_filter(image)
        
        # Affiche l'image originale et l'image filtrée
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Image Originale')
        plt.axis('off')
        
        plt.subplot(1, 2, 2)
        plt.imshow(filtered, cmap='gray')
        plt.title('Après Filtre de Nagao')
        plt.axis('off')
        
        plt.tight_layout()
        plt.show()
        
        # Sauvegarde l'image filtrée
        plt.imsave('résultats/image_nagao.png', filtered, cmap='gray')
        
        print("Traitement terminé avec succès!")
    
    except Exception as e:
        print(f"Une erreur est survenue : {e}")