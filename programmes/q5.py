import numpy as np
from PIL import Image
from numba import njit

@njit
def apply_nagao_filter_optimized(img_array, masks, height, width):
    filtered_img = np.zeros_like(img_array)
    for y in range(1, height-1):
        for x in range(1, width-1):
            neighborhood = img_array[y-1:y+2, x-1:x+2]
            averages = 0.0
            for m in masks:
                mask_sum = 0
                count = 0
                for i in range(3):
                    for j in range(3):
                        if m[i, j] == 1:
                            mask_sum += neighborhood[i, j]
                            count += 1
                averages += mask_sum / count
            filtered_img[y, x] = averages / len(masks)
    return filtered_img

def apply_nagao_filter(image_path, output_path):
    # Load the grayscale image
    image = Image.open(image_path).convert('L')
    img_array = np.array(image)
    
    # Define Nagao masks (9 regions)
    masks = np.array([
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]],
        [[0, 1, 1],
         [0, 1, 1],
         [0, 1, 1]],
        [[1, 1, 0],
         [1, 1, 0],
         [1, 1, 0]],
        [[0, 0, 0],
         [1, 1, 1],
         [0, 0, 0]],
        [[0, 1, 0],
         [1, 1, 1],
         [0, 1, 0]],
        [[1, 0, 0],
         [1, 1, 0],
         [1, 0, 0]],
        [[0, 0, 1],
         [0, 1, 1],
         [0, 0, 1]],
        [[1, 0, 1],
         [1, 1, 1],
         [1, 0, 1]],
        [[0, 1, 0],
         [1, 1, 1],
         [0, 1, 0]]
    ])
    
    height, width = img_array.shape
    filtered_img = apply_nagao_filter_optimized(img_array, masks, height, width)
    
    # Save the filtered image
    filtered_image = Image.fromarray(filtered_img.astype(np.uint8))
    filtered_image.save(output_path)

# Usage
apply_nagao_filter('images_initiales/gray_portrait.png', 'résultats/nagao_gray_portrait.png')