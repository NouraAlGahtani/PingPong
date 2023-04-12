import turtle as turtle
import os


player_a_score = 0
player_b_score = 0

win = turtle.Screen() # to create a window
win.title("THE PINGPONG GAME") #Name of the game duh
win.bgcolor('purple') # color of main Page aka homescreen
win.setup(width=800, height=600) # size of the game
win.tracer(0) # Speeeeeeeeeeeeeeeed


# Create left paddle for the game

paddle_left = turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square') # i kinda want to change the shape but i cant sadly :/
paddle_left.color('pink')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)




# now same thing but right side hehe
paddle_right = turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square') # i kinda want to change the shape but i cant sadly :/
paddle_right.color('white')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)


# now we will create the ball
ball = turtle.Turtle()
ball.speed(1) # 1 slowest and 0 fastest
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0,0)
ball_dx = 1.5 # setting up pixs
ball_dy = 1.5





