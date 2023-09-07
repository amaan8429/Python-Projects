from PIL import Image, ImageFilter

img = Image.open("./Images/pikachu.jpg")

#prints the image object
# print(img)

# print(img.size)

# print(img.format)

# print(img.mode)

# filteredimg = img.filter(ImageFilter.BLUR)
# filteredimg = img.filter(ImageFilter.SHARPEN)
# filteredimg.save("newimg.png","png")

# filteredimg = img.convert('L')
# filteredimg.save("grey.png","png")

# filteredimg = img.rotate(90)
# filteredimg.save("rotated.png","png")
#
# filteredimg.show()

# resize = img.resize((200,200))
# resize.save("resized.png","png")

# box = (100, 100, 400, 400)
# region = img.crop(box)
# region.save("region.png","png")
#
# img.thumbnail((400,400))
# img.save("thumbnail.png","png")