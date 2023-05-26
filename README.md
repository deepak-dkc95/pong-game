# Pong Game

Classic Arcade [Pong](https://en.wikipedia.org/wiki/Pong) Game 

## Description
The game is designed to start automatically once the game is run.

### Controls
Right paddle - Arrow keys Up and Down\
Left Paddle - W and S keys

### Functionality
The ball gains speed each time it hits a paddle.\
The score of opponent increases by 1 upon missing to hit the ball with paddle.\
the ball resets its position and speed upon scoring.\
The game ends when a play scores 10 points.

## Installation

(In most IDEs, the package is pre-installed.)\
Use the package manager [pip](https://pypi.org/project/turtle/) to install turtle.

```bash
pip install turtle
```

## Usage

```python
# import statement
from turtle import Turtle, Screen 

# returns a screen object for interaction
screen = Screen()

# screen setup
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("THE PONG GAME")
screen.tracer(0)

# returns Turtle object
ball = Turtle()
```
