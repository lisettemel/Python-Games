'''
Lisette Melo Reyes
A01028066

Program to play Snake
'''

"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
import random
from turtle import *

from freegames import square, vector

Screen().bgcolor("black")

# Move initial place of the food
food = vector(50, 0)

snake = [vector(10, 0)]
aim = vector(0, -10)
colours = ('#ED6A5A', '#72DDF7','#9067C6', '#EFCA08', '#04E762')



def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    
    "Go around the edges"
    if head.x == -200:
        head.x = 180
        
    elif head.x == 180:
        head.x = -200
        
    elif head.y == -200:
        head.y = 180
    
    elif head.y == 180:
        head.y = -200
        
        
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    
    if not inside(head):
        inside
    
    elif head in snake:
        square(head.x, head.y, 9, 'blue')
        update()
        return

    snake.append(head)
   
    # Adds lenght to the snake
    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10

        
    else:
        snake.pop(0)

    clear()
        
    # Randomize the colors of the snake
    for body in snake:
        square(body.x, body.y, 9, random.choice(colours))

    # Random food place

    if food == head:
        food.x = random.choice(move)
        food.y = random.choice(move)
    
        
        
        
    square(food.x, food.y, 9, '#FF3A20')
    update()
#     Make the snake faster or slower
    ontimer(move, 90)


    


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()