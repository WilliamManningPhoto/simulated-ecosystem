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
        self.eating_cooldown = 0
        self.reproduction_cooldown = 0
        
    def Movement(self, env):
        self.energy -= 1
        self.eating_cooldown = max(0, self.eating_cooldown - 1)
        self.reproduction_cooldown = max(0, self.reproduction_cooldown - 1)



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

        self.Eating(env)

        if self.energy >= 50 and self.reproduction_cooldown <= 0:
            self.Reproduction(env)
            self.energy -= 30
            self.reproduction_cooldown = 2

    
    def Escape_attack(self):
        print("escape the foxes attack on a unsuccessful attack")

    def Eating(self, env): # Eating when animal is on prey

        if isinstance(self.standing_on, Grass):
            if self.eating_cooldown <= 0:
                self.energy += 10
                env.Remove_grass(self.standing_on)
                self.standing_on = None
                self.eating_cooldown = self.prey_cooldown
    
    def Reproduction(self, env): # Reproduce asexually
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy

            if not (0 <= new_x < env.size_grid and 0 <= new_y < env.size_grid):
                continue

            if env.grid[new_y][new_x] is None or isinstance(env.grid[new_y][new_x], Grass):
                baby = Hare(new_x, new_y)
                baby.energy = 20
                baby.standing_on = env.grid[new_y][new_x]
                env.hares.append(baby)
                env.grid[new_y][new_x] = baby
                return  # Only spawn one baby

    def Age_animal(self):
        print("age dat boi")

class Fox_behaviour:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.energy = 50
        self.standing_on = None
        self.eating_cooldown = 0
        self.reproduction_cooldown = 0
    
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
        self.energy -= 1
        self.eating_cooldown = max(0, self.eating_cooldown - 1)

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

        can_eat = self.eating_cooldown <= 0
        hare_tile_ok = isinstance(target_tile, Hare) and can_eat

        # Only move to grass, empty tile or hare
        if isinstance(target_tile, Grass) or target_tile is None or hare_tile_ok:
            env.grid[self.y][self.x] = self.standing_on
            self.standing_on = target_tile
            self.x = new_x
            self.y = new_y
            env.grid[new_y][new_x] = self

            self.Eating(env)

        if self.energy >= 150 and self.reproduction_cooldown <= 0:
            self.Reproduction(env)
            self.energy -= 100
            self.reproduction_cooldown = 5

        
    def Pounce(self):
        print("special ability to jump 2 squares?, extra energy?")

    def Eating(self, env): # Eating when item next to animal

        if isinstance(self.standing_on, Hare):
            if self.eating_cooldown <= 0:
                self.energy += 40
                eaten = self.standing_on
                self.standing_on = None
                env.Remove_hare(eaten)
                self.eating_cooldown = self.prey_cooldown
                
    def Reproduction(self, env): # Reproduce asexually
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        random.shuffle(directions)

        for dx, dy in directions:
            new_x = self.x + dx
            new_y = self.y + dy

            if not (0 <= new_x < env.size_grid and 0 <= new_y < env.size_grid):
                continue

            if env.grid[new_y][new_x] is None or isinstance(env.grid[new_y][new_x], Grass):
                baby = Fox(new_x, new_y)
                baby.standing_on = None
                env.foxes.append(baby)
                env.grid[new_y][new_x] = baby
                return  # Only spawn one baby
            
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

class Hare(Hare_behaviour):
    prey = (Grass,)
    prey_cooldown = 2

class Fox(Fox_behaviour):
    prey = (Hare,)
    vision_range = 5
    prey_cooldown = 8

class Simulation:
    def __init__(self, env, data): # Working year cycle (dt)
        self.days = 150 # Modify for length of simulation
        self.env = env
        self.data = data
        self.year = self.days * 24 
        self.step = 0

    def Day_cycle(self): # Day/night for active/inactive animals, slow metabolism at night?
        print("day cycle get working")

    def Weather_cycle(self): # Weather for hunting conditions? lower success chance?
        print("Get simulation running")

    def Print_map(self):
        for row in self.env.grid:
            print(" ".join(self.env.symbol(cell) for cell in row))

    def Update_loop(self): # Update eat timestep (dt)

        self.data.Statistics()
        self.env.Grow_grass()
            
        for hare in list(self.env.hares):  # list() so we can remove during iteration
            hare.Movement(self.env)
            if hare.energy <= 0:
                self.env.Remove_hare(hare)

        for fox in list(self.env.foxes):
            fox.Movement(self.env)
            if fox.energy <= 0:
                self.env.Remove_fox(fox)

        #self.Print_map()
        print(f"Grass: {len(self.env.grass)}")
        print(f"Hares: {len(self.env.hares)}")
        print(f"Foxes: {len(self.env.foxes)}")
        print("Step", self.step)
        self.step += 1

