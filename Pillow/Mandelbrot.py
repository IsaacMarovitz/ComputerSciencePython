from PIL import Image
import math, time

xSize = 1000
ySize = 1000
max_iterations = 255
xOffset = 4 / xSize
yOffset = 4 / ySize
startTime = time.time()
image = Image.new("RGB", (xSize, ySize))

def mandelbrot(c, z=complex(0, 0), iterations=1):
    zNew = z**2 + c
    if abs(zNew) > 2 or iterations >= max_iterations:
        return iterations
    else:
        iterations += 1
        return mandelbrot(c, zNew, iterations)

for x in range(xSize):
    for y in range(ySize):
        cx = x*xOffset-2
        cy = y*yOffset-2
        mandelbrotNum = mandelbrot(complex(cx, cy))
        image.putpixel((x, y), (mandelbrotNum, mandelbrotNum, mandelbrotNum))

image.save("Mandelbrot.png")
print(f"Finished Mandelbrot in {time.time() - startTime} seconds.")
