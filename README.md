# The Pong Arcade Game
## Objective
Develop a program to create the classic arcade game - Pong. Pong is the video-game version of table-tennis
## Gameplay and Directions
+ This is a two player game. The player on the right and on the left each has a paddle
+ The ball oscillates between the two sides
+ If it hits either the top or the bottom edge of the screen, it bounces off and goes forward at an angle
+ If it hits the paddle, it bounces and moves towards the other side
+ The right-side player must use the 'w' key to move the paddle upwards, and the 's' key to move it downwards
+ The left-side player must use the 'Up' arrow key to move the paddle upwards, and the 'Down' arrow key to move it downwards
+ If the ball misses the paddle and hits the side wall, the opposite player scores a point. The game restarts and the ball starts moving from the net, in the direction opposite to which it had started in the earlier round
+ The game continues until the game is manually stopped by the user

## Additional Points
+ The scoreboard.py, ball.py, net.py and paddle.py all contain classes that are referenced to in the main.py file. Therefore, it is preferred that all five files be contained within the same folder
+ To use the code, you must copy and paste it into your IDE or code editor and run it there
+ All the graphics have been created using the Turtle module
+ The turtle module documentation can be accessed here: https://docs.python.org/3/library/turtle.html
