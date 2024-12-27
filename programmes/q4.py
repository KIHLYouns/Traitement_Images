import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def plot_grayscale_histogram(image_path):
    """
    Affiche l'histogramme d'une image en niveaux de gris.
    
    Paramètres:
    - image_path : chemin de l'image en niveaux de gris
    """
    # Ouvre l'image
    image = Image.open(image_path).convert('L')
    
    # Convertit l'image en tableau numpy
    image_array = np.array(image)
    
    # Calcule l'histogramme
    hist, bins = np.histogram(image_array.flatten(), bins=256, range=(0, 256))
    
    # Crée une figure pour afficher l'image et son histogramme
    plt.figure(figsize=(12, 5))
    
    # Affiche l'image originale
    plt.subplot(1, 2, 1)
    plt.imshow(image_array, cmap='gray')
    plt.title('Image en Niveaux de Gris')
    plt.axis('off')
    
    # Affiche l'histogramme
    plt.subplot(1, 2, 2)
    plt.plot(bins[:-1], hist, color='black')
    plt.title('Histogramme')
    plt.xlabel('Intensité')
    plt.ylabel('Nombre de Pixels')
    plt.grid(True, alpha=0.2)
    
    plt.tight_layout()
    plt.show()
    
    # Sauvegarde l'histogramme
    plt.figure(figsize=(8, 6))
    plt.plot(bins[:-1], hist, color='black')
    plt.title('Histogramme')
    plt.xlabel('Intensité')
    plt.ylabel('Nombre de Pixels')
    plt.grid(True, alpha=0.2)
    plt.savefig('résultats/histogramme_gris.png')
    plt.close()

if __name__ == "__main__":
    try:
        # Chemin de l'image en niveaux de gris générée par q3.py
        image_path = 'images_initiales/image_gris.png'
        plot_grayscale_histogram(image_path)
        print("Histogramme généré avec succès!")
        
    except Exception as e:
        print(f"Une erreur est survenue : {e}")