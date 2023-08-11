# Need to install exif module "pip install exif"
from exif import Image

folder_path = 'sample_images'
img_filename = 'image_1.jpg'
img_path = f'{folder_path}/{img_filename}'

with open(img_path, 'rb') as img_file:
    img = Image(img_file)
    
print(img.has_exif)