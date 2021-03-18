# Brick-Breaker

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

## IMP points

- subclass doesnt inherit private variables & private methods into its own
- In ball.py we are able to use __paddleCollision & __borderCollision in the subclass because moveBall() is a public method inherited and it calls these 2 func from parent class when these func are not found in child class
- Inheritance is implemented in brickAfterCollision() in brick.py
- 1 brick break = +5 SCORE
- After Fastball powerup time limit, speed equals to previous speed (direction may differ) before powerup
- 6 types of bricks:
    - Breakable = 3 types with 3 strengths
    - Unbreakable
    - Explosive
- All oop concepts are implemented