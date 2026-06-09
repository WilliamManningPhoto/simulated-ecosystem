#include <iostream>
#include <SFML/Graphics.hpp>
#include <vector>
#include <cstdlib>
#include <string>

const int CELL = 20;
const int MAP_HEIGHT = 800;
const int MAP_WIDTH = 1500;

void drawGrid(sf::RenderWindow& window) {
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

int main() {
    sf::RenderWindow window(sf::VideoMode(1500, 800), "Ecosystem_Simulator"); // Render the window with a 800 by 1500 pixel space

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close(); // X to close
        }
        window.clear(sf::Color::Black);
        drawGrid(window);
        window.display();
    }
}