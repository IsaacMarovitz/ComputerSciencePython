from PIL import Image
from PIL import UnidentifiedImageError

fileName = "./Test.jpeg"

def avg_grayscale(image):
    filteredImage = Image.new("RGB", (image.width, image.height))

    for x in range(0, image.width):
        for y in range(0, image.height):
            gray = int((image.getpixel((x, y))[0] + image.getpixel((x, y))[1] + image.getpixel((x, y))[2]) / 3)
            filteredImage.putpixel((x, y), (gray, gray, gray))

    return filteredImage

def r_grayscale(image):
    filteredImage = Image.new("RGB", (image.width, image.height))

    for x in range(0, image.width):
        for y in range(0, image.height):
            gray = image.getpixel((x, y))[0]
            filteredImage.putpixel((x, y), (gray, gray, gray))

    return filteredImage

def g_grayscale(image):
    filteredImage = Image.new("RGB", (image.width, image.height))

    for x in range(0, image.width):
        for y in range(0, image.height):
            gray = image.getpixel((x, y))[1]
            filteredImage.putpixel((x, y), (gray, gray, gray))

    return filteredImage

def b_grayscale(image):
    filteredImage = Image.new("RGB", (image.width, image.height))

    for x in range(0, image.width):
        for y in range(0, image.height):
            gray = image.getpixel((x, y))[2]
            filteredImage.putpixel((x, y), (gray, gray, gray))

    return filteredImage

try:
    image = Image.open(fileName, mode="r")
except UnidentifiedImageError:
    pass
except ValueError:
    pass

filteredImage = avg_grayscale(image)
filteredImage.save("FilteredAvg.png")

filteredImage = r_grayscale(image)
filteredImage.save("FilteredR.png")

filteredImage = g_grayscale(image)
filteredImage.save("FilteredG.png")

filteredImage = b_grayscale(image)
filteredImage.save("FilteredB.png")
