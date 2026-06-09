// Definitions for all entity constructors
// Each class passes shared data up the inheritance chain

#include "entities.h"

// Base entity constructor, sets position for all entities on the grid
Entity::Entity(int x, int y){
    this->x = x;
    this->y = y;
}

// Rock constructor setup to pass to Entity
Rock::Rock(int x, int y) : Entity(x, y){

}

// Animal constructor, passes position up to Entity then sets animal specific values
Animal::Animal(int x, int y, int energy, int eating_cooldown, int reproduction_cooldown) : Entity(x, y){
    this->energy = energy;
    this->eating_cooldown = eating_cooldown;
    this->reproduction_cooldown = reproduction_cooldown;
}

// Hare passes position and its fixed stats up to Animal
Hare::Hare(int x, int y) : Animal(x, y, 25, 2, 2) {

}
// FOX passes position and its fixed stats up to Animal
Fox::Fox(int x, int y) : Animal(x, y, 50, 6, 36) {

}

// Plant constructor, passes position up to Entity then sets plant specific values
Plant::Plant(int x, int y, int reproduction_cooldown) : Entity(x, y){
    this->reproduction_cooldown = reproduction_cooldown;
}

// Grass passes position and its reproduction rate up to Plant
Grass::Grass(int x, int y) : Plant(x, y, 1){

}

// Tree passes position and its reproduction rate up to Plant
Tree::Tree(int x, int y) : Plant(x, y, 1){

}

//temps
void Hare::move() {}
void Fox::move() {}
void Grass::plant_reproduction() {}
void Tree::plant_reproduction() {}