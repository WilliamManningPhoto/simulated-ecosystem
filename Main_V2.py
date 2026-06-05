### Confined grid size of 30 for simulation consistency
### Time frame of 1 year for simulation consistency

import random
import matplotlib.pyplot as plt

class Animal_behaviour:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 10
        
    def Movement(self): # Movement of animals
        print("get movement working")

    def Prey_finder(self): # Location of nearest prey
        print("get prey finder working")

    def Eating(self): # Eating when item next to animal
        print("get eating working")
    
    def Reproduction(self): # Reproduce with nearest other
        print("commit birth")

    def Age_animal(self):
        print("age dat boi")

    def Death(self): # Die of age, starvation been eaten
        print("commit death")

class Rocks:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Grass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Plant_growth(self): # Reproduction
        print("grow ma plants mate")

class Rabbit(Animal_behaviour):
    prey = (Grass,)
    reproduction_cooldown = 1

class Fox(Animal_behaviour):
    prey = (Rabbit,)
    reproduction_cooldown = 3

class Simulation:
    def Time_frame(self): # Working year cycle (dt)
        print("Time frame get working")

    def Day_cycle(self): # Day/night for active/inactive animals
        print("day cycle get working")

    def Weather_cycle(self): # Weather for hunting conditions
        print("Get simulation running")

    def Update_loop(self): # Update eat timestep (dt)
        print("Get simulation running")

class Environment:
    def __init__(self):
        self.size_grid = 30
        self.rocks = []
        self.grass = []
        self.rabbits = []
        self.foxes = []

    def Terrain_generation(self): # Generate basic terrain grid
        self.grid = [[None for _ in range(self.size_grid)] for _ in range(self.size_grid)] # Setup of grid size
               
        self.Spawn_obstacles()
        self.Rocks_fill()
        #self.Spawn_plants()
        #self.Spawn_animals()

        for row in self.grid:
            print(" ".join(self.symbol(cell) for cell in row))
        
    
    def Spawn_obstacles(self):
        amount = random.randint(
            self.size_grid * self.size_grid // 25, # Minimum rate of spawning for Rocks
            self.size_grid * self.size_grid // 20 # Maximum rate of spawning for Rocks
        )

        for _ in range(amount):
            x = random.randint(0, self.size_grid - 1) 
            y = random.randint(0, self.size_grid - 1)

            R = Rocks(x, y)
            self.rocks.append(R) # Modify to change rocks symbol
            self.grid[y][x] = R # Access the grid above and place R where grass i
        
        self.Rocks_fill()
        self.Rocks_fill_enclosed()
        

    def Rocks_fill(self):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        # Copy initial seeds so we don't expand newly created rocks in same pass
        seeds = list(self.rocks)

        for rock in seeds:
            x, y = rock.x, rock.y

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # Bounds check
                if 0 <= nx < self.size_grid and 0 <= ny < self.size_grid:

                    # Only expand into empty tiles
                    if self.grid[ny][nx] is None:

                        # 50% base chance, reduced slightly per direction bias
                        if random.random() < 0.50:

                            # Prevent over-clustering
                            neighbors = 0
                            for dx2, dy2 in directions:
                                tx, ty = nx + dx2, ny + dy2
                                if 0 <= tx < self.size_grid and 0 <= ty < self.size_grid:
                                    if isinstance(self.grid[ty][tx], Rocks):
                                        neighbors += 1

                            if neighbors < 3:
                                R = Rocks(nx, ny)
                                self.rocks.append(R)
                                self.grid[ny][nx] = R # Place new rock
                                
    def Rocks_fill_enclosed(self):
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        to_fill = []

        for y in range(self.size_grid):
            for x in range(self.size_grid):

                if self.grid[y][x] is None:

                    surrounded = True

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < self.size_grid and 0 <= ny < self.size_grid:
                            if not isinstance(self.grid[ny][nx], Rocks):
                                surrounded = False
                                break
                        else:
                            surrounded = False
                            break

                    if surrounded:
                        to_fill.append((x, y))

        for x, y in to_fill:
            R = Rocks(x, y)
            self.rocks.append(R)
            self.grid[y][x] = R

    def Spawn_plants(self): # Spawn rocks and grass
        
        amount = random.randint(
            self.size_grid * self.size_grid // 4,
            self.size_grid * self.size_grid // 2
        )

        for _ in range(amount):
            x = random.randint(0, self.size_grid - 1)
            y = random.randint(0, self.size_grid - 1)

            g = Grass(x, y)
            self.grass.append(g)
            self.grid[y][x] = g

    def Spawn_animals(self): # Spawn animals
        print("get animals spawning")
    
    def symbol(self, cell): # Animal identification
        if isinstance(cell, Rocks):
            return "R"
        if isinstance(cell, Grass):
            return "G"
        if isinstance(cell, Rabbit):
            return "R"
        if isinstance(cell, Fox):
            return "F"
        return "."
        
class Data_Collection:
    def Statistics(self): # Stats on animals alive
        print("get statistics working")
    
    def Graphs(self): # Graphing said stats
        print("get graph showing")
            
S = Simulation()
E = Environment()
D = Data_Collection()

E.Terrain_generation()