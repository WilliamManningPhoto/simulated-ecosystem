#include <iostream>

#include "simulation.h"
#include "environment.h"
#include "entities.h"

Simulation::Simulation(Environment& env) : env(env), step(0), running(true){

};


void Simulation::update_loop(){
    env.grow_grass();
    for (auto& hare : env.hares) {
        hare->move(env);
    }

    step++;
    if (step >= SIMULATION_DAYS * 24) {
        running = false;
    }
    std::cout << "Step: " << step << std::endl;
};
