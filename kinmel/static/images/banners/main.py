from PIL import Image
image = Image.open('2.jpg')
print(image.size)
new_image = image.resize((1200,300))
new_image.save('2.jpg')
image.show()