import random

def generate_heightmap(size):

    terrain = []

    for i in range(size):
        terrain.append(random.randint(0,10))

    return terrain
