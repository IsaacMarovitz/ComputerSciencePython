from PIL import Image
import random

xdim = 1024
ydim = 1024
snakeCount = 2000

image = Image.new("RGB", (xdim, ydim))

def snake():
    snakeOffEdge = False
    x = random.randint(0, xdim)
    randomColor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for y in range(ydim):
        if not snakeOffEdge:
            index = random.randint(1, 3)
            if index == 1:
                x = x-1
                if x < 0:
                    snakeOffEdge = True
                else:
                    image.putpixel((x, y), randomColor)
            elif index == 2:
                image.putpixel((x, y), randomColor)
            elif index == 3:
                x = x+1
                if x >= xdim:
                    snakeOffEdge = True
                else:
                    image.putpixel((x, y), randomColor)

for x in range(snakeCount):
    snake()

image.save("Snakes.png")
print("Image Complete")