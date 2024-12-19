import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def transform_image(image_path, transformation, bits=8):
    """
    Transforme une image couleur en image en niveaux de gris ou binaire.
    
    Paramètres:
    - image_path : chemin de l'image couleur
    - transformation : type de transformation ('grayscale' ou 'binary')
    - bits : nombre de bits pour l'image en niveaux de gris (par défaut 8)
    """
    # Lire l'image couleur
    image = Image.open(image_path)
    image = image.convert('RGB')  # S'assurer que l'image est en RGB
    
    if transformation == 'grayscale':
        # Convertir en niveaux de gris
        gray_image = image.convert('L')
        
        # Réduire le nombre de bits si nécessaire
        if bits < 8:
            factor = 2 ** (8 - bits)
            gray_image = gray_image.point(lambda x: (x // factor) * factor)
        
        # Afficher et sauvegarder l'image en niveaux de gris
        gray_image.show()
        gray_image.save('résultats/portrait_gris.png')
        print(f"L'image en niveaux de gris a été sauvegardée sous le nom 'gray_portrait.png'")
    
    elif transformation == 'binary':
        # Convertir en niveaux de gris
        gray_image = image.convert('L')
        
        # Convertir en binaire
        binary_image = gray_image.point(lambda x: 255 if x > 128 else 0, '1')
        
        # Afficher et sauvegarder l'image binaire
        binary_image.show()
        binary_image.save('résultats/portrait_binaire.png')
        print(f"L'image binaire a été sauvegardée sous le nom 'binary_portrait.png'")
    else:
        print("Transformation non reconnue. Utilisez 'grayscale' ou 'binary'.")

if __name__ == "__main__":
    # Chemin de l'image couleur représentant votre portrait
    image_path = 'images_initiales/portrait.jpeg'
    
    # Demander à l'utilisateur de choisir la transformation
    transformation = input("Choisissez la transformation ('grayscale' ou 'binary'): ").strip().lower()
    
    # Si l'utilisateur choisit 'grayscale', demander le nombre de bits
    if transformation == 'grayscale':
        try:
            bits = int(input("Entrez le nombre de bits pour l'image en niveaux de gris (1-8): ").strip())
            if not 1 <= bits <= 8:
                raise ValueError
            transform_image(image_path, transformation, bits)
        except ValueError:
            print("Entrée invalide pour les bits. Veuillez entrer un nombre entier entre 1 et 8.")
    else:
        transform_image(image_path, transformation)