#include <iostream>
#include <SFML/Graphics.hpp>
#include <vector>
#include <cstdlib>
#include <string>

#include "environment.h"
#include "renderer.h"

int main() {
    srand(time(0));
    Environment env;
    sf::RenderWindow window(sf::VideoMode(1500, 800), "Ecosystem_Simulator"); // Render the window with a 800 by 1500 pixel space

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close(); // X to close
        }
        window.clear(sf::Color::Black);
        draw_grid(window);
        draw_entities(window, env);
        window.display();
    }
}