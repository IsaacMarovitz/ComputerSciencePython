import random
import math

num_of_point_to_calculate = 10000000
num_of_points = 0
num_of_points_in_circle = 0
pi = 0

for _ in range(num_of_point_to_calculate):
    num_of_points += 1
    point_x = random.random()
    point_y = random.random()
    distance_from_center = math.sqrt(point_x * point_x + point_y * point_y)
    if (distance_from_center < 1):
        num_of_points_in_circle += 1

pi = 4 * (num_of_points_in_circle / num_of_points)
print(pi)