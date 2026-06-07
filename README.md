# Ecosystem Simulator

A Python-based predator-prey ecosystem simulator that models interactions between grass, rabbits, and foxes on a 2D grid.

The simulation demonstrates population dynamics, resource competition, reproduction, predation, and extinction events. Population data is recorded over time and visualized using Matplotlib.

## Features

* Grid-based ecosystem simulation
* Terrain generation
* Grass growth and spreading
* Rabbit foraging behavior
* Fox hunting behavior with escape mechanics
* Energy-based survival system
* Reproduction with configurable cooldowns
* Population tracking over time
* Automatic graph generation

## Species

### Grass

* Spreads into adjacent empty cells
* Serves as the food source for rabbits

### Rabbits

* Search for nearby grass
* Gain energy by eating grass
* Lose energy each timestep
* Reproduce when energy requirements are met
* Die when energy reaches zero

### Foxes

* Search for nearby rabbits
* Gain energy by successfully hunting rabbits
* Hunting includes a chance for prey to escape
* Lose energy each timestep
* Reproduce when energy requirements are met
* Die when energy reaches zero

## Requirements

* Python 3.x
* Matplotlib

Install dependencies:

```bash
pip install matplotlib
```

You will be prompted to enter the world size:

```text
Enter the size of the world: (35 is for the best!)
```

The simulation will run for a fixed number of timesteps and display a graph showing population changes over time.

## Example Population Graph 1
<img width="640" height="480" alt="Ecosystem_trial" src="https://github.com/user-attachments/assets/be3f39c8-3b09-4dc8-b499-0b360bebcc86" />


The generated graph tracks:

* Rabbit population
* Fox population
* Grass population

## Example Population Graph 2
<img width="640" height="480" alt="Ecosystem_trial_V2" src="https://github.com/user-attachments/assets/dc73dbcf-64f3-43a6-a5ac-311064b9fc98" />

The generated graph tracks:

* Rabbit population
* Fox population

This allows you to observe predator-prey cycles, ecosystem stability, and extinction events. ( It will crash from unstable ecosystem :) )

## Simulation Mechanics

### Reproduction

Animals reproduce when:

* Their energy exceeds a species-specific threshold
* Their reproduction cooldown has expired
* An adjacent cell is available

After reproduction:

* Energy is reduced
* A cooldown is applied

## License

This project is open source and available under the MIT License.
