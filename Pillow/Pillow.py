from PIL import Image
import math

xdim = 800
ydim = 800

image = Image.new("RGB", (xdim, ydim))

'''for x in range(xdim):
    for y in range(ydim):
        r = int(math.sqrt((255-x)**2 + (255-y)**2)%256)
        g = int(math.sqrt(x**2 + y**2)%256)
        b = int(((x*y)/2)%256)
        image.putpixel((x, y), (0, 0, b))'''

def checkerBoard(squares):
    for x in range(xdim):
        for y in range(ydim):
            if (x//(xdim/squares))%2 != (y//(ydim/squares))%2:
                r = 255
            else:
                r = 0
            image.putpixel((x, y), (r, 0, 0))

def drawSquare(x, y, dim):
    for i in range(dim):
        for j in range(dim):
            image.putpixel((x+i, y+j), (255, 0, 0))
        
def fadedCheckerBoard(squares):
    for x in range(squares):
        for y in range(squares):
            if x%2 == y%2:
                drawSquare(xdim//squares*x, ydim//squares*y, xdim//squares-(x*(xdim//squares//squares)))

fadedCheckerBoard(8)
print("Image complete")
image.save("checkerboard.png")