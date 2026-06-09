
#include "renderer.h"
#include "constants.h"

void draw_grid(sf::RenderWindow& window) {
    sf::Color gridColor(40, 40, 40); // Dark grey
    sf::RectangleShape line; 

    // Vertical lines
    for (int x = 0; x < MAP_WIDTH; x += CELL) {
        line.setSize(sf::Vector2f(1.f, MAP_HEIGHT));
        line.setFillColor(gridColor);
        line.setPosition(x, 0);
        window.draw(line);
    }
    // Horizontal lines
    for (int y = 0; y < MAP_HEIGHT; y += CELL) {
        line.setSize(sf::Vector2f(MAP_WIDTH, 1.f));
        line.setFillColor(gridColor);
        line.setPosition(0, y);
        window.draw(line);
    }
}

void draw_entities(sf::RenderWindow& window, Environment& env){
    
}