### Confined grid size of 30 for simulation consistency
### Time frame of 1 year for simulation consistency

import random
import matplotlib.pyplot as plt

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
GREY = "\033[90m"
RESET = "\033[0m"

class Hare_behaviour:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 25
        self.standing_on = None
        
    def Movement(self, env):
        self.energy -= 1

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy

            # Bounds check
            if not (0 <= new_x < env.size_grid and 0 <= new_y < env.size_grid):
                continue

            target = env.grid[new_y][new_x]

            # Move to grass or empty tile only
            if isinstance(target, Grass) or target is None:
                env.grid[self.y][self.x] = self.standing_on  # Restore old tile
                self.standing_on = target # Remember new tile
                self.x = new_x
                self.y = new_y
                env.grid[new_y][new_x] = self    # Move to new tile
                break

    
    def Escape_attack(self):
        print("escape the foxes attack on a unsuccessful attack")

    def Eating(self): # Eating when item next to animal
        print("get eating working")
    
    def Mate_finder(self):
        print("find mate")
    
    def Reproduction(self): # Reproduce with nearest other
        print("commit birth")

    def Age_animal(self):
        print("age dat boi")

class Fox_behaviour:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 50
        self.standing_on = None
    
    def Prey_finder(self, env): # Location of nearest prey
        nearest = None
        nearest_dist = float("inf")

        for hare in env.hares:
            dx = abs(hare.x - self.x)
            dy = abs(hare.y - self.y)
            dist = dx + dy

            if dist <= self.vision_range and dist < nearest_dist:
                nearest = hare
                nearest_dist = dist
        return nearest
            
    def Movement(self, env): # Movement of fox
        self.energy -= 3

        target = self.Prey_finder(env)

        if target:
            # Move toward hare
            dx = 1 if target.x > self.x else -1 if target.x < self.x else 0
            dy = 1 if target.y > self.y else -1 if target.y < self.y else 0
        else:
            # Roam randomly
            dx, dy = random.choice([(0,1), (0,-1), (1,0), (-1,0)])

        new_x = self.x + dx
        new_y = self.y + dy

        # Bounds check
        if not (0 <= new_x < env.size_grid and 0 <= new_y < env.size_grid):
            return

        target_tile = env.grid[new_y][new_x]

        # Only move to grass or empty tile
        if isinstance(target_tile, Grass) or target_tile is None:
            env.grid[self.y][self.x] = self.standing_on
            self.standing_on = target_tile
            self.x = new_x
            self.y = new_y
            env.grid[new_y][new_x] = self
        
    def Pounce(self):
        print("special ability to jump 2 squares?, extra energy?")

    def Eating(self): # Eating when item next to animal
        print("get eating working")
    
    def Mate_finder(self):
        print("find mate")
    
    def Reproduction(self): # Reproduce with nearest other
        print("commit birth")

    def Age_animal(self):
        print("age dat boi")


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

class Hare(Hare_behaviour):
    prey = (Grass,)
    reproduction_cooldown = 1

class Fox(Fox_behaviour):
    prey = (Hare,)
    reproduction_cooldown = 3
    vision_range = 5

class Simulation:
    def __init__(self,env): # Working year cycle (dt)
        self.env = env
        self.year = 365 * 24 # Modify for length of simulation
        self.step = 0

    def Day_cycle(self): # Day/night for active/inactive animals
        print("day cycle get working")

    def Weather_cycle(self): # Weather for hunting conditions
        print("Get simulation running")

    def Print_map(self):
        for row in self.env.grid:
            print(" ".join(self.env.symbol(cell) for cell in row))

    def Update_loop(self): # Update eat timestep (dt)
            
        for hare in list(self.env.hares):  # list() so we can remove during iteration
            hare.Movement(self.env)
            if hare.energy <= 0:
                self.env.remove_hare(hare)

        for fox in list(self.env.foxes):
            fox.Movement(self.env)
            if fox.energy <= 0:
                self.env.remove_fox(fox)

        self.Print_map()
        print("Step", self.step)
        self.step += 1

class Environment:
    def __init__(self):
        self.size_grid = 30
        self.rocks = []
        self.grass = []
        self.hares = []
        self.foxes = []

    def Terrain_generation(self): # Generate basic terrain grid
        self.grid = [[None for _ in range(self.size_grid)] for _ in range(self.size_grid)] # Setup of grid size
               
        self.Spawn_obstacles()
        self.Rocks_fill()
        self.Spawn_plants()
        self.Spawn_animals()
          
    def Spawn_obstacles(self): # Spawn obstacles such as rocks
        amount = random.randint(
            self.size_grid * self.size_grid // 30, # Minimum rate of spawning for Rocks
            self.size_grid * self.size_grid // 25 # Maximum rate of spawning for Rocks
        )

        for _ in range(amount):
            x = random.randint(0, self.size_grid - 1) 
            y = random.randint(0, self.size_grid - 1)

            R = Rocks(x, y)
            self.rocks.append(R) # Modify to change rocks symbol
            self.grid[y][x] = R # Access the grid above and place R where grass i
        
        for i in range(5):
            self.Rocks_fill()
            self.Rocks_fill_enclosed()
          
    def Rocks_fill(self): # Flood fill rocks for clustering
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

                        # 15% base chance, reduced slightly per direction bias
                        if random.random() < 0.15:

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
                                
    def Rocks_fill_enclosed(self): # Fill pockets
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

    def Spawn_plants(self): # Spawn Plants such as grass

        for y in range(self.size_grid):
            for x in range(self.size_grid):

                if self.grid[y][x] is None:
                    g = Grass(x, y)
                    self.grass.append(g)
                    self.grid[y][x] = g

    def Spawn_animals(self): # Spawn animals
        hare_amount = int((self.size_grid * self.size_grid) * 0.05) # 45 initial hares
        fox_amount = int((self.size_grid * self.size_grid) * 0.01) # 9 initial foxes

        grass_tiles = [(g.x, g.y) for g in self.grass]
        spawn_tiles = random.sample(grass_tiles, hare_amount)
        
        for x, y in spawn_tiles:
            h = Hare(x, y)
            self.hares.append(h)
            self.grid[y][x] = h
        
        grass_tiles = [(g.x, g.y) for g in self.grass]
        spawn_tiles = random.sample(grass_tiles, fox_amount)

        for x, y in spawn_tiles:
            f = Fox(x, y)
            self.foxes.append(f)
            self.grid[y][x] = f
    
    def remove_hare(self, hare):
        self.grid[hare.y][hare.x] = hare.standing_on
        self.hares.remove(hare)

    def remove_fox(self, fox):
        self.grid[fox.y][fox.x] = fox.standing_on
        self.foxes.remove(fox)

    def symbol(self, cell):
        if isinstance(cell, Rocks):
            return f"{GREY}R{RESET}"

        if isinstance(cell, Grass):
            return f"{GREEN}G{RESET}"

        if isinstance(cell, Hare):
            return f"{YELLOW}H{RESET}"

        if isinstance(cell, Fox):
            return f"{RED}F{RESET}"

        return "."
        
class Data_Collection:
    def Statistics(self): # Stats on animals alive
        print("get statistics working")
    
    def Graphs(self): # Graphing said stats
        print("get graph showing")
            
E = Environment()
S = Simulation(E)

E.Terrain_generation()

for steps in range(S.year):
    S.Update_loop()
    input("Press Enter for next step...")
