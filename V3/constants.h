#pragma once

// Utilised to hold constants i want globally also easy to modify for fun
const int CELL = 20;
const int MAP_HEIGHT = 800;
const int MAP_WIDTH = 1500;
const int GRID_SIZE = 100;
const float TIME_INTERVAL = 0.001; // 1000 simulation tick per second
const int SIMULATION_DAYS = 365; // Amount of days to run each runs 24 ticks per day

// Spawn rates of entities
const float ROCK_MIN = 0.001;
const float ROCK_MAX = 0.005;

const float HARE_MIN = 0.05;
const float HARE_MAX = 0.15;

const float FOX_MIN = 0.001;
const float FOX_MAX = 0.003;

const float TREE_MIN = 0.01;
const float TREE_MAX = 0.02;