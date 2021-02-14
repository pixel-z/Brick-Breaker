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

## IMP points

- subclass doesnt inherit private variables & private methods into its own
- In ball.py we are able to use __paddleCollision & __borderCollision in the subclass because moveBall() is a public method inherited and it calls these 2 func from parent class when these func are not found in child class