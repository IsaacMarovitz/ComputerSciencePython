'''
	Properties: x and y (1,1)
	Methods:
		- rotate90 (CCW) (-1,1)
		- rotaten90 (CW) (1,-1)
		- rotate180 (-1,-1)
		- translate(2, 5) --> (3, 6)
		- mirror_x (1, -1)
		- mirror_y (-1, 1)
		
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rotate90(self):
        self.x = self.x-2

    def roataten90(self):
        self.y = self.y-2

    def translate(self):
        self.x = self.x+1
        self.y = self.y+1

    def mirror_x(self):
        self.y = -1 * self.y
    
    def mirror_y(self):
        self.x = -1 * self.x

    def print(self):
        print(f"{point.x}, {point.y}")

point = Point(1, 1)
point.rotate90()
point.print()