import random

class Grass:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rabbit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10


class Fox:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 20


class World:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)] # Setup of grid size

        self.grass = []
        self.rabbits = []
        self.foxes = []

    def spawn_grass(self):
        amount = random.randint(
            self.size * self.size // 4,
            self.size * self.size // 2
        )

        for _ in range(amount):
            x = random.randint(0, self.size - 1) # Rate of spawning for grass
            y = random.randint(0, self.size - 1)

            g = Grass(x, y)
            self.grass.append(g) # Modify to change grass symbol
            self.grid[y][x] = g

    def spawn_rabbits(self):
        amount = random.randint(
            self.size * self.size //20,
            self.size * self.size //8
        )
        for _ in range(amount):
            x = random.randint(0, self.size - 1) # Rate of spawning for rabbits
            y = random.randint(0, self.size - 1)

            r = Rabbit(x,y)
            self.rabbits.append(r) # Modify to change rabbits symbol
            self.grid[y][x] = r

    def spawn_foxes(self):
        amount = random.randint(
            self.size * self.size //40,
            self.size * self.size //16
        )
        for _ in range(amount):
            x = random.randint(0, self.size - 1) # Rate of spawning for foxes
            y = random.randint(0, self.size - 1)

            r = Fox(x,y)
            self.foxes.append(r) # Modify to change foxes symbol
            self.grid[y][x] = r

    def print_grid(self): # Printing of grid with organisms
        for row in self.grid:
            print(" ".join(self.symbol(cell) for cell in row))

    def symbol(self, cell):
        if isinstance(cell, Grass):
            return "G"
        if isinstance(cell, Rabbit):
            return "R"
        if isinstance(cell, Fox):
            return "F"
        return "."


size = int(input("Enter the size of the world: "))

world = World(size)
world.spawn_grass()
world.spawn_rabbits()
world.spawn_foxes()
world.print_grid()