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

    def print_counts(self):
        print(f"Grass: {len(self.grass)}")
        print(f"Rabbits: {len(self.rabbits)}")
        print(f"Foxes: {len(self.foxes)}")

    def time_step(self):
        self.move_rabbits()
        self.move_foxes()
        self.grow_grass()

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
            self.grid[y][x] = g # Access the grid above and place G where grass is

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

    def move_rabbits(self):
        for rabbit in self.rabbits:
            self.grid[rabbit.y][rabbit.x] = None # Get rid of current position

            dx, dy = random.choice([
                (0,1),(0,-1),(1,0),(-1,0) # Choose next square randomly (update for ovement to grass)
            ])

            new_x = max(0, min(self.size-1, rabbit.x + dx)) # Modify old position with new one
            new_y = max(0, min(self.size-1, rabbit.y + dy))

            rabbit.x = new_x # Attatch new position to rabbit
            rabbit.y = new_y

            self.grid[new_y][new_x] = rabbit # Put on grid in new position

    def move_foxes(self):
        for fox in self.foxes:
            self.grid[fox.y][fox.x] = None # Get rid of current position

            dx, dy = random.choice([
                (0,1),(0,-1),(1,0),(-1,0) # Choose next square randomly (update for movement to rabbit)
            ])

            new_x = max(0, min(self.size-1, fox.x + dx)) # Modify old position with new one
            new_y = max(0, min(self.size-1, fox.y + dy))

            fox.x = new_x # Attatch new position to Fox
            fox.y = new_y

            self.grid[new_y][new_x] = fox # Put on grid in new position
    
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


    

size = int(input("Enter the size of the world: "))

world = World(size)
world.spawn_grass()
world.spawn_rabbits()
world.spawn_foxes()
world.print_grid()

while True:
    world.time_step()
    world.print_grid()
    world.print_counts()
    input("Press Enter for next step...")
