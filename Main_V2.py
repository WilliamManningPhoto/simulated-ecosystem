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

    def Death(self): # Die
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
        self.grid = []
        self.animals = []
        self.grass = []
        self.rocks = []

    def Terrain_generation(self): # Generate basic terrain grid
        self.grid = [[None for _ in range(30)] for _ in range(30)] # Setup of grid size
               
        for row in self.grid:
            print(" ".join(self.symbol(cell) for cell in row))

    def Spawn_terrain(self): # Spawn rocks and grass
        print("get terrain spawning")

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