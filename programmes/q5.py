import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from tqdm import tqdm

def read_image(filepath, resize_factor=0.1):
    """
    Lire une image en niveaux de gris et redimensionner pour un traitement rapide.
    
    Paramètres:
    - filepath : chemin du fichier image
    - resize_factor : facteur de redimensionnement (par défaut 0.1 pour réduire la taille à 10%)
    
    Retourne:
    - image : image sous forme de tableau numpy 2D
    """
    # Ouvrir l'image et la convertir en niveaux de gris
    image = Image.open(filepath).convert('L')
    if resize_factor < 1.0:
        # Calculer la nouvelle taille de l'image
        new_size = (int(image.width * resize_factor), int(image.height * resize_factor))
        # Redimensionner l'image pour accélérer les tests
        image = image.resize(new_size, Image.Resampling.LANCZOS)
    # Convertir l'image en un tableau numpy
    return np.array(image)

def nagao_filter(image):
    """
    Appliquer le filtre de Nagao à une image en niveaux de gris.
    
    Le filtre de Nagao est un filtre de lissage non linéaire qui préserve les contours
    en analysant plusieurs régions autour de chaque pixel et en choisissant celle
    avec la variance minimale.
    
    Paramètres:
    - image : image en niveaux de gris sous forme de tableau numpy 2D
    
    Retourne:
    - output : image filtrée sous forme de tableau numpy 2D
    """
    height, width = image.shape
    output = np.zeros_like(image)
    padded = np.pad(image, 2, mode='reflect')  # Ajouter un padding pour gérer les bords

    # Définition des 9 régions de Nagao
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
    
    # Utilisation de tqdm pour afficher la progression
    with tqdm(total=height, desc="Traitement des lignes") as pbar:
        for i in range(height):
            for j in range(width):
                min_var = float('inf')  # Initialiser la variance minimale
                best_mean = 0  # Initialiser la moyenne de la meilleure région
                
                # Parcourir chaque région
                for region in regions:
                    pixels = []  # Liste pour stocker les pixels de la région
                    # Rassembler les pixels de chaque sous-bloc de la région
                    for r in region:
                        y1, x1, y2, x2 = r
                        block = padded[i + y1 : i + y2, j + x1 : j + x2]
                        pixels.extend(block.flatten())
                    
                    pixels = np.array(pixels)
                    var = np.var(pixels)  # Calculer la variance de la région
                    if var < min_var:
                        min_var = var  # Mettre à jour la variance minimale
                        best_mean = np.mean(pixels)  # Enregistrer la moyenne correspondante
                
                # Assigner la moyenne de la meilleure région au pixel de sortie
                output[i, j] = best_mean
            
            pbar.update(1)  # Mettre à jour la barre de progression après chaque ligne traitée

    return output

if __name__ == "__main__":
    try:
        # Lecture de l'image avec PIL
        print("Chargement de l'image...")
        image = read_image('../images_initiales/portrait_gris.png', resize_factor=0.1)
        
        print("Application du filtre de Nagao...")
        filtered = nagao_filter(image)
        
        print("Sauvegarde des résultats...")
        # Affichage des images avant et après le filtrage
        plt.figure(figsize=(10,5))
        
        # Afficher l'image originale
        plt.subplot(1, 2, 1)
        plt.imshow(image, cmap='gray')
        plt.title('Image originale')
        plt.axis('off')
        
        # Afficher l'image filtrée
        plt.subplot(1, 2, 2)
        plt.imshow(filtered, cmap='gray')
        plt.title('Après filtre de Nagao')
        plt.axis('off')
        
        plt.tight_layout()
        plt.savefig('../résultats/portrait_nagao.png')  # Sauvegarder la figure
        plt.close()
        
        print("Traitement terminé avec succès!")
    
    except Exception as e:
        print(f"Erreur: {str(e)}")
        plt.close()