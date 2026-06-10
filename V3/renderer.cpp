#include <SFML/Graphics.hpp>

#include "renderer.h"
#include "constants.h"
#include "environment.h"

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

// Like my symbol function in python to draw onto the grid
void draw_entities(sf::RenderWindow& window, Environment& env){
    for (auto& hare : env.hares){ //Loop through all declared hares
        sf::CircleShape circle(18.f); // Set shape
        circle.setFillColor(sf::Color::White); // Set colour

        int pos_x;
        int pos_y;
        pos_x = hare->x * CELL + CELL / 2;
        pos_y = hare->y * CELL + CELL / 2;

        circle.setPosition(pos_x, pos_y);
        window.draw(circle);
    }
    for (auto& fox : env.foxes){
        sf::CircleShape circle(18.f);
        circle.setFillColor(sf::Color::Red);

        int pos_x;
        int pos_y;
        pos_x = fox->x * CELL + CELL / 2;
        pos_y = fox->y * CELL + CELL / 2;

        circle.setPosition(pos_x, pos_y);
        window.draw(circle);
    }
    for (auto& grass : env.grass){
        sf::RectangleShape square(sf::Vector2f(18.f, 18.f));
        square.setFillColor(sf::Color::Green);

        int pos_x;
        int pos_y;
        pos_x = grass->x * CELL + CELL / 2;
        pos_y = grass->y * CELL + CELL / 2;

        square.setPosition(pos_x, pos_y);
        window.draw(square);
    }
    for (auto& tree : env.trees){
        sf::RectangleShape square(sf::Vector2f(18.f, 18.f));
        square.setFillColor(sf::Color(139, 69, 19)); // Custom RGB colours
        
        int pos_x;
        int pos_y;
        pos_x = tree->x * CELL + CELL / 2;
        pos_y = tree->y * CELL + CELL / 2;

        square.setPosition(pos_x, pos_y);
        window.draw(square);
    }
    for (auto& rock : env.rocks){
        sf::RectangleShape square(sf::Vector2f(18.f, 18.f));
        square.setFillColor(sf::Color(128, 128, 128));

        int pos_x;
        int pos_y;
        pos_x = rock->x * CELL + CELL / 2;
        pos_y = rock->y * CELL + CELL / 2;

        square.setPosition(pos_x, pos_y);
        window.draw(square);
    }
}