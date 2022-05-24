'''
Lisette Melo
A01028066
María Fernanda Martínez
A01027631

Cannon shot game

Video de explicación: https://youtu.be/Q64RwmhyWhI 

'''

"""Cannon, hitting targets with projectiles.

Exercises

1. Keep score by counting target hits.
2. Vary the effect of gravity.
3. Apply gravity to the targets.
4. Change the speed of the ball.

"""
# Librerias
from random import randrange, random, uniform
from turtle import *
from freegames import vector

# Definir las variables 
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
size = (15, 30)
color = (['blue', 'magenta', 'green', 'yellow'])
state = {'score': 0, 'lives': 3, 'shots': 0}
writer = Turtle(visible = False)

def tap(x, y):
    "Respond to screen tap."
    
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Velocity of the cannon
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25
        # Counter of shots
        state['shots'] += 1
      

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    # Show score and lives  
    clear()
    writer.undo()
    writer.up()
    writer.goto(0,170)
    writer.down()
    writer.write(f"Score: {state['score']} Lives: {state['lives']}", align = 'center', font = ('Times New Roman', 20))

    # Change sizes and colors of targets randomly
    for target, size, color in targets:
        goto(target.x, target.y)
        dot(size, color)

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    # Generate a new target at random times
    if randrange(30) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        size = randrange(15, 30)
        colormode(255)
        color = [randrange(0, 255), randrange(0, 255), randrange(0, 255)] 
        targets.append([target, size, color])

    # Move the existing targets
    for target, size, color in targets:
        target.x -= 0.5

    # Move the cannon shot
    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    # Make a copy of the existing target list before redrawing
    dupe = targets.copy()
    targets.clear()

    # Detect if the bullet hits a target
    for target, size, color in dupe:
        if abs(target - ball) > 15:
            targets.append([target, size, color])
         # Add one point on score when the cannon touches the target    
        else:
            state['score'] += 1

    draw()
    # Write game over and state the percentage
    if not state['lives']:
        writer.undo()
        writer.up()
        writer.goto(0,170)
        writer.down()
        SPS =state['score']/state['shots']*100
        writer.write(f"GAME OVER! {SPS}%", align = 'center', font = ('Times New Roman', 20))
       

        return
    # Detect when a target reaches the left side
    for target, size, color in targets:
        if not inside(target):
            targets.remove([target, size, color])
            #targets.remove(target)
            state['lives'] -= 1
            
        
    # Speed of the whole game
    ontimer(move, 30)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

# No pudimos hacer que los targets dejaran de parpadear 
