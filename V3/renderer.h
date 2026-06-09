#pragma once

#include <iostream>
#include <SFML/Graphics.hpp>
#include <vector>
#include <cstdlib>
#include <string>

#include "environment.h"

// Draw grid with lines
void draw_grid(sf::RenderWindow& window);

// Render all entities onto map
void draw_entities(sf::RenderWindow& window, Environment& env);