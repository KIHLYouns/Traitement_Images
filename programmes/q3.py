import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def transform_image(image_path, transformation, bits=8):
    """
    Transforme une image couleur en niveaux de gris ou en image binaire.
    
    Paramètres:
    - image_path : chemin de l'image couleur
    - transformation : type de transformation ('gris' ou 'binaire')
    - bits : nombre de bits pour l'image en niveaux de gris (par défaut 8)
    """
    # Ouvre l'image et la convertit en mode RGB
    image = Image.open(image_path)
    image = image.convert('RGB')

    # Affiche l'image originale
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title('Image Originale')
    plt.axis('off')
    
    if transformation == 'gris':
        # Convertit l'image en niveaux de gris
        gray_image = image.convert('L')
        
        # Réduit le nombre de bits si nécessaire
        if bits < 8:
            factor = 2 ** (8 - bits)
            gray_image = gray_image.point(lambda x: (x // factor) * factor)
        
        # Affiche l'image en niveaux de gris
        plt.subplot(1, 2, 2)
        plt.imshow(gray_image, cmap='gray')
        plt.title('Image en Niveaux de Gris')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        # Sauvegarde l'image en niveaux de gris
        gray_image.save('résultats/image_gris.png')
        print("L'image en niveaux de gris a été sauvegardée sous le nom 'image_gris.png'")
    
    elif transformation == 'binaire':
        # Convertit l'image en niveaux de gris
        gray_image = image.convert('L')
        
        # Convertit l'image en binaire (noir et blanc)
        binary_image = gray_image.point(lambda x: 255 if x > 128 else 0, '1')
        
        # Affiche l'image binaire
        plt.subplot(1, 2, 2)
        plt.imshow(binary_image, cmap='gray')
        plt.title('Image Binaire')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        # Sauvegarde l'image binaire
        binary_image.save('résultats/image_binaire.png')
        print("L'image binaire a été sauvegardée sous le nom 'image_binaire.png'")
    
    else:
        print("Transformation non reconnue. Veuillez choisir 'gris' ou 'binaire'.")

if __name__ == "__main__":
    # Chemin de l'image couleur
    image_path = 'images_initiales/thousand-yard_stare.jpeg'
    
    # Demande à l'utilisateur de choisir la transformation
    transformation = input("Choisissez la transformation ('gris' ou 'binaire') : ").strip().lower()
    
    if transformation == 'gris':
        try:
            # Demande le nombre de bits à l'utilisateur
            bits = int(input("Entrez le nombre de bits pour l'image en niveaux de gris (1-8) : ").strip())
            if not 1 <= bits <= 8:
                raise ValueError
            # Applique la transformation en niveaux de gris
            transform_image(image_path, transformation, bits)
        except ValueError:
            print("Entrée invalide pour les bits. Veuillez entrer un nombre entier entre 1 et 8.")
    elif transformation == 'binaire':
        # Applique la transformation binaire
        transform_image(image_path, transformation)
    else:
        print("Option de transformation non valide.")