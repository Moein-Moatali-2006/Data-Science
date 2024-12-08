import os
import cv2


image = cv2.imread("numbers.jpg")

height, width = image.shape[:2]

tile_size = 20
tiles_per_folder = 500 
count = 0

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

for i in range(0, height, tile_size):
    for j in range(0, width, tile_size):
        if i + tile_size <= height and j + tile_size <= width:
            tile = image[i:i + tile_size, j:j + tile_size]

            folder_index = count // tiles_per_folder
            folder_path = os.path.join(output_dir, f"folder_{folder_index}")
            os.makedirs(folder_path, exist_ok=True)

            tile_filename = os.path.join(folder_path, f"number_{count}.png")
            cv2.imwrite(tile_filename, tile)

            count += 1

