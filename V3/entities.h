#pragma once

class Animal { // Animal class has hare and fox use same data format
    public:
        int x, y;
        int energy;
        int eating_cooldown;
        int reproduction_cooldown;
        
        Animal(int x, int y, int energy, int eating_cooldown, int reproduction_cooldown);
        virtual void move() = 0; // Allow for independent movement functions
};

class Plant{
    public:
        int x, y;
        int reproduction_cooldown;

        Plant(int x, int y, int reproduction_cooldown);
        virtual void plant_reproduction() = 0;
};

class Hare : public Animal {
public:
    Hare(int x, int y); // Constructor declariations
    void move() override;
};

class Fox : public Animal {
public:
    Fox(int x, int y);
    void move() override;
};

class Grass : public Plant{
public:
    Grass(int x, int y);
    void plant_reproduction();
};

class Tree : public Plant{
public:
    Tree(int x, int y);
    void plant_reproduction();
};