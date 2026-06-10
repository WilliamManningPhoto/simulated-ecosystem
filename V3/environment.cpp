// Define the Environment constructor so its initialised
// Definitions for all Environment functions

#include <iostream>
#include <cstdlib> 

#include "environment.h"
#include "constants.h"

// Looping through the grid to make it empty at first
Environment::Environment(){
    for (int y = 0; y < GRID_SIZE; y++) {
        for (int x = 0; x < GRID_SIZE; x++) {
            grid[y][x] = nullptr; // None in C++
        }
    }

    terrain_generation();
}

 // Calling all placement for initial setup
void Environment::terrain_generation(){
    obstacle_placement();
    plant_placement();
    animal_placement();
}

 // Rock placement
void Environment::obstacle_placement(){
    int amount = ROCK_MIN * GRID_SIZE * GRID_SIZE + rand() % (int)((ROCK_MAX - ROCK_MIN) * GRID_SIZE * GRID_SIZE);

    for (int i = 0; i < amount; i++){
        int x = rand() % GRID_SIZE;
        int y = rand() % GRID_SIZE;

        if (grid[y][x] == nullptr){
            Rock* r = new Rock(x, y);
            rocks.push_back(r);
            grid[y][x] = r;
        }
    }
    rock_fill();
}

void Environment::rock_fill(){

}

 // Grass, Trees
void Environment::plant_placement(){
    for (int y = 0; y < GRID_SIZE; y++){
        for (int x = 0; x < GRID_SIZE; x++){
            Grass* g = new Grass(x, y);
            grass.push_back(g);
            grid[x][y] = g;
        }
    }
}

// Hares and foxes placed
void Environment::animal_placement(){

}

// If entity dies remove from game
void Environment::entity_removal(){

}
