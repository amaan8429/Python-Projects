import sys #used to take input from the command line
import os   #this helps to interact with the system like creating a folder and stuff
from PIL import Image  #to edit images


#taking input of the jpeg files folder and new folder to store the converted images.
image_folder = sys.argv[1] + "/"
output_folder = sys.argv[2] + "/"

#creating a new folder if it does not exists
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

#looping over each file in the folder
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')  #opening the image
    clean_name = os.path.splitext(filename)[0]  #to extract the filename without the extension
    img.save(f"{output_folder}{clean_name}.png", "png")
    print("all done")
