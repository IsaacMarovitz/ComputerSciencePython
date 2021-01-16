import random
import matplotlib.pyplot as plt

num_flips = 100
num_simulations = 100000
numbers = []
num_count = []

for _ in range(num_simulations):
    num_heads = 0
    for _ in range(num_flips):
        num = random.randint(0, 1)
        if (num == 0):
            num_heads += 1
    numbers.append(num_heads)

for x in range(num_flips):
    num_count.append(numbers.count(x))

plt.plot(num_count)
plt.show()