import random

class Grass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Animal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10

class Rabbit(Animal):
        prey = (Grass,)


class Fox(Animal):
        prey = (Rabbit,)


class World:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)] # Setup of grid size

        self.grass = []
        self.rabbits = []
        self.foxes = []

    def print_counts(self):
        print("Grass on grid:", self.count_grass_on_grid())
        print("Rabbits on grid:", self.count_rabbits_on_grid())
        print("Foxes on grid:", self.count_foxes_on_grid())

    def time_step(self):
        for rabbit in self.rabbits:
            self.move_animal(rabbit)

        for fox in self.foxes:
            self.move_animal(fox)
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
    
    def find_nearest_prey(self, animal):

        prey_types = animal.prey

        for radius in range(1,self.size):

            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):

                    x = animal.x + dx
                    y = animal.y + dy

                    if 0 <= x < self.size and 0 <= y < self.size:

                        cell = self.grid[y][x]

                        if isinstance(cell, prey_types):
                            return (x, y)
    
    def move_towards(self,animal,target):
        tx, ty = target

        self.grid[animal.y][animal.x] = None

        dx = 0
        dy = 0

        if tx > animal.x:
            dx = 1
        elif tx < animal.x:
            dx = -1

        if ty > animal.y:
            dy = 1
        elif ty < animal.y:
            dy = -1

        new_x = max(0, min(self.size - 1, animal.x + dx))
        new_y = max(0, min(self.size - 1, animal.y + dy))

        animal.x = new_x
        animal.y = new_y

        self.grid[new_y][new_x] = animal
        
    def random_move(self, animal):

        self.grid[animal.y][animal.x] = None

        dx, dy = random.choice([
            (0,1), (0,-1), (1,0), (-1,0)
        ])

        new_x = max(0, min(self.size - 1, animal.x + dx))
        new_y = max(0, min(self.size - 1, animal.y + dy))

        animal.x = new_x
        animal.y = new_y

        self.grid[new_y][new_x] = animal

    def move_animal(self,animal):
        target = self.find_nearest_prey(animal)

        if target:
            self.move_towards(animal, target)
        else:
            self.random_move(animal)


        
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

    def count_grass_on_grid(self):
        count = 0

        for row in self.grid:
            for cell in row:
                if isinstance(cell, Grass):
                    count += 1

        return count
    
    def count_rabbits_on_grid(self):
        count = 0

        for row in self.grid:
            for cell in row:
                if isinstance(cell, Rabbit):
                    count += 1

        return count
    
    def count_foxes_on_grid(self):
        count = 0

        for row in self.grid:
            for cell in row:
                if isinstance(cell, Fox):
                    count += 1

        return count
    




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
