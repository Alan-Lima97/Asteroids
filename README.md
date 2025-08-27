# Asteroids

A clone of the classic **Asteroids** arcade game, built with Python and Pygame.

---

##  Project Structure

- *main.py*
  - Initializes the window, game loop, and game state.
  
- *player.py*
  - Defines the player-controlled spaceship.

- *asteroidfield.py*
  - Manages asteroid creation and updates.

- *shot.py*
  - Handles bullets fired by the player.

- *circleshape.py*
  - Base class for circular shapes.

- *constants.py*
  - Stores global constants.

- *gameover.py*
  - Displays the Game Over screen with the final score and interactive options.

---

##  How to Play

1. Clone this repository and navigate into it:

	```bash
	git clone https://github.com/Alan-Lima97/Asteroids.git
	cd Asteroids
	```

2. Install Pygame (if you don’t already have it):
	- pip install pygame

3. Run the game:
	- python main.py

## Controls

- W = move foward
- S = move backward
- A = rotate left
- D = rotate right
- Space = shoot

## Gameplay

- You start with 3 lives. Each collision with an asteroid costs one life.

- Destroying asteroids gives you points, based on their size:

	- Large: 20 points
	- Medium: 40 points
	- Small: 00 points

- Your score and remaining lives are displayed at the top of the screen.

- When all lives are lost, the Game Over screen appears:

	- Shows your final score.
	- Press ENTER to restart or ESC/close window to quit.
