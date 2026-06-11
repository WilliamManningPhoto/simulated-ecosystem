#pragma once

#include "entities.h"
#include "environment.h"

class Simulation{
    public:
        int step;
        bool running;
        
        Environment& env;
        Simulation(Environment& env);

    void update_loop();
};