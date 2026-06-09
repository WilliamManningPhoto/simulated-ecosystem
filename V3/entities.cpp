#include "entities.h"

Animal::Animal(int x, int y, int energy, int eating_cooldown, int reproduction_cooldown){
    this->x = x;
    this->y = y;
    this->energy = energy;
    this->eating_cooldown = eating_cooldown;
    this->reproduction_cooldown = reproduction_cooldown;
}

Hare::Hare(int x, int y) : Animal(x, y, 25, 2, 2) {

}

Fox::Fox(int x, int y) : Animal(x, y, 50, 6, 36) {

}

Plant::Plant(int x, int y, int reproduction_cooldown){
    this->x = x;
    this->y = y;
    this->reproduction_cooldown = reproduction_cooldown;
}

Grass::Grass(int x, int y) : Plant(x, y, 1){

}

Tree::Tree(int x, int y) : Plant(x, y, 1){

}