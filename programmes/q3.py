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
    # Ouvre l'image et la convertit en RGB
    image = Image.open(image_path)
    image = image.convert('RGB')
    
    if transformation == 'gris':
        # Convertit l'image en niveaux de gris
        gray_image = image.convert('L')
        
        # Réduit le nombre de bits si nécessaire
        if bits < 8:
            factor = 2 ** (8 - bits)
            gray_image = gray_image.point(lambda x: (x // factor) * factor)
        
        # Affiche l'image en niveaux de gris
        gray_image.show()
        
        # Sauvegarde l'image en niveaux de gris
        gray_image.save('résultats/portrait_gris.png')
        print("L'image en niveaux de gris a été sauvegardée sous le nom 'portrait_gris.png'")
    
    elif transformation == 'binaire':
        # Convertit l'image en niveaux de gris
        gray_image = image.convert('L')
        
        # Convertit l'image en binaire (noir et blanc)
        binary_image = gray_image.point(lambda x: 255 if x > 128 else 0, '1')
        
        # Affiche l'image binaire
        binary_image.show()
        
        # Sauvegarde l'image binaire
        binary_image.save('résultats/portrait_binaire.png')
        print("L'image binaire a été sauvegardée sous le nom 'portrait_binaire.png'")
    
    else:
        print("Transformation non reconnue. Veuillez choisir 'gris' ou 'binaire'.")

if __name__ == "__main__":
    # Chemin de l'image couleur
    image_path = 'images_initiales/portrait.jpeg'
    
    # Demande à l'utilisateur de choisir la transformation
    transformation = input("Choisissez la transformation ('gris' ou 'binaire') : ").strip().lower()
    
    if transformation == 'gris':
        try:
            bits = int(input("Entrez le nombre de bits pour l'image en niveaux de gris (1-8) : ").strip())
            if not 1 <= bits <= 8:
                raise ValueError
            transform_image(image_path, transformation, bits)
        except ValueError:
            print("Entrée invalide pour les bits. Veuillez entrer un nombre entier entre 1 et 8.")
    elif transformation == 'binaire':
        transform_image(image_path, transformation)
    else:
        print("Option de transformation non valide.")