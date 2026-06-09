// Define the Environment constructor so its initialised
// Definitions for all Environment functions

#include "environment.h"
#include "constants.h"

// Looping through the grid to make it empty at first
Environment::Environment(){
    for (int y = 0; y < GRID_SIZE; y++) {
        for (int x = 0; x < GRID_SIZE; x++) {
            grid[y][x] = nullptr; // None in C++
        }
    }
}


void Environment::terrain_generation(){

}

void Environment::obstacle_placement(){

}

void Environment::plant_placement(){

}

void Environment::animal_placement(){

}

void Environment::entity_removal(){

}
