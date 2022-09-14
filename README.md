# Conways Game Of Life

Implementation of Conway's "Game Of Life" keeping in mind the idea of decoupling and reusing capabilities


The game is implemented using Python 3.9.5, numpy, and [Pygame](https://www.pygame.org/).

## Running The Game

I recommend Using Python (3.9.5) on a separate environment using Virtualenv and install the dependencies with:

```shell
pip install -r requirements.txt
```

Given that all the dependencies were installed, running the
game is as simple as

```shell
python main.py
```

## Understand The Code

This game was created as a study of decoupling systems. 
The intention was to show that you can have multiple systems encapsulated and being used with each other, just maintaining the contract of the functions.
I have created diferent classes for the diferent systems that interacts with the user.

### The Boards
The boards are, as the name said, the board of the game, in which the cells are stored as positions and statuses. For the effects of the example, i have created two boards. One implemented in Numpy, and another implemented using the example of Matheus Gomes from his post [Conway's Game Of Life 
can be implemented in a few lines of Python](https://matgomes.com/conways-game-of-life-python).
Both boards have a common ground in his functions and contracts that allows to comunicate with the game system

### The Game
the class Life contains the rules of the game, and the way the cycles are excecuted. this class can use any board that is implemented as a Board System

### The Renderer
this is a simple class that allows to render a game via Pygame

The idea of the exercise is to demostrate that you can have decoupled systems that can comunicate and interact with eachother without needing to depend entirely in their implementation. 
with this in mind, we can have diferent kinds of boards, games or renderers, only changing the systems, and using the other systems respecting their contracts.

