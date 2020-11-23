# Mandelbrot Set and Fractals - 01/11/20
# Sources:
# This program creates 4 different pictures of fractals

# 1. Colour - This one creates a picture of a particularly itricate part of the Mandelbrot Set
# I made a colour palette that I then use to colour in the fractal by selecting a different colour
# bassed off of the last digit of the number returned by the Mandelbrot function (Range 0-255)

# 2. Smooth

# 3. Julia - A black and white picture of the Julia Set. I choose to just make this black and white
# because I think that this fractal just looks very pretty on it's own, and it has a lot more intricate
# details than the Mandelbrot Set

# I have also included a video and a seperate folder along with my Python script. I wanted to create
# an animated video of the Julia Set, but unfortuntley Python is a bit too slow to render that many frames
# so I made a seperate program using the Rust programming language that does just that. 
# I've included instructions in that folder to run that program if you would like.

from PIL import Image
import math, time
import colorsys

xSize = 1000
ySize = 1000
max_iterations = 255
escape_radius = 10

def mandelbrot(c, z=complex(0, 0), iterations=1):
    zNew = z**2 + c
    if abs(zNew) > 2 or iterations >= max_iterations:
        return (iterations, zNew)
    else:
        iterations += 1
        return mandelbrot(c, zNew, iterations)

def julia(c, z):
    iterations = 1
    zx = z[0]
    zy = z[1]
    while (zx * zx + zy * zy  < escape_radius**2 and iterations < max_iterations):
        xtemp = zx * zx - zy * zy 
        zy = 2 * zx * zy + c[1]
        zx = xtemp + c[0]

        iterations = iterations + 1

    return iterations    

'''
xLimits = (0.12, 0.22)
yLimits = (-0.65, -0.55)

startTime = time.time()
image = Image.new("RGB", (xSize, ySize))

for y in range(ySize):
    cy = y * (yLimits[1] - yLimits[0]) / ySize + yLimits[0]
    for x in range(xSize):
        cx = x * (xLimits[1] - xLimits[0]) / xSize + xLimits[0]
        mandelbrotNum = mandelbrot(complex(cx, cy))
        string = str(mandelbrotNum)
        finalDigit = int(string[len(string)-1])

        purple = (159, 0, 255)
        green = (0, 178, 51)
        yellow = (255, 237, 0)
        red = (255, 63, 49)
        blue = (0, 205, 255)

        if finalDigit == 0:
            image.putpixel((x, y), blue)
        elif finalDigit == 1:
            image.putpixel((x, y), (255, 255, 255))
        elif finalDigit == 2:
            image.putpixel((x, y), green)
        elif finalDigit == 3:
            image.putpixel((x, y), yellow)
        elif finalDigit == 4:
            image.putpixel((x, y), red)
        elif finalDigit == 5:
            image.putpixel((x, y), blue)
        elif finalDigit == 6:
            image.putpixel((x, y), purple)
        elif finalDigit == 7:
            image.putpixel((x, y), green)
        elif finalDigit == 8:
            image.putpixel((x, y), yellow)
        elif finalDigit == 9: 
            image.putpixel((x, y), red)

image.save("Mandelbrot1.png")
print(f"Finished Mandelbrot in {time.time() - startTime} seconds.")
'''
xLimits = (-2, 2)
yLimits = (-2, 2)

startTime = time.time()
image = Image.new("RGB", (xSize, ySize))

for y in range(ySize):
    cy = y * (yLimits[1] - yLimits[0]) / ySize + yLimits[0]
    for x in range(xSize):
        cx = x * (xLimits[1] - xLimits[0]) / xSize + xLimits[0]
        mandelbrotNum = mandelbrot(complex(cx, cy))
        abs_z = mandelbrotNum[1].real**2 + mandelbrotNum[1].imag**2
        if mandelbrotNum[0] < max_iterations:
            smooth_value = int(mandelbrotNum[0] - math.log2(abs(math.log(abs_z)) / math.log(max_iterations))) * 15
        else:
            smooth_value = 255
        image.putpixel((x, y), (smooth_value, smooth_value, smooth_value))

image.save("Mandelbrot2.png")
print(f"Finished Mandelbrot in {time.time() - startTime} seconds.")

xLimits = (-1.8, 1.8)
yLimits = (-1.8, 1.8)

startTime = time.time()
image = Image.new("RGB", (xSize, ySize))

for y in range(ySize):
    cy = y * (yLimits[1] - yLimits[0]) / ySize + yLimits[0]
    for x in range(xSize):
        cx = x * (xLimits[1] - xLimits[0]) / xSize + xLimits[0]
        juliaNum = julia((-0.7, 0.27015), (cx, cy))
        image.putpixel((x, y), (juliaNum, juliaNum, juliaNum))

image.save("Julia.png")
print(f"Finished Julia in {time.time() - startTime} seconds.")

# On my honour, I have neither given nor received unauthorised aid
# Isaac Marovitz