class Environment:
    def __init__(self):
        self.size_grid = 60
        self.rocks = []
        self.hares = []
        self.foxes = []

        self.history_rabbits = []
        self.history_foxes = []
        self.history_grass = []

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
    
    @property
    def grass(self):
        return [cell for row in self.grid for cell in row if isinstance(cell, Grass)]

    def Spawn_plants(self): # Spawn plants such as grass
        for y in range(self.size_grid):
            for x in range(self.size_grid):
                if self.grid[y][x] is None:
                    self.grid[y][x] = Grass(x, y)

    def Spawn_animals(self):
        hare_amount = int((self.size_grid * self.size_grid) * 0.02) # initial hares
        fox_amount = int((self.size_grid * self.size_grid) * 0.005) # initial foxes

        grass_tiles = [(g.x, g.y) for g in self.grass]
        spawn_tiles = random.sample(grass_tiles, hare_amount)

        for x, y in spawn_tiles:
            h = Hare(x, y)
            h.standing_on = None
            self.hares.append(h)
            self.grid[y][x] = h

        grass_tiles = [(g.x, g.y) for g in self.grass]
        spawn_tiles = random.sample(grass_tiles, fox_amount)

        for x, y in spawn_tiles:
            f = Fox(x, y)
            f.standing_on = None
            self.foxes.append(f)
            self.grid[y][x] = f
    
    def Grow_grass(self): # Grow grass into empty spaces
        claimed = set()
        current_grass = self.grass
        for grass in current_grass:
            if random.random() < 0.5: # Grass spawn rate adjust for more/less
                dx, dy = random.choice([(0,1),(0,-1),(1,0),(-1,0),(0,2),(0,-2),(2,0),(-2,0),(1,1),(1,-1),(1,-1),(-1,-1)])
                new_x, new_y = grass.x + dx, grass.y + dy
                if 0 <= new_x < self.size_grid and 0 <= new_y < self.size_grid:
                    if self.grid[new_y][new_x] is None and (new_x, new_y) not in claimed:
                        claimed.add((new_x, new_y))
                        self.grid[new_y][new_x] = Grass(new_x, new_y)
    
    def Remove_grass(self, grass):
        self.grid[grass.y][grass.x] = None

    def Remove_hare(self, hare):
        if hare in self.hares:
            if self.grid[hare.y][hare.x] is hare:
                self.grid[hare.y][hare.x] = hare.standing_on
            self.hares.remove(hare)
            hare.standing_on = None

    def Remove_fox(self, fox):
        if fox in self.foxes:
            if self.grid[fox.y][fox.x] is fox:
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
    def __init__(self, env):
        self.env = env

    def Statistics(self): # Stats on animals alive

        self.env.history_grass.append(len(self.env.grass))
        self.env.history_rabbits.append(len(self.env.hares))
        self.env.history_foxes.append(len(self.env.foxes))
    
    def Graphs(self, env):
        plt.plot(env.history_rabbits, label="Rabbits")
        plt.plot(env.history_foxes, label="Foxes")
        #plt.plot(env.history_grass, label="Grass")

        plt.legend()
        plt.show()

'''
E = Environment()
D = Data_Collection(E)
S = Simulation(E, D)


E.Terrain_generation()

for steps in range(S.year):
    S.Update_loop()
    #input("Press Enter for next step...")

D.Graphs(E)
'''
all_hare_runs = []
all_fox_runs = []

for run in range(5):
    E = Environment()
    D = Data_Collection(E)
    S = Simulation(E, D)
    E.Terrain_generation()
    for steps in range(S.year):
        S.Update_loop()
    all_hare_runs.append(E.history_rabbits)
    all_fox_runs.append(E.history_foxes)

for run in all_hare_runs:
    plt.plot(run, color='yellow', alpha=0.4)
for run in all_fox_runs:
    plt.plot(run, color='red', alpha=0.4)
plt.show()