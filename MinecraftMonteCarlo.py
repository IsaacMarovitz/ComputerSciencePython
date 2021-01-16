import numpy, multiprocessing
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from collections import Counter
from tqdm import tqdm

diamond_chance = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random_weights = [27/126, 6/126, 11/126, 11/126, 24/126, 10/126, 20/126, 3/126, 12/126, 2/126]
world_size = 30000000
chunk_size = 16
number_of_chunks = (world_size**2) / (chunk_size**2)
number_of_chunks_to_test = 1000
number_of_diamonds = 0
diamond_count = []
diamond_count_occurence = []
number_of_simulations = 50000

processes_completed = 0

def run_sim(index):
    global number_of_chunks_to_test, number_of_chunks, random_weights, processes_completed
    # print(f"Started process {index}")
    number_of_diamonds = 0
    for _ in range(number_of_chunks_to_test):
        number_of_diamonds += numpy.random.choice(diamond_chance, p=random_weights)

    # print(f"Finished process {index}")
    processes_completed += 1
    return round((number_of_diamonds / number_of_chunks_to_test) * number_of_chunks)    

# Source: https://stackoverflow.com/questions/61330427/set-y-axis-in-millions
def trillions(x, pos):
    return '%1.1fT' % (x * 1e-12)

if __name__ == "__main__":
    formatter = FuncFormatter(trillions)

    with multiprocessing.Pool(4) as pool:
        # Source: https://stackoverflow.com/questions/41920124/multiprocessing-use-tqdm-to-display-a-progress-bar
        diamond_count = list(tqdm(pool.imap(run_sim, range(number_of_simulations)), total=number_of_simulations))

    print("Finished Simulations")
    diamond_count_occurence = Counter(diamond_count)
    # Helped for this line by Max Fan
    sorted_dict = {k:diamond_count_occurence[k] for k in sorted(diamond_count_occurence.keys())}
    print(sorted_dict)

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.get_xl
    ax.plot(sorted_dict.keys(), sorted_dict.values())
    ax.set_ylabel('No. of Worlds with x Diamond Ores')
    ax.set_xlabel('No. of Diamond Ores in World (in Trillions)')
    ax.xaxis.set_major_formatter(formatter)
    ax.set_title('Total Number of Diamond Ores per Minecraft World')
    ax.margins(x=0, y=0)
    plt.show()
