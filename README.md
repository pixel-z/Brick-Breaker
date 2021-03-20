# Brick-Breaker

Terminal-based game
##  Dimensions
- BOARD = [45 x 150]
- Without borders:  
    ```
     1                                          148
    3|------------------------------------------|
     |                                          |
     |                                          |
     |                                          |
     |                                          |
     |                                          |
     |                                          |
     |                                          |
     |                                          |
     |                                          |
     |                   41-----paddle          |
   42|------------------------------------------|
    ```

- BRICK = [1 x 5]
## Instructions
Install python libraries (pip can also be used instead of pip3):

    pip3 install numpy colorama
To run the game:

    python3 main.py

## How to play
- __a__ = move paddle left
- __d__ = move paddle right
- __w__ = launch ball from paddle
- __x__ = duplicating ball
- __l__ = lvl up
- __q__ = quit

## IMP points

- Subclass doesnt inherit private variables & private methods into its own
- In ball.py we are able to use __paddleCollision & __borderCollision in the subclass because moveBall() is a public method inherited and it calls these 2 func from parent class when these func are not found in child class
- Inheritance is implemented in brickAfterCollision() in brick.py
- 1 brick break = +5 SCORE
- After Fastball powerup time limit, speed equals to previous speed (direction may differ) before powerup
- 7 types of bricks:
    - Breakable = 3 types with 3 strengths
    - Unbreakable
    - Explosive
    - Rainbow = changes its strengths till it is hit with ball
- Sound effects for collisions, level up, powerup, etc.
- After certain time in a level the bricks start to come down (FALL_BRICK_TIME)
- All oop concepts are implemented

## Features

### Lvls
- 3 levels are implemented
- Level 3 is the boss level
- __l__ can be used to skip between levels

### Falling Bricks
- After certain seconds the bricks come 1 row below after ball hits our paddle.
- When any brick hits paddle row then gameOver

### Powerup 2.0
- When a brick containing powerup breaks completely then the powerup goes in the direction of the ball with the same speed.

### Boss Level
- Boss shoots lasers below with a fixed interval
- It has 5 health
- At health 3, it forms defensive row below it of strength 1
- At health 1, it forms defensive row below it of strength 2

## PowerUps Implemented
- FastBall
- MultiplyBall
- PaddleShrink
- PaddleExpand
- ThruBall
- PaddleGrab
- FireBall
- ShootingPaddle
