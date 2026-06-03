import random

class Grass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class World:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)] # Setup of grid size

        self.grass = []

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

    def print_grid(self): # Printing of grid with organisms
        for row in self.grid:
            print(" ".join(self.symbol(cell) for cell in row))

    def symbol(self, cell):
        if isinstance(cell, Grass):
            return "G"
        return "."
    
    def time_step(self):
        self.grow_grass()

    def grow_grass(self):
        new_grass = []

        for grass in self.grass:
            if random.random() < 0.25:  # 25% chance to try spreading

                directions = [
                    (0, 1), (0, -1), (1, 0), (-1, 0)
                ]

                dx, dy = random.choice(directions)

                new_x = grass.x + dx
                new_y = grass.y + dy

                # check bounds
                if 0 <= new_x < self.size and 0 <= new_y < self.size:

                    # only grow if empty
                    if self.grid[new_y][new_x] is None:

                        g = Grass(new_x, new_y)
                        new_grass.append(g)
                        self.grid[new_y][new_x] = g

        self.grass.extend(new_grass)
    
    def print_counts(self):
        print(f"Grass: {len(self.grass)}")

size = int(input("Enter the size of the world: "))

world = World(size)
world.spawn_grass()
world.print_grid()

while True:
    world.time_step()
    world.print_grid()
    world.print_counts()
    input("Press Enter for next step...")
