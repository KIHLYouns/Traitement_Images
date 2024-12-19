import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def plot_histogram(image_path):
    """
    Affiche l'histogramme des canaux de couleur d'une image.
    
    Paramètres:
    - image_path : chemin de l'image couleur
    """
    # Lire l'image couleur
    image = Image.open(image_path)
    image = image.convert('RGB')  # S'assurer que l'image est en RGB
    
    # Convertir l'image en tableau numpy
    image_array = np.array(image)
    
    # Séparer les canaux de couleur
    red_channel = image_array[:, :, 0]
    green_channel = image_array[:, :, 1]
    blue_channel = image_array[:, :, 2]
    
    # Calculer les histogrammes pour chaque canal
    red_hist, red_bins = np.histogram(red_channel, bins=256, range=(0, 256))
    green_hist, green_bins = np.histogram(green_channel, bins=256, range=(0, 256))
    blue_hist, blue_bins = np.histogram(blue_channel, bins=256, range=(0, 256))
    
    # Tracer les histogrammes
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.plot(red_bins[:-1], red_hist, color='red')
    plt.title('Histogramme Rouge')
    plt.xlabel('Intensité')
    plt.ylabel('Nombre de Pixels')
    
    plt.subplot(1, 3, 2)
    plt.plot(green_bins[:-1], green_hist, color='green')
    plt.title('Histogramme Vert')
    plt.xlabel('Intensité')
    plt.ylabel('Nombre de Pixels')
    
    plt.subplot(1, 3, 3)
    plt.plot(blue_bins[:-1], blue_hist, color='blue')
    plt.title('Histogramme Bleu')
    plt.xlabel('Intensité')
    plt.ylabel('Nombre de Pixels')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Chemin de l'image couleur représentant votre portrait
    image_path = 'images_initiales/portrait.jpeg'
    
    # Afficher l'histogramme de l'image couleur
    plot_histogram(image_path)