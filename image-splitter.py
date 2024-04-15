import os
from PIL import Image

# Specify the input folder containing the images
input_folder = "whole_images"

# Specify the output folder to save the sub-images
output_folder = "cut_images"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over all images in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Open the image
        image_path = os.path.join(input_folder, filename)
        main_image = Image.open(image_path)

        # Get the width and height of the main image
        width, height = main_image.size

        # Calculate the size of each sub-image
        sub_image_size = (width // 2, height // 2)

        # Create a list to store the sub-images
        sub_images = []

        # Crop the main image into four sub-images
        for i in range(2):
            for j in range(2):
                left = j * sub_image_size[0]
                top = i * sub_image_size[1]
                right = left + sub_image_size[0]
                bottom = top + sub_image_size[1]
                sub_image = main_image.crop((left, top, right, bottom))
                sub_images.append(sub_image)

        # Save the sub-images in the output folder
        for i, sub_image in enumerate(sub_images):
            output_filename = f"{os.path.splitext(filename)[0]}_sub_{i+1}.jpg"
            output_path = os.path.join(output_folder, output_filename)
            sub_image.save(output_path